#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 10:57:56 2019

@author: guangping
"""


# libraries

import pandas as pd
import numpy as np
import algorithm
import modifications
import random
import os

#code
    
#TODO: open one file
def print_json(X):
    print("get json file")    
    with open('RESULT/zurichCarsharing-0.100000-0-garrow.json') as json_file:
        X.data = json.load(json_file)
        # Data
        X.df=pd.DataFrame({'x': X.data["updateTime"], 'y1': X.data["updateTime"], 'y2': X.data["updateTime"], 'y3': X.data["updateTime"]})

def spagetti_json(X):
    # Make a data frame
    X.df=pd.DataFrame({'x': range(1,11), 'cg': np.random.randn(10), 'rs': np.random.randn(10)+range(1,11), 'sl': np.random.randn(10)+range(11,21), 'slk': np.random.randn(10)+range(6,16), 
                 'arrow': np.random.randn(10)+range(4,14)+(0,0,0,0,0,0,0,-3,-8,-6), 'gsl': np.random.randn(10)+range(2,12), 'gslk': np.random.randn(10)+range(5,15), 
                 'garrow': np.random.randn(10)+range(4,14)})    
def box_json(X):
    a = pd.DataFrame({ 'algorithm' : np.repeat('A',500), 'runtime[s]': np.random.normal(10, 5, 500) })
    b = pd.DataFrame({ 'algorithm' : np.repeat('B',500), 'runtime[s]': np.random.normal(13, 1.2, 500) })
    c = pd.DataFrame({ 'algorithm' : np.repeat('C',20), 'runtime[s]': np.random.normal(25, 4, 20) })
    d = pd.DataFrame({ 'algorithm' : np.repeat('D',100), 'runtime[s]': np.random.uniform(12, size=100) })
    X.df=a.append(b).append(c).append(d)   

def violin_json(X):
    a1 = pd.DataFrame({ 'algorithm' : np.repeat('cg',500), 'runtime[s]': np.random.normal(10, 5, 500),'category' : np.repeat('1000',500) })
    a2 = pd.DataFrame({ 'algorithm' : np.repeat('cg',500), 'runtime[s]': np.random.normal(10, 5, 500),'category' : np.repeat('2000',500) })
    a3 = pd.DataFrame({ 'algorithm' : np.repeat('cg',500), 'runtime[s]': np.random.normal(10, 5, 500),'category' : np.repeat('4000',500) })
    b1 = pd.DataFrame({ 'algorithm' : np.repeat('rs',500), 'runtime[s]': np.random.normal(10, 5, 500),'category' : np.repeat('1000',500) })
    b2 = pd.DataFrame({ 'algorithm' : np.repeat('rs',500), 'runtime[s]': np.random.normal(10, 5, 500),'category' : np.repeat('2000',500) })
    b3 = pd.DataFrame({ 'algorithm' : np.repeat('rs',500), 'runtime[s]': np.random.normal(10, 5, 500),'category' : np.repeat('4000',500) })
    c1 = pd.DataFrame({ 'algorithm' : np.repeat('sl',500), 'runtime[s]': np.random.normal(10, 5, 500),'category' : np.repeat('1000',500) })
    c2 = pd.DataFrame({ 'algorithm' : np.repeat('sl',500), 'runtime[s]': np.random.normal(10, 5, 500),'category' : np.repeat('2000',500) })
    c3 = pd.DataFrame({ 'algorithm' : np.repeat('sl',500), 'runtime[s]': np.random.normal(10, 5, 500),'category' : np.repeat('4000',500) })
    X.df=a1.append(a2).append(a3).append(b1).append(b2).append(b3).append(c1).append(c2).append(c3)   


# for one category, one mod and one algo
def get_folder(X,folder):
    for filename in os.listdir(folder):
        with open(os.path.join(folder, filename)) as json_file:
            X.data = merge_dols(turnDict(X.data),turnDict(json.load(json_file)))
    decimalDict(X.data)
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    