# In[15]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
image_size = 28 # width and length
no_of_different_labels = 10 #  i.e. 0, 1, 2, 3, ..., 9
image_pixels = image_size * image_size
data_path = "data/mnist/"
train_data = np.loadtxt(data_path + "mnist_train.csv", 
                        delimiter=",")
test_data = np.loadtxt(data_path + "mnist_test.csv", 
                       delimiter=",")


# In[78]:



def my_pdf_1(x, mu=0.0, sigma=1.0):
    eps = np.finfo(float).eps
    x = float(x-mu)/(sigma + eps)
    return math.exp(-x*x/2.0)/math.sqrt(2.0*math.pi)/(sigma + eps)


# In[79]:


def get_my_mean_and_std(k=0, l=0):
    s,t = 0,0
    for i in range(10000):
        if(test_data[i,0]==k):
            s = s+1
            t = t+test_data[i,l+1]
            
    mean_1 = t/s

    s,t = 0,0
    for i in range(10000):
        if(test_data[i,0]==k):
            s=s+1
            diff_1 = test_data[i,l+1]-mean_1
            t=t+diff_1*diff_1
    std_1=np.sqrt(t/(s-1))
        
    return mean_1, std_1


# In[80]:


get_my_mean_and_std(1,10)
my_pdf_1(10,1,3)


# In[93]:


my_test_image1=plt.imread('data/new_three.jpg')
my_test_image=my_test_image1[:,:,0]
im_5=my_test_image.reshape(1, 784)
plt.imshow(my_test_image)
plt.show()
my_test_image.ndim, my_test_image.shape


# In[82]:


my_test_image[14,:]


# In[86]:


my_list=[]
for i in range(10):
    pdf_t=0
    for j in range(784):
        x=im_5[0,j]
        m_1,std_1=get_my_mean_and_std(i,j)
        pdf_deger=my_pdf_1(x, m_1, std_1)
        pdf_t = pdf_t + pdf_deger
    print(pdf_t)
    my_list.append(pdf_t)


# In[87]:


max(my_list)