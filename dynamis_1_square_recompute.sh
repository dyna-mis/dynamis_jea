#!/bin/bash
if [ $2 = "grid" ];
	then
		 build/Release/src/dynaMIS -f $1 -a $2 -m $3 -r $4  -l 30 -w 30 -d . -c
		 build/Release/src/dynaMIS -f $1 -a $2 -m $3 -r $4  -l 30 -w 30 -g -d . -c
	else
		if [ $2 = "gridK" ];
			then
 			build/Release/src/dynaMIS -c -f $1 -a $2 -m $3 -r $4  -l 30 -w 30 -k 2 -d .
			build/Release/src/dynaMIS -c -f $1 -a $2 -m $3 -r $4  -l 30 -w 30 -k 4 -d  .
		    build/Release/src/dynaMIS -c -f $1 -a $2 -m $3 -r $4  -l 30 -w 30 -k 2 -g -d .
            build/Release/src/dynaMIS -c -f $1 -a $2 -m $3 -r $4  -l 30 -w 30 -k 4 -g -d .
			else
				if [ $2 = "line" ];
                                	then
                                    build/Release/src/dynaMIS -c -t ./tmp -f $1 -a $2 -m $3 -r $4  -l 30 -w 30 -d .
                                    build/Release/src/dynaMIS -c -g -t ./tmp -f $1 -a $2 -m $3 -r $4  -l 30 -w 30 -d .
			       		else
					    build/Release/src/dynaMIS -c -t ./tmp -f $1 -a $2 -m $3 -r $4  -l 30 -w 30 -d .
		
				fi
		fi
fi
