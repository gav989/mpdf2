#inequalities.py


def integerlist(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Write down the integers that satisfy "
		else:
			explanation = ""
		start = random.randrange(1,4) * (-1)**random.randrange(1,4)
		finish = start + random.randrange(5,8)
		integers = [start]
		for i in range(start,finish):
			integers.append(i + 1)
		if random.randrange(0,2)==1:
			sign1 = " $\\leq$ "
		else:
			sign1 = " $<$ "
			integers.remove(integers[0])
		if random.randrange(0,2)==1:
			sign2 = " $\\leq$ "
		else:
			sign2 = " $<$ "
			integers.remove(integers[len(integers)-1])
		answer = ""
		for i in range (0,len(integers)):
			answer = answer + str(integers[i])
			if i<len(integers)-1:
				answer = answer + ", "
		question = str(start) + sign1 + " x " + sign2 + str(finish)
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def ineqnumline1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Express as an inequality: "
		else:
			explanation = ""
		a = random.randrange(-9,6)
		b = a + 1
		c = b + 1
		d = c + 1
		e = d + 1
		if a<0:
			ax = str(-3)
		else:
			ax = str(0)
		if b<0:
			bx = str(20)
		else:
			bx = str(23)
		if c<0:
			cx = str(44)
		else:
			cx = str(47)
		if d<0:
			dx = str(67)
		else:
			dx = str(70)
		if e<0:
			ex = str(91)
		else:
			ex = str(94)
		dec = random.randrange(0,4)
		if dec==0:
			ineq = "x $>$ " + str(c)
			img = "ineqgt"
		elif dec==1:
			ineq = "x $\\geq$ " + str(c)
			img = "ineqgeq"
		elif dec==2:
			ineq = "x $<$ " + str(c)
			img = "ineqlt"
		else:
			ineq = "x $\\leq$ " + str(c)
			img = "ineqleq"
		image = "\\begin{overpic}[scale=0.38]{algebra/images/" + img + "} \\put(" + ax + ",-10){" + str(a) + "} \\put(" + bx + ",-10){" + str(b) + "} \\put(" + cx + ",-10){" + str(c) + "} \\put(" + dx + ",-10){" + str(d) + "} \\put(" + ex + ",-10){" + str(e) + "}\\end{overpic}"
		question = image
		answer = ineq
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def ineqnumline2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Represent "
			explanation2 = " on a number line."
		else:
			explanation1 = ""
			explanation2 = ""
		a = random.randrange(-9,6)
		b = a + 1
		c = b + 1
		d = c + 1
		e = d + 1
		if a<0:
			ax = str(-3)
		else:
			ax = str(0)
		if b<0:
			bx = str(20)
		else:
			bx = str(23)
		if c<0:
			cx = str(44)
		else:
			cx = str(47)
		if d<0:
			dx = str(67)
		else:
			dx = str(70)
		if e<0:
			ex = str(91)
		else:
			ex = str(94)
		dec = random.randrange(0,4)
		if dec==0:
			ineq = "x $>$ " + str(c)
			img = "ineqgt"
		elif dec==1:
			ineq = "x $\\geq$ " + str(c)
			img = "ineqgeq"
		elif dec==2:
			ineq = "x $<$ " + str(c)
			img = "ineqlt"
		else:
			ineq = "x $\\leq$ " + str(c)
			img = "ineqleq"
		image = "\\begin{overpic}[scale=0.38]{algebra/images/" + img + "} \\put(" + ax + ",-10){" + str(a) + "} \\put(" + bx + ",-10){" + str(b) + "} \\put(" + cx + ",-10){" + str(c) + "} \\put(" + dx + ",-10){" + str(d) + "} \\put(" + ex + ",-10){" + str(e) + "}\\end{overpic}"
		question = ineq
		answer = image
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def ineqnumline3(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = random.randrange(-9,6)
		b = a + 1
		c = b + 1
		d = c + 1
		e = d + 1
		f = random.randrange(2,13)
		g = random.randrange(1,11)*(-1)**random.randrange(1,3)
		h = f*c + g
		if g<0:
			sign = " - "
		else:
			sign = " + "
		if a<0:
			ax = str(-3)
		else:
			ax = str(0)
		if b<0:
			bx = str(20)
		else:
			bx = str(23)
		if c<0:
			cx = str(44)
		else:
			cx = str(47)
		if d<0:
			dx = str(67)
		else:
			dx = str(70)
		if e<0:
			ex = str(91)
		else:
			ex = str(94)
		dec = random.randrange(0,4)
		if dec==0:
			ineq = "x > " + str(c)
			equation = str(f) + "x" + sign + str(abs(g)) + " > " + str(h)
			img = "ineqgt"
		elif dec==1:
			ineq = "x \\geq " + str(c)
			equation = str(f) + "x" + sign + str(abs(g)) + " \\geq " + str(h)
			img = "ineqgeq"
		elif dec==2:
			ineq = "x < " + str(c)
			equation = str(f) + "x" + sign + str(abs(g)) + " < " + str(h)
			img = "ineqlt"
		else:
			ineq = "x \\leq " + str(c)
			equation = str(f) + "x" + sign + str(abs(g)) + " \\leq " + str(h)
			img = "ineqleq"
		image = "\\begin{overpic}[scale=0.38]{algebra/images/" + img + "} \\put(" + ax + ",-10){" + str(a) + "} \\put(" + bx + ",-10){" + str(b) + "} \\put(" + cx + ",-10){" + str(c) + "} \\put(" + dx + ",-10){" + str(d) + "} \\put(" + ex + ",-10){" + str(e) + "}\\end{overpic}"
		question = "Solve $" + equation + "$ and represent your solution on a number line"
		answer = "$" + ineq + "$\\\\[0.3cm]" + image
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)