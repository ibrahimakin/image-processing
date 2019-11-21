#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[2]:


vektor1 = np.array([2,1])
vektor2 = np.array([3,5])


# In[3]:


vektor1 + vektor2


# In[4]:


v_1 = [1, 3]
v_2 = [2, -3]
v_1, v_2


# In[5]:


def my_add(vector1, vector2):
    vector3 = [0, 0]
    vector3[0] = vector1[0] + vector2[0]
    vector3[1] = vector1[1] + vector2[1]
    return vector3

def my_add_1(vec1, vec2):
    
    s = len(vec1)
    result_vec = []
    
    for i in range(s):
        temp = vec1[i] + vec2[i]
        result_vec.append(temp)

    return result_vec


# In[6]:


my_add(v_1, v_2)


# In[8]:


v_1 = [1,3,1]
v_2 = [2,-3,6]
my_add_1(v_1, v_2)


# In[9]:


import random


# In[10]:


def my_create_vectors(m=5, n=2):
    # m, n = 2, 3
    my_vec = []
    for i in range(m):
        my_vec.append([])
        for j in range(n):
            t = random.randint(-10, 10)
            my_vec[i].append(t)
            
    return my_vec
v_s = my_create_vectors()
v_s


# In[11]:


def my_center(vec1, vec2):
    
    s = len(vec1)
    result_vec = []
    
    for i in range(s):
        temp = (vec1[i] + vec2[i])/2
        result_vec.append(temp)
    
    return result_vec


# In[14]:


v_1 = [1,3,1]
v_2 = [-2,-3,6]
my_center(v_1, v_2)


# In[15]:



def my_distance(v1, v2):
    s = len(v1)
    t = 0
    for i in range(s):
        t = t + (v1[i] - v2[i])**2
    
    return t**0.5


# In[16]:


vector_1 = [0,4,0]
vector_2 = [3,0,0]
my_distance(vector_1, vector_2)


# In[ ]:




