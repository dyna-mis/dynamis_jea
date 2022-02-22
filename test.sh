#!/bin/bash
declare -a exact=("wmis")
#declare -a algo=("line")
declare -a algo=("graph" "ors" "grid" "gridK" "line")
declare -a algoR=("graph" "line")
#declare -a algoR=("line")

declare -a algoE=("wmis" "graph" "ors" "grid" "gridK" "line")
declare -a algoRE=("wmis" "graph" "line")

#declare -a algoE=("line")
#declare -a algoRE=("line")

declare -a mod=("add" "sub") 
declare -a parK=("2,4")

#E1* 10000 400
#  E1
for problem in INPUT/square/*;
	do
        for file in $problem/*;
		do
		if [[ $file == *10000 ]];
			then
                	for a in "${algo[@]}";
                		do
                        	for m in "${mod[@]}";
                        		do			
								./dynamis_1_square.sh $file $a $m 0.04 ./OUTPUT/E1    
					done
                        	done
			fi

       		done
	done

# E1-Rect
for problem in INPUT/rectangle/*;
        do
        for file in $problem/*;
		do
                if [[ $file == *10000 ]];
                        then
                        for a in "${algoR[@]}";
                                do
                                for m in "${mod[@]}";
                                        do
                                        ./dynamis_1_rectangle.sh $file $a $m 0.04 ./OUTPUT/E1_Rect
                                        done
                                done
                	fi
		done

       done



#E2*, E3* prac
# E2, E3
for file in INPUT/square/prac/*;
                do
                        for a in "${algoE[@]}";
                                        do
                                        ./dynamis_1_square.sh $file $a mix 0.1 ./OUTPUT/E23
                                        done
                done

# E2-Rect, E3-Rect
for file in INPUT/rectangle/prac/*;
                do
                        for a in "${algoRE[@]}";
                                        do
                                        ./dynamis_1_rectangle.sh $file $a mix 0.1 ./OUTPUT/E23_Rect
                                        done
                done




#E4* exact 1000 100 
# E4
for file in INPUT/square/sin1000/*;
                do
                if [[ $file == * ]];
                        then
                        for a in "${algoE[@]}";
                                do
                                for m in "${mod[@]}";
                                        do
                                        ./dynamis_1_square.sh $file $a $m 0.1 ./OUTPUT/E4
                                        done
                                done
                        fi

                done
# E4-Rect
for file in INPUT/rectangle/sin1000/*;
                do
                if [[ $file == * ]];
                        then
                        for a in "${algoRE[@]}";
                                do
                                for m in "${mod[@]}";
                                        do
                                        ./dynamis_1_rectangle.sh $file $a $m 0.1 ./OUTPUT/E4_Rect
                                        done
                                done
                        fi
                done




#E5* recomputation and update 
# E5
for problem in INPUT/square/*;
        do
        for file in $problem/*;
                do
                        for a in "${algo[@]}";
                                do
                                for m in "${mod[@]}";
                                        do
										./dynamis_1_square_recompute.sh $file $a $m 0.1 ./OUTPUT/E5
										./dynamis_1_square.sh $file $a $m 0.1 ./OUTPUT/E5
                                        done
                                done

                done
        done
# E5-Rect
for problem in INPUT/rectangle/*;
        do
        for file in $problem/*;
                do
                        for a in "${algoR[@]}";
                                do
                                for m in "${mod[@]}";
                                        do
										./dynamis_1_rectangle_recompute.sh $file $a $m 0.1 ./E5_Rect
                                        ./dynamis_1_rectangle.sh $file $a $m 0.1 ./E5_Rect
                                        done
                                done
                done

       done


