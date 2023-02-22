from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt
count=0
year=2000
# check the max population value
# maximun check's result is 159004
max_pop=-1
for root,dirs,files in os.walk("/Users/zwy/research/MetroGAN/Data/pop raw/pop raw "+str(year)):
	for name in files:
		# constrain the type of raw images are tiff.
		if not name.endswith('.tiff'):
			continue
		count+=1
		print(name)
		img=Image.open(root+"/"+name)
		img_arr=np.array(img)
		'''if img_arr.max()>max_pop:
			max_pop=img_arr.max()'''
		img_arr=(img_arr/177493.0)
		img_arr[img_arr<0]=0
		img=Image.fromarray(img_arr)
		img.save("/Users/zwy/research/MetroGAN/Data/multi-year_dataset/train/pop/Y"+str(year)+'-'+name)