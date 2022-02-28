#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:16:52 2019

@author: guangping

"""
import DATA
import pandas as pd
import linePlot
from pathlib import Path
import os


ymin = 0
ymax= 0
for mod in ['add', 'sub']:
    for model in ['uniform', 'gaussian']:
        dirname = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        result_path = Path(dirname + "\\" + '\dynamis_jea\OUTPUT\E5_Rect')
        outPutName = os.path.dirname(os.path.dirname(__file__)) + '\plots'+"\\"+ mod + '-' + model + '-' + 'update' + '-' + 'rectangle'
        if mod == "add" and model == "uniform":
            ymin = 0.0008
            ymax = 5
        if mod == "sub" and model == "uniform":
            ymin = 0.0008
            ymax = 5
        if mod == "add" and model == "gaussian":
            ymin = 0.0008
            ymax = 5
        if mod == "sub" and model == "gaussian":
            ymin = 0.0008
            ymax = 5




        linePlot.getLine_Runtime(result_path, mod, model, 'rect', outPutName,ymin, ymax)


        if mod == "add" and model == "uniform":
            ymin = 0.008
            ymax = 50
        if mod == "sub" and model == "uniform":
            ymin = 0.008
            ymax = 50
        if mod == "add" and model == "gaussian":
            ymin = 0.008
            ymax = 50
        if mod == "sub" and model == "gaussian":
            ymin = 0.008
            ymax = 50
        outPutName = os.path.dirname(os.path.dirname(__file__)) + '\plots'+"\\"+ mod + '-' + model + '-' + 'recompute' + '-' + 'rectangle'
        linePlot.getLine_Runtime_recompute(result_path, mod, model, 'rect', outPutName, ymin, ymax)
