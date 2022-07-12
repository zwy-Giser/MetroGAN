# filt data that built-up area is less than 20% of the picture
from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt
import shutil
count=0

both_delete_list=[]
single_delete_list=[]
for root,dirs,files in os.walk(r"C:\research\city_architecture\data\multi-year dataset\built-up_area"):
#for root,dirs,files in os.walk(r"C:\research\city_architecture\data\multi-year dataset\filted"):
	for name in files:
		count+=1
		#print(name)
		img=Image.open(root+"\\"+name)
		img_arr=np.array(img)
		prefix=name[:name.index('-')]
		city_name=name[name.index('-')+1:]
		#city_name=city_name[city_name.index('-')+1:]
		#if city_name not in single_delete_list:
		if img_arr.sum()/(128*128)<0.01:
			#print("sum:",img_arr.sum())
			#print(city_name)
			'''shutil.move(root+'\\'+name,
						"C:\\research\\city_architecture\\data\\multi-year dataset\\filted\\built-"+name)
			shutil.move("C:\\research\\city_architecture\\data\\multi-year dataset\\nightlight\\"+name,
						"C:\\research\\city_architecture\\data\\multi-year dataset\\filted\\nightlight-"+name)'''
			if city_name not in single_delete_list:
				single_delete_list.append(city_name)
			elif city_name in single_delete_list:
				both_delete_list.append(city_name)
			print("both:",city_name)
	print(both_delete_list)
	print(len(both_delete_list))
for name in both_delete_list:
	shutil.move("C:\\research\\city_architecture\\data\\multi-year dataset\\dem\\"+name,
				"C:\\research\\city_architecture\\data\\multi-year dataset\\filted\\dem-"+name)
	shutil.move("C:\\research\\city_architecture\\data\\multi-year dataset\\water\\"+name,
				"C:\\research\\city_architecture\\data\\multi-year dataset\\filted\\water-"+name)