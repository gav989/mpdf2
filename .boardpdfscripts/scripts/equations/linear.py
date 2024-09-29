#linear.py

def onestepadd(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve "
		else:
			explanation = ""
		x = random.randrange(3,13)
		a = random.randrange(1,13)
#write question
		tempquestions.write(explanation + "$x + " + str(a) + " = " + str(x+a) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$x = " + str(x) + "$")


def onestepsubtract(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve "
		else:
			explanation = ""
		x = random.randrange(3,13)
		a = random.randrange(1,13)
#write question
		tempquestions.write(explanation + "$x - " + str(a) + " = " + str(x) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$x = " + str(x+a) + "$")

def onestepsubtract2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve "
		else:
			explanation = ""
		x = random.randrange(3,13)
		a = random.randrange(1,13)
#write question
		tempquestions.write(explanation + "$" + str(x + a) + " - x = " + str(a) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$x = " + str(x) + "$")

def onestepmultiply(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve "
		else:
			explanation = ""
		x = random.randrange(3,13)
		a = random.randrange(2,13)
#write question
		tempquestions.write(explanation + "$" + str(a) + "x = " + str(a*x) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$x = " + str(x) + "$")

def onestepdivide(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve "
		else:
			explanation = ""
		x = random.randrange(3,13)
		a = random.randrange(2,13)
#write question
		tempquestions.write(explanation + "$\\dfrac{x}{" + str(a) + "} = " + str(x) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$x = " + str(a*x) + "$")

def onestepdivide2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve "
		else:
			explanation = ""
		x = random.randrange(3,13)
		a = random.randrange(1,13)
#write question
		tempquestions.write(explanation + "$\\dfrac{" + str(x*a) + "}{x} = " + str(a) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$x = " + str(x) + "$")


def twostep1(n,explanationn,equalss):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve "
		else:
			explanation = ""
		if equalss==1:
			temp = random.randrange(1,6)
			if temp==1:
				equals = " > "
			elif temp==2:
				equals = " < "
			elif temp==3:
				equals = " \\geq "
			elif temp==4:
				equals = " \\leq "
			else:
				equals = " = "
		else:
			equals = " = "
			temp = 0
		x = random.randrange(1,13)
		a = random.randrange(2,13)
		signdec = random.randrange(0,2)
		if signdec==1:
			sign = " + "
			b = random.randrange(1,13)
			c = a*x + b
		else:
			sign = " - "	
			if a*x>15:
				b = random.randrange(1,13)
			else:
				b = random.randrange(1,a*x)
			c = a*x - b
#write question
		if random.randrange(1,3)==1:
			swap = 0
			tempquestions.write(explanation + "$" + str(a) + "x" + sign +  str(b) + equals + str(c) + "$")
		else:
			swap = 1
			tempquestions.write(explanation + "$" + str(c) + equals + str(a) + "x" + sign +  str(b) + "$")
		tempquestions.write("\n")
#write answer
		if swap==1:
			tempquestions.write("$" + str(x) + equals + "x$")
		else:
			tempquestions.write("$x" + equals + str(x) + "$")
			
def twostep2(n,explanationn,equalss):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve "
		else:
			explanation = ""
		if equalss==1:
			temp = random.randrange(1,6)
			if temp==1:
				equals = " > "
			elif temp==2:
				equals = " < "
			elif temp==3:
				equals = " \\geq "
			elif temp==4:
				equals = " \\leq "
			else:
				equals = " = "
		else:
			equals = " = "
			temp = 0
		x = random.randrange(1,13)*(-1)**random.randrange(1,3)
		a = random.randrange(2,13)
		b = random.randrange(1,36)
		if random.randrange(0,4)>1:
			a = random.randrange(1,7)
			choices=(2,4,5)
			choice = random.choice(choices)
			a = a * choice
			x = x / choice
			if a%1==0:
				a = int(a)
			if x%1==0:
				x = int(x)
		signdec = random.randrange(0,2)
		if signdec==1:
			sign = " + "
			c = int(a*x + b)
		else:
			sign = " - "	
			c = int(a*x - b)
#write question
		if random.randrange(1,3)==1:
			tempquestions.write(explanation + "$" + str(a) + "x" + sign +  str(b) + equals + str(c) + "$")
			swap = 0
		else:
			tempquestions.write(explanation + "$" + str(c) + equals + str(a) + "x" + sign +  str(b) + "$")
			swap = 1
		tempquestions.write("\n")
#write answer
		if swap==1:
			tempquestions.write("$" + str(x) + equals + "x$")
		else:
			tempquestions.write("$x" + equals + str(x) + "$")

def twostep3(n,explanationn,equalss):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve "
		else:
			explanation = ""
		if equalss==1:
			temp = random.randrange(1,6)
			if temp==1:
				equals = " > "
			elif temp==2:
				equals = " < "
			elif temp==3:
				equals = " \\geq "
			elif temp==4:
				equals = " \\leq "
			else:
				equals = " = "
		else:
			equals = " = "
			temp = 0
		x = random.randrange(1,13)*(-1)**random.randrange(1,3)
		a = random.randrange(2,13)
		b = random.randrange(1,36)
		if random.randrange(0,4)>1:
			a = random.randrange(1,7)
			choices=(2,4,5)
			choice = random.choice(choices)
			a = a * choice
			x = x / choice
			if a%1==0:
				a = int(a)
			if x%1==0:
				x = int(x)
		signdec = random.randrange(0,2)
		if signdec==1:
			sign = " + "
			c = int(a*x + b)
		else:
			sign = " - "	
			c = int(b - a*x)
#write question
		if random.randrange(1,3)==1:
			tempquestions.write(explanation + "$" + str(b) + sign  + str(a) + "x" + equals + str(c) + "$")
			swap = 0
		else:
			tempquestions.write(explanation + "$" + str(c) + equals + str(b) + sign + str(a) + "x" + "$")
			swap = 1
		tempquestions.write("\n")
#write answer
		if swap==1:
			tempquestions.write("$" + str(x) + equals + "x$")
		else:
			tempquestions.write("$x" + equals + str(x) + "$")


def twostep4(n,explanationn,equalss):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve "
		else:
			explanation = ""
		d = random.randrange(2,13)
		signdec = random.randrange(0,2)
		if signdec==1:
			sign = " + "
			n = random.randrange(1,16)
			a = n + random.randrange(2,12)
			x = d * (a - n)
		else:
			a = random.randrange(1,12)
			sign = " - "	
			n = random.randrange(1,(13-a))
			x = d * (a + n)
		if equalss==1:
			temp = random.randrange(1,6)
			if temp==1:
				equals = " > "
			elif temp==2:
				equals = " < "
			elif temp==3:
				equals = " \\geq "
			elif temp==4:
				equals = " \\leq "
			else:
				equals = " = "
		else:
			equals = " = "
			temp = 0
		qleft = "\\dfrac{x}{" + str(d) + "}" + sign + str(n)
		qright = str(a)
		swap = random.randrange(0,2)
		if swap==1:
			temp2 = qleft
			qleft = qright
			qright = temp2
#write question
		tempquestions.write(explanation + "$" + qleft + equals + qright + "$")
		tempquestions.write("\n")
#write answer
		if swap==1:
			tempquestions.write("$" + str(x) + equals + "x$")
		else:
			tempquestions.write("$x" + equals + str(x) + "$")

def twostep5(n,explanationn,equalss):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve "
		else:
			explanation = ""
		d = random.randrange(2,13)
		a = random.randrange(1,16) * (-1)**random.randrange(1,3)
		n = random.randrange(1,16)
		signdec = random.randrange(0,2)
		if signdec==1:
			sign = " + "
			if a==n:
				a = a + 1
			x = d * (a - n)
		else:
			sign = " - "
			if a==(n*-1):
				a = a - 1	
			x = d * (a + n)
		if equalss==1:
			temp = random.randrange(1,6)
			if temp==1:
				equals = " > "
			elif temp==2:
				equals = " < "
			elif temp==3:
				equals = " \\geq "
			elif temp==4:
				equals = " \\leq "
			else:
				equals = " = "
		else:
			equals = " = "
			temp = 0
		qleft = "\\dfrac{x}{" + str(d) + "}" + sign + str(n)
		qright = str(a)
		swap = random.randrange(0,2)
		if swap==1:
			temp2 = qleft
			qleft = qright
			qright = temp2
#write question
		tempquestions.write(explanation + "$" + qleft + equals + qright + "$")
		tempquestions.write("\n")
#write answer
		if swap==1:
			tempquestions.write("$" + str(x) + equals + "x$")
		else:
			tempquestions.write("$x" + equals + str(x) + "$")

def twostep6(n,explanationn,equalss):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve "
		else:
			explanation = ""
		d = random.randrange(2,13)
		a = random.randrange(1,13)
		n = random.randrange(1,16)
		signdec = random.randrange(0,2)
		if signdec==1:
			sign = " + "
			x = d * a - n
		else:
			sign = " - "	
			x = d * a + n
		if equalss==1:
			temp = random.randrange(1,6)
			if temp==1:
				equals = " > "
			elif temp==2:
				equals = " < "
			elif temp==3:
				equals = " \\geq "
			elif temp==4:
				equals = " \\leq "
			else:
				equals = " = "
		else:
			equals = " = "
			temp = 0
		qleft = "\\dfrac{x" + sign + str(n) + "}{" + str(d) + "}"
		qright = str(a)
		swap = random.randrange(0,2)
		if swap==1:
			temp2 = qleft
			qleft = qright
			qright = temp2
#write question
		tempquestions.write(explanation + "$" + qleft + equals + qright + "$")
		tempquestions.write("\n")
#write answer
		if swap==1:
			tempquestions.write("$" + str(x) + equals + "x$")
		else:
			tempquestions.write("$x" + equals + str(x) + "$")

def twostep7(n,explanationn,equalss):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve "
		else:
			explanation = ""
		d = random.randrange(2,13)
		a = random.randrange(1,13)*(-1)**random.randrange(1,3)
		n = random.randrange(1,16)
		signdec = random.randrange(0,2)
		if signdec==1:
			sign = " + "
			x = d * a - n
		else:
			sign = " - "	
			x = d * a + n
		if equalss==1:
			temp = random.randrange(1,6)
			if temp==1:
				equals = " > "
			elif temp==2:
				equals = " < "
			elif temp==3:
				equals = " \\geq "
			elif temp==4:
				equals = " \\leq "
			else:
				equals = " = "
		else:
			equals = " = "
		qleft = "\\dfrac{x" + sign + str(n) + "}{" + str(d) + "}"
		qright = str(a)
		swap = random.randrange(0,2)
		if swap==1:
			temp2 = qleft
			qleft = qright
			qright = temp2
#write question
		tempquestions.write(explanation + "$" + qleft + equals + qright + "$")
		tempquestions.write("\n")
#write answer
		if swap==1:
			tempquestions.write("$" + str(x) + equals + "x$")
		else:
			tempquestions.write("$x" + equals + str(x) + "$")

def twostep8(n,explanationn,equalss):
	import random
	from math import ceil
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve "
		else:
			explanation = ""
		if equalss==1:
			temp = random.randrange(1,6)
			if temp==1:
				equals = " > "
			elif temp==2:
				equals = " < "
			elif temp==3:
				equals = " \\geq "
			elif temp==4:
				equals = " \\leq "
			else:
				equals = " = "
		else:
			equals = " = "
		nums = (2,2,2,2,2 ,3,3,3,3,3 ,3 ,4,4,4,4 ,5,5,5,5,5 ,5 ,6,6, 7,7,7 ,7 ,7 ,3,5,7,4,5,7,5,7,6,7,7)
		dens = (3,5,7,9,11,4,5,7,8,10,11,5,7,9,11,6,7,8,9,11,12,7,11,8,9,10,11,12,2,2,2,3,3,3,4,4,5,5,6)
		choice = random.randrange(0,39)
		a = nums[choice]
		b = dens[choice]
		c = a*random.randrange(2,5)
		x = int(c*b/a)
		qleft = "\\dfrac{" + str(a) + "x}{" + str(b) + "}"
		qright = str(c) 
		swap = random.randrange(0,2)
		if swap==1:
			temp2 = qleft
			qleft = qright
			qright = temp2
#write question
		tempquestions.write(explanation + "$" + qleft + equals + qright + "$")
		tempquestions.write("\n")
#write answer
		if swap==1:
			tempquestions.write("$" + str(x) + equals + "x$")
		else:
			tempquestions.write("$x" + equals + str(x) + "$")


def threestep1(n,explanationn,equalss):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve "
		else:
			explanation = ""
		if equalss==1:
			temp = random.randrange(1,6)
			if temp==1:
				equals = " > "
			elif temp==2:
				equals = " < "
			elif temp==3:
				equals = " \\geq "
			elif temp==4:
				equals = " \\leq "
			else:
				equals = " = "
		else:
			equals = " = "
			temp = 0
		x = random.randrange(1,13)
		coefficients = [1,2,3,4,5,6,7,8,9,10]
		a = random.choice(coefficients)
		coefficients.remove(a)
		b = random.randrange(1,13)
		c = random.choice(coefficients)
		signdec = random.randrange(0,2)
		if signdec==1:
			sign1 = " + "
			temp = a*x + b
		else:
			sign1 = " - "	
			temp = a*x - b
		d = temp - c*x
		if d < 0:
			sign2 = " - "
		else:
			sign2 = " + "
		d = abs(d)
		if a<c:
			swap = 1
		else:
			swap = 0
		if a==1:
			a = ""
		if c==1:
			c = ""
#write question
		if d==0:
			tempquestions.write(explanation + "$" + str(a) + "x" + sign1 + str(b) + equals + str(c) + "x$")
		else:
			tempquestions.write(explanation + "$" + str(a) + "x" + sign1 + str(b) + equals + str(c) + "x" + sign2 + str(d) + "$")
		tempquestions.write("\n")
#write answer
		if swap==1:
			tempquestions.write("$" + str(x) + equals + "x$")
		else:
			tempquestions.write("$x" + equals + str(x) + "$")


def threestep2(n,explanationn,equalss):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve "
		else:
			explanation = ""
		if equalss==1:
			temp = random.randrange(1,6)
			if temp==1:
				equals = " > "
			elif temp==2:
				equals = " < "
			elif temp==3:
				equals = " \\geq "
			elif temp==4:
				equals = " \\leq "
			else:
				equals = " = "
		else:
			equals = " = "
			temp = 0
		x = random.randrange(1,13) * (-1)**random.randrange(1,3)
		coefficients = [1,2,3,4,5,6]
		coeffdiff = [2,4,5,10]
		a = random.choice(coefficients)
		c = a + random.choice(coeffdiff)
		if random.randrange(0,3)==1:
			temp = a
			a = c
			c = temp
		ints = [1,2,3,4,5,6,7,8,9,10]
		b = random.choice(ints)
		ints.remove(b)
		d = random.choice(ints)
		signdec = random.randrange(0,2)
		if signdec==1:
			sign1 = " + "
			tempb = b
		else:
			sign1 = " - "	
			tempb = 0 - b
		signdec = random.randrange(0,2)
		if signdec==1:
			sign2 = " + "
			tempd = d
		else:
			sign2 = " - "	
			tempd = 0 - d
		x = (tempb - tempd)/(c - a)
		if x%1==0:
			x = int(x)
		if a<c:
			swap = 1
		else:
			swap = 0
		if a==1:
			a = ""
		if c==1:
			c = ""
#write question
		if d==0:
			tempquestions.write(explanation + "$" + str(a) + "x" + sign1 + str(b) + equals + str(c) + "x$")
		else:
			tempquestions.write(explanation + "$" + str(a) + "x" + sign1 + str(b) + equals + str(c) + "x" + sign2 + str(d) + "$")
		tempquestions.write("\n")
#write answer
		if swap==1:
			tempquestions.write("$" + str(x) + equals + "x$")
		else:
			tempquestions.write("$x" + equals + str(x) + "$")

def threestep3(n,explanationn,equalss):
#on ks4 higher unit 3
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve "
		else:
			explanation = ""
		if equalss==1:
			temp = random.randrange(1,6)
			if temp==1:
				equals = " > "
			elif temp==2:
				equals = " < "
			elif temp==3:
				equals = " \\geq "
			elif temp==4:
				equals = " \\leq "
			else:
				equals = " = "
		else:
			equals = " = "
		num = random.randrange(1,10)
		den = random.randrange(2,10)
		dec = random.randrange(0,2)
		if dec==0:
			sign1 = " + "
			x = 0 - Fraction(den * num,den-1)
		else:
			sign1 = " - "
			x = Fraction(den * num,den+1)
		equation = "$\\dfrac{x}{" + str(den) + "} = " + str(num) + sign1 + "x$"
		if x<0:
			signa = "- "
			x = 0 - x
		else:
			signa = ""
		xnum = x.numerator
		xden = x.denominator
		if xnum%xden==0:
			x = int(xnum / xden)
		else:
			x = "\\dfrac{" + str(xnum) + "}{" + str(xden) + "}"
#write question
		tempquestions.write(explanation + equation)
		tempquestions.write("\n")
#write answer
		tempquestions.write("$x" + equals + signa + str(x) + "$")



def fourstep1(n,explanationn,equalss):
#on ks4 higher unit 3
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve "
		else:
			explanation = ""
		if equalss==1:
			temp = random.randrange(1,6)
			if temp==1:
				equals = " > "
			elif temp==2:
				equals = " < "
			elif temp==3:
				equals = " \\geq "
			elif temp==4:
				equals = " \\leq "
			else:
				equals = " = "
		else:
			equals = " = "
		coef = random.randrange(2,10)
		num = random.randrange(1,10)*(-1)**random.randrange(1,3)
		den = random.randrange(2,10)
		if num < 0:
			sign = " - "
		else:
			sign = " + "
		equation = "$" + str(coef) + "x" + sign + str(abs(num)) + equals + "\\dfrac{x}{" + str(den) + "}$"
		x = 0 - Fraction(den * num,den*coef - 1)
		if x<0:
			signa = "- "
			x = 0 - x
		else:
			signa = ""
		xnum = x.numerator
		xden = x.denominator
		if xnum%xden==0:
			x = int(xnum / xden)
		else:
			x = "\\dfrac{" + str(xnum) + "}{" + str(xden) + "}"
#write question
		tempquestions.write(explanation + equation)
		tempquestions.write("\n")
#write answer
		tempquestions.write("$x" + equals + signa + str(x) + "$")
