# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 09:51:42 2022

@author: MSI GF63
"""

from pdf2image import convert_from_path, convert_from_bytes

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
def convert_pdf(pdf):
   path='Documents2scrape\\'+pdf
   l=path.split('\\')
   file=l[-1]
   pdf_name=file.split('.')[0]
   #print(pdf_name)
   images=convert_from_path(path)

   save_path="Documents2scrape\\Converted_images\\"   
   for i,image in enumerate(images):
       fname = "image_"+pdf_name+" " + str(i) + ".png"
       image.save(save_path+fname, "PNG")
    
        
