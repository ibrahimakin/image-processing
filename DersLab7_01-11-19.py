# In[28]:


import numpy as np
import matplotlib.pyplot as plt
data_path = "data/"

x = [180,170,170,175,181,175,177,185,179,160] #boy
y = [95,70,60,79,60,63,83,80,75,50]           #kilo


# In[13]:


x, y, len(x), len(y)


# In[14]:


X = np.stack((x, y), axis=0)
X


# In[15]:


sigma_1=np.cov(X)
sigma_1


# In[16]:


X_test = np.stack((x, x), axis=0)
X_test


# In[17]:


sigma_2=np.cov(X_test)
sigma_2


# In[51]:


def generateData():
    x = [180,170,170,175,181,175,177,185,179,160] #boy
    y = [95,70,60,79,60,63,83,80,75,50]
    X = np.stack((x, y), axis=0)
    return X
def getCovMatris(X):
    
    sigma_1=np.cov(X)
    return sigma_1
    


# In[52]:


data1=generateData()
getCovMatris(data1)


# In[54]:


def multivariate_normal(x, d, mean, covariance):
    """pdf of the multivariate normal distribution."""
    x_m = x - mean
    return (1. / (np.sqrt((2 * np.pi)**d * np.linalg.det(covariance))) * 
            np.exp(-(np.linalg.solve(covariance, x_m).T.dot(x_m)) / 2))


# In[55]:


x=generateData()
np.mean(x[0,:]), np.mean(x[1,:])


# In[56]:


x1=[175,72]
d1=2        

data=generateData()
#mean1=np.array([np.mean(x[0,:]), np.mean(x[1,:])])
mean1=np.array([np.mean(x[0,:]),np.mean(x[1,:])])
covariance1=getCovMatris(data)


# In[57]:


multivariate_normal(x1, d1, mean1, covariance1)


# In[58]:


for i in range(10):
    v=164+i
    x1=[160+i,72]
    
    s = multivariate_normal(x1, d1, mean1, covariance1)
    print(v," ",s)


# In[ ]: