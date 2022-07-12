#%%
# !Abolished
# Because the intermediate results of water data is very large, we incorporate 
# the classify and resize operations into clip operation.

from PIL import Image
import numpy as np
import os

for root,dirs,files in os.walk(r"C:\research\city_architecture\data\dataset20211214\unresample\water"):
	for name in files:
		if not name.endswith('.tiff'):
			continue
		img=Image.open(root+"\\"+name)
		# binarize
		img_arr=np.array(img)
		img_arr[img_arr>50]=255
		img_arr[img_arr<=50]=0
		img=Image.fromarray(img_arr)

		# resize
		img=img.resize((256,256),Image.NEAREST).convert("1")

		# save
		img.save("C:\\research\\city_architecture\\data\\processed data\\water\\"+name)
# %%
