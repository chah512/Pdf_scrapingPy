# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 10:54:13 2022

@author: MSI GF63
"""

import numpy as np
import re

#uppercase_reg="[A-Z]+( ([A-Z]|')+)*"
#siren_reg="[A-Z]+ [1-9]+"
#print(re.match(uppercase_reg, "TOTALENERGIES ELECTRICITE ET GAZ FRANCE").group())

def Special_accept(expression):
    uppercase_reg="[A-Z]+( ([A-Z]|')+)*"
    a=re.match(uppercase_reg, expression)
    if  a :
        if a.group()==expression:
            return True
    else:
        return False
    
    
def siren_accept(expression):
    siren_reg="[A-Z]+ [0-9]+"
    b=re.match(siren_reg,expression)
    if b :
        if b.group()==expression:
            return True
        else:
            return False
    else:
        return False
    
        


def isKeyValue(line):
    #check for xxxx(xxx: xxxx): xxxxx Form (accepted)
    position1=line.find("(")
    position2=line.rfind(")")
    removed=line[position1:position2+1]
    extracted_line=line.replace(removed,"")
    l=extracted_line.split(":")
    if len(l)==2 :
        #check for NB: xxxxxx form (refused)
        if l[0]=="NB " or l[1]=="":
            return False
        else :
            if line.upper()[0]==line[0]:
                #print(line.upper()[0])# just to analyse code
                return True
            else:
                return False
    else:
        if len(l)==3:
            if l[0]=="NB ":
                return False
            else:
                if line.upper()[0]==line[0]:
                    #print(line.upper()[0])# just to analyse code
                    return True
                else:
                    return False
        else:
            return False


def optimized_clean(expression):
    if(expression==""):
        return expression
    else:
        reg_cleanse="[^* ].*[^* \.]"
        if re.search(reg_cleanse, expression):
            return re.search(reg_cleanse,expression).group()
        else:
            return expression.strip()
    
        
        
def To_KeyValue(line):
    position1=line.find("(")
    position2=line.find(")")
    removed=line[position1:position2+1]
    extracted_line=line.replace(removed,"")
    l=extracted_line.split(":")
    if len(l)==2:
        k=optimized_clean(l[0])
        v=optimized_clean(l[1])#need cleanse
    else:
        if len(l)==3:
            k=optimized_clean(l[0])+"("+optimized_clean(l[1])+")"
            v=optimized_clean(l[2])
    return k,v
    
def Check_PrKey(line):
    reg="[A-Z](\w| )*:"
    if re.match(reg,line):
        return True
    else:
        return False
def Is_Key_Value_err(line):
    reg="\*[A-Z].*"
    if re.match(reg,line):
        l=line.split(" ")
        if l[-1].upper()==l[-1]:
            return True 
    return False    
def To_Key_Value_err(line):
    reg="\*[A-Z].*"
    if re.match(reg,line):
        l=line.split(" ")
        if l[-1].upper()==l[-1]:
            v=l[-1].strip()
            k=optimized_clean(" ".join(l[:-1]))
            return k,v 