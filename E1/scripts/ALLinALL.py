import scatterPlot
from pathlib import Path
import os


'''
for mod in ['add','sub']:
     for data in ['uniform','gaussian']:
'''

for mod in ['add', 'sub']:
  for model in ['uniform', 'gaussian']:
        result_path = Path('../../../dynamis_jea/OUTPUT/E1')
        print(result_path)
        assert result_path.is_dir()
        outPutName = os.path.dirname(os.path.dirname(__file__)) + '\plots'+"\\"+mod+'-'+model

        scatterPlot.getScatter_UPDATE_SIZE(result_path, mod, model,'no',outPutName)
