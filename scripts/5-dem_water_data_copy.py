# filt data that built-up area is less than 20% of the picture
from PIL import Image
import numpy as np
import os
import shutil
count=0

both_delete_list=[]
single_delete_list=[]
for root,dirs,files in os.walk(r"D:\BaiduNetdiskDownload\multi-year dataset filted\built-up_area"):
	for name in files:
		count+=1
		#print(name)
		prefix=name[:name.index('-')]
		city_name=name[name.index('-')+1:]
		# copy file in dem and water folder
		shutil.copyfile("D:\\BaiduNetdiskDownload\\multi-year dataset filted\\dem_origin\\"+city_name,
						"D:\\BaiduNetdiskDownload\\multi-year dataset filted\\dem\\"+name)
		shutil.copyfile("D:\\BaiduNetdiskDownload\\multi-year dataset filted\\water_origin\\"+city_name,
						"D:\\BaiduNetdiskDownload\\multi-year dataset filted\\water\\"+name)
		'''print("D:\\BaiduNetdiskDownload\\multi-year dataset filted\\dem_origin\\"+city_name,
				"D:\\BaiduNetdiskDownload\\multi-year dataset filted\\dem\\"+name,
				"D:\\BaiduNetdiskDownload\\multi-year dataset filted\\water_origin\\"+city_name,
				"D:\\BaiduNetdiskDownload\\multi-year dataset filted\\water\\"+name)'''
		print(count)