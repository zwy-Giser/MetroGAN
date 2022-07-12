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
		img.save("C:\\research\\city_architecture\\data\\global_city_dataset\\built-up area 1990\\"+name)

		img_2000=(img_arr>=4).astype(int)*255
		img=Image.fromarray(img_2000).convert("1")
		img.save("C:\\research\\city_architecture\\data\\global_city_dataset\\built-up area 2000\\"+name)'''

		img_2014=((img_arr>=3).astype(int)*255)
		img=Image.fromarray(img_2014).convert("L")
		img2=img.resize((256,256),Image.NEAREST).convert("1")
		print(name.replace(".png",".tiff"))
		img2.save("C:\\research\\city_architecture\\data\\processed data\\built-up area 2014\\"+name.replace(".png",".tiff"))



		# the rest of three solutions to binarize the built-up area and using plt to contrast them

		#img_bi=img.resize((256,256),Image.BICUBIC)
		#fn = lambda x : 255 if x > 80 else 0
		#img_thres = img_bi.point(fn, mode='1')
		#img1=img_bi.convert("1")
		'''fig,axs=plt.subplots(2,2,dpi=300.0,tight_layout=True)
		axs[0][0].set_xticks([])
		axs[0][0].set_yticks([])
		axs[0][0].set_title("origin")
		axs[0][0].imshow(img.convert("1"))
		axs[0][1].set_xticks([])
		axs[0][1].set_yticks([])
		axs[0][1].set_title("nearest")
		axs[0][1].imshow(img2)
		axs[1][0].set_xticks([])
		axs[1][0].set_yticks([])
		axs[1][0].set_title("bicubic+threshold")
		axs[1][0].imshow(img_thres)
		axs[1][1].set_xticks([])
		axs[1][1].set_yticks([])
		axs[1][1].set_title("bicubic+convert(1)")
		axs[1][1].imshow(img1)
		plt.savefig("建成区四种采样模式.png")'''

# %%
