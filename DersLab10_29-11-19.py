#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import cv2


# In[ ]:


data_main_folder = "D:/DIP_course_data"
import os.path
dirs=[d for d in os.listdir(data_main_folder) if os.path.isdir(os.path.join())]
dirs


# In[ ]:


data_faces_of_class=np.zeros((1000,100*100+1))
folder_counter=-1
s=-1
for dir_ in dirs:
    folder_caounter=folder_counter+1
    
    new_folder = data_main_folder + "/" + dir_
    files = [d for d in os.listdir(new_folder) if os.path.isfile(os.path.join(new_folder, d))]
    for file_ in files:
        s = s + 1
        file_name_with_folder = new_folder + "/" + file_
        print(file_name_with_folder)
        ori_img = cv2.imread(file_name_with_folder)
        print(ori_img.shape)
        resized_img = cv2.resize(ori_img,(100,100))
        # img = cv2.resize(ori_img,(100,100))
        print(resized_img.shape)
        
        image_gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
        print(image_gray.shape)
        plt.imshow(image_gray)
        plt.show()
        
        image_gray_one_dim = image_gray.reshape(1,100*100)
        
        print(image_gray_one_dim.shape)
        data_faces_of_class[s,0] = folder_counter
        data_faces_of_class[s,1:100*100+1] = image_gray_one_dim
        # cv2.imshow('Original image', resized_img)
        # cv2.imshow('Gray image', image_gray)
        # print(dir_, files)
        

