#!/bin/bash
if [ $2 = "line" ];
	then
 	build/Release/src/dynaMIS -f $1 -a $2 -m $3 -r $4  -l 10 -w 10 -g -p -d .
	build/Release/src/dynaMIS -f $1 -a $2 -m $3 -r $4  -l 10 -w 10 -p -d .
	else
		if [ $2 = "graph" ];
			then
			build/Release/src/dynaMIS -f $1 -a $2 -m $3 -r $4  -l 10 -w 10 -x -p -d .
        	build/Release/src/dynaMIS -f $1 -a $2 -m $3 -r $4  -l 10 -w 10 -p -d .
			else	
        	build/Release/src/dynaMIS -f $1 -a $2 -m $3 -r $4  -l 10 -w 10 -p -d .  -t ./tmp

		fi
fi

