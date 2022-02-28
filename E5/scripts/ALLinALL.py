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



for mod in ['add', 'sub']:
    for model in ['uniform', 'gaussian']:
        print(mod, model)
        dirname = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
        result_path = Path(os.path.join(dirname, "dynamis_jea", "OUTPUT", "E5"))
        assert result_path.is_dir()
        outPutName = os.path.join(os.path.dirname(os.path.dirname(__file__)), mod + '-' + model + '-' + 'update' + '-' + 'square')
        linePlot.getLine_Runtime(result_path, mod, model, 'rect', outPutName)
        print("recompute")
        outPutName = os.path.join(os.path.dirname(os.path.dirname(__file__)),  mod + '-' + model + '-' + 'recompute' + '-' + 'square')
        linePlot.getLine_Runtime_recompute(result_path, mod, model, 'rect', outPutName)
