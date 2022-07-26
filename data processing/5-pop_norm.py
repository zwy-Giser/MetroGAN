from PIL import Image
import numpy as np
import os

#for root,dirs,files in os.walk(r"C:\research\city architecture\data\LandScan Global 2015"):
for root,dirs,files in os.walk(r"C:\research\city architecture\data\light_resample"):
	for name in files:
		if not name.endswith('.tiff'):
			continue
		print(name)
		img=Image.open(root+"\\"+name)
		img_arr=np.array(img)
		print(img_arr.max())
		#img_arr=img_arr/180262.0
		'''img_arr=img_arr/63
		img=Image.fromarray(img_arr)
		#img.save("C:\\research\\city architecture\\data\\pop_resample\\"+name[:-4]+".tiff")
		img.save("C:\\research\\city architecture\\data\\light_resample\\"+name[:-4]+".tiff")'''