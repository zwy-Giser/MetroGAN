#%%
import imp
from osgeo import gdal
from osgeo import ogr
import os
import numpy as np
import csv
import pandas as pd
import geopandas as gpd
from shapely.geometry.point import Point

#%%
# calculate bonding box from array cordinates to wgs84
def boundingBoxToOffsets(bbox, geot):
    col1 = int((bbox[0] - geot[0]) / geot[1])
    col2 = int((bbox[1] - geot[0]) / geot[1]) + 1
    row1 = int((bbox[3] - geot[3]) / geot[5])
    row2 = int((bbox[2] - geot[3]) / geot[5]) + 1
    return [row1, row2, col1, col2]

# calculate new geotransform of bonding box
def geotFromOffsets(row_offset, col_offset, geot):
    new_geot = [
    geot[0] + (col_offset * geot[1]),
    geot[1],
    0.0,
    geot[3] + (row_offset * geot[5]),
    0.0,
    geot[5]
    ]
    return new_geot

# zone anlysis
# res_df: a dataframe to store results, with two column named pos_x and pos_y.
#         function will pass some columns in vector file to res_df, and it's need to be rectifed to your need.
# raster: input raster dataset(raster file read by gdal)
# vector: vector(zone) geodataframe(shapefile read by geopandas)
def zonal(raster, vector,res_df):
    mem_driver = ogr.GetDriverByName("Memory")
    mem_driver_gdal = gdal.GetDriverByName("MEM")
    shp_name = "temp"
    
    geot = raster.GetGeoTransform()
    nodata = raster.GetRasterBand(1).GetNoDataValue()
    
    for row in range(vector.shape[0]):
        if vector.loc[row,"geometry"] is not None:
            if os.path.exists(shp_name):
                mem_driver.DeleteDataSource(shp_name)  # delete temporary raster if it already exists
            tp_ds = mem_driver.CreateDataSource(shp_name)  # create a new, empty raster in memory
            tp_lyr = tp_ds.CreateLayer('polygons', None, ogr.wkbPolygon)  # create a temporary polygon layer
            
            # Get the output Layer's Feature Definition
            featureDefn = tp_lyr.GetLayerDefn()
            # create a new feature
            tmp_feature = ogr.Feature(featureDefn)
            tmp_feature.SetGeometry(ogr.CreateGeometryFromWkt(str(vector.loc[row,"geometry"])))
            tp_lyr.CreateFeature(tmp_feature)  
            
            
            # directly use the loc to append a row to dataframe
            # pass the colums from vector to res_df
            attr_list=["UID","country","province","city","pop"]
            for attr in attr_list:
                res_df.loc[row,attr]=vector.loc[row,attr]
            # prepare for calculate max point position
            offsets = boundingBoxToOffsets(tmp_feature.GetGeometryRef().GetEnvelope(),\
            geot)  # get the bounding box of the polygon feature and convert the coordinates to cell offsets
            new_geot = geotFromOffsets(offsets[0], offsets[2], geot)  # calculate the new geotransform for the polygonized raster
            
            mask = mem_driver_gdal.Create(\
            "", \
            offsets[3] - offsets[2], \
            offsets[1] - offsets[0], \
            1, \
            gdal.GDT_Byte)  # create the raster for the rasterized polygon in memory
            
            mask.SetGeoTransform(new_geot)  # set the geotransfrom the rasterized polygon
            gdal.RasterizeLayer(mask, [1], tp_lyr, burn_values=[1])  # rasterize the polygon feature
            mask_array = mask.ReadAsArray()  # read data from the rasterized polygon
            
            raster_array = raster.GetRasterBand(1).ReadAsArray(\
            offsets[2],\
            offsets[0],\
            offsets[3] - offsets[2],\
            offsets[1] - offsets[0])  # read data from the input raster that corresponds to the location of the rasterized polygon
            
            # get masked raster array
            if raster_array is not None:
                masked_raster_array = np.ma.MaskedArray(\
                raster_array,\
                mask=np.logical_or(raster_array==nodata, np.logical_not(mask_array)))
            # calculate max point position
            if masked_raster_array is not None:
                '''
                codes to save x and y cordinates into Dataframe.
                
                max_pos=np.unravel_index(masked_raster_array.argmax(), masked_raster_array.shape)
                print((max_pos[1] * new_geot[1]),new_geot[0])
                max_lat=float(new_geot[0] + (max_pos[1] * new_geot[1]))
                max_lon=float(new_geot[3] + (max_pos[0] * new_geot[5]))
                res_df.loc[row,"pos_x"],res_df.loc[row,"pos_y"]=max_lat,max_lon
                #print(masked_raster_array[max_pos[0]][max_pos[1]])
                print(max_pos)
                '''
                max_pos=np.unravel_index(masked_raster_array.argmax(), masked_raster_array.shape)
                max_lat=float(new_geot[0] + (max_pos[1] * new_geot[1]))
                max_lon=float(new_geot[3] + (max_pos[0] * new_geot[5]))
                res_df.loc[row,"geometry"]=Point(max_lat,max_lon)
    return res_df


#%%
# load raster files
pop_raster=gdal.Open(r"..\original data\landscan pop\LandScan Global 2015\lspop2015.tif")
# result file
# res_points=pd.DataFrame(columns=["UID","country","province","city","pop","pos_x","pos_y"])
res_points=gpd.GeoDataFrame(columns=["UID","country","province","city","pop"],geometry=[])
# load vector file
cities=gpd.read_file(r"C:\research\city_architecture\data\original data\population and cities\GADM_level2_wgs84_pop.shp",encoding="utf-8")
cities
cities=cities[['UID','NAME_0','NAME_1','NAME_2','pop_sast_4','geometry']]
cities.rename(columns={"pop_sast_4":"pop","NAME_0":"country","NAME_1":"province","NAME_2":"city"},inplace=True)
cities_over100K=cities[cities['pop']>=100000]
cities_over100K.reset_index(drop=True,inplace=True)
# %%
zonal(pop_raster,cities_over100K,res_points)
print(res_points)
# %%
res_points=res_points.astype({"UID":int,"pop":float})
res_points.to_file('city_centroids.gpkg', driver='GPKG',encoding='utf-8')

# %%
# file types geopandas can save, and their corresponding "driver" argument.
import fiona
fiona.supported_drivers
