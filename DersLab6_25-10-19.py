# In[53]:


import numpy as np
import matplotlib.pyplot as plt
data_path = "data/"
im_1=plt.imread(data_path+"rbf3dstill.jpg")
im_1.shape


# In[68]:


im_2=np.zeros((118,158),dtype=np.uint8)
im_2.shape
im_2=im_1[:,:,0]
im_3=np.zeros((118,158),dtype=np.uint8)
#im_3=im_1[:,:,0]
plt.imshow(im_2,cmap='gray')
plt.show()


# In[69]:


m,n=im_2.shape


# In[70]:


for i in range(1,m-1):
    for j in range(1,n-1):
        s = im_2[i-1,j-1]/9 + im_2[i-1,j]/9 + im_2[i-1,j+1]/9 + im_2[i,j-1]/9 + im_2[i,j]/9 + im_2[i,j+1]/9 + im_2[i+1,j-1]/9 + im_2[i+1,j]/9 + im_2[i+1,j+1]/9
        s=int(s)
        
        #s=im_2[i-1,j+1]
        
        #print(s, end=' * ')
        
        im_3[i,j]=s


# In[72]:


plt.subplot(1,2,1)
plt.imshow(im_2,cmap='gray')

plt.subplot(1,2,2)
plt.imshow(im_3,cmap='gray')


# In[75]:


plt.imsave(data_path + "test4.jpg", im_2,cmap='gray')
plt.imsave(data_path + "test4-1.jpg", im_3,cmap='gray')