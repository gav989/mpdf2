#pythagoras.py

def pythagoras1(n,explanationn):
	import random
	from math import sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		nl = " \\\\[0.1cm] "
		rotation = random.randrange(0,3)*90
		if rotation==0:
			aco = "-2,46"
			bco = "43,3"
			cco = "54,46"
		elif rotation==270:
			aco = "40,85"
			bco = "3,50"
			cco = "54,44"
		elif rotation==180:
			aco = "84,51"
			bco = "45,90"
			cco = "30,48"
		else:
			aco = "50,10" 
			bco = "100,45"
			cco = "38,53"
		a = random.randrange(3,13)
		b = random.randrange(3,13)
		c = "?"
		image = "\\hfill\\begin{overpic}[angle=" + str(rotation) + ",scale=0.5]{shape/images/pythag} \\put(" + aco + "){" + str(a) + "cm} \\put(" + bco + "){" + str(b) + "cm} \\put(" + cco + "){" + str(c) + "cm} \\end{overpic}\\hfill"
		answer = sqrt(a**2 + b**2)
		question = "Find the missing side length" + nl + image
		if answer%1==0:
			answer = int(answer)
		answer = str(answer)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def pythagoras2(n,explanationn):
	import random
	from math import sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		nl = " \\\\[0.1cm] "
		rotation = random.randrange(0,3)*90
		if rotation==0:
			aco = "-2,46"
			bco = "43,3"
			cco = "54,46"
		elif rotation==270:
			aco = "40,85"
			bco = "3,50"
			cco = "54,44"
		elif rotation==180:
			aco = "84,51"
			bco = "45,90"
			cco = "30,48"
		else:
			aco = "50,10" 
			bco = "100,45"
			cco = "35,53"
		if random.randrange(0,2)==1:
			a = random.randrange(3,13)
			c = a + random.randrange(3,10)
			b = "?"
			answer = sqrt(c**2 - a**2)
		else:
			b = random.randrange(3,13)
			c = b + random.randrange(3,10)
			a = "?"
			answer = sqrt(c**2 - b**2)
		image = "\\hfill\\begin{overpic}[angle=" + str(rotation) + ",scale=0.5]{shape/images/pythag} \\put(" + aco + "){" + str(a) + "cm} \\put(" + bco + "){" + str(b) + "cm} \\put(" + cco + "){" + str(c) + "cm} \\end{overpic}\\hfill"
		question = "Find the missing side length" + nl + image
		if answer%1==0:
			answer = int(answer)
		answer = str(answer)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
