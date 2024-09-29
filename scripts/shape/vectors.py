#vectors.py



def addvectors1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		x1 = random.randrange(-8,9)
		if x1==0:
			y1 = random.randrange(1,9)*(-1)**random.randrange(1,3)
		else:
			y1 = random.randrange(-8,9)
		x2 = random.randrange(-8,9)
		if x2==0:
			y2 = random.randrange(1,9)*(-1)**random.randrange(1,3)
		else:
			y2 = random.randrange(-8,9)
		vector1 = "\\Large{$\\left(\\begin{smallmatrix}" + str(x1) + "\\\\" + str(y1) + "\\end{smallmatrix}\\right)$}"
		vector2 = "\\Large{$\\left(\\begin{smallmatrix}" + str(x2) + "\\\\" + str(y2) + "\\end{smallmatrix}\\right)$}"
		question = vector1 + " $\\normalsize+$ " + vector2
		x3 = x1 + x2
		y3 = y1 + y2
		vector3 = "\\Large{$\\left(\\begin{smallmatrix}" + str(x3) + "\\\\" + str(y3) + "\\end{smallmatrix}\\right)$}"
		answer = vector3
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def subtractvectors1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		x1 = random.randrange(-8,9)
		if x1==0:
			y1 = random.randrange(1,9)*(-1)**random.randrange(1,3)
		else:
			y1 = random.randrange(-8,9)
		x2 = random.randrange(-8,9)
		if x2==0:
			y2 = random.randrange(1,9)*(-1)**random.randrange(1,3)
		else:
			y2 = random.randrange(-8,9)
		vector1 = "\\Large{$\\left(\\begin{smallmatrix}" + str(x1) + "\\\\" + str(y1) + "\\end{smallmatrix}\\right)$}"
		vector2 = "\\Large{$\\left(\\begin{smallmatrix}" + str(x2) + "\\\\" + str(y2) + "\\end{smallmatrix}\\right)$}"
		question = vector1 + " $\\normalsize-$ " + vector2
		x3 = x1 - x2
		y3 = y1 - y2
		vector3 = "\\Large{$\\left(\\begin{smallmatrix}" + str(x3) + "\\\\" + str(y3) + "\\end{smallmatrix}\\right)$}"
		answer = vector3
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def expandvectors1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		x1 = random.randrange(-8,9)
		if x1==0:
			y1 = random.randrange(1,9)*(-1)**random.randrange(1,3)
		else:
			y1 = random.randrange(-8,9)
		vector1 = "\\Large{$\\left(\\begin{smallmatrix}" + str(x1) + "\\\\" + str(y1) + "\\end{smallmatrix}\\right)$}"
		c1 = random.randrange(2,9)
		question = str(c1) + vector1
		x3 = x1 * c1
		y3 = y1 * c1
		vector3 = "\\Large{$\\left(\\begin{smallmatrix}" + str(x3) + "\\\\" + str(y3) + "\\end{smallmatrix}\\right)$}"
		answer = vector3
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def expandvectors2(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		x1 = random.randrange(-8,9)
		if x1==0:
			y1 = random.randrange(1,9)*(-1)**random.randrange(1,3)
		else:
			y1 = random.randrange(-8,9)
		vector1 = "\\Large{$\\left(\\begin{smallmatrix}" + str(x1) + "\\\\" + str(y1) + "\\end{smallmatrix}\\right)$}"
		choices = [1,3,4,5,6,7,8]
		c1 = rounddp(random.choice(choices)/2,1) * (-1)**random.randrange(1,3)
		if c1%1==0:
			c1 = int(c1)
		question = "$" + str(c1) + "$" + vector1
		x3 = rounddp(x1 * c1,1)
		y3 = rounddp(y1 * c1,1)
		if x3%1==0:
			x3 = int(x3)
		if y3%1==0:
			y3 = int(y3)
		vector3 = "\\Large{$\\left(\\begin{smallmatrix}" + str(x3) + "\\\\" + str(y3) + "\\end{smallmatrix}\\right)$}"
		answer = vector3
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def addvectors2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		x1 = random.randrange(-8,9)
		if x1==0:
			y1 = random.randrange(1,9)*(-1)**random.randrange(1,3)
		else:
			y1 = random.randrange(-8,9)
		x2 = random.randrange(-8,9)
		if x2==0:
			y2 = random.randrange(1,9)*(-1)**random.randrange(1,3)
		else:
			y2 = random.randrange(-8,9)
		c1 = random.randrange(1,9)
		if c1==1:
			c2 = random.randrange(2,9)
			x3 = c1*x1 + c2*x2
			y3 = c1*y1 + c2*y2
			c1 = ""
		else:
			c2 = random.randrange(1,9)
			x3 = c1*x1 + c2*x2
			y3 = c1*y1 + c2*y2
			if c2==1:
				c2 = ""
		vector1 = "\\Large{$\\left(\\begin{smallmatrix}" + str(x1) + "\\\\" + str(y1) + "\\end{smallmatrix}\\right)$}"
		vector2 = "\\Large{$\\left(\\begin{smallmatrix}" + str(x2) + "\\\\" + str(y2) + "\\end{smallmatrix}\\right)$}"
		question = str(c1) + vector1 + "\\normalsize $+$ " + str(c2) + vector2
		vector3 = "\\Large{$\\left(\\begin{smallmatrix}" + str(x3) + "\\\\" + str(y3) + "\\end{smallmatrix}\\right)$}"
		answer = vector3
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def subtractvectors2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		x1 = random.randrange(-8,9)
		if x1==0:
			y1 = random.randrange(1,9)*(-1)**random.randrange(1,3)
		else:
			y1 = random.randrange(-8,9)
		x2 = random.randrange(-8,9)
		if x2==0:
			y2 = random.randrange(1,9)*(-1)**random.randrange(1,3)
		else:
			y2 = random.randrange(-8,9)
		c1 = random.randrange(1,9)
		if c1==1:
			c2 = random.randrange(2,9)
			x3 = c1*x1 - c2*x2
			y3 = c1*y1 - c2*y2
			c1 = ""
		else:
			c2 = random.randrange(1,9)
			x3 = c1*x1 - c2*x2
			y3 = c1*y1 - c2*y2
			if c2==1:
				c2 = ""
		vector1 = "\\Large{$\\left(\\begin{smallmatrix}" + str(x1) + "\\\\" + str(y1) + "\\end{smallmatrix}\\right)$}"
		vector2 = "\\Large{$\\left(\\begin{smallmatrix}" + str(x2) + "\\\\" + str(y2) + "\\end{smallmatrix}\\right)$}"
		question = str(c1) + vector1 + "\\normalsize $-$ " + str(c2) + vector2
		vector3 = "\\Large{$\\left(\\begin{smallmatrix}" + str(x3) + "\\\\" + str(y3) + "\\end{smallmatrix}\\right)$}"
		answer = vector3
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def vectorssimeqadd(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the values of a and b given that  "
		else:
			explanation = ""
		x1 = random.randrange(-8,9)
		if x1==0:
			y1 = random.randrange(1,9)*(-1)**random.randrange(1,3)
		else:
			y1 = random.randrange(-8,9)
		x2 = random.randrange(-8,9)
		if x2==0:
			y2 = random.randrange(1,9)*(-1)**random.randrange(1,3)
		else:
			y2 = random.randrange(-8,9)
		c1 = random.randrange(1,9)
		if c1==1:
			c2 = random.randrange(2,9)
			x3 = c1*x1 + c2*x2
			y3 = c1*y1 + c2*y2
		else:
			c2 = random.randrange(1,9)
			x3 = c1*x1 + c2*x2
			y3 = c1*y1 + c2*y2
		vector1 = "\\Large{$\\left(\\begin{smallmatrix}" + str(x1) + "\\\\" + str(y1) + "\\end{smallmatrix}\\right)$}"
		vector2 = "\\Large{$\\left(\\begin{smallmatrix}" + str(x2) + "\\\\" + str(y2) + "\\end{smallmatrix}\\right)$}"
		vector3 = "\\Large{$\\left(\\begin{smallmatrix}" + str(x3) + "\\\\" + str(y3) + "\\end{smallmatrix}\\right)$}"
		question = "\\mbox{a" + vector1 + "\\normalsize $+$ b"  + vector2 + "\\normalsize = " + vector3 + "}"
		answer = "a = " + str(c1) + " and b = " + str(c2)
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def vectorssimeqsubtract(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the values of a and b given that  "
		else:
			explanation = ""
		x1 = random.randrange(-8,9)
		if x1==0:
			y1 = random.randrange(1,9)*(-1)**random.randrange(1,3)
		else:
			y1 = random.randrange(-8,9)
		x2 = random.randrange(-8,9)
		if x2==0:
			y2 = random.randrange(1,9)*(-1)**random.randrange(1,3)
		else:
			y2 = random.randrange(-8,9)
		c1 = random.randrange(1,9)
		if c1==1:
			c2 = random.randrange(2,9)
			x3 = c1*x1 - c2*x2
			y3 = c1*y1 - c2*y2
		else:
			c2 = random.randrange(1,9)
			x3 = c1*x1 - c2*x2
			y3 = c1*y1 - c2*y2
		vector1 = "\\Large{$\\left(\\begin{smallmatrix}" + str(x1) + "\\\\" + str(y1) + "\\end{smallmatrix}\\right)$}"
		vector2 = "\\Large{$\\left(\\begin{smallmatrix}" + str(x2) + "\\\\" + str(y2) + "\\end{smallmatrix}\\right)$}"
		vector3 = "\\Large{$\\left(\\begin{smallmatrix}" + str(x3) + "\\\\" + str(y3) + "\\end{smallmatrix}\\right)$}"
		question = "\\mbox{a" + vector1 + "\\normalsize $-$ b"  + vector2 + "\\normalsize = " + vector3 + "}"
		answer = "a = " + str(c1) + " and b = " + str(c2)
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
