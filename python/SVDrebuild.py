#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
import os
from PIL import Image

np.set_printoptions(threshold=np.inf)


# In[2]:


def loadingdata(filepath):
    if os.path.isfile(filepath):
        file = np.load(filepath)
        return file
    else:
        print('File not found')
    


# In[3]:


print('loading data.....')

#us1r = np.load('./LS/LS1.npy')
us1r = loadingdata('./LS/LS1.npy')
us2r = loadingdata('./LS/LS2.npy')
us3r = loadingdata('./LS/LS3.npy')
us4r = loadingdata('./LS/LS4.npy')
vs1r = loadingdata('./RS/RS1.npy')
vs2r = loadingdata('./RS/RS2.npy')
vs3r = loadingdata('./RS/RS3.npy')
vs4r = loadingdata('./RS/RS4.npy')

print('loading completed')


# In[4]:


print('Rebuilding.....')

um1r = np.hstack((us1r, us2r))
vm1r = np.vstack((vs1r, vs2r))
um2r = np.hstack((um1r, us3r))
vm2r = np.vstack((vm1r, vs3r))
um3r = np.hstack((um2r, us4r))
vm3r = np.vstack((vm2r, vs4r))



try:
    savefolderpath = './re'
    os.makedirs(savefolderpath)
    test1 = np.dot(us1r, vs1r)
    cv2.imwrite("./re/r1.jpg", test1)
    test2 = np.dot(um1r, vm1r)
    cv2.imwrite("./re/r2.jpg", test2)
    test3 = np.dot(um2r, vm2r)
    cv2.imwrite("./re/r3.jpg", test3)
    test4 = np.dot(um3r, vm3r)
    cv2.imwrite("./re/r4.jpg", test4)
    print('完成!!')
    os.system("pause")
    
except FileExistsError:
    test1 = np.dot(us1r, vs1r)
    cv2.imwrite("./re/r1.jpg", test1)
    test2 = np.dot(um1r, vm1r)
    cv2.imwrite("./re/r2.jpg", test2)
    test3 = np.dot(um2r, vm2r)
    cv2.imwrite("./re/r3.jpg", test3)
    test4 = np.dot(um3r, vm3r)
    cv2.imwrite("./re/r4.jpg", test4)
    print('完成!!')
    os.system("pause")
except PermissionError:
    print("權限不足。")
    os.system("pause")


# In[5]:


'''銘傳大學 資傳系 專研第五組 製作人廖柏宇'''

