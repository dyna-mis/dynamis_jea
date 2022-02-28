#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:03:53 2019

@author: guangping
"""
from matplotlib import colors as cn
# full names
from matplotlib.lines import Line2D

A_CG = "CONFLICT_GRAPH"
A_RS = "RANGE_SEARCH"

A_SL = "SEPERATION_LINE"
A_SLK = "SEPERATION_LINE_K"
#arrow
A_ARROW = "ARROW"
A_GSL = "GREEDY_SEPERATION_LINE"
A_GSLK = "GREEDY_SEPERATION_LINE_K"
#greedy arrow
A_GARROW = "GREEDY_ARROW"
# short names shown in files
A_KEYS = ["cg","rs","sl","slk","arrow","gsl","gslk","garrow"]
#colors
#A_COLORS = {A_CG : cn.CSS4_COLORS["seagreen"], A_RS : cn.CSS4_COLORS["green"], A_SL: cn.CSS4_COLORS["orange"], A_SLK : cn.CSS4_COLORS["gray"],
#           A_ARROW: cn.CSS4_COLORS["blue"] , A_GSL: cn.CSS4_COLORS["darkred"], A_GSLK: cn.CSS4_COLORS["peru"], A_GARROW:cn.CSS4_COLORS["coral"]}
#A_COLORS = {A_CG : cn.CSS4_COLORS["seagreen"], A_RS : cn.CSS4_COLORS["green"], A_SL: cn.CSS4_COLORS["orange"], A_SLK : cn.CSS4_COLORS["gray"],
 #          A_ARROW: cn.CSS4_COLORS["blue"] , A_GSL: cn.CSS4_COLORS["darkred"], A_GSLK: cn.CSS4_COLORS["peru"], A_GARROW:cn.CSS4_COLORS["coral"]}
 # light green, green, drakgreen, blue, red, purple
#colors =["#e5f5f9","#99d8c9","#2ca25f","#377eb8","#e41a1c","#984ea3"]
Light_Green = '#41b6c4'
Green ="#253494"
Dark_Green = "#000000"
Red = "#e41a1c"
Blue = "#006837"
Purple = "#f6720a"
color_dict = dict({'line':Purple,
                   'g-line':Purple,
                   'grid':Light_Green,
                   'g-grid':Light_Green,
                   'grid-2':Green,
                   'g-grid-2':Green,
                   'grid-4':Dark_Green,
                   'g-grid-4':Dark_Green,
                   'MIS-ORS': Red,
                   'MIS-graph':Blue,
                   })
#order = [5, 9, 2, 6, 3, 7, 4, 8, 1, 0]
algo_list = ['line', 'g-line', 'grid', 'g-grid', 'grid-2', 'g-grid-2', 'grid-4', 'g-grid-4', 'MIS-ORS', 'MIS-graph']
marks_list =["o","x","o","x","o","x","o","x","s","^",]
#marks_list =["o","x","o","x","o","x","o","x","o","^",]
#marks_list =["o","x","s","^",]

#marks_list =["o","x","o","x","o","x","o","x"]
#marks_list =["o","o","o","o"]

