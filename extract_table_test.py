# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 10:13:05 2022

@author: MSI GF63
"""

import json
import ast
import re
import pandas as pd
import csv
#from extract_table_test import *


def extract_table_position(data_name):
    f=open('Documents2scrape\\JSON_FILES\\'+data_name+'.json')
    data = json.load(f)
    reg="Tableau [A-Z]"
    reg2="\+[0-9| ]+"
    l=[]
    flag=[]
    #print(data[53]['Text'])
    for i in range(len(data)):
        if re.match(reg,data[i]['Text']):
            l.append(i)
            flag.append(data[i]['Text'])
        if re.match(reg2,data[i]['Text']):   
            j=i
            if not re.match(reg2,data[j+1]['Text']):     
                 l.append(j)
    return l

def extract_table(data_name,positions):
    f=open('Documents2scrape\\JSON_FILES\\'+data_name+'.json')
    data = json.load(f)
    table_number=len(positions)/2
    tables_list=[]
    for i in range(len(positions)):
        if positions[i]%2==0:
            Li1=[]
            Li2=[]
            Li3=[]
            table=[] 
            for j in range(positions[i]+1,positions[i+1]+1,1):
                left=data[j]['Geometry']['BoundingBox']['Left']
                #print(left)
                #print(data[j]['Text'])
                if left>=0.61:
                    Li3.append(data[j]['Text'])
                if left>=0.32 and left<=0.6:
                    Li2.append(data[j]['Text'])
                if left<=0.3 and left>=0.068:
                    Li1.append(data[j]['Text'])

            
            while len(Li2)>len(Li1):
                Li2[0]=Li2[0] +" " +Li2[1]
                del Li2[1]
            while len(Li3)>len(Li1):         
                Li3[0]=Li3[0] +" " +Li3[1]
                del Li3[1]
   
            for k in range(len(Li1)):
                Line=[]
                Line.append(Li1[k])
                Line.append(Li2[k])
                Line.append(Li3[k])
                table.append(Line)
            tables_list.append(table)    
    return tables_list

def csvTable_To_json(table_name):
    json_array=[]
    with open('Outputs\\csv\\'+table_name+'.csv') as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            json_array.append(row)
    with open('Outputs\\json\\'+table_name+'(json).json', 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(json_array,ensure_ascii=False, indent=4)
        jsonf.write(jsonString)    

def extract_table_in_files(data_name):
    p=extract_table_position(data_name)
    print(p)
    l=extract_table(data_name, p)
    #1er table as dataframe
    for i in range(len(l)):
        t1=l[i]
        char=i+65               
        columns=t1[0]
        del t1[0]
        df=pd.DataFrame(t1)
        df.columns=columns
        print(df)
        df.to_csv('Outputs\\csv\\'+data_name+'_table_'+chr(char)+'.csv', index=False)
        csvTable_To_json(data_name+'_table_'+chr(char))



                

        
        
#csvTable_To_json('formatted_page_5_table_A')
    
