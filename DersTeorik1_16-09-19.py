#
import os
#
os.getcwd()
#
os.listdir()
#
jpg_files=[f for f in os.listdir() if f.endswith('jpg')]
jpg_files
#
import numpy as np
import matplotlib.pyplot as plt
im_1=plt.imread(jpg_files[0])
print(type(im_1))
print(im_1.size)
print(im_1.ndim)
print(im_1.shape)
print(im_1[100,100,1])
print(im_1[100,100,2])
#print(im_1[100,100,3]) #error
print(im_1[100,100,0])
print(im_1[100,100,:])
print(im_1[100,:,1])
#
plt.imshow(im_1)
plt.show()
#
im_2=im_1[:,:,0]
plt.imshow(im_2)
plt.show()
#
plt.imsave('MerhabaSonSinif.jpg',im_2)
#