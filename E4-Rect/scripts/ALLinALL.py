import scatterPlot
import DATA
import collections
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from collections import OrderedDict
import copy
import os
from pathlib import Path
from pprint import pprint
instance_list = ["post_office_box",
                 "viewpoint_AT",
                 "post_CH",
                 "middle_hotels_CH",
                 "middle_hotels_AT",
                 ]

for mod in ['add', 'sub']:
  for model in ['uniform', 'gaussian']:
            dirname = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
            result_path = Path(os.path.join(dirname, "dynamis_jea", "OUTPUT", "E4_Rect"))
            assert result_path.is_dir()
            outPutName = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'plots', mod+'-'+model+'-'+'rectangle')
            scatterPlot.getScatter_UPDATE_RATIO(result_path, model, mod,'no',outPutName)


