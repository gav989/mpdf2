#!/bin/bash  

#YOU CAN'T HAVE ANY OTHER PDFS IN SCRIPTS

#EDIT THESE - output must be actual filename output
scriptname="donowhigheryear11.py"
output="Year 11 Higher Do Now"


mkdir yearoutput


for i in {01..31}
	do
		( cd ./scripts/ && python $scriptname && mv "$output.pdf" $i.pdf )
	done
mkdir yearoutput/01\ -\ January
mv ./scripts/*".pdf" yearoutput/01\ -\ January


for i in {01..29}
	do
		( cd ./scripts/ && python $scriptname && mv "$output.pdf" $i.pdf )
	done
mkdir yearoutput/02\ -\ February
mv ./scripts/*".pdf" yearoutput/02\ -\ February


for i in {01..31}
	do
		( cd ./scripts/ && python $scriptname && mv "$output.pdf" $i.pdf )
	done
mkdir yearoutput/03\ -\ March
mv ./scripts/*".pdf" yearoutput/03\ -\ March


for i in {01..30}
	do
		( cd ./scripts/ && python $scriptname && mv "$output.pdf" $i.pdf )
	done
mkdir yearoutput/04\ -\ April
mv ./scripts/*".pdf" yearoutput/04\ -\ April


for i in {01..31}
	do
		( cd ./scripts/ && python $scriptname && mv "$output.pdf" $i.pdf )
	done
mkdir yearoutput/05\ -\ May
mv ./scripts/*".pdf" yearoutput/05\ -\ May


for i in {01..30}
	do
		( cd ./scripts/ && python $scriptname && mv "$output.pdf" $i.pdf )
	done
mkdir yearoutput/06\ -\ June
mv ./scripts/*".pdf" yearoutput/06\ -\ June


for i in {01..31}
	do
		( cd ./scripts/ && python $scriptname && mv "$output.pdf" $i.pdf )
	done
mkdir yearoutput/07\ -\ July
mv ./scripts/*".pdf" yearoutput/07\ -\ July


for i in {01..31}
	do
		( cd ./scripts/ && python $scriptname && mv "$output.pdf" $i.pdf )
	done
mkdir yearoutput/08\ -\ August
mv ./scripts/*".pdf" yearoutput/08\ -\ August


for i in {01..30}
	do
		( cd ./scripts/ && python $scriptname && mv "$output.pdf" $i.pdf )
	done
mkdir yearoutput/09\ -\ September
mv ./scripts/*".pdf" yearoutput/09\ -\ September


for i in {01..31}
	do
		( cd ./scripts/ && python $scriptname && mv "$output.pdf" $i.pdf )
	done
mkdir yearoutput/10\ -\ October
mv ./scripts/*".pdf" yearoutput/10\ -\ October


for i in {01..30}
	do
		( cd ./scripts/ && python $scriptname && mv "$output.pdf" $i.pdf )
	done
mkdir yearoutput/11\ -\ November
mv ./scripts/*".pdf" yearoutput/11\ -\ November


for i in {01..31}
	do
		( cd ./scripts/ && python $scriptname && mv "$output.pdf" $i.pdf )
	done
mkdir yearoutput/12\ -\ December
mv ./scripts/*".pdf" yearoutput/12\ -\ December