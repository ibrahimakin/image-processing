#
my_list = [9,3,5,6,2,3,6]
#
print(my_list)
#
for i in my_list:
    print(i)
#
def my_function1():
    my_list = [9,3,5,6,2,3,6]
    for i in range(len(my_list)):
        print(i,my_list[i])
my_function1()
#
def my_function1(my_list=[9,3,5,6,2,3,6]):
    #my_list = [9,3,5,6,2,3,6]
    for i in range(len(my_list)):
        #print(i,my_list[i])
        my_list[i]=my_list[i]+1
    print(my_list)
#my_function1(['bir',2,3,4,54,5,56,6])
my_function1([1,2,3,4,54,5,56,6])
#
import numpy as np
mylist1 = np.array(list([9,3,5,6,2,3,6]))
print(mylist1)
#
mylist1+1
#
def my_function2(my_array=list([9,3,5,6,2,3,6])):
    return my_array+10
array2=my_function2()
print(array2)
#
import os
os.getcwd()
#
import numpy as np
import matplotlib.pyplot as plt
im1=plt.imread('comu.jpg')
plt.imshow(im1)
plt.show()
#
im1=plt.imread('comu.jpg')
i,j,p=im1.shape
im2=np.zeros((i,j,3),dtype=int)
for m in range(im1.shape[0]):
    for n in range(im1.shape[1]):
        im2[m,n,0]=im1[m,n,0]-25
        im2[m,n,0]=im1[m,n,0]
        im2[m,n,0]=im1[m,n,0]
        
plt.imshow(im2)
plt.show()
print(im2.shape)
#
def myf2(im100,s=5):
    im1=im100
    m,n,p=im1.shape
    im2=np.zeros((m,n,3),dtype=int)
    m,n,im2.shape
    for m in range(im1.shape[0]):
        for n in range(im1.shape[1]):
            im2[m,n,0]=im1[m,n,0]-25
            im2[m,n,0]=im1[m,n,0]
            im2[m,n,0]=im1[m,n,0]
    return im100
#
im1=plt.imread('comu.jpg')
plt.imshow(im1)
#plt.show()

def myf3(im500):
    
    m,n,p=im500.shape
    new_m=int(m/2)
    new_n=int(n/2)
    im600=np.zeros((new_m,new_n),dtype=int)
    
    for m in range(new_m):
        for n in range(new_n):
            s0=(im500[m,n,0]/3+im500[m,n,1]/3+im500[m,n,2]/3)
            
            #s1=(im500[m,n+1,0]+im500[m,n+1,1]+im500[m,n+1,2])/3
            
            #s2=(im500[m+1,n,0]+im500[m+1,n,1]+im500[m+1,n,2])/3
            
            #s3=(im500[m+1,n+1,0]+im500[m+1,n+1,1]+im500[m+1,n+1,2])/3
            
            #s=(s0+s1+s2+s3)/4
            im600[m,n]=int(s0)
            
    return im600
im3=myf3(im1)
plt.imshow(im3,cmap='gray')
plt.show(im3)
#
im5=plt.imread('comu.jpg')
#plt.imshow(im1)
#plt.show()

def myf4(im500):
    
    m,n,p=im500.shape
    new_m=int(m/2)
    new_n=int(n/2)
    im600=np.zeros((new_m,new_n,3),dtype=int)
    
    for m in range(0,im500.shape[0],2):
        for n in range(0,im500.shape[1],2):
            s0=(im500[m,n,0]/3+im500[m,n,1]/3+im500[m,n,2]/3)
            
            s1=(im500[m,n+1,0]/3+im500[m,n+1,1]/3+im500[m,n+1,2]/3)
            
            s2=(im500[m+1,n,0]/3+im500[m+1,n,1]/3+im500[m+1,n,2]/3)
            
            s3=(im500[m+1,n+1,0]/3+im500[m+1,n+1,1]/3+im500[m+1,n+1,2]/3)
            
            s=(s0+s1+s2+s3)/4
            im600[m,n]=int(s)
            
    return im600
im6=myf4(im5)
plt.imshow(im6)
plt.show(im6)
#
import numpy as np
def my_f_4(im_20):    #çözünürlüğü yarı yarıya düşür
    m,n,p=im_20.shape
    new_m=int(m/2)
    new_n=int(n/2)
    im_30=np.zeros((new_m,new_n,3),dtype=int)
    for m in range(new_m):
        for n in range(new_n):
            im_30[m,n,0]=int(im_20[m*2,n*2,0])
            im_30[m,n,1]=int(im_20[m*2,n*2,1])
            im_30[m,n,2]=int(im_20[m*2,n*2,2])
    return im_30
#
im_1=plt.imread('comu.jpg')
im_40=my_f_4(im_1)
im_50=my_f_4(im_40)
im_150=my_f_4(im_50)
plt.imshow(im_150)
#