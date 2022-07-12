#%%
from PIL import Image
import numpy as np
import os

# examine the max/min DN in pictures and using them to normalize the pictures
# because max dn is 89429.34, which is too large to show the image 
# clealy(merely all pixels are black), we manually set the max_dn is 100

max_dn=-100
min_dn=10000
for root,dirs,files in os.walk(r"D:\BaiduNetdiskDownload\multi-year dataset filted\multi-year_dataset\train\nightlight"):
	for name in files:
		if not name.endswith('.tiff'):
			continue
		
		img=Image.open(root+"\\"+name)
		img_arr=np.array(img)
		#print(img_arr)
		#print(name, img_arr.max())
		if img_arr.min()<min_dn:
			min_dn=img_arr.min()
		if(img_arr.max()>max_dn):
			max_dn=img_arr.max()
		img.close()
print("min elevator:",min_dn)
print("max elevator:",max_dn)
#%%
# using 100 as the max value
for root,dirs,files in os.walk("D:\\BaiduNetdiskDownload\\multi-year dataset filted\\multi-year_dataset\\test\\nightlight"):
	for name in files:
		if not name.endswith('.tiff'):
			continue
		img=Image.open(root+"\\"+name)
		img_arr=np.array(img)
		img_arr=(img_arr-min_dn)/(max_dn-min_dn)
		img=Image.fromarray(img_arr)
		#img=img.resize((128,128),Image.BICUBIC)
		# because torchvision.ToTensor can only deal with 8 bit picture, we normalize the picture here
		# in F mode, pixel ranges [0,255],so mulplying img_arr with 255 can show the picture clearly
		# fromarray makes img in F mode in default because img_arr's type is float
		
		print(name)

		img.save("D:\\BaiduNetdiskDownload\\multi-year dataset filted\\multi-year_dataset\\test\\nightlight_resample\\"+name)

# %%
