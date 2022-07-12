#%%
from PIL import Image
import numpy as np
import os

# examine the max/min DN in pictures and using them to normalize the pictures
# because max dn is 89429.34, which is too large to show the image 
# clealy(merely all pixels are black), we manually set the max_dn is 100

max_dn=-100
min_dn=10000
for root,dirs,files in os.walk("/Users/zwy/Downloads/cityGAN dataset/CityGAN dataset/train/built-up area 2014"):
	for name in files:
		if not name.endswith('.tiff'):
			continue
		
		img=Image.open(root+"/"+name)
		img_arr=np.array(img)
		#print(img_arr)
		#print(name, img_arr.max())
		if img_arr.min()<min_dn:
			min_dn=img_arr.min()
		if(img_arr.max()>max_dn):
			max_dn=img_arr.max()
		img.close()
print("min elevator:",float(min_dn))
print("max elevator:",max_dn)
#%%
# using 100 as the max value
for root,dirs,files in os.walk(r"C:\research\city_architecture\data\dataset20211214\unresample\night_light"):
	for name in files:
		if not name.endswith('.tiff'):
			continue
		img=Image.open(root+"\\"+name)
		img=img.resize((256,256),Image.BICUBIC)
		# because torchvision.ToTensor can only deal with 8 bit picture, we normalize the picture here
		# in F mode, pixel ranges [0,255],so mulplying img_arr with 255 can show the picture clearly
		# fromarray makes img in F mode in default because img_arr's type is float
		img_arr=np.array(img)
		img_arr[img_arr>100]=100
		img_arr=(img_arr-(-1.5))/(float(100-(-1.5)))
		img=Image.fromarray(img_arr)
		
		print(name)
		img.save("C:\\research\\city_architecture\\data\\processed data\\nightlight\\"+name)
