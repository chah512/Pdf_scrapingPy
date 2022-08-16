# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 08:51:47 2022

@author: MSI GF63
"""

import numpy as np
import cv2
from PIL import Image
from matplotlib import pyplot as plt
img = cv2.imread('Documents2scrape\\Converted_images\\image_AH 0.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = cv2.resize(img, (2480,3508), fx=0.5, fy=0.5) 
vals = img.mean(axis=1).flatten()
# plot histogram with 255 bins
b, bins, patches = plt.hist(vals, 255)
plt.xlim([0,255])
plt.show()
print(img.shape)

