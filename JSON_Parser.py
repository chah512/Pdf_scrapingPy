# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 13:44:40 2022

@author: MSI GF63
"""

import json
import ast
from text_filter import *
import pandas as pd

    
def clean_data(data_name):    
    f=open('Documents2scrape\\JSON_FILES\\'+data_name+'.json')
    data = json.load(f)
    #print(data)
    key_value_list=[]
    key_list=[]
    n=0
    for i in range(len(data)):
        sentence=data[i]['Text']
        if data[i]['Geometry']['BoundingBox']['Height']>=0.01 and data[i]['Geometry']['BoundingBox']['Top']<=0.19 :
            if siren_accept(sentence):
                kv=sentence.split(" ")
                key_value_list.append((kv[0],kv[1]))
                

            #print('siren')#to analyse code
            else:
                if Special_accept(sentence):
                    switcher = {
                             0: "Type de document",
                             1: "Titre de document",
                             2: "Société",
                                }
                    custom_key=switcher.get(n,"inconnue"+str(n))
                    n=n+1
                    key_value_list.append((custom_key,sentence))
                    #print("special")#to analyse code
                else:
                    if isKeyValue(sentence):
                        if To_KeyValue(sentence)[0] in key_list:
                            print(To_KeyValue(sentence)[0]+"--------- already taken")
                            for j in range(len(key_value_list)):
                                if key_value_list[j][0]==To_KeyValue(sentence)[0]:
                                    if To_KeyValue(sentence)[1] not in key_value_list[j]:
                                        key_value_list[j].append(To_KeyValue(sentence)[1])
                                 
                                    
                        else:
                            print(To_KeyValue(sentence)[0]+":"+To_KeyValue(sentence)[1]+"--------- new take")
                            key_value_list.append([To_KeyValue(sentence)[0],To_KeyValue(sentence)[1]])
                            key_list.append(To_KeyValue(sentence)[0])
                            #print("(:) form")#to analyse code
                    else:
                         if Is_Key_Value_err(sentence):
                             k,v=To_Key_Value_err(sentence)
                             if k=="Le":
                                 k="Date de Document"
                             if k in key_list:
                                print(k+"----------already taken")
                                for j in range(len(key_value_list)):
                                    if key_value_list[j][0]==k:
                                        if v not in key_value_list[j]:
                                            key_value_list[j].append(v)
                             else:
                                 print(k+":"+v+"--------- new take")
                                 key_value_list.append([k,v])
                                 key_list.append(k)    
        else:
            if isKeyValue(sentence):
                if To_KeyValue(sentence)[0] in key_list:
                    print(To_KeyValue(sentence)[0]+"--------- already taken")
                    for j in range(len(key_value_list)):
                        if key_value_list[j][0]==To_KeyValue(sentence)[0]:
                            if To_KeyValue(sentence)[1] not in key_value_list[j]:
                                key_value_list[j].append(To_KeyValue(sentence)[1])
                         
                            
                else:
                    print(To_KeyValue(sentence)[0]+":"+To_KeyValue(sentence)[1]+"--------- new take")
                    key_value_list.append([To_KeyValue(sentence)[0],To_KeyValue(sentence)[1]])
                    key_list.append(To_KeyValue(sentence)[0])
                    #print("(:) form")#to analyse code
            else:
                 if Is_Key_Value_err(sentence):
                     k,v=To_Key_Value_err(sentence)
                     if k=="Le":
                         k="Date de Document"
                     if k in key_list:
                        print(k+"----------already taken")
                        for j in range(len(key_value_list)):
                            if key_value_list[j][0]==k:
                                if v not in key_value_list[j]:
                                    key_value_list[j].append(v)
                     else:
                         print(k+":"+v+"--------- new take")
                         key_value_list.append([k,v])
                         key_list.append(k)       
    final_list=[]                
    for i in range(len(key_value_list)):
        temp_value=key_value_list[i][1::]
        temp_value=tuple(temp_value)
        final_list.append((key_value_list[i][0],temp_value))
    kv_dict=dict(final_list)
    #print(final_list)
    extracted_json=json.dumps(kv_dict,ensure_ascii=False)
    print(extracted_json) 
    with open("Outputs\\json\\"+data_name+'_cleaned.json',"w",encoding='utf-8') as outfile:
        outfile.write(extracted_json)    
#clean_data("formatted_page_1")

def json_to_csv(json_data):
    pdobj=pd.read_json("Outputs\\json\\"+json_data+'.json',orient='index')
    pdobj.to_csv('Outputs\\csv\\'+json_data+'(csv).csv',index=True)
    
    
    
clean_data('formatted_page_6')
json_to_csv('formatted_page_6_cleaned')