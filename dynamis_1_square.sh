#!/bin/bash
if [ $2 = "grid" ];
	then
		build/Release/src/dynaMIS -f $1 -a $2 -m $3 -r $4  -l 30 -w 30 -d $5 
		build/Release/src/dynaMIS -f $1 -a $2 -m $3 -r $4  -l 30 -w 30 -g -d $5
	else
		if [ $2 = "gridK" ];
			then
 			build/Release/src/dynaMIS -f $1 -a $2 -m $3 -r $4  -l 30 -w 30 -k 2 -d $5
			build/Release/src/dynaMIS -f $1 -a $2 -m $3 -r $4  -l 30 -w 30 -k 4 -d $5
			build/Release/src/dynaMIS -f $1 -a $2 -m $3 -r $4  -l 30 -w 30 -k 2 -g -d $5
            build/Release/src/dynaMIS -f $1 -a $2 -m $3 -r $4  -l 30 -w 30 -k 4 -g -d $5
			else
			       if [ $2 = "line" ];
					then	
					build/Release/src/dynaMIS  -t $TMPDIR -f $1 -a $2 -m $3 -r $4  -l 30 -w 30 -d $5
					build/Release/src/dynaMIS -g -t $TMPDIR -f $1 -a $2 -m $3 -r $4  -l 30 -w 30 -d $5
					else 
					build/Release/src/dynaMIS  -t $TMPDIR -f $1 -a $2 -m $3 -r $4  -l 30 -w 30 -d $5
				fi
		fi
fi
