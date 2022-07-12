#%%
from PIL import Image
import numpy as np
import os
import shutil
from random import sample
count=0
# generate test city list
for root,dirs,files in os.walk("/Users/zwy/research/MetroGAN/Data/multi-year_dataset/test/nightlight"):
	for name in files:
		img=Image.open(root+'/'+name)
		img_arr=np.array(img)
		img_arr=img_arr/67.0
		img_norm=Image.fromarray(img_arr)
		img_norm.save("/Users/zwy/research/MetroGAN/Data/multi-year_dataset/test/NTL/"+name)
# %%
