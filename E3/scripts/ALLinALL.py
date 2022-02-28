import scatterPlot
import DATA
import collections
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from collections import OrderedDict
import copy

from pathlib import Path
from pprint import pprint
import os

'''
for mod in ['add','sub']:
     for data in ['uniform','gaussian']:
'''
for mod in ['mix']:
  for model in ['hamlets', 'peaks']:
        dirname = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
        result_path = Path(os.path.join(dirname, "dynamis_jea", "OUTPUT", "E23"))
        assert result_path.is_dir()
        outPutName = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'plots', mod+'-'+model+'-'+str(10000)+'-'+'square')
        scatterPlot.getScatter_UPDATE_SIZE(result_path, mod, model,'no',outPutName)


