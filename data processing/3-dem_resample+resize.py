#%%
from PIL import Image
import numpy as np
import os
#%%
# examine the max/min elevator in pictures and using them to normalize the pictures
max_elevator=0
min_elevator=10000
for root,dirs,files in os.walk(r"C:\research\city_architecture\data\dataset20211214\unresample\dem"):
	for name in files:
		if not name.endswith('.tiff'):
			continue
		
		img=Image.open(root+"\\"+name)
		img_arr=np.array(img)
		#print(img_arr)
		#print(name, img_arr.max())
		if img_arr.min()<min_elevator:
			min_elevator=img_arr.min()
		if(img_arr.max()>max_elevator):
			max_elevator=img_arr.max()
print("min elevator:",min_elevator)
print("max elevator:",max_elevator)

#%%
# resize and normalize pictures
for root,dirs,files in os.walk(r"C:\research\city_architecture\data\dataset20211214\unresample\dem"):
	for name in files:
		if not name.endswith('.tiff'):
			continue
		img=Image.open(root+"\\"+name)
		img_arr=np.array(img)
		img_arr=(img_arr-min_elevator)/(float(max_elevator-min_elevator))
		# because torchvision.ToTensor can only deal with 8 bit picture, we normalize the picture here
		# in F mode, pixel ranges [0,255],so mulplying img_arr with 255 can show the picture clearly
		# fromarray makes img in F mode in default because img_arr's type is float
		img=Image.fromarray(img_arr)
		img=img.resize((128,128),Image.BICUBIC)
		print(name)
		img.save("C:\\research\\city_architecture\\data\\multi-year dataset\\dem\\"+name)

# %%
