#!/bin/bash

declare -a exps =("E1" "E1_Rect" "E2" "E2_Rect" "E3" "E3_Rect" "E4" "E4_Rect" "E5" "E5_Rect")
#E1* 10000 400
#  E1
for exp in ${exp[@]};
	do	
		$exp/ALLinALL.py 
	done


