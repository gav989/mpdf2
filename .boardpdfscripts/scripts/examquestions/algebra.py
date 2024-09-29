#!/usr/bin/env python3
#algebra.py

def celfahfunctionmachine(n,explanationn):
#in old fia4
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		degc = "$\\SI{}{\\SIUnitSymbolDegree C}$"
		degf = "$\\SI{}{\\SIUnitSymbolDegree F}$"
		intro = "This function machine can be used to convert between degrees celsius (" + degc + ") and degrees Fahrenheit (" + degf + ")."
		image = "\\hfill\\includegraphics[scale=0.4]{examquestions/images/celfah}\\hfill"		
		cel = 50 * random.randrange(1,11)
		fah = int(1.8 * cel + 32)
		intro2 = "Use the function machine to convert"
		questiona = "(a) " + str(cel) + degc + " to Fahrenheit."
		answera = str(fah) + degf
		fah = 32 + 9 * random.randrange(2,13)
		cel = int((fah - 32)/1.8)
		questionb = "(b) " + str(fah) + degf + " to Celsius."
		answerb = str(cel) + degc
		question = intro + nl + image + nl + intro2 + nl + questiona + nl + questionb
		answer = "(a) " + answera + nl + "(b) " + answerb
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def plumberformula(n,explanationn):
#in old fia4
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		coeff = random.randrange(2,9) * 5
		miles = random.randrange(5,21)
		hours = random.randrange(2,9)
		intro = "A plumber uses the following formula to work out the charge for a job."
		formula = "\\hspace{2cm} $C = d + " + str(coeff) + "h$"
		explanation = "$C$ is the charge in pounds." + nl + "$d$ is the distance in miles to travel to the job." + nl + "$h$ is the number of hours worked"
		questiona = "The plumber travels " + str(miles) + " miles to a job and works for " + str(hours) + " hours." + nl + "Work out how much he charges."
		question = intro + nl + formula + nl + explanation + nl + questiona
		answer = "\\pounds" + str(miles + coeff * hours)
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def quadraticsimeq(n,explanationn):
#past paper
	from fractions import Fraction
	from math import floor,ceil,sqrt
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		a = random.randrange(1,6)
		b = random.randrange(1,13) * (-1)**random.randrange(1,3)
		c = random.randrange(floor(b**2/(4*a)) - 8,floor(b**2/(4*a)))
		while c==0:
			c = random.randrange(floor(b**2/(4*a)) - 8,floor(b**2/(4*a)))
		while sqrt(b**2 - 4*a*c)%1==0:
			a = random.randrange(1,6)
			b = random.randrange(1,13) * (-1)**random.randrange(1,3)
			c = random.randrange(floor(b**2/(4*a)) - 8,floor(b**2/(4*a)))
			while c==0:
	        	        c = random.randrange(floor(b**2/(4*a)) - 8,floor(b**2/(4*a)))
		x1 = round((-b + sqrt(b**2 - 4*a*c))/(2*a),2)
		x2 = round((-b - sqrt(b**2 - 4*a*c))/(2*a),2)
		if a==1:
			m = random.randrange(2,6)
		elif a==4:
			choices = [1,3,4,5]
			m = random.choice(choices)
		else:
			m = random.randrange(1,6)
		ccc = random.randrange(1,6)
		aa = m**2 - a
		cc = ccc**2 - c
		if random.randrange(1,3)==1:
			sign5 = " + "
			bb = 2 * m * ccc - b
		else:
			sign5 = " - "
			bb = 2 * m * ccc * (-1) - b
		if b<0:
			sign1 = " - "
			b = abs(b)
		else:
			sign1 = " + "
		if c<0:
			sign2 = " - "
			c = abs(c)
		else:
			sign2 = " + "
		if b==1:
			b = ""
		if a==1:
			a = ""
		if aa<0:
			aa = aa * (-1)
			bb = bb * (-1)
			cc = cc * (-1)
		if bb<0:
			sign3 = " - "
			bb = abs(bb)
		else:
			sign3 = " + "
		if cc<0:
			sign4 = " - "
			cc = abs(cc)
		else:
			sign4 = " + "
		if aa==1:
			aa = ""
		if m==1:
			m = ""
		equation0 = "$" + str(a) + "x^{2}" + sign1 + str(b) + "x" + sign2 + str(c) + " = 0$"
		intro = "Here are the equations of two graphs."
		if bb==0:
			equation1 = "$y^{2} = " + str(aa) + "x^{2}" + sign4 + str(cc) + "$"
		else:
			equation1 = "$y^{2} = " + str(aa) + "x^{2}" + sign3 + str(bb) + "x" + sign4 + str(cc) + "$"
		equation2 = "$y = " + str(m) + "x" + sign5 + str(ccc) + "$"
		questiona = "(a) Show that the point of intersection of these graphs satisfies the equation " + equation0 + "."
		questionb = "(b) Solve the equation " + equation0 + ", giving your answers correct to 2 decimal places."
		question = intro + nl + equation1 + nl + equation2 + nl + questiona + nl + questionb
		answer = "(b) x = " + str(x2) + " and x = " + str(x1)
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
