#%%
from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt
count=0
for root,dirs,files in os.walk(r"C:\research\city_architecture\data\dataset20211214\unresample\built area"):
	for name in files:
		if not name.endswith('.png'):
			continue
		count+=1
		#print(name)
		img=Image.open(root+"\\"+name)
		img_arr=np.array(img)
		'''img_1990=(img_arr>=5).astype(int)*255
		img=Image.fromarray(img_1990).convert("1")
		img.save("C:\\research\\city_architecture\\data\\global_city_dataset\\built-up area 1990\\"+name)'''

		img_2000_arr=((img_arr>=4).astype(int)*255)
		img_2000=Image.fromarray(img_2000_arr).convert("L")
		img_2000_resize=img_2000.resize((128,128),Image.NEAREST).convert("1")
		img_2000_resize.save("C:\\research\\city_architecture\\data\\multi-year dataset\\built-up_area\\Y2000-"+name.replace(".png",".tiff"))

		img_2014_arr=((img_arr>=3).astype(int)*255)
		img_2014=Image.fromarray(img_2014_arr).convert("L")
		img_2014_resize=img_2014.resize((128,128),Image.NEAREST).convert("1")
		print(name.replace(".png",".tiff"))
		img_2014_resize.save("C:\\research\\city_architecture\\data\\multi-year dataset\\built-up_area\\Y2014-"+name.replace(".png",".tiff"))



# %%
