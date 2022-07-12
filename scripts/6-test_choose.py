#%%
from PIL import Image
import numpy as np
import os
import shutil
from random import sample
count=0
# generate test city list
for root,dirs,files in os.walk("/Users/zwy/research/MetroGAN/Data/multi-year_dataset/train/built-up_area"):
	test_cities=sample(files,4)
	print(test_cities)
	final_test_cities=test_cities[:]
	for name in test_cities:
		prefix=name[:name.index('-')]
		city_name=name[name.index('-')+1:]
		if prefix=='Y2000':
			#print(root+"/Y2014-"+city_name)
			isExists=os.path.exists(root+"/Y2014-"+city_name)
			if isExists:
				final_test_cities.append("Y2014-"+city_name)
		elif prefix=='Y2014':
			#print(root+"/Y2000-"+city_name)
			isExists=os.path.exists(root+"/Y2000-"+city_name)
			if isExists:
				final_test_cities.append("Y2000-"+city_name)
		else:
			print("bug!")
	print(final_test_cities)

#%%
# extract test cities' files
#test_root="D:\\BaiduNetdiskDownload\\multi-year dataset filted\\multi-year_dataset\\test"
test_root="/Users/zwy/research/MetroGAN/Data/multi-year_dataset/test"
for root,dirs,files in os.walk("/Users/zwy/research/MetroGAN/Data/multi-year_dataset/train"):
	for dir in dirs:
		count=0
		for sub_root,sub_dir,sub_files in os.walk(root+"/"+dir):
			print(sub_root)
			for name in sub_files:
				count+=1
				if name not in final_test_cities:
					continue
				srcfile=sub_root+"/"+name
				dstfile=test_root+"/"+dir+"/"+name
				isExists=os.path.exists(test_root+"/"+dir)
				# judge existence
				if not isExists:
					os.makedirs(test_root+"/"+dir) 
				try:
					#print(srcfile,dstfile)
					shutil.move(srcfile, dstfile)
				except:
					print("=================Error:"+name)


# %%
