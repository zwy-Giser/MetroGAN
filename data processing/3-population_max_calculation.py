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
for root,dirs,files in os.walk("/Users/zwy/research/MetroGAN/Data/pop raw resize 128/pop raw "+str(year)):
	for name in files:
		# constrain the type of raw images are tiff.
		if not name.endswith('.tiff'):
			continue
		count+=1
		img=Image.open(root+"/"+name)
		img_arr=np.array(img)
		if img_arr.max()>max_pop:
			max_pop=img_arr.max()

print(max_pop)


