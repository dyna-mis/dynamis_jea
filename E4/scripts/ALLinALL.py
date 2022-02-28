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

for mod in ['add', 'sub']:
  for model in ['uniform', 'gaussian']:
            dirname = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
            result_path = Path(dirname + "\\" + '\dynamis_jea\OUTPUT\E4')
            assert result_path.is_dir()
            outPutName = os.path.dirname(os.path.dirname(__file__)) + '\plots'+"\\"+mod+'-'+model+'-'+'square'
            scatterPlot.getScatter_UPDATE_RATIO(result_path, model, mod,'no',outPutName)


