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
	from utilities.rounding import rounddp
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
		x1 = rounddp((-b + sqrt(b**2 - 4*a*c))/(2*a),2)
		x2 = rounddp((-b - sqrt(b**2 - 4*a*c))/(2*a),2)
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



def simeqapplesbananas1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		choices1 = [2,2,2,3,5,7,3,3,3,4,5,7,4,4,5,7,5,5,6,7]
		choices2 = [3,5,7,2,2,2,4,5,7,3,3,3,5,7,4,4,6,7,5,5]
		choice = random.randrange(0,len(choices1))
		same = random.randrange(1,8)
		x = random.randrange(1,10)
		y = random.randrange(1,10)
		if random.randrange(1,3)==1:
			a = choices1[choice]
			b = same
			c = a * x + b * y
			d = choices2[choice]
			e = same
			f = d * x + e * y
		else:
			a = same
			b = choices1[choice]
			c = a * x + b * y
			d = same
			e = choices2[choice]
			f = d * x + e * y
		question = str(a) + " apples and " + str(b) + " bananas cost " + str(c) + "p. " + str(d) + " apples and " + str(e) + " bananas cost " + str(f) + "p. How much do apples and bananas cost?"
		answer = "Apples cost " + str(x) + "p, bananas cost " + str(y) + "p"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def simeqapplesbananas2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		choices1 = [2,2,2,3,5,7,3,3,3,4,5,7,4,4,5,7,5,5,6,7]
		choices2 = [3,5,7,2,2,2,4,5,7,3,3,3,5,7,4,4,6,7,5,5]
		choice = random.randrange(0,len(choices1))
		fac1 = random.randrange(1,5)
		fac2 = fac1 * random.randrange(2,6)
		if random.randrange(0,2)==1:
			temp = fac1
			fac1 = fac2
			fac2 = temp
		x = random.randrange(1,10)
		y = random.randrange(1,10)
		if random.randrange(1,3)==1:
			a = choices1[choice]
			b = fac1
			c = a * x + b * y
			d = choices2[choice]
			e = fac2
			f = d * x + e * y
		else:
			a = fac1
			b = choices1[choice]
			c = a * x + b * y
			d = fac2
			e = choices2[choice]
			f = d * x + e * y
		question = str(a) + " apples and " + str(b) + " bananas cost " + str(c) + "p. " + str(d) + " apples and " + str(e) + " bananas cost " + str(f) + "p. How much do apples and bananas cost?"
		answer = "Apples cost " + str(x) + "p, bananas cost " + str(y) + "p"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def simeqapplesbananas3(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		choices1 = [2,2,2,3,5,7,3,3,3,4,5,7,4,4,5,7,5,5,6,7]
		choices2 = [3,5,7,2,2,2,4,5,7,3,3,3,5,7,4,4,6,7,5,5]
		templist=list(range(0,20))
		choice1 = random.choice(templist)
		templist.remove(choice1)
		choice2 = random.choice(templist)
		x = random.randrange(1,10)
		y = random.randrange(1,10)
		a = choices1[choice1]
		b = choices1[choice2]
		c = a * x + b * y
		d = choices2[choice1]
		e = choices2[choice2]
		f = d * x + e * y
		question = str(a) + " apples and " + str(b) + " bananas cost " + str(c) + "p. " + str(d) + " apples and " + str(e) + " bananas cost " + str(f) + "p. How much do apples and bananas cost?"
		answer = "Apples cost " + str(x) + "p, bananas cost " + str(y) + "p"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def ratiophones(n,explanationn):
	import random
	from math import floor
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.04cm] "
		num1s = [15,15,15,15,25,25,35]
		num2s = [25,35,45,75,35,75,105]
		test = 1
		while test<20:
			choice = random.randrange(0,len(num1s))
			num1 = num1s[choice]
			num2 = num2s[choice]
			if random.randrange(0,2)==1:
				temp = num1
				num1 = num2
				num2 = temp
			diff2 = (random.randrange(1,10)*2+1)*5
			price1 = num1 + diff2
			price2 = num2 + diff2
			if price1>price2:
				lowest = price2
			else:
				lowest = price1
			diff1 = random.randrange(0,floor(lowest/10))*10 + 10
			test = gcd(price1 + diff1,price2 + diff1)
		hcf1 = gcd(price1,price2)
		rat1 = str(int(price1/hcf1)) + " : " + str(int(price2/hcf1))
		hcf2 = gcd(price1+diff1,price2+diff1)
		rat2 = str(int((price1+diff1)/hcf2)) + " : " + str(int((price2+diff1)/hcf2))
		hcf3 = gcd(price1-diff2,price2-diff2)
		rat3 = str(int((price1-diff2)/hcf3)) + " : " + str(int((price2-diff2)/hcf3))
		intro = "The prices of two cat beds are in the ratio x : y."
		line2 = "When the prices are both increased by \\pounds" + str(diff1) + ", the ratio becomes " + rat2 + "."
		line3 = "When the prices are both reduced by \\pounds" + str(diff2) + ", the ratio becomes " + rat3 + "."
		line4 = "Express the ratio x : y in its lowest terms."
		question = intro + nl + line2 + nl + line3 + nl + line4
		answer = "\\pounds" + str(price1) + " : \\pounds" + str(price2) + nl + rat1
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def equationoflineperprectangle(n,explanationn):
#in higher unit 5
	import random
	from math import floor,ceil
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		gradient = rounddp(random.randrange(1,7) * (-1)**random.randrange(1,3)/2,1)
		c = random.randrange(1,6)*(-1)**random.randrange(1,3)
		if gradient%1==0:
			gradient = int(gradient)
			xs = [1,2,3,4,5,6,-1,-2,-3,-4,-5,-6]
			x1 = random.choice(xs)
		else:
			xs = [2,4,6,-2,-4,-6]
			x1 = random.choice(xs)
		y1 = c + x1*gradient
		if y1%1==0:
			y1 = int(y1)
		coo1 = "\\mbox{(" + str(x1) + " , " + str(y1) + ")}"
		gradient2 = rounddp((-1)/gradient,2)
		c2 = rounddp(y1-(((-1)/gradient) * x1),2)
		if c2%1==0:
			c2 = int(c2)
		if gradient==1:
			gradient = ""
		if gradient==-1:
			gradient = "-"
		if c<0:
			sign = " - "
		else:
			sign = " + "
		if gradient2%1==0:
			gradient2 = int(gradient2)
		if gradient2==1:
			gradient2 = ""
		if gradient2==-1:
			gradient2 = "-"
		if c2<0:
			sign2 = " - "
		else:
			sign2 = " + "
		c2 = abs(c2)
		if c2==0.33:
			c2 = "$\\dfrac{1}{3}$"
		elif c2==0.67:
			c2 = "$\\dfrac{2}{3}$"
		elif rounddp(c2-floor(c2),2)==0.33:
			c2 = str(floor(c2)) + "$\\dfrac{1}{3}$"
		elif rounddp(c2-floor(c2),2)==0.67:
			c2 = str(floor(c2)) + "$\\dfrac{2}{3}$"
		if gradient2==0.33:
			gradient2 = "$\\dfrac{1}{3}$"
		if gradient2==-0.33:
			gradient2 = "-$\\dfrac{1}{3}$"
		if gradient2==0.67:
			gradient2 = "$\\dfrac{2}{3}$"
		if gradient2==-0.67:
			gradient2 = "-$\\dfrac{2}{3}$"

		line1 = "A has coordinates (0 , " + str(c) + ") and B has coordinates " + coo1 + "."
		questiona = "(a) Find the equation of line AB."
		questionb = "(b) A and B are two vertices of rectangle ABCD.\\\\ Find the equation of line BC."

		equation = "\\mbox{y = " + str(gradient) + "x" + sign + str(abs(c)) + "}"
		answer = "\\mbox{y = " + str(gradient2) + "x" + sign2 + str(c2) + "}"
		question = line1 + nl + questiona + nl + questionb
		answer = "(a) " + equation + "\\\\ (b) " + answer
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def sequenceintersection(n,explanationn):
#in higher unit 5
	import random
	from math import floor,ceil
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		n = random.randrange(5,21)
		coeffs = list(range(-12,13))
		coeffs.remove(0)
		coeff1 = random.choice(coeffs)
		coeffs.remove(coeff1)
		coeff2 = random.choice(coeffs)
		v = random.randrange(30,100)*(-1)**random.randrange(1,3)
		num1 = v - coeff1 * n
		num2 = v - coeff2 * n
		if coeff1<0 and num1>0:
			if coeff1==-1:
				coeff1 = ""
			else:
				coeff1 = str(abs(coeff1))
			seq1 = str(num1) + " - " + coeff1 + "n"
		elif num1>0:
			if coeff1==-1:
				coeff1 = "-"
			elif coeff1==1:
				coeff1 = ""
			else:
				coeff1 = str(abs(coeff1))
			seq1 = coeff1 + "n + " + str(num1)
		else:
			if coeff1==-1:
				coeff1 = "-"
			elif coeff1==1:
				coeff1 = ""
			else:
				coeff1 = str(coeff1)
			seq1 = coeff1 + "n - " + str(abs(num1))
		if coeff2<0 and num2>0:
			if coeff2==-1:
				coeff2 = ""
			else:
				coeff2 = str(abs(coeff2))
			seq2 = str(num2) + " - " + coeff2 + "n"
		elif num2>0:
			if coeff2==-1:
				coeff2 = "-"
			elif coeff2==1:
				coeff2 = ""
			else:
				coeff2 = str(abs(coeff2))
			seq2 = coeff2 + "n + " + str(num2)
		else:
			if coeff2==-1:
				coeff2 = "-"
			elif coeff2==1:
				coeff2 = ""
			else:
				coeff2 = str(coeff2)
			seq2 = coeff2 + "n - " + str(abs(num2))
		question = "The nth term of sequence A is \\mbox{" + seq1 + "} and the nth term for sequence B is \\mbox{" + seq2 + "}. The sequences A and B have one term with the same value, v, in the same position, n. Find the values of n and v."
		answer = "n = " + str(n) + " and v = " + str(v)
		
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def nthtermsimeq(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		a = random.randrange(2,7)
		b = random.randrange(2,10) * (-1)**random.randrange(1,3)
		answer = "a = " + str(a) + ", b = " + str(b)
		if b<0:
			sign = " - "
		else:
			sign = " + "
		terms = [2,3,4,5,6,7,8,9,10]
		words = ["second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
		n1 = random.choice(terms)
		terms.remove(n1)
		n2 = random.choice(terms)
		word1 = words[n1-2]
		word2 = words[n2-2]

		t1 = a * n1**2 + b * n1
		t2 = a * n2**2 + b * n2
		b = abs(b)
		if b==1:
			b = ""
		expression = str(a) + "n$^{2}$" + sign + str(b) + "n"
		question = "an$^{2}$ + bn, " + word1 + " term is " + str(t1) + ", " + word2 + " term is " + str(t2) + ". Find a and b."
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
