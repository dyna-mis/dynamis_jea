#!/bin/bash

#declare -a exps=("E1" "E1_Rect" "E2" "E2_Rect" "E3" "E3_Rect" "E4" "E4_Rect" "E5" "E5_Rect")
declare -a exps=("E1")
#E1* 10000 400
#  E1
for exp in "${exps[@]}";
	do	
		python3 $exp/scripts/ALLinALL.py 
	done


