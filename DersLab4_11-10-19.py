# In[21]:


# https://www.python-course.eu/neural_network_mnist.php
# download mnist_train.csv and mnist_test.csv


# In[23]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
image_size = 28 # width and length
no_of_different_labels = 10 #  i.e. 0, 1, 2, 3, ..., 9
image_pixels = image_size * image_size
data_path = "data/mnist/"
train_data = np.loadtxt(data_path + "mnist_train.csv", 
                        delimiter=",")
test_data = np.loadtxt(data_path + "mnist_test.csv", 
                       delimiter=",") 
test_data[:10]


# In[24]:


train_data.ndim, train_data.shape


# In[25]:


train_data[10,0]


# In[26]:


im_3 = train_data[10,:]


# In[27]:


im_3.shape


# In[28]:


im_4 = im_3[1:]


# In[29]:


im_4.shape


# In[30]:


im_5 = im_4.reshape(28,28)


# In[31]:


plt.imshow(im_5, cmap = 'gray')
plt.show()


# In[32]:


m,n = train_data.shape
m,n


# In[33]:


def my_counter(k = 0):
    s = 0
    for i in range(m):
        if(train_data[i,0] == k):
            s = s+1
    return s
for i in range(10):
    c = my_counter(i)
    print(i, "   ", c)


# In[41]:


import math
def my_pdf_1(x, mu=0.0, sigma=1.0):
    x = float(x-mu)/sigma
    return math.exp(-x*x/2.0)/math.sqrt(2.0*math.pi)/sigma
my_pdf_1(10,1,3)


# In[42]:


m,n = train_data.shape
def get_my_mean_and_std(k=0, l=0):
    #k,l = 0,350
    s,t = 0,0
    for i in range(m):
        if(train_data[i,0]==k):
            s = s+1
            t = t+train_data[i,l+1]
    mean_1 = t/s

    s,t = 0,0
    for i in range(m):
        if(train_data[i,0]==k):
            s=s+1
            diff_1 = train_data[i,l+1]-mean_1
            t=t+diff_1*diff_1
    std_1=np.sqrt(t/(s-1))
        
    #print(mean_1,std_1)
    return mean_1, std_1


# In[49]:


m_1,std_1 = get_my_mean_and_std(2,100)
my_pdf_1(40, m_1, std_1)


# In[53]:


im_1=plt.imread("maxresdefault.jpg")
plt.imshow(im_1)
plt.show()
test_value = im_1[0,0,0]


# In[54]:


m_1, std_1 = get_my_mean_and_std(2,100)
my_pdf_1(test_value, m_1, std_1)





