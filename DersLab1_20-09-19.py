#
import os
#
os.getcwd()
#
import numpy as np
import matplotlib.pyplot as plt
im_1=plt.imread('comu.jpg')
im_1.ndim,type(im_1),im_1.shape
#
im_1[100,100,:]
m,n,p=im_1.shape
plt.imshow(im_1)
plt.show()
#
im_1[100,100,:]
#
m,n,p
#
new_image=np.zeros((m,n),dtype=float)
#
for i in range(m):
    for j in range(n):
        #s=(im_1[i,j,0]+im_1[i,j,1]+im_1[i,j,2])/3
        s=(im_1[i,j,0]/3+im_1[i,j,1]/3+im_1[i,j,2]/3)
        new_image[i,j]=s
#
plt.imshow(new_image)
plt.show()
#
plt.imshow(new_image,cmap='gray')
plt.show()
#
new_image2=np.zeros((n,m),dtype=float)
for i in range(m):
    for j in range(n):
        #s=(im_1[i,j,0]+im_1[i,j,1]+im_1[i,j,2])/3
        s=(im_1[i,j,0]/3+im_1[i,j,1]/3+im_1[i,j,2]/3)
        new_image2[j,i]=s
plt.imshow(new_image2)
plt.show()
#
plt.imsave("test3.jpg",new_image2,cmap='gray')
#
test=plt.imread('test3.jpg')
test[100,19,:]
#