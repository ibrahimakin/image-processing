#
my_list_1=[2,4,3,5,6,3,3,2,1] #ortalama
t=0
s=0
for i in my_list_1:
    s=s+1
    t=t+i
mean_1=t/s
mean_1
#
def my_f_1(my_list_1=[2,4,3,5,6,3,3,2,1]):
    t=0
    s=0
    for i in my_list_1:
        s=s+1
        t=t+i
    mean_2=t/s
    
    #varyans
    t=0
    s=0
    for i in my_list_1:
        s=s+1
        t=t+(i-mean_2)*(i-mean_2)
    var_2=t/(s-1)
    return mean_2,var_2
my_f_1()
#
my_histogram={}
for i in my_list_1:
    if i in my_histogram.keys():
        my_histogram[i]=my_histogram[i]+1
    else:
        my_histogram[i]=1
my_histogram
#
import matplotlib.pyplot as plt
import numpy as np
#
image_1=plt.imread('comu.jpg')
image_1.ndim,image_1.shape
#
m,n,p=image_1.shape
m,n,p
#
my_histogram={}
for i in range(m):
    for j in range(n):
        if image_1[i,j,0] in my_histogram.keys():
            my_histogram[image_1[i,j,0]]=my_histogram[image_1[i,j,0]]+1
        else:
            my_histogram[image_1[i,j,0]]=1
#
my_histogram
#
def my_f_2(image_1=plt.imread('comu.jpg')):
    #image_1.ndim,image_1.shape
    m,n,p=image_1.shape
    #m,n,p
    my_histogram={}
    for i in range(m):
        for j in range(n):
            if image_1[i,j,0] in my_histogram.keys():
                my_histogram[image_1[i,j,0]]=my_histogram[image_1[i,j,0]]+1
            else:
                my_histogram[image_1[i,j,0]]=1
    return my_histogram
#
x=[]
y=[]
for key in my_histogram.keys():
    x.append(key)
    y.append(my_histogram[key])
plt.plot(x,y)
plt.show()
plt.bar(x,y)
plt.show()
#
def my_f_3(my_histogram=my_f_2()):
    x=[]
    y=[]
    for key in my_histogram.keys():
        x.append(key)
        y.append(my_histogram[key])
    return x,y
x,y=my_f_3()
plt.bar(x,y)
plt.show()
#