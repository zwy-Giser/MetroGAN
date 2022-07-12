
#%%
import rasterio 
import geopandas
import rasterio.mask
import rasterio.plot
from PIL import Image
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from shapely.wkt import loads
from shapely.ops import cascaded_union
import math
import sys, os, time
import glob
import copy

from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.cm as cm



#读取文件
# built area
built_area=rasterio.open(r"C:\research\city_architecture\data\original data\DEM\globaldem2.jp2")
print("read_file:GHS_BUILT_LDSMT_GLOBE_R2018A_3857_30_V2_0-ESRI.vrt","crs:",built_area.crs,"bounds:",built_area.bounds)

#读取城市点数据
cities=gpd.read_file(r"C:\research\city_architecture\data\original data\population and cities\city_centroids.gpkg",encoding="utf-8")
#cities=cities[['UID','NAME_0','NAME_1','NAME_2','pop_sast_4','geometry']]
#cities.rename(columns={"pop_sast_4":"pop","NAME_0":"country","NAME_1":"province","NAME_2":"city"},inplace=True)

#cities_over100K=cities[cities['pop']>=100000]
#cities_over100K.reset_index(drop=True,inplace=True)
#cities_over100K
print(cities)
print(cities.loc[0,"geometry"],cities.loc[0,"geometry"].x,cities.loc[0,"geometry"].y)
#%%
#计算距离

# Bounding box surrounding the point at given coordinates,
# assuming local approximation of Earth surface as a sphere
# of radius given by WGS84
def bounding_box_at_location(latlon, sizeKm):
    widthKm, heightKm = sizeKm
    latitudeInDegrees, longitudeInDegrees = latlon
    # degrees to radians
    def deg2rad(degrees):
        return math.pi*degrees/180.0

    # radians to degrees
    def rad2deg(radians):
        return 180.0*radians/math.pi

    # Semi-axes of WGS-84 geoidal reference
    WGS84_a = 6378137.0  # Major semiaxis [m]
    WGS84_b = 6356752.3  # Minor semiaxis [m]

    # Earth radius at a given latitude, according to the WGS-84 ellipsoid [m]
    def WGS84EarthRadius(lat):
        # http://en.wikipedia.org/wiki/Earth_radius
        An = WGS84_a*WGS84_a * math.cos(lat)
        Bn = WGS84_b*WGS84_b * math.sin(lat)
        Ad = WGS84_a * math.cos(lat)
        Bd = WGS84_b * math.sin(lat)
        return math.sqrt( (An*An + Bn*Bn)/(Ad*Ad + Bd*Bd) )

    lat = deg2rad(latitudeInDegrees)
    lon = deg2rad(longitudeInDegrees)
    widthMeters = 1000*widthKm/2.0
    heightMeters = 1000*heightKm/2.0

    # Radius of Earth at given latitude
    radius = WGS84EarthRadius(lat)
    # Radius of the parallel at given latitude
    pradius = radius*math.cos(lat)

    latMin = lat - heightMeters/radius
    latMax = lat + heightMeters/radius
    lonMin = lon - widthMeters/pradius
    lonMax = lon + widthMeters/pradius

    return (rad2deg(latMin), rad2deg(lonMin), rad2deg(latMax), rad2deg(lonMax))


import geojson 
from shapely.geometry import Polygon,MultiPolygon
def clip_pic(cities,raster_data,w,out_filepath):
	half_size=w*1000#边长
	for index,city in cities.iterrows():
		if index<7286:continue
		#将坐标转换为geojson
		pos=(city["geometry"].y,city["geometry"].x)
		latMin,lonMin,latMax,lonMax=bounding_box_at_location(pos,(w,w))
		multipolygon = MultiPolygon([Polygon([(lonMin, latMin ), (lonMin, latMax), (lonMax, latMax ),(lonMax, latMin)])])

		'''		
		tmp_geometry={
			"type": "Polygon",
			"coordinates": [
				[
					[ latMin, lonMin ],
					[ latMin, lonMax ],
					[ latMax, lonMax ],
					[ latMax, lonMin ],
					[ latMin, lonMin ]
				]
			]
		}
		print(tmp_geometry)'''
  
		#print(multipolygon)
		out_image, out_transform = rasterio.mask.mask(raster_data, multipolygon, crop=True)
		img=Image.fromarray(out_image[0])
		
		file_path=out_filepath+"{id}-{country}-{province}-{city}".format(id=index,country=city["country"],province=city["province"],city=city["city"])
		print(index)
		file_path=file_path.replace('/','_')
		file_path=file_path.replace('|','_')
		file_path=file_path.replace('?','_')
        
		img.save(file_path+".tiff")

clip_pic(cities,built_area,100,"C:\\research\\city_architecture\\data\\dataset20211214\\unresample\\dem\\")
