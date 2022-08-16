# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 14:05:45 2022

@author: MSI GF63
"""
from text_filter import *
line="* Pour les personnes morales : nom du site des travaux ou nom de la copropriété :"
position1=line.find("(")
position2=line.rfind(")")
removed=line[position1:position2+1]
extracted_line=line.replace(removed,"")
print(extracted_line)
l=extracted_line.split(":")
print(len(l))
print(isKeyValue(line))
#,v=To_KeyValue(line)
a="*"
print(a.upper())
k,v=To_KeyValue(line)
print(k)
#
print(v) 