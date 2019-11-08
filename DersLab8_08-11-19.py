# In[1]:


import numpy as np
import matplotlib.pyplot as plt
data_path = "data/"


# In[3]:


im_1=plt.imread(data_path + "test_1.jpg")


# In[5]:


im_1.shape


# In[6]:


plt.imshow(im_1) 
plt.show()


# In[7]:


my_histogram_R_G_B={}    # R,G,B her biri için ayrı ayrı  histogram 
m,n,p=im_1.shape 
for i in range(m):
    for j in range(n):
        s=(im_1[i,j,0])   # ,im_1[i,j,1],im_1[i,j,2])   #  s=im_1[i,j,:], s cannot be Key        
        if (0,s) in my_histogram_R_G_B.keys():              # because its type is np.ndar            
            my_histogram_R_G_B[(0,s)]=my_histogram_R_G_B[(0,s)]+1        
        else:            
            my_histogram_R_G_B[(0,s)]=1 
my_histogram_R_G_B


# In[12]:


# my_histogram_R_G_B={}    # R,G,B her biri için ayrı ayrı  histogram 
m,n,p=im_1.shape 
for i in range(m):    
    for j in range(n):        
        s=(im_1[i,j,1])   # ,im_1[i,j,1],im_1[i,j,2])   #  s=im_1[i,j,:], s cannot be Key        
        if (1,s) in my_histogram_R_G_B.keys():              # because its type is np.ndar            
            my_histogram_R_G_B[(1,s)]=my_histogram_R_G_B[(1,s)]+1        
        else:            
            my_histogram_R_G_B[(1,s)]=1 
my_histogram_R_G_B


# In[13]:


# my_histogram_R_G_B={}    # R,G,B her biri için ayrı ayrı  histogram 
m,n,p=im_1.shape 
for i in range(m):    
    for j in range(n):        
        s=(im_1[i,j,2])   # ,im_1[i,j,1],im_1[i,j,2])   #  s=im_1[i,j,:], s cannot be Key        
        if (2,s) in my_histogram_R_G_B.keys():              # because its type is np.ndar            
            my_histogram_R_G_B[(2,s)]=my_histogram_R_G_B[(2,s)]+1        
        else:            
            my_histogram_R_G_B[(2,s)]=1 
    my_histogram_R_G_B


# In[15]:


my_histogram={}   # (R,G,B) üçlü histogram
m,n,p=im_1.shape 
for i in range(m):    
    for j in range(n):        
        s=(im_1[i,j,0],im_1[i,j,1],im_1[i,j,2])   #  s=im_1[i,j,:], s cannot be Key in di        
        if s in my_histogram.keys():              # because its type is np.ndarray             
            my_histogram[s]=my_histogram[s]+1
        else:            
            my_histogram[s]=1


# In[16]:


my_histogram


# In[ ]: