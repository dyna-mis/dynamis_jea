#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 10:57:56 2019

@author: guangping
"""


# libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

import algorithm
import modifications
import seaborn as sns
from matplotlib.font_manager import FontProperties
import DATA
import math

def get_marks_list():
    return algorithm.marks_list;

def export_legend(legend, filename="D:\GIT\Python\dynamis_jea_plots\E1\plots\legend.pdf"):
    fig  = legend.figure
    fig.canvas.draw()
    bbox  = legend.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig(filename, dpi="figure", bbox_inches=bbox)

def logRound(x):
    log_x =math.log(x,10)
    return pow(10,math.ceil(log_x)-1)


#ymax = 1.01
def draw_scatter_ratio(df,x_axis_name,y_axis_name, name, x_min, x_max, y_min, y_max):
    fig = plt.figure()
    ax = fig.add_axes([0.13, 0.2, 0.99, 0.99])
    sns.set()

    sns_plot = sns.lmplot( x=x_axis_name, y=y_axis_name, data=df, fit_reg=False, hue='z', palette=algorithm.color_dict,
                           markers=get_marks_list(),legend=False,scatter_kws={'alpha':0.4,"s": 30}, hue_order=algorithm.algo_list)
    sns_plot.set(xscale="log")
    fontP = FontProperties()
    fontP.set_size('small')

    leg= plt.legend(loc='lower right', prop=fontP,frameon=False, labels=algorithm.algo_list)


    xmin,xmax,ymin,ymax = plt.axis()
    #plt.xlim([logRound(xmin),xmax])
    # ratio used
    plt.xlim([x_min,x_max])
    plt.ylim([ymin,ymax])

    # Move the legend to an empty part of the plot

    for lh in leg.legendHandles:
        lh.set_alpha(1)
        plt.figure()


    sns_plot.savefig(name+".pdf")
    plt.figure()



def scatter_json(scatter_list,x_data_name, y_data_name, x_axis_name, y_axis_name):
    runTime = []
    quality = []
    z= []
    for key,value in scatter_list.fL_data.items():
       runTime.extend(value.f_data[x_data_name])
       quality.extend(value.f_data[y_data_name])
       for d in value.f_data[y_data_name]:
            z.append(key)
#    return pd.DataFrame({'runtime[s]': runTime, 'quality[%]': quality,'z':z})
    df = pd.DataFrame({x_axis_name: runTime, y_axis_name: quality,'z':z})
    df = df.sample(frac=1).reset_index(drop=True)
    return df
class scatter_DATA:
    mod_type= "the type of modification"
    discription ="scatter_data"
    data= {}
    df = "panda dataFrame" 




def getScatter_UPDATE_RATIO(folderName, instance, mod, skipName,outPutName):
    x = DATA.folderList(folderName,instance, mod,skipName)
    scatter_date =scatter_json(x,'updateFullTime_milisecond','update sizeRatio','runtime[ms]','update solution size(ratio)')

    xmin = 0.00008
    xmax = 1.2
    ymin = 200
    ymax= 1.01

    draw_scatter_ratio(scatter_date,'runtime[ms]','update solution size(ratio)',outPutName,xmin, xmax, ymin, ymax)



