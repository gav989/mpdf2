#!/usr/bin/env python3
#metricconversions.py

def mcdistance(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Convert "
		else:
			explanation = ""
		units = [" mm"," cm"," m"," km"]
		unitsfull = ["millimetres","centimetres","metres","kilometres"]
		unit1 = random.randrange(0,3)
		unit2 = unit1+1
		if unit1==0:
			scale = 10
		elif unit1==1:
			scale = 100
		else:
			scale = 1000
		direc = random.randrange(0,2)
		start = round(random.randrange(1,101)/10**random.randrange(0,2),1)
		if direc==1:
			end = int(round(start*scale,0))
			swap = 1
		else:
			end = round(start/scale,4)
			swap = 0
		if swap==1:
			temp = unit1
			unit1 = unit2
			unit2 = temp
		unit1 = units[unit1]
		unit3 = units[unit2]
		unit2 = unitsfull[unit2]
		if start%1==0:
			start = int(start)
		if end%1==0:
			end = int(end)
#write question
		tempquestions.write(explanation + str(start) + unit1 + " to " + unit2)

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(end) + unit3)


def mcmass(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Convert "
		else:
			explanation = ""
		units = [" mg"," g"," kg"," t"]
		unitsfull = ["milligrams","grams","kilograms","tonnes"]
		unit1 = random.randrange(0,3)
		unit2 = unit1+1
		scale = 1000
		direc = random.randrange(0,2)
		start = round(random.randrange(1,101)/10**random.randrange(0,2),1)
		if direc==1:
			end = int(round(start*scale,0))
			swap = 1
		else:
			end = round(start/scale,4)
			swap = 0
		if swap==1:
			temp = unit1
			unit1 = unit2
			unit2 = temp
		unit1 = units[unit1]
		unit3 = units[unit2]
		unit2 = unitsfull[unit2]
		if start%1==0:
			start = int(start)
		if end%1==0:
			end = int(end)
#write question
		tempquestions.write(explanation + str(start) + unit1 + " to " + unit2)

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(end) + unit3)


def mccapacity(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Convert "
		else:
			explanation = ""
		units = [" ml"," L"]
		unitsfull = ["millilitres","litres"]
		unit1 = 0
		unit2 = 1
		scale = 1000
		direc = random.randrange(0,2)
		start = round(random.randrange(1,101)/10**random.randrange(0,2),1)
		if direc==1:
			end = int(round(start*scale,0))
			swap = 1
		else:
			end = round(start/scale,4)
			swap = 0
		if swap==1:
			temp = unit1
			unit1 = unit2
			unit2 = temp
		unit1 = units[unit1]
		unit3 = units[unit2]
		unit2 = unitsfull[unit2]
		if start%1==0:
			start = int(start)
		if end%1==0:
			end = int(end)
#write question
		tempquestions.write(explanation + str(start) + unit1 + " to " + unit2)

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(end) + unit3)
