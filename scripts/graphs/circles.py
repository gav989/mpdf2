#!/usr/bin/env python3
#circles.py
def tangenteq(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		x = 0
		y = 0
		while x==0 and y==0:
			x = random.randrange(0,10) * (-1)**random.randrange(1,3)
			y = random.randrange(0,10) * (-1)**random.randrange(1,3)
		if x==0:
			equation = "$y = " + str(y) + "$"
		elif y==0:
			equation = "$x = " + str(x) + "$"
		else:
			rgrad = Fraction(y,x)
			tgrad = Fraction(-1,rgrad)
			c = Fraction(-1*tgrad*x + y,1)
			if tgrad<0:
				sign1 = "-"
				tgrad = tgrad * -1
			else:
				sign1 = ""
			if c<0:
				sign2 = "-"
				c = c * -1
			else:
				sign2 = "+"
			if tgrad.denominator==1:
				mfrac = str(tgrad.numerator)
			else:
				mfrac = "\\dfrac{" + str(tgrad.numerator) + "}{" + str(tgrad.denominator) + "}"
			if c.denominator==1:
				cfrac = str(c.numerator)
			else:
				cfrac = "\\dfrac{" + str(c.numerator) + "}{" + str(c.denominator) + "}"
			
			equation = "$y = " + sign1 + mfrac + "x" + sign2 + cfrac + "$"
#write question
		tempquestions.write("The point (" + str(x) + " , " + str(y) + ") lies on the circumference of a circle with centre (0 , 0). Find the equation of the tangent at this point.")
		tempquestions.write("\n")
#write answer
		tempquestions.write(equation)



def circleeq(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the equation of the circle that has centre (0 , 0) and passes through "
		else:
			explanation = ""
		x = random.randrange(-8,9)
		if x==0:
			y = random.randrange(1,9)*(-1)**random.randrange(1,3)
		else:
			y = random.randrange(-8,9)
		answer = "x$^{2}$ + y$^{2}$ = " + str(x**2 + y**2)
		question = explanation + "\\mbox{(" + str(x) + " , " + str(y) + ")}"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
