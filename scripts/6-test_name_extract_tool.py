import numpy
import os
test_names=[]
test_dir=r"C:\research\city_architecture\data\global_city_dataset\test\built-up area 1975 resize"
for root, dirs, files in os.walk(test_dir):
    test_names=files

test_names_tiff=[]
for i in test_names:
    test_names_tiff.append(i.replace("png","tiff"))
test_names.extend(test_names_tiff)
print(test_names)