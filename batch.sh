#!/bin/bash  

#EDIT THESE - output must be actual filename output
scriptname="starterskillscheck.py"
output="Skills Check"

#EDIT RANGE
for i in {01..10}
	do
		( cd ./scripts/ && python $scriptname; mv "$output.pdf" "$output"\ -\ $i.pdf )
	done
mkdir batchoutput
mv ./scripts/"$output"* batchoutput