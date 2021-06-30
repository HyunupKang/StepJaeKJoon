#!/bin/bash

#n=10
row=0
col=-1
n=5
value=1
sing=1

array_list="array"

for i in `seq 1 ${n}`
do
    eval ${array_list}${i}=${i}
    array+=("array$i")
done

while [ ${n} -gt 0 ]
do
    for((i=0; i<${n}; i++))
    do
        let "col+=sing"
        let ${array[${row}]}[${col}]=${value}
        let "value+=1"
    done
    
    let "n-=1"
    
    for((j=0; j<${n}; j++))
    do
        let "row+=sing"
        let ${array[${row}]}[${col}]=${value}
        let "value+=1"        
    done
    
    let "sing*=-1"
    
done


for((i=0; i<${#array[*]}; ++i))
do
	Line=${array[i]}[*]
	Line=(${!Line})
	for((j=0; j<${#Line[*]}; ++j))
	do
		printf "%7s" "${Line[j]} "
	done
	echo
done
