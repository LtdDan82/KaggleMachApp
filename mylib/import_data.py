# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 20:11:46 2020

@author: LtdDan82
@github: https://github.com/LtdDan82
"""

import pandas as pd
import os
import glob

#%%
def get_filelist(path):
    '''
    Import all *.csv files in given path to a list
    
    Input: str or pathlike object
    Returns: list. List of Files
    '''
    #path = os.getcwd()
    try:
        os.chdir(path + '/data')
        filelist = glob.glob( '**.csv' )   
    except FileNotFoundError:
        filesinpath = os.listdir(path)
        filelist = [ filename for filename in filesinpath if filename.endswith(".csv") ]

    
     
    return filelist
#%%

def csv_to_dataframe(filelist):
    '''
    Loops through all files in "filelist" and generates pandas dataframes
    
    Input: list of str
    Returns: dict of pandas dataframes
    '''
    
    data = {}
    for file in filelist:
        data[file] = pd.read_csv(file)          
    return data
#%%
def get_alldata():
    '''
    Function that combines get_filelist and csv_to_dataframe function
    
    Input: None
    Returns: dict of pandas dataframes
    '''
    
    path = os.getcwd()
    print(path)
    filelist = get_filelist(path)
    alldata = csv_to_dataframe(filelist)
    
    return alldata


    