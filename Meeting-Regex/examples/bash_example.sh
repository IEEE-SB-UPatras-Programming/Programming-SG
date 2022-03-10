#!/bin/bash

regex="\"(.+)\"\s+\"(.+)\""

while read -r line
do 
    if [[ $line =~ $regex ]] 
    then
        echo ${BASH_REMATCH[1]} ${BASH_REMATCH[2]}
    fi
done
