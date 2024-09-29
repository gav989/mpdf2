#!/usr/bin/env python3
#measuring.py

def measureline(n,explanationn):
	import random
	from math import sqrt
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		answer = rounddp(random.randrange(20,131)/10,1)
		question = "\\rule{" + str(1.04*answer) + "cm}{0.4pt}"
		answer = str(answer)
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer + "cm")
