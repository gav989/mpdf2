#angles.py

def straightline(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing angle and give a reason for your answer\\\\[0.1cm]"
		else:
			explanation = ""
		nl = " \\\\[0.1cm] "
		a = random.randrange(95,170)
		b = 180-a
		a = str(a) + "\\mydeg"
		b = str(b) + "\\mydeg"
		if random.randrange(0,2)==1:
			answer = a
			a = "?"
		else:
			answer = b
			b = "?"
		aco = "25,23"
		bco = "51,22"
		image = "\\centering\\begin{overpic}[scale=0.36]{shape/images/straightline} \\put(" + aco + "){" + str(a) + "} \\put(" + bco + "){" + str(b) + "} \\end{overpic}"
		question = explanation + image
		answer = answer + ", because angles on a straight line add up to 180\\mydeg"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def aroundapoint(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing angle and give a reason for your answer\\\\[0.1cm]"
		else:
			explanation = ""
		nl = " \\\\[0.1cm] "
		a = random.randrange(95,170)
		b = random.randrange(20,floor(int((270-a)/2))-10)
		c = 270 - a - b
		a = str(a) + "\\mydeg"
		b = str(b) + "\\mydeg"
		c = str(c) + "\\mydeg"
		dec = random.randrange(0,3)
		if dec==1:
			answer = a
			a = "?"
		elif dec==2:
			answer = b
			b = "?"
		else:
			answer = c
			c = "?"
		aco = "40,57"
		bco = "42,25"
		cco = "52,41"
		image = "\\centering\\begin{overpic}[scale=0.36]{shape/images/aroundapoint} \\put(" + aco + "){" + str(a) + "} \\put(" + bco + "){" + str(b) + "} \\put(" + cco + "){" + str(c) + "} \\end{overpic}"
		question = explanation + image
		answer = answer + ", because angles around a point add up to 360\\mydeg"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def inatriangle(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing angle and give a reason for your answer\\\\[0.1cm]"
		else:
			explanation = ""
		nl = " \\\\[0.1cm] "
		a = random.randrange(15,80)
		b = random.randrange(15,80)
		c = 180 - a - b
		a = str(a) + "\\mydeg"
		b = str(b) + "\\mydeg"
		c = str(c) + "\\mydeg"
		dec = random.randrange(0,3)
		if dec==1:
			answer = a
			a = "?"
		elif dec==2:
			answer = b
			b = "?"
		else:
			answer = c
			c = "?"
		aco = "17,5"
		bco = "68,5"
		cco = "50,50"
		image = "\\centering\\begin{overpic}[scale=0.36]{shape/images/anglesintriangle} \\put(" + aco + "){" + str(a) + "} \\put(" + bco + "){" + str(b) + "} \\put(" + cco + "){" + str(c) + "} \\end{overpic}"
		question = explanation + image
		answer = answer + ", because angles in a triangle add up to 180\\mydeg"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def opposite(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the missing angle and give a reason for your answer\\\\[0.1cm]"
		else:
			explanation = ""
		nl = " \\\\[0.1cm] "
		a = random.randrange(95,170)
		b = a
		a = str(a) + "\\mydeg"
		b = str(b) + "\\mydeg"
		if random.randrange(0,2)==1:
			answer = a
			a = "?"
		else:
			answer = b
			b = "?"
		aco = "41,24"
		bco = "41,43"
		image = "\\centering\\begin{overpic}[scale=0.36]{shape/images/opposite} \\put(" + aco + "){" + str(a) + "} \\put(" + bco + "){" + str(b) + "} \\end{overpic}"
		question = explanation + image
		answer = answer + ", because opposite angles are equal"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def polygonanglestable(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		sides = [3,4,5,6,8,9,10,12,15,18,20,24,30,40,45,60,90,120,180,360,720]
		sides = random.choice(sides)
		intsum = 180 * (sides - 2)
		interior = intsum/sides
		exterior = 360/sides
		if interior%1==0:
			interior = int(interior)
		if exterior%1==0:
			exterior = int(exterior)
		sides = str(sides)
		interior = str(interior) + "\\mydeg"
		intsum = str(intsum) + "\\mydeg"
		exterior = str(exterior) + "\\mydeg"

		atable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ M{1.5cm} | M{1.2cm} } Sides & " + str(sides) + " \\\\ \\hline Interior Sum & " + str(intsum)  + "  \\\\ \\hline Interior  & " + str(interior) + " \\\\ \\hline Exterior & " + str(exterior) + "  \\\\  \\end{tabular}"
		allfour = [sides,intsum,interior,exterior]
		onlyone = ["","","",""]
		temp = random.randrange(0,4)
		onlyone[temp] = allfour[temp]
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ M{1.5cm} | M{1.2cm} } Sides & " + onlyone[0] + " \\\\ \\hline Interior Sum & " + onlyone[1]  + "  \\\\ \\hline Interior  & " + onlyone[2] + " \\\\ \\hline Exterior & " + onlyone[3] + "  \\\\  \\end{tabular}"
		question = "Complete for a regular polygon: \\\\[0.2cm]" + qtable
		answer = atable

#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
