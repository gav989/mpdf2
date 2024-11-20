#!/usr/bin/env python3
#writcalc.py
import random
from utilities.rounding import rounddp

def singledigitaddition(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(1,10)
		b = random.randrange(1,10)
		question = explanation + str(a) + " + " + str(b)
		answer = str(a+b)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)
	

def twodigitaddition(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(10,100)
		b = random.randrange(10,100)
		question = explanation + str(a) + " + " + str(b)
		answer = str(a+b)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def threedigitaddition(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(100,1000)
		b = random.randrange(100,1000)
		question = explanation + str(a) + " + " + str(b)
		answer = str(a+b)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def fulladdition(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		selection = (2,3,3,4,4)
		c = random.choice(selection)
		d = random.choice(selection)
		a = random.randrange(10**(c-1),10**c)
		b = random.randrange(10**(d-1),10**d)
		question = explanation + str(a) + " + " + str(b)
		answer = str(a+b)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def decimaladdition(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		digits = random.randrange(1,3)
		a = random.randrange(1,10) + 10 * random.randrange(1,10**random.randrange(1,3))
		a = a / 10**random.randrange(1,2)
		b = random.randrange(1,10) + 10 * random.randrange(1,10**random.randrange(1,3))
		b = b / 10**random.randrange(1,2)
		question = explanation + str(a) + " + " + str(b)
		answer = rounddp(a+b,3)
		if answer%1==0:
			answer = int(answer)
		answer = str(answer)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def singledigitsubtraction(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(1,10)
		b = random.randrange(1,10)
		if a<b:
			c = a
			a = b
			b = c
		question = explanation + str(a) + " - " + str(b)
		answer = str(a-b)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def twodigitsubtraction(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(10,100)
		b = random.randrange(10,100)
		if a<b:
			c = a
			a = b
			b = c
		question = explanation + str(a) + " - " + str(b)
		answer = str(a-b)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def threedigitsubtraction(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(10,100)
		b = random.randrange(10,100)
		if a<b:
			c = a
			a = b
			b = c
		question = explanation + str(a) + " - " + str(b)
		answer = str(a-b)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def fullsubtraction(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		selection = (2,3,3,4,4)
		c = random.choice(selection)
		d = random.choice(selection)
		a = random.randrange(10**(c-1),10**c)
		b = random.randrange(10**(d-1),10**d)
		if a<b:
			c = a
			a = b
			b = c
		question = explanation + str(a) + " - " + str(b)
		answer = str(a-b)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def fullsubtraction(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		selection = (2,3,3,4,4)
		c = random.choice(selection)
		d = random.choice(selection)
		a = random.randrange(10**(c-1),10**c)
		b = random.randrange(10**(d-1),10**d)
		if a<b:
			c = a
			a = b
			b = c
		question = explanation + str(a) + " - " + str(b)
		answer = str(a-b)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def decimalsubtraction(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		digits = random.randrange(1,3)
		a = random.randrange(1,10) + 10 * random.randrange(1,10**random.randrange(1,3))
		a = a / 10**random.randrange(1,2)
		b = random.randrange(1,10) + 10 * random.randrange(1,10**random.randrange(1,3))
		b = b / 10**random.randrange(1,2)
		if a<b:
			c = a
			a = b
			b = c
		question = explanation + str(a) + " - " + str(b)
		answer = rounddp(a-b,3)
		if answer%1==0:
			answer = int(answer)
		answer = str(answer)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def timestables(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(2,13)
		b = random.randrange(2,13)
		question = explanation + str(a) + " $\\times$ " + str(b)
		answer = str(a*b)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)



def threebyonemultiplication(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
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
		question = explanation + str(a) + " $\\times$ " + str(b)
		answer = str(a*b)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def fourbyonemultiplication(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
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
		question = explanation + str(a) + " $\\times$ " + str(b)
		answer = str(a*b)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def twobyonemultiplication(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
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
		question = explanation + str(a) + " $\\times$ " + str(b)
		answer = str(a*b)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def twobytwomultiplication(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(11,100)
		b = random.randrange(11,100)
		question = explanation + str(a) + " $\\times$ " + str(b)
		answer = str(a*b)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def twobythreemultiplication(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
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
		question = explanation + str(a) + " $\\times$ " + str(b)
		answer = str(a*b)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def threebythreemultiplication(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
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
		question = explanation + str(a) + " $\\times$ " + str(b)
		answer = str(a*b)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def decimalmultiplication0(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
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
		question = explanation + str(a) + " $\\times$ " + str(b)
		answer = str(answer)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def decimalmultiplication1(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
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
		question = explanation + str(a) + " $\\times$ " + str(b)
		answer = str(answer)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def decimalmultiplication2(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
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
		question = explanation + str(a) + " $\\times$ " + str(b)
		answer = str(answer)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def decimalmultiplicationgiven1(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
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
		question = str(a) + " $\\times$ " + str(b) + " = " + str(ab) + ", \\mbox{find " + str(newleft) + " $\\times$ " + str(newright) + "}"
		answer = rounddp(ab * 10**(left + right),5)
		if answer%1==0:
			answer = int(answer)
		answer = str(answer)
		question = explanation + question
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def decimalmultiplicationgiven2(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
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
		question = explanation + question
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def multnapier21(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		top = random.randrange(1,10)*10 + random.randrange(1,10)
		right = random.randrange(2,10)
		answer = str(top*right)
		top = list(str(top))
		right = list(str(right))
		question = "\\centering\\begin{overpic}[scale=2]{functions/images/napier21} \\put(25,79){" + top[0] + "} \\put(72,79){" + top[1] + "} \\put(103,45){" + right[0] + "} \\end{overpic}"
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def multnapier22(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		top = random.randrange(1,10)*10 + random.randrange(1,10)
		right = random.randrange(11,100)
		if random.randrange(0,2)==1:
			temp = top
			top = right
			right = temp
		answer = str(top*right)
		top = list(str(top))
		right = list(str(right))
		question = "\\centering\\begin{overpic}[scale=2]{functions/images/napier22} \\put(22,102){" + top[0] + "} \\put(60,102){" + top[1] + "} \\put(83,76){" + right[0] + "} \\put(83,38){" + right[1] + "} \\end{overpic}"
#write question
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def multnapier32(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		top = random.randrange(101,999)
		right = random.randrange(11,100)
		answer = str(top*right)
		top = list(str(top))
		right = list(str(right))
		question = "\\centering\\begin{overpic}[scale=2]{functions/images/napier32} \\put(19,86){" + top[0] + "} \\put(50,86){" + top[1] + "} \\put(82,86){" + top[2] + "} \\put(102,63){" + right[0] + "} \\put(102,33){" + right[1] + "} \\end{overpic}"
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def multnapier33(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		top = random.randrange(101,999)
		right = random.randrange(101,999)
		answer = str(top*right)
		top = list(str(top))
		right = list(str(right))
		question = "\\centering\\begin{overpic}[scale=2]{functions/images/napier33} \\put(16,101){" + top[0] + "} \\put(43,101){" + top[1] + "} \\put(71,101){" + top[2] + "} \\put(88,82){" + right[0] + "} \\put(88,56){" + right[1] + "} \\put(88,29){" + right[2] + "} \\end{overpic}"
#write question
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def multnapier212(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		top = random.randrange(1,10)*10 + random.randrange(1,10)
		right = random.randrange(2,10)
		answer = str(top*right)
		question = "\\raggedright $" + str(top) + "\\times" + str(right) + "$"
		question = "\\noindent\\begin{minipage}[t]{\\linewidth}" + question + "\\\\[0.3cm] \\centering\\includegraphics[scale=2]{functions/images/napier21}\\end{minipage}"
#write question
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def multnapier222(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		top = random.randrange(1,10)*10 + random.randrange(1,10)
		right = random.randrange(11,100)
		if random.randrange(0,2)==1:
			temp = top
			top = right
			right = temp
		answer = str(top*right)
		question = "\\raggedright $" + str(top) + "\\times" + str(right) + "$"
		question = "\\noindent\\begin{minipage}[t]{\\linewidth}" + question + "\\\\[0.3cm] \\centering\\includegraphics[scale=2]{functions/images/napier22}\\end{minipage}"
#write question
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def multnapier322(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		top = random.randrange(101,999)
		right = random.randrange(11,100)
		answer = str(top*right)
		question = "\\raggedright $" + str(top) + "\\times" + str(right) + "$"
		question = "\\noindent\\begin{minipage}[t]{\\linewidth}" + question + "\\\\[0.7cm] \\raggedleft\\includegraphics[scale=2]{functions/images/napier32}\\end{minipage}"
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def multnapier332(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		top = random.randrange(101,999)
		right = random.randrange(101,999)
		answer = str(top*right)
		question = "\\raggedright $" + str(top) + "\\times" + str(right) + "$"
		question = "\\noindent\\begin{minipage}[t]{\\linewidth}" + question + "\\\\[0.7cm] \\raggedleft\\includegraphics[scale=2]{functions/images/napier33}\\end{minipage}"
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def multnapier21dec(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		top = random.randrange(1,10)*10 + random.randrange(1,10)
		top = rounddp(top/10,1)
		right = random.randrange(2,10)
		answer = rounddp(top*right,4)
		if answer%1==0:
			answer = int(answer)
		answer = str(answer)
		question = "\\raggedright $" + str(top) + "\\times" + str(right) + "$"
		question = "\\noindent\\begin{minipage}[t]{\\linewidth}" + question + "\\\\[0.3cm] \\centering\\includegraphics[scale=2]{functions/images/napier21}\\end{minipage}"
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def multnapier22dec(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
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
		question = "\\noindent\\begin{minipage}[t]{\\linewidth}" + question + "\\\\[0.3cm] \\centering\\includegraphics[scale=2]{functions/images/napier22}\\end{minipage}"
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def multnapier32dec(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
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
		question = "\\noindent\\begin{minipage}[t]{\\linewidth}" + question + "\\\\[0.7cm] \\raggedleft\\includegraphics[scale=2]{functions/images/napier32}\\end{minipage}"
###################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def multnapier33dec(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
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
		question = "\\noindent\\begin{minipage}[t]{\\linewidth}" + question + "\\\\[0.7cm] \\raggedleft\\includegraphics[scale=2]{functions/images/napier33}\\end{minipage}"
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)




def divisiontables(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(2,13)
		b = random.randrange(2,13)
		question = explanation + str(a*b) + " $\\div$ " + str(a)
		answer = str(b)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)




def divisiontablesten(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(2,13) * 10
		b = random.randrange(2,13)
		question = explanation + str(a*b) + " $\\div$ " + str(a)
		answer = str(b)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)




def singledigitdivision(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(2,10)
		b = random.randrange(13,10**(random.randrange(2,3)))
		question = explanation + str(a*b) + " $\\div$ " + str(a)
		answer = str(b)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)




def twodigitdivision(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(11,40)
		if random.randrange(0,2)==1:
			b = random.randrange(1,7) + random.randrange(0,7)*10 + random.randrange(1,7)*100
		else:
			b = random.randrange(1,7) + random.randrange(1,7)*10
		question = explanation + str(a*b) + " $\\div$ " + str(a)
		answer = str(b)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)




def twodigitdivisioneasy(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(11,20)
		if random.randrange(0,2)==1:
			b = random.randrange(1,7) + random.randrange(0,7)*10 + random.randrange(1,7)*100
		else:
			b = random.randrange(1,7) + random.randrange(1,7)*10
		question = explanation + str(a*b) + " $\\div$ " + str(a)
		answer = str(b)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)




def twodigittables(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation1 = "Write out the first five numbers in the "
			explanation2 = " times table"
		else:
			explanation1 = ""
			explanation2 = ""
		n = random.randrange(1,9) + random.randrange(1,9)*10
		question = explanation1 + str(n) + explanation2
		answer = str(n) + ", " + str(n*2) + ", " + str(n*3) + ", " + str(n*4) + ", " + str(n*5)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)




def decimaldivision1(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		a = random.randrange(2,10)
		b = random.randrange(1,10**random.randrange(1,3)) * 10 + random.randrange(1,10)
		c = a*b
		while c%10==0:
			c = c/10
		c = c/10**random.randrange(1,4)
		b = c/a		
		question = explanation + str(c) + " $\\div$ " + str(a)
		answer = str(rounddp(b,6))
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)




def decimaldivision2(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		divisor = (2,4,5,6,8)
		a = random.choice(divisor)
		if a==6:
			c = 3 * ((random.randrange(20,300)*2)-1)
		elif a==5:
			c = 5 * random.randrange(20,200) - random.randrange(1,5)
		else:
			c = (random.randrange(100,1000)*2)-1
		b = c/a		
		question = explanation + str(c) + " $\\div$ " + str(a)
		answer = str(rounddp(b,6))
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)




def decimaldivision3(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		divisors = [2,3,4,5,6,7,8,9,11,12]
		divisor = rounddp(random.choice(divisors)/10**random.randrange(1,3),2)
		answer = rounddp(random.randrange(11,100)/10**random.randrange(0,3),2)
		amount = rounddp(divisor * answer,4)
		if amount%1==0:
			amount = int(amount)
		if answer%1==0:
			answer = int(answer)
		question = "$" + str(amount) + "\\div" + str(divisor) + "$"
		answer = explanation + str(answer)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)




def decimaldivision4(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		divisor = random.randrange(1,10)*10 + random.randrange(1,10)
		divisor = rounddp(divisor/10**random.randrange(1,3),2)
		answer = rounddp((random.randrange(1,7)*10 + random.randrange(1,7))/10**random.randrange(0,3),2)
		amount = rounddp(divisor * answer,4)
		if amount%1==0:
			amount = int(amount)
		if answer%1==0:
			answer = int(answer)
		question = "$" + str(amount) + "\\div" + str(divisor) + "$"
		answer = explanation + str(answer)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)




def divisionbydecimal(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		aas = [2,3,4,5,6,7,8,9,11,12]
		a = random.choice(aas)
		b = random.randrange(2,13)
		c = a * b
		a = a/10
		b = b * 10
		question = explanation + str(c) + " $\\div$ " + str(a)
		answer = str(b)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)




def divisionbydecimal2(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		aas = [2,3,4,5,6,7,8,9,11,12]
		a = random.choice(aas)
		b = rounddp(random.randrange(20,1300)/10**random.randrange(1,3),2)
		c = rounddp(a * b,5)
		if c%1==0:
			int(c)
		a = rounddp(a/10,1)
		b = rounddp(b * 10,5)
		if b%1==0:
			b = int(b)
		question = explanation + str(c) + " $\\div$ " + str(a)
		answer = str(b)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)




def divisibility(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation = "True or false, "
		else:
			explanation = ""
		divisors = [2,3,4,5,6,7,8,9,10]
		divisor = random.choice(divisors)
		dec = random.randrange(0,2)
		if dec==1:
			checker = divisor * random.randrange(15,100)
			answer = "True"
		else:
			checker = divisor * random.randrange(15,100) + random.randrange(1,divisor)
			answer = "False"
		question = explanation + str(divisor) + " is a factor of " + str(checker)
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)




