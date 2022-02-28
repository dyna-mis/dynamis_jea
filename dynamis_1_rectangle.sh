#!/bin/bash
if [ $2 = "line" ];
	then
 	build/Release/src/dynaMIS -f $1 -a $2 -m $3 -r $4  -l 10 -w 10 -g -p -d $5
	build/Release/src/dynaMIS -f $1 -a $2 -m $3 -r $4  -l 10 -w 10 -p -d $5
	else
		if [ $2 = "graph" ];
			then
			build/Release/src/dynaMIS -f $1 -a $2 -m $3 -r $4  -l 10 -w 10 -x -p -d $5
        	build/Release/src/dynaMIS -f $1 -a $2 -m $3 -r $4  -l 10 -w 10 -p -d $5
			else	
        	build/Release/src/dynaMIS -f $1 -a $2 -m $3 -r $4  -l 10 -w 10 -p -d $5  -t ./tmp

		fi
fi

