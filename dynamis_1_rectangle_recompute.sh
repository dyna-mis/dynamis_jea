#!/bin/bash
if [ $2 = "line" ];
	then
 	build/Release/src/dynaMIS -c -f $1 -a $2 -m $3 -r $4  -l 30 -w 30 -g -p -d $5
	build/Release/src/dynaMIS -c -f $1 -a $2 -m $3 -r $4  -l 30 -w 30 -p -d $5
	else
    build/Release/src/dynaMIS -c -f $1 -a $2 -m $3 -r $4  -l 30 -w 30 -p -d .$5  -t ./tmp
fi

