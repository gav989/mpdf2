#trig.py

def solvesin1(n,explanationn):
	import random
	from math import asin,acos,atan,degrees
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation1 = "Solve "
			explanation2 = " for all values in the range $0 \\mydeg \\leq x \\leq360 \\mydeg$"
		else:
			explanation1 = ""
			explanation2 = ""
		trigword = "\\text{sin x}"
		value = rounddp(random.randrange(1,100)*0.01*(-1)**random.randrange(0,2),2)
		answer1 = rounddp(degrees(asin(value)),2)
		if answer1>0:
			answer2 = rounddp(180-answer1,2)
		else:
			answer2 = rounddp(360 + answer1,2)
			answer1 = rounddp(180 - answer1,2)
		question = "$" + trigword + " = " + str(value) + "$"
		answer = "x = " + str(answer1) + " and x = " + str(answer2)
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def solvecos1(n,explanationn):
	import random
	from math import asin,acos,atan,degrees
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation1 = "Solve "
			explanation2 = " for all values in the range $0 \\mydeg \\leq x \\leq360 \\mydeg$"
		else:
			explanation1 = ""
			explanation2 = ""
		trigword = "\\text{cos x}"
		value = rounddp(random.randrange(1,100)*0.01*(-1)**random.randrange(0,2),2)
		answer1 = rounddp(degrees(acos(value)),2)
		answer2 = rounddp(360 - answer1,2)
		question = "$" + trigword + " = " + str(value) + "$"
		answer = "x = " + str(answer1) + " and x = " + str(answer2)
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def solvetan1(n,explanationn):
	import random
	from math import asin,acos,atan,degrees
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation1 = "Solve "
			explanation2 = " for all values in the range $0 \\mydeg \\leq x \\leq360 \\mydeg$"
		else:
			explanation1 = ""
			explanation2 = ""
		trigword = "\\text{tan x}"
		value = rounddp(random.randrange(1,100)*0.01*(-1)**random.randrange(0,2),2)
		answer1 = rounddp(degrees(atan(value)),2)
		if answer1>0:
			answer2 = rounddp(answer1 + 180,2)
		else:
			answer2 = rounddp(answer1 + 360,2)
			answer1 = rounddp(answer1 + 180,2)
		question = "$" + trigword + " = " + str(value) + "$"
		answer = "x = " + str(answer1) + " and x = " + str(answer2)
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
