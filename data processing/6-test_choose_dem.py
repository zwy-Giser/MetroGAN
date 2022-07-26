#%%
from PIL import Image
import numpy as np
import os
import shutil
count=0
#%%
test_cities=[]
test_root="/Users/zwy/research/CityGAN/Data/multi-year_dataset/test/nightlight"
train_root="/Users/zwy/research/CityGAN/Data/multi-year_dataset/train/nightlight"

move_list=[]
for root,dirs,files in os.walk(test_root):
	count=0
	
	for file_name in files:
		file_name=file_name[file_name.index('-')+1:]
		name=file_name[file_name.index('-')+1:]
		for _, _, train_files in os.walk(train_root):
			for train_file in train_files:
				if name in train_file:
					print(train_file)
					count+=1
					move_list.append(train_file)
print(move_list)
#%%
srcroot="/Users/zwy/research/CityGAN/Data/multi-year_dataset/train/"
dstroot="/Users/zwy/research/CityGAN/Data/multi-year_dataset/test/"
type_list=["built-up_area/","dem/","nightlight/","water/"]
for name in move_list:
	for type_ in type_list:
		try:
			shutil.move(srcroot+type_+name, dstroot+type_+name)
			print(name)
			print(srcroot+type_+name, dstroot+type_+name)
		except:
			pass
#%%
# test
test_root="/Users/zwy/research/CityGAN/Data/multi-year_dataset/test/nightlight"
train_root="/Users/zwy/research/CityGAN/Data/multi-year_dataset/train/nightlight"

move_list=[]
for root,dirs,files in os.walk(test_root):
	count=0
	
	for file_name in files:
		if "Y2000" in file_name:
			file_name=file_name.replace("Y2000","Y2014")
		else:
			file_name=file_name.replace("Y2014","Y2000")
		if file_name in files:
			continue
		print(file_name)
#%%
# 检查是否有含'的名字，似乎在之前的rename中替换过一次，但是没有脚本保留
# 弃用，应该没有被替换
for root,dirs,files in os.walk(r'C:\research\city_architecture\data\global_city_dataset\train\dem resize'):
    for name in files:
        if '\'' in name:
            print(name)
            new_name=name.replace('\'','_')
            os.rename(root+"\\"+name, root+"\\"+new_name)
