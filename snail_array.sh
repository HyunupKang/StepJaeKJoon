#!/bin/bash

array1=(0 0 0 0 0)
array2=(0 0 0 0 0)
array3=(0 0 0 0 0)
array4=(0 0 0 0 0)
array5=(0 0 0 0 0)

array=(array1 array2 array3 array4 array5)

row=0
col=-1
n=5
value=1
sing=1

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
		printf "${Line[j]} "
	done
	echo
done