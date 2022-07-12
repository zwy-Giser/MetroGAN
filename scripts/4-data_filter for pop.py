#%%
# filt data that built-up area is less than 20% of the picture
from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt
import shutil
count=0

both_delete_list=[]
single_delete_list=[]
for root,dirs,files in os.walk("/Users/zwy/research/MetroGAN/Data/multi-year_dataset/train/pop"):
	for name in files:
		if os.path.exists("/Users/zwy/research/MetroGAN/Data/multi-year_dataset/train/built-up_area/"+name):
			print(name)
			continue
		if os.path.exists("/Users/zwy/research/MetroGAN/Data/multi-year_dataset/test/built-up_area/"+name):
			shutil.move("/Users/zwy/research/MetroGAN/Data/multi-year_dataset/train/pop/"+name,
					"/Users/zwy/research/MetroGAN/Data/multi-year_dataset/test/pop/"+name)
			continue
		shutil.move("/Users/zwy/research/MetroGAN/Data/multi-year_dataset/train/pop/"+name,
					"/Users/zwy/research/MetroGAN/Data/multi-year_dataset/pop filted/"+name)
# %%
# Using prefix of file name to examine which special characters have been replaced
def GetPrefix(name):
	prefix1=name[:name.index('-')]
	name=name[name.index('-')+1:]
	prefix2=name[:name.index('-')]
	return prefix1+'-'+prefix2
for root,dirs,files in os.walk("/Users/zwy/research/MetroGAN/Data/multi-year_dataset/pop filted"):
	for name in files:
		prefix=GetPrefix(name)
		for root2,dirs2,files2 in os.walk("/Users/zwy/research/MetroGAN/Data/multi-year_dataset/train/built-up_area"):
			for built_up_name in files2:
				prefix2=GetPrefix(built_up_name)
				if prefix==prefix2:
					print(name,built_up_name)
					break
# %%
