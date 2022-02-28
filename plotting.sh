#!/bin/bash 

declare -a exps=("E1" "E1-Rect" "E2" "E2-Rect" "E3" "E3-Rect" "E4" "E4-Rect" "E5" "E5-Rect")
#E1* 10000 400
#  E1
for exp in "${exps[@]}";
	do	
		python3 $exp/scripts/ALLinALL.py 
	done


