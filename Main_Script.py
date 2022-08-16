# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 09:29:37 2022

@author: MSI GF63
"""

from text_filter import *
from extract_table_test import *
from JSON_Parser import *

for i in range(6):
    clean_data('formatted_page_'+str(i+1))
    json_to_csv('formatted_page_'+str(i+1)+'_cleaned')
    extract_table_in_files('formatted_page_'+str(i+1))
        
    
