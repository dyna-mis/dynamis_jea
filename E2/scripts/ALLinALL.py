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

for instance in instance_list:
        for mod in ['mix']:
            dirname = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
            result_path = Path(os.path.join(dirname, "dynamis_jea", "OUTPUT", "E23")) 
            print(result_path)
            assert result_path.is_dir()
            outPutName = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'plots', mod+'-'+instance+'-'+'square')
            scatterPlot.getScatter_UPDATE_RATIO(result_path, instance, mod,'no',outPutName)
