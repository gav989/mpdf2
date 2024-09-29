#!/usr/bin/env python3
#questiontemplate.py

def timestables(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(2,13)
		b = random.randrange(2,13)
#write question
		tempquestions.write(explanation + str(a) + " $\\times$ " + str(b))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a*b))

def threebyonemultiplication(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(2,10)
		b = random.randrange(111,1000)
		if random.randrange(0,2)==1:
			c = a
			a = b
			b = c
#write question
		tempquestions.write(explanation + str(a) + " $\\times$ " + str(b))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a*b))

def fourbyonemultiplication(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(2,10)
		b = random.randrange(1011,10000)
		if random.randrange(0,2)==1:
			c = a
			a = b
			b = c
#write question
		tempquestions.write(explanation + str(a) + " $\\times$ " + str(b))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a*b))

def twobyonemultiplication(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(2,10)
		b = random.randrange(11,100)
		if random.randrange(0,2)==1:
			c = a
			a = b
			b = c
#write question
		tempquestions.write(explanation + str(a) + " $\\times$ " + str(b))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a*b))

def twobytwomultiplication(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(11,100)
		b = random.randrange(11,100)
#write question
		tempquestions.write(explanation + str(a) + " $\\times$ " + str(b))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a*b))

def twobythreemultiplication(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(101,1000)
		b = random.randrange(11,100)
		if random.randrange(0,2)==1:
			c = a
			a = b
			b = c
#write question
		tempquestions.write(explanation + str(a) + " $\\times$ " + str(b))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a*b))

def threebythreemultiplication(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(101,1000)
		b = random.randrange(101,1000)
		if random.randrange(0,2)==1:
			c = a
			a = b
			b = c
#write question
		tempquestions.write(explanation + str(a) + " $\\times$ " + str(b))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a*b))

def decimalmultiplication0(n,explanationn):
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
		a = random.randrange(1,10) + 10 * random.randrange(1,10**random.randrange(1,3))
		a = a / 10**random.randrange(1,3)
		b = random.randrange(2,10)
		if random.randrange(0,2)==1:
			c = a
			a = b
			b = c
		answer = rounddp(a*b,6)
		if answer%1==0:
			answer = int(answer)
#write question
		tempquestions.write(explanation + str(a) + " $\\times$ " + str(b))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def decimalmultiplication1(n,explanationn):
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
		a = random.randrange(1,10) + 10 * random.randrange(1,10**random.randrange(1,3))
		a = a / 10**random.randrange(1,3)
		b = random.randrange(11,100)
		if random.randrange(0,2)==1:
			c = a
			a = b
			b = c
		answer = rounddp(a*b,6)
		if answer%1==0:
			answer = int(answer)
#write question
		tempquestions.write(explanation + str(a) + " $\\times$ " + str(b))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))

def decimalmultiplication2(n,explanationn):
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
		a = random.randrange(1,10) + 10 * random.randrange(1,10**random.randrange(1,3))
		a = a / 10**random.randrange(1,3)
		b = random.randrange(1,10) + 10 * random.randrange(1,10)
		b = b / 10**random.randrange(1,3)
		if random.randrange(0,2)==1:
			c = a
			a = b
			b = c
		answer = rounddp(a*b,6)
		if answer%1==0:
			answer = int(answer)
#write question
		tempquestions.write(explanation + str(a) + " $\\times$ " + str(b))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def decimalmultiplicationgiven1(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Given that "
		else:
			explanation = ""
		a = random.randrange(1,5)*10
		if a==1:
			a = a + random.randrage(5,10)
		else:
			a = a + random.randrange(1,10)
		btop = int(1000/a)
		b = random.randrange(1,btop)*10 + random.randrange(1,10)
		ab = a*b
		if random.randrange(1,3)==2:
			temp = a
			a = b
			b = temp
		left = random.randrange(-2,3)
		if left==0:
			right = random.randrange(1,3)*(-1)**random.randrange(1,3)
		else:
			right = random.randrange(-2,3)
		newleft = rounddp(a*10**left,4)
		newright = rounddp(b*10**right,4)
		if newleft%1==0:
			newleft = int(newleft)
		if newright%1==0:
			newright = int(newright)
		question = str(a) + " $\\times$ " + str(b) + " = " + str(ab) + ", find \\mbox{" + str(newleft) + " $\\times$ " + str(newright) + "}"
		answer = rounddp(ab * 10**(left + right),5)
		if answer%1==0:
			answer = int(answer)
		answer = str(answer)
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def decimalmultiplicationgiven2(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Given that "
		else:
			explanation = ""
		a = random.randrange(1,5)*10
		if a==1:
			a = a + random.randrage(5,10)
		else:
			a = a + random.randrange(1,10)
		btop = int(1000/a)
		b = random.randrange(1,btop)*10 + random.randrange(1,10)
		ab = a*b
		if random.randrange(1,3)==2:
			temp = a
			a = b
			b = temp
		left = random.randrange(-2,3)
		if left==0:
			right = random.randrange(1,3)*(-1)**random.randrange(1,3)
		else:
			right = random.randrange(-2,3)
		newleft = rounddp(a*10**left,4)
		newright = rounddp(b*10**right,4)
		if newleft%1==0:
			newleft = int(newleft)
		if newright%1==0:
			newright = int(newright)
		answer = rounddp(ab * 10**(left + right),5)
		if answer%1==0:
			answer = int(answer)
		question = str(a) + " $\\times$ " + str(b) + " = " + str(ab) + ", find \\mbox{" + str(answer) + " $\\div$ " + str(newright) + "}"
		answer = str(newleft)
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def multnapier21(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		top = random.randrange(1,10)*10 + random.randrange(1,10)
		right = random.randrange(2,10)
		answer = str(top*right)
		top = list(str(top))
		right = list(str(right))
		question = "\\centering\\begin{overpic}[scale=2]{fouroperators/images/napier21} \\put(25,79){" + top[0] + "} \\put(72,79){" + top[1] + "} \\put(103,45){" + right[0] + "} \\end{overpic}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def multnapier22(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		top = random.randrange(1,10)*10 + random.randrange(1,10)
		right = random.randrange(11,100)
		if random.randrange(0,2)==1:
			temp = top
			top = right
			right = temp
		answer = str(top*right)
		top = list(str(top))
		right = list(str(right))
		question = "\\centering\\begin{overpic}[scale=2]{fouroperators/images/napier22} \\put(22,102){" + top[0] + "} \\put(60,102){" + top[1] + "} \\put(83,76){" + right[0] + "} \\put(83,38){" + right[1] + "} \\end{overpic}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def multnapier32(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		top = random.randrange(101,999)
		right = random.randrange(11,100)
		answer = str(top*right)
		top = list(str(top))
		right = list(str(right))
		question = "\\centering\\begin{overpic}[scale=2]{fouroperators/images/napier32} \\put(19,86){" + top[0] + "} \\put(50,86){" + top[1] + "} \\put(82,86){" + top[2] + "} \\put(102,63){" + right[0] + "} \\put(102,33){" + right[1] + "} \\end{overpic}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def multnapier33(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		top = random.randrange(101,999)
		right = random.randrange(101,999)
		answer = str(top*right)
		top = list(str(top))
		right = list(str(right))
		question = "\\centering\\begin{overpic}[scale=2]{fouroperators/images/napier33} \\put(16,101){" + top[0] + "} \\put(43,101){" + top[1] + "} \\put(71,101){" + top[2] + "} \\put(88,82){" + right[0] + "} \\put(88,56){" + right[1] + "} \\put(88,29){" + right[2] + "} \\end{overpic}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def multnapier212(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		top = random.randrange(1,10)*10 + random.randrange(1,10)
		right = random.randrange(2,10)
		answer = str(top*right)
		question = "\\raggedright $" + str(top) + "\\times" + str(right) + "$"
		question = "\\noindent\\begin{minipage}[t]{\\linewidth}" + question + "\\\\[0.3cm] \\centering\\includegraphics[scale=2]{fouroperators/images/napier21}\\end{minipage}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def multnapier222(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		top = random.randrange(1,10)*10 + random.randrange(1,10)
		right = random.randrange(11,100)
		if random.randrange(0,2)==1:
			temp = top
			top = right
			right = temp
		answer = str(top*right)
		question = "\\raggedright $" + str(top) + "\\times" + str(right) + "$"
		question = "\\noindent\\begin{minipage}[t]{\\linewidth}" + question + "\\\\[0.3cm] \\centering\\includegraphics[scale=2]{fouroperators/images/napier22}\\end{minipage}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def multnapier322(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		top = random.randrange(101,999)
		right = random.randrange(11,100)
		answer = str(top*right)
		question = "\\raggedright $" + str(top) + "\\times" + str(right) + "$"
		question = "\\noindent\\begin{minipage}[t]{\\linewidth}" + question + "\\\\[0.7cm] \\raggedleft\\includegraphics[scale=2]{fouroperators/images/napier32}\\end{minipage}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def multnapier332(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		top = random.randrange(101,999)
		right = random.randrange(101,999)
		answer = str(top*right)
		question = "\\raggedright $" + str(top) + "\\times" + str(right) + "$"
		question = "\\noindent\\begin{minipage}[t]{\\linewidth}" + question + "\\\\[0.7cm] \\raggedleft\\includegraphics[scale=2]{fouroperators/images/napier33}\\end{minipage}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def multnapier21dec(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		top = random.randrange(1,10)*10 + random.randrange(1,10)
		top = rounddp(top/10,1)
		right = random.randrange(2,10)
		answer = rounddp(top*right,4)
		if answer%1==0:
			answer = int(answer)
		answer = str(answer)
		question = "\\raggedright $" + str(top) + "\\times" + str(right) + "$"
		question = "\\noindent\\begin{minipage}[t]{\\linewidth}" + question + "\\\\[0.3cm] \\centering\\includegraphics[scale=2]{fouroperators/images/napier21}\\end{minipage}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def multnapier22dec(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		top = random.randrange(1,10)*10 + random.randrange(1,10)
		right = random.randrange(1,10)*10 + random.randrange(1,10)
		top = rounddp(top/10**random.randrange(0,2),1)
		if top%1==0:
			top = int(top)
			right = rounddp(right/10,1)
		else:
			right = rounddp(right/10**random.randrange(0,2),1)
			if right%1==0:
				right = int(right)
		if random.randrange(0,2)==1:
			temp = top
			top = right
			right = temp
		answer = rounddp(top*right,4)
		if answer%1==0:
			answer = int(answer)
		answer = str(answer)
		question = "\\raggedright $" + str(top) + "\\times" + str(right) + "$"
		question = "\\noindent\\begin{minipage}[t]{\\linewidth}" + question + "\\\\[0.3cm] \\centering\\includegraphics[scale=2]{fouroperators/images/napier22}\\end{minipage}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def multnapier32dec(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		top = random.randrange(1,10)*100 + random.randrange(0,10)*10 + random.randrange(1,9)
		right = random.randrange(1,10)*10 + random.randrange(1,10)
		top = rounddp(top/10**random.randrange(0,3),2)
		if top%1==0:
			top = int(top)
			right = rounddp(right/10,1)
		else:
			right = rounddp(right/10**random.randrange(0,2),1)
			if right%1==0:
				right = int(right)
		answer = rounddp(top*right,4)
		if answer%1==0:
			answer = int(answer)
		answer = str(answer)
		question = "\\raggedright $" + str(top) + "\\times" + str(right) + "$"
		question = "\\noindent\\begin{minipage}[t]{\\linewidth}" + question + "\\\\[0.7cm] \\raggedleft\\includegraphics[scale=2]{fouroperators/images/napier32}\\end{minipage}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def multnapier33dec(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		top = random.randrange(1,10)*100 + random.randrange(0,10)*10 + random.randrange(1,9)
		if random.randrange(0,5)==1:
			top = rounddp((random.randrange(1,10)*10 + random.randrange(1,10))/100,2)
		right = random.randrange(1,10)*100 + random.randrange(0,10)*10 + random.randrange(1,9)
		top = rounddp(top/10**random.randrange(0,3),2)
		if top%1==0:
			top = int(top)
			right = rounddp(right/10,1)
		else:
			right = rounddp(right/10**random.randrange(0,3),2)
			if right%1==0:
				right = int(right)
		if random.randrange(0,2)==1:
			temp = top
			top = right
			right = temp
		answer = rounddp(top*right,4)
		if answer%1==0:
			answer = int(answer)
		answer = str(answer)
		question = "\\raggedright $" + str(top) + "\\times" + str(right) + "$"
		question = "\\noindent\\begin{minipage}[t]{\\linewidth}" + question + "\\\\[0.7cm] \\raggedleft\\includegraphics[scale=2]{fouroperators/images/napier33}\\end{minipage}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))
