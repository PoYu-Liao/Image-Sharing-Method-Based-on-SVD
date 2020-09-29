#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
import os
from PIL import Image

np.set_printoptions(threshold=np.inf)


# In[2]:


print('Loading.....')

def get_approx_matrix(u, sigma, v, rank): 
    m = len(u)
    n = len(v)
    a = np.zeros((m, n))
    k = 0
    while k < rank:
        uk = u[:, k].reshape(m, 1)
        vk = v[k].reshape(1, n)
        a += sigma[k] * np.dot(uk, vk)
        k += 1


    return a.astype("float")


# In[3]:


def uxs1(u, sigma, rank): 
    m = len(u)
    k = 0
    c = 0
    
    while k < rank:
        uk = u[:, k].reshape(m, 1)
        d = sigma[k] *uk
        k += 1
        if c==0:
            b = d
            
         
        elif c==1:
            ua = np.hstack((b, d))
           
        else:
            ua = np.hstack((ua, d))
        c+=1
            
    
    ua.astype("float")

    return ua


# In[4]:


def vxs1(v, rank): 
    n = len(v)
    cc = 0
    k = 0
    while k < rank:
        vk = v[k, :].reshape(1, n)
        k += 1
        if cc==0:
            temp = vk
            
         
        elif cc==1:
            vv = np.vstack((temp, vk))
           
        else:
            vv = np.vstack((vv, vk))
        cc+=1
       
        

    vv.astype("float")
   
    return vv


# In[5]:


filepath = "./model.jpg"


if os.path.isfile(filepath):
 
    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

    print('Building.....')
    a = np.array(img)
    u0, sigma0, v0 = np.linalg.svd(a)

    R = get_approx_matrix(u0, sigma0, v0, 200)

    usr = uxs1(u0, sigma0, 200)

    us1r, us2r, us3r, us4r = np.hsplit(usr, 4)
    
    savefolderpath1 = "./LS"
    if os.path.isdir(savefolderpath1):
        cv2.imwrite("./LS/ls1r.jpg", us1r)
        cv2.imwrite("./LS/ls2r.jpg", us2r)
        cv2.imwrite("./LS/ls3r.jpg", us3r)
        cv2.imwrite("./LS/ls4r.jpg", us4r)
        np.save('./LS/LS1', us1r)
        np.save('./LS/LS2', us2r)
        np.save('./LS/LS3', us3r)
        np.save('./LS/LS4', us4r)
    
    else: 
        try:
            os.makedirs(savefolderpath1)
            cv2.imwrite("./LS/ls1r.jpg", us1r)
            cv2.imwrite("./LS/ls2r.jpg", us2r)
            cv2.imwrite("./LS/ls3r.jpg", us3r)
            cv2.imwrite("./LS/ls4r.jpg", us4r)
            np.save('./LS/LS1', us1r)
            np.save('./LS/LS2', us2r)
            np.save('./LS/LS3', us3r)
            np.save('./LS/LS4', us4r)
        except PermissionError:
            print("權限不足。")
            os.system("pause")

    vr = vxs1(v0, 200)

    vs1r, vs2r, vs3r, vs4r = np.vsplit(vr, 4)
    savefolderpath2 = "./RS"
    if os.path.isdir(savefolderpath2):
        cv2.imwrite("./RS/rs1.jpg", vs1r)
        cv2.imwrite("./RS/rs2.jpg", vs2r)
        cv2.imwrite("./RS/rs3.jpg", vs3r)
        cv2.imwrite("./RS/rs4.jpg", vs4r)
        np.save('./RS/RS1', vs1r)
        np.save('./RS/RS2', vs2r)
        np.save('./RS/RS3', vs3r)
        np.save('./RS/RS4', vs4r)
        print('完成!!')
        os.system("pause")
    else:
        try:
            os.makedirs(savefolderpath2)
            cv2.imwrite("./RS/rs1.jpg", vs1r)
            cv2.imwrite("./RS/rs2.jpg", vs2r)
            cv2.imwrite("./RS/rs3.jpg", vs3r)
            cv2.imwrite("./RS/rs4.jpg", vs4r)
            np.save('./RS/RS1', vs1r)
            np.save('./RS/RS2', vs2r)
            np.save('./RS/RS3', vs3r)
            np.save('./RS/RS4', vs4r)
            print('完成!!')
            os.system("pause")
        except PermissionError:
            print("權限不足。")
            os.system("pause")

else:
  print("找不到model.jpg")
  os.system("pause")


# In[ ]:


'''銘傳大學 資傳系 專研第五組 製作人廖柏宇'''

