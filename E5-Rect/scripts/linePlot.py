#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 10:57:56 2019

@author: guangping
"""


# libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import DATA

import algorithm

def getLine_Runtime(result_path, mod, model, skipName, outPutName,ymin, ymax):
    frames = []
    for size in ['-1000-', '-2000-', '-4000-', '-8000-', '-16000-', '-32000-']:
        x = DATA.folderList(result_path, mod, model, size, skipName, True)
        df = runtime_json(x, 'updateFullTime_milisecond', 'updateSize', 'runtime[ms]', 'solution size |A|', size)
        frames.append(df)
    result = pd.concat(frames)
    draw_Runtimes(result, outPutName,ymin, ymax)


def getLine_Runtime_recompute(result_path, mod, model, skipName, outPutName, ymin, ymax):
    frames = []
    for size in ['-1000-', '-2000-', '-4000-', '-8000-', '-16000-', '-32000-']:
        x = DATA.folderList(result_path, mod, model, size, skipName, False)
        df = runtime_json(x, 'updateFullTime_milisecond', 'updateSize', 'runtime[ms]', 'solution size |A|',
                                 size)
        frames.append(df)
    result = pd.concat(frames)
    draw_Runtime_recompute(result, outPutName, ymin, ymax)





def export_legend(legend, filename="D:\GIT\Python\dynamis_jea_plots\E5-Rect\plots\legend.pdf"):
    fig  = legend.figure
    fig.canvas.draw()
    bbox  = legend.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig(filename, dpi="figure", bbox_inches=bbox)


def runtime_json(scatter_list,x_data_name, y_data_name, x_axis_name, y_axis_name,size):
    runTime = []
    quality = []
    s= []
    z= []
    size = size[1: -1]
    for key,value in scatter_list.fL_data.items():
       runTime.extend(value.f_data[x_data_name])
       for d in value.f_data[x_data_name]:
            quality.append(size)
            z.append(key)
            s.append(size)
    return pd.DataFrame({x_axis_name: runTime, y_axis_name: quality,'algorithm':z,'instance size':s})
def draw_Runtimes(result,name,ymin, ymax):
     sns.set(style="darkgrid",rc={"lines.linewidth": 10})
     sns.set(style="darkgrid")

     fig = plt.figure()
     ax = fig.add_axes([0.13, 0.2, 0.99, 0.99])
     pq = sns.lineplot(x='instance size', y= 'runtime[ms]',data=result,hue='algorithm',
                       palette=algorithm.color_dict,markers=True,err_style='bars',
                       size=0.5,sort=False, hue_order=algorithm.algo_list)
     w= pq.lines[0].get_linewidth()
     line_sty = "--"
     line_sty_2 = 'none'
     ax.lines[3].set_linestyle(line_sty)
     ax.lines[7].set_linestyle(line_sty)
#     ax.lines[11].set_linestyle(line_sty)
#     ax.lines[15].set_linestyle(line_sty)
     for e in ax.lines:
         e.set_linewidth(1.5)
     ax.lines[3].set_linewidth(1.5)
     ax.lines[7].set_linewidth(1.5)
#     ax.lines[11].set_linewidth(1.5)
#     ax.lines[15].set_linewidth(1.5)
     ax.lines[2].set_linestyle(line_sty_2)
     ax.lines[6].set_linestyle(line_sty_2)
#     ax.lines[10].set_linestyle(line_sty_2)
#     ax.lines[14].set_linestyle(line_sty_2)
     #pq._legend.remove()
     pq.set_yscale('log')
     #plt.ylim([0.0008,10000])
     #pq.set_xscale('log')
     plt.ylim([ymin,ymax])
     leg = ax.legend(algorithm.algo_list,loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=10)
     ax.get_legend().set_visible(False)
     #ax.legend(['line','g-line','grid','g-grid','grid-2','g-grid-2','grid-4','g-grid-4','MIS-ORS','MIS-graph'],
             #  bbox_to_anchor=(1, 1), loc='bottom', borderaxespad=0.)
     plt.savefig(name+".pdf", bbox_inches = "tight")
     plt.figure()
     export_legend(leg)
def draw_Runtime_recompute(result,name,ymin, ymax):
     sns.set(style="darkgrid",rc={"lines.linewidth": 2.5})
     fig = plt.figure()
     ax = fig.add_axes([0.13, 0.2, 0.99, 0.99])
     pq = sns.lineplot(x='instance size', y= 'runtime[ms]',data=result,hue='algorithm',palette=algorithm.color_dict,markers=True,err_style='bars',size=0.5,sort=False,)
     w= pq.lines[0].get_linewidth()
     line_sty = "--"
     line_sty_2 = 'none'
     ax.lines[3].set_linestyle(line_sty)
     ax.lines[7].set_linestyle(line_sty)
#     ax.lines[11].set_linestyle(line_sty)
#     ax.lines[15].set_linestyle(line_sty)
     for e in ax.lines:
         e.set_linewidth(1.5)
     ax.lines[2].set_linestyle(line_sty_2)
     ax.lines[6].set_linestyle(line_sty_2)
#     ax.lines[10].set_linestyle(line_sty_2)
 #    ax.lines[14].set_linestyle(line_sty_2)
     #pq._legend.remove()
     pq.set_yscale('log')
     plt.ylim([ymin, ymax])
     #pq.set_xscale('log')
     #plt.ylim([0.001,1.2])
     leg = ax.legend(algorithm.algo_list,loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=3)
     ax.get_legend().set_visible(False)
     #ax.legend(['line','g-line','grid','g-grid','grid-2','g-grid-2','grid-4','g-grid-4','MIS-ORS','MIS-graph'],
               #bbox_to_anchor=(1, 1), loc='bottom', borderaxespad=0.)
     plt.savefig(name+".pdf", bbox_inches = "tight")
     plt.figure()
     ax.get_legend().set_visible(True)
     leg_lines = leg.get_lines()
     leg_lines[1].set_linestyle(":")
#     leg_lines[3].set_linestyle(":")
#     leg_lines[5].set_linestyle(":")
#     leg_lines[7].set_linestyle(":")
     export_legend(leg)
    
    
