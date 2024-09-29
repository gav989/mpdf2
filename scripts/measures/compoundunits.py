#!/usr/bin/env python3
#compoundunits.py

def speedconv1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Convert "
			explanation2 = " to km/h"
		else:
			explanation1 = ""
			explanation2 = ""
		ms = random.randrange(1,100)*10
		kmh = ms * 3.6
		if kmh%1==0:
			kmh = int(kmh)
#write question
		tempquestions.write(explanation1 + str(ms) + " m/s" + explanation2)

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(kmh) + " km/h")


def speedconv2(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Convert "
			explanation2 = " to m/s"
		else:
			explanation1 = ""
			explanation2 = ""
		kmh = random.randrange(10,51)*10
		ms = rounddp(kmh/3.6,2)
		if ms%1==0:
			ms = int(ms)
#write question
		tempquestions.write(explanation1 + str(kmh) + " km/h" + explanation2)

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(ms) + " m/s")
