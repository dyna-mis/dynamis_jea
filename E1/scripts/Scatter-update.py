#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 17:30:28 2019

@author: guangping
"""
import test
for mod in ['0','1','2']:
    for  data in ['GAUSSIAN', 'UNIFORM']:
        for size in ['1000', '2000', '4000']:
            folderName = '/home/guangping/dev/RESULT/'+mod+'/'+data+'/'+size+'/'
            outPutName = 'SCATTER/'+mod+'-'+data+'-'+size+'-'+'all'
            test.getScatter(folderName,'all',outPutName)
for mod in ['0','1','2']:
    for  data in ['GAUSSIAN', 'UNIFORM']:
        for size in ['1000', '2000', '4000']:
            folderName = '/home/guangping/dev/RESULT/'+mod+'/'+data+'/'+size+'/'
            outPutName = 'SCATTER/'+mod+'-'+data+'-'+size+'-'+'no-gslk'
            test.getScatter(folderName,'gslk',outPutName)