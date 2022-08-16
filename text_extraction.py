# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 14:22:22 2022

@author: MSI GF63
"""

import numpy as np
import cv2
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'



def ocr_core(image):
    
    text=pytesseract.image_to_string(image,lang='fra',config='-c page_separator=""')
    return text
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
def remove_noise(image):
    return cv2.medianBlur(image,5)
def thresholding(image):
    #need thrershold optimization !!!!!!!@TODO/TO SEARCH
    return cv2.threshold(image,127,255,cv2.THRESH_BINARY )
def extract_txt(image_name):
    img = cv2.imread('Documents2scrape\\Converted_images\\'+image_name)
    img = cv2.resize(img, (0,0), fx=0.9, fy=0.9) 
    img=get_grayscale(img)
    #img=thresholding(img)[1]
    print(ocr_core(img))
    #img2=get_grayscale(img2)
    cv2.imshow('Image', img) 
    cv2.waitKey(0)

    # Find the contours in the image and store them in an array
    #contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #text_contours = cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

    # Show the contours
    #cv2.imshow('Contours', text_contours)
    #cv2.waitKey(0)
    #text = pytesseract.image_to_string(img, lang='eng')
    text_file = open("Documents2scrape\\Converted_images\\AllText.txt", "w")
    text_file.write(ocr_core(img[1]))   
    
extract_txt("image_AH 0.png")   
