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


def export_legend(legend, filename="D:\GIT\Python\dynamis_jea_plots\E1-Rect\plots\legend.pdf"):
    fig  = legend.figure
    fig.canvas.draw()
    bbox  = legend.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig(filename, dpi="figure", bbox_inches=bbox)

def logRound(x):
    log_x =math.log(x,10)
    return pow(10,math.ceil(log_x)-1)
#code
def draw_scatter(df,x_axis_name,y_axis_name,name, x_min, x_max, y_min, y_max):
    fig = plt.figure()
    ax = fig.add_axes([0.13, 0.2, 0.99, 0.99])
    sns.set()
    # Use the 'hue' argument to provide a factor variable  #'edgecolor':'k'
    sns_plot = sns.lmplot( x=x_axis_name, y=y_axis_name, data=df,
                           fit_reg=False, hue='z', palette=algorithm.color_dict,
                           markers=algorithm.marks_list,
                           legend=False,scatter_kws={'alpha':0.5,"s": 80},
                            hue_order=algorithm.algo_list)
    #sns_plot = sns.lmplot( x=x_axis_name, y=y_axis_name, data=df, fit_reg=False, hue='z',legend=False,scatter_kws={'alpha':0.4,"s": 20})
    sns_plot.set(xscale="log")
    fontP = FontProperties()
    fontP.set_size('small')



    handles, labels = plt.gca().get_legend_handles_labels()
    leg = ax.legend(handles, labels,
                     loc='lower right', prop=fontP, frameon=1, bbox_to_anchor=(1.05, 1), ncol=10)


    #xmin,xmax,ymin,ymax = plt.axis()
    plt.xlim([logRound(x_min),x_max])
    # ratio used

    plt.xlim([x_min,x_max])
    plt.ylim([y_min,y_max])
    ax.get_legend().set_visible(False)
    # Move the legend to an empty part of the plot

    for lh in leg.legendHandles:
        lh.set_alpha(1)
        plt.figure()


    sns_plot.savefig(name+".pdf")
    plt.figure()
    ax.get_legend().set_visible(True)
    #export_legend(leg)


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

def getScatter_UPDATE_SIZE(folderName,mod, model, skipName,outPutName):
    x = DATA.folderList(folderName,mod, model,skipName)
    scatter_date =scatter_json(x,'updateFullTime_milisecond','updateSize','runtime[ms]','solution size |A|')
    xmin = 0.00008
    xmax = 12
    #ymin = 450
    ymin = 400
    ymax= 700
    if model == "gaussian" and mod == "add":
        xmin = 0.00008
        xmax = 50
        #ymin = 350
        ymin = 300
        ymax = 600
    if model == "gaussian" and mod == "sub":
        xmin = 0.00008
        xmax = 50
        ymin = 300
        #ymin = 350
        ymax = 500


    draw_scatter(scatter_date,'runtime[ms]','solution size |A|',outPutName, xmin, xmax, ymin, ymax)

