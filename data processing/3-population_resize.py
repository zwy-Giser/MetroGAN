#%%
from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt
count=0
year=2014
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
		img_arr[img_arr<0]=0
		img=Image.fromarray(img_arr)
		img=img.resize((128,128),Image.BICUBIC)
        
		#img_resize.show()
		img.save("/Users/zwy/research/MetroGAN/Data/pop raw resize 128/pop raw {year}/".format(year=year)
		+name)



# %%
