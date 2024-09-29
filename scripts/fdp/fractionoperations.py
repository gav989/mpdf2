#!/usr/bin/env python3
#operations.py


def fractioncompare(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Which is larger, "
		else:
			explanation = ""
		nums = (1,2,1,2,3,1,3,2,3,4,1,5,4,3,5,2,7,5,3,7,4,5,6,7,8,9)
		dens = (5,9,4,7,10,3,8,5,7,9,2,9,7,5,8,3,10,7,4,9,5,6,7,8,9,10)
		f1 = random.randrange(0,len(nums)-2)
		f2 = f1 + random.randrange(1,3)
		f1 = "$\\dfrac{" + str(nums[f1]) + "}{" + str(dens[f1]) + "}$"
		f2 = "$\\dfrac{" + str(nums[f2]) + "}{" + str(dens[f2]) + "}$"
		answer = f2
		if random.randrange(1,3)==2:
			f2 = f1
			f1 = answer
#write question
		tempquestions.write(explanation + f1 + " or " + f2)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def fractionofamount1(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		den = random.randrange(2,13)
		num = 1
		amount = den * random.randrange(2,13)
		frac = Fraction(num,den)
		num = frac.numerator
		den = frac.denominator
#write question
		tempquestions.write(explanation + "$\\dfrac{" + str(num) + "}{" + str(den) + "}$ of " + str(amount))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(int(amount/den*num)))

def fractioninceasy(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Increase "
		else:
			explanation = ""
		startprice = random.randrange(2,10) * 10
		dens = []
		for i in range(2,13):
			if startprice%i==0:
				dens.append(i)
		den = random.choice(dens)
		endprice = startprice + (startprice/den)
#write question
		tempquestions.write(explanation + "\\pounds" + str(int(startprice)) + " by $\\dfrac{1}{" + str(den) + "}$")

		tempquestions.write("\n")
#write answer
		tempquestions.write("\\pounds" + str(int(endprice)))

def fractionofamount2(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		nums = (2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,5,5,5,5,5,5,6,6,7,7,7,7,7,8,8,9,9,10,11)
		dens = (3,5,7,9,11,4,5,7,8,10,11,5,7,9,11,6,7,8,9,11,12,7,11,8,9,10,11,12,9,11,10,11,11,12)
		choice = random.randrange(0,34)
		num = nums[choice]
		den = dens[choice]
		amount = den * random.randrange(2,13)
		frac = Fraction(num,den)
		num = frac.numerator
		den = frac.denominator
#write question
		tempquestions.write(explanation + "$\\dfrac{" + str(num) + "}{" + str(den) + "}$ of " + str(amount))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(int(amount/den*num)))


def fractionofamountreverse(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the original amount when "
		else:
			explanation = ""
		nums = (2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,5,5,5,5,5,5,6,6,7,7,7,7,7,8,8,9,9,10,11)
		dens = (3,5,7,9,11,4,5,7,8,10,11,5,7,9,11,6,7,8,9,11,12,7,11,8,9,10,11,12,9,11,10,11,11,12)
		choice = random.randrange(0,34)
		num = nums[choice]
		den = dens[choice]
		amount = den * random.randrange(2,13)
		frac = Fraction(num,den)
		num = frac.numerator
		den = frac.denominator
#write question
		tempquestions.write(explanation + "$\\dfrac{" + str(num) + "}{" + str(den) + "}$ of it is " + str(int(amount/den*num)))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(amount))



def fractionofamount3(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		dens = (2,3,4,5,8,10)
		mults = (2,5,10)
		den = random.choice(dens)
		num = random.randrange(1,den)
		amount = den * random.randrange(2,10) * random.choice(mults)
		frac = Fraction(num,den)
		num = frac.numerator
		den = frac.denominator
#write question
		tempquestions.write(explanation + "$\\dfrac{" + str(num) + "}{" + str(den) + "}$ of " + str(amount))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(int(amount/den*num)))

def fractionofamount4(n,explanationn):
	import random
	from fractions import Fraction
	from utilities.rounding import rounddp,rounddpstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		nums = (2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,5,5,5,5,5,5,6,6,7,7,7,7,7,8,8,9,9,10,11)
		dens = (3,5,7,9,11,4,5,7,8,10,11,5,7,9,11,6,7,8,9,11,12,7,11,8,9,10,11,12,9,11,10,11,11,12)
		choice = random.randrange(0,34)
		num = nums[choice]
		den = dens[choice]
		amount = rounddp(den * random.randrange(2,13) * 0.1,1)
		frac = Fraction(num,den)
		num = frac.numerator
		den = frac.denominator		
		answer = (amount/den) * num
		if amount%1==0:
			amount = int(amount)
		else:
			amount = rounddpstring(amount,2)
		if answer%1==0:
			answer = int(answer)
		else:
			answer = rounddpstring(answer,2)
		question = "$\\dfrac{" + str(num) + "}{" + str(den) + "}$ of \\pounds" + str(amount)
		answer = "\\pounds" + str(answer)
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def fractionsequivalent(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		num = random.randrange(1,12)
		den = random.randrange(num+1,13)
		mult = random.randrange(2,13)
		num2 = num * mult
		den2 = den * mult
#write question
		dec = random.randrange(0,2)
		if dec==1:
			tempquestions.write("$\\dfrac{" + str(num) + "}{" + str(den) + "} = \\dfrac{" + str(num2) + "}{?}$")
		else:
			tempquestions.write("$\\dfrac{" + str(num) + "}{" + str(den) + "} = \\dfrac{?}{" + str(den2) + "}$")

		tempquestions.write("\n")
#write answer
		
		if dec==1:
			tempquestions.write(str(den2))
		else:
			tempquestions.write(str(num2))



def fractionsimplify(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		num = random.randrange(1,12)
		den = random.randrange(num+1,13)
		frac = Fraction(num,den)
		mult = random.randrange(2,10)
		num = num * mult
		den = den * mult
#write question
		tempquestions.write(explanation + "$\\dfrac{" + str(num) + "}{" + str(den) + "}$")

		tempquestions.write("\n")
#write answer
		tempquestions.write("$\\dfrac{" + str(frac.numerator) + "}{" + str(frac.denominator) + "}$")


def fractionsimplify1step(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		nums = (2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,5,5,5,5,5,5,6,6,7,7,7,7,7,8,8,9,9,10,11)
		dens = (3,5,7,9,11,4,5,7,8,10,11,5,7,9,11,6,7,8,9,11,12,7,11,8,9,10,11,12,9,11,10,11,11,12)
		choice = random.randrange(0,len(nums))
		num = nums[choice]
		den = dens[choice]
		frac = Fraction(num,den)
		mults = [2,3,5,7,11]
		mult = random.choice(mults)
		num = frac.numerator * mult
		den = frac.denominator * mult
		
#write question
		tempquestions.write(explanation + "$\\dfrac{" + str(num) + "}{" + str(den) + "}$")

		tempquestions.write("\n")
#write answer
		tempquestions.write("$\\dfrac{" + str(frac.numerator) + "}{" + str(frac.denominator) + "}$")


def fractionconvert1(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Convert "
			explanation2 = " to a mixed number"
		else:
			explanation1 = ""
			explanation2 = ""
		number = random.randrange(1,4)
		denominator = random.randrange(2,13)
		numerator = random.randrange(1,denominator)
		frac = Fraction(numerator,denominator)
		thfrac = "$\\dfrac{" + str(frac.denominator*number+frac.numerator) + "}{" + str(frac.denominator) + "}$"
		mixed = "$" + str(number) + "\\dfrac{" + str(frac.numerator) + "}{" + str(frac.denominator) + "}$"
#write question
		tempquestions.write(explanation1 + thfrac + explanation2)

		tempquestions.write("\n")
#write answer
		tempquestions.write(mixed)

def fractionconvert1simplify(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Convert "
			explanation2 = " to a mixed number and simplify "
		else:
			explanation1 = ""
			explanation2 = ""
		number = random.randrange(1,4)
		denominator = random.randrange(2,13)
		numerator = random.randrange(1,denominator)
		frac = Fraction(numerator,denominator)
		scalers = [2,3,4,5,6,7,8,9,10,12,15,16,20,25,24,28,30,35,36,40]
		scaler = random.choice(scalers)
		top = (frac.denominator * number + frac.numerator) * scaler
		bottom = frac.denominator * scaler
		thfrac = "$\\dfrac{" + str(top) + "}{" + str(bottom) + "}$"
		mixed = "$" + str(number) + "\\dfrac{" + str(frac.numerator) + "}{" + str(frac.denominator) + "}$"
#write question
		tempquestions.write(explanation1 + thfrac + explanation2)

		tempquestions.write("\n")
#write answer
		tempquestions.write(mixed)


def fractionconvert2(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Convert "
			explanation2 = " to an improper fraction"
		else:
			explanation1 = ""
			explanation2 = ""
		number = random.randrange(1,4)
		denominator = random.randrange(2,13)
		numerator = random.randrange(1,denominator)
		frac = Fraction(numerator,denominator)
		thfrac = "$\\dfrac{" + str(frac.denominator*number+frac.numerator) + "}{" + str(frac.denominator) + "}$"
		mixed = "$" + str(number) + "\\dfrac{" + str(frac.numerator) + "}{" + str(frac.denominator) + "}$"
#write question
		tempquestions.write(explanation1 + mixed + explanation2)

		tempquestions.write("\n")
#write answer
		tempquestions.write(thfrac)

def fractionsadd(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		n =  random.randrange(1,6)
		d = n + random.randrange(1,8)
		f1 = Fraction(n,d)
		n =  random.randrange(1,6)
		d = n + random.randrange(1,8)
		f2 = Fraction(n,d)
		f3 = f1 + f2
		i3 = f3.numerator//f3.denominator
		if i3==0:
			i3 = ""
		else:
			f3 = f3 - i3
			i3 = str(i3) + " "
#write question
		tempquestions.write(explanation + "$\\dfrac{" + str(f1.numerator) + "}{" + str(f1.denominator) + "} + \\dfrac{" + str(f2.numerator) + "}{" + str(f2.denominator) + "}$")

		tempquestions.write("\n")
#write answer
		if f3.numerator==0:
			tempquestions.write(i3)
		else:
			tempquestions.write("$" + i3 + "\\dfrac{" + str(f3.numerator) + "}{" + str(f3.denominator) + "}$")

def fractionssubtract(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		n =  random.randrange(5,10)
		d = n + random.randrange(1,4)
		f1 = Fraction(n,d)
		n =  random.randrange(1,5)
		d = n + random.randrange(4,8)
		f2 = Fraction(n,d)
		f3 = f1 - f2
		i3 = f3.numerator//f3.denominator
		if i3==0:
			i3 = ""
		else:
			f3 = f3 - i3
			i3 = str(i3) + " "
#write question
		tempquestions.write(explanation + "$\\dfrac{" + str(f1.numerator) + "}{" + str(f1.denominator) + "} - \\dfrac{" + str(f2.numerator) + "}{" + str(f2.denominator) + "}$")

		tempquestions.write("\n")
#write answer
		if f3.numerator==0:
			tempquestions.write(i3)
		else:
			tempquestions.write("$" + i3 + "\\dfrac{" + str(f3.numerator) + "}{" + str(f3.denominator) + "}$")

def fractionsmultiply(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		n =  random.randrange(1,6)
		d = n + random.randrange(1,8)
		f1 = Fraction(n,d)
		n =  random.randrange(1,6)
		d = n + random.randrange(1,8)
		f2 = Fraction(n,d)
		f3 = f1 * f2
		i3 = f3.numerator//f3.denominator
		if i3==0:
			i3 = ""
		else:
			f3 = f3 - i3
			i3 = str(i3) + " "
#write question
		tempquestions.write(explanation + "$\\dfrac{" + str(f1.numerator) + "}{" + str(f1.denominator) + "} \\times \\dfrac{" + str(f2.numerator) + "}{" + str(f2.denominator) + "}$")

		tempquestions.write("\n")
#write answer
		if f3.numerator==0:
			tempquestions.write(i3)
		else:
			tempquestions.write("$" + i3 + "\\dfrac{" + str(f3.numerator) + "}{" + str(f3.denominator) + "}$")



def fractionsmultiplysimplifyfirst(n,explanationn):
	import random
	from fractions import Fraction
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		n =  random.randrange(1,6)
		d = n + random.randrange(1,8)
		f1 = Fraction(n,d)
		n =  random.randrange(1,6)
		d = n + random.randrange(1,8)
		f2 = Fraction(n,d)
		f3 = f1 * f2
		i3 = f3.numerator//f3.denominator
		if i3==0:
			i3 = ""
		else:
			f3 = f3 - i3
			i3 = str(i3) + " "
		f1n = f1.numerator
		f2n = f2.numerator
		f1d = f1.denominator
		f2d = f2.denominator
		mults = [2,3,5,7]
		random.shuffle(mults)
		mult1s = [mults[0]]
		mult2s = [mults[1]]
		mults.pop(0)
		mults.pop(0)
		if random.randrange(0,2)==1:
			mult1s.append(mult1s[0])
		else:
			mult1s.append(mults[0])
			mults.pop(0)
		if random.randrange(0,2)==1:
			mult2s.append(mult2s[0])
		else:
			mult2s.append(mults[0])
			mults.pop(0)
		mult1 = mult1s[0] * mult1s[1]
		mult2 = mult2s[0] * mult2s[1]	

		f1n *= mult1
		f2d *= mult1
		f1d *= mult2
		f2n *= mult2
		lcm1 = gcd(f1n,f1d)
		lcm2 = gcd(f2n,f2d)
		f1n = int(f1n/lcm1)
		f1d = int(f1d/lcm1)
		f2n = int(f2n/lcm2)
		f2d = int(f2d/lcm2)
		
		
#write question
		tempquestions.write(explanation + "$\\dfrac{" + str(f1n) + "}{" + str(f1d) + "} \\times \\dfrac{" + str(f2n) + "}{" + str(f2d) + "}$")

		tempquestions.write("\n")
#write answer
		if f3.numerator==0:
			tempquestions.write(i3)
		else:
			tempquestions.write("$" + i3 + "\\dfrac{" + str(f3.numerator) + "}{" + str(f3.denominator) + "}$")



def fractionsmultiplyinteger(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		integer = random.randrange(2,10)
		n =  random.randrange(1,6)
		d = n + random.randrange(1,8)
		f2 = Fraction(n,d)
		f3 = integer * f2
		i3 = f3.numerator//f3.denominator
		if i3==0:
			i3 = ""
		else:
			f3 = f3 - i3
			i3 = str(i3) + " "
#write question
		if random.randrange(0,2)==1:
			tempquestions.write(explanation + str(integer) + " $\\times$ $\\dfrac{" + str(f2.numerator) + "}{" + str(f2.denominator) + "}$")
		else:
			tempquestions.write(explanation + "$\\dfrac{" + str(f2.numerator) + "}{" + str(f2.denominator) + "}$ $\\times$ " + str(integer))
		

		tempquestions.write("\n")
#write answer
		if f3.numerator==0:
			tempquestions.write(i3)
		else:
			tempquestions.write("$" + i3 + "\\dfrac{" + str(f3.numerator) + "}{" + str(f3.denominator) + "}$")

def fractionsdivide(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		n =  random.randrange(1,6)
		d = n + random.randrange(1,8)
		f1 = Fraction(n,d)
		n =  random.randrange(1,6)
		d = n + random.randrange(1,8)
		f2 = Fraction(n,d)
		f3 = f1 / f2
		i3 = f3.numerator//f3.denominator
		if i3==0:
			i3 = ""
		else:
			f3 = f3 - i3
			i3 = str(i3) + " "
#write question
		tempquestions.write(explanation + "$\\dfrac{" + str(f1.numerator) + "}{" + str(f1.denominator) + "} \\div \\dfrac{" + str(f2.numerator) + "}{" + str(f2.denominator) + "}$")

		tempquestions.write("\n")
#write answer
		if f3.numerator==0:
			tempquestions.write(i3)
		else:
			tempquestions.write("$" + i3 + "\\dfrac{" + str(f3.numerator) + "}{" + str(f3.denominator) + "}$")



def fractionsdivideinteger(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		order = random.randrange(0,2)
		if order==1:
			n =  random.randrange(1,6)
			d = n + random.randrange(1,8)
			f1 = Fraction(n,d)
			f2 = random.randrange(2,10)
		else:
			n =  random.randrange(1,6)
			d = n + random.randrange(1,8)
			f2 = Fraction(n,d)
			f1 = random.randrange(2,10)
		f3 = f1 / f2
		i3 = f3.numerator//f3.denominator
		if i3==0:
			i3 = ""
		else:
			f3 = f3 - i3
			i3 = str(i3) + " "
#write question
		if order==1:
			tempquestions.write(explanation + "$\\dfrac{" + str(f1.numerator) + "}{" + str(f1.denominator) + "}$ $\\div$ " + str(f2))
		else:
			tempquestions.write(explanation + str(f1) + " $\\div$ $\\dfrac{" + str(f2.numerator) + "}{" + str(f2.denominator) + "}$")

		tempquestions.write("\n")
#write answer
		if f3.numerator==0:
			tempquestions.write(i3)
		else:
			tempquestions.write("$" + i3 + "\\dfrac{" + str(f3.numerator) + "}{" + str(f3.denominator) + "}$")


def mixednumbersadd(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		n =  random.randrange(1,6)
		d = n + random.randrange(1,8)
		f1 = Fraction(n,d)
		n =  random.randrange(1,6)
		d = n + random.randrange(1,8)
		f2 = Fraction(n,d)
		i1 = random.randrange(1,4)
		i2 = random.randrange(0,3)
		f3 = f1 + f2
		i3 = f3.numerator//f3.denominator
		f3 = f3 - i3
		i3 = i3 + i2 + i1
		i3 = str(i3) + " "
		if i2==0:
			i2 = ""
#write question
		tempquestions.write(explanation + "$" + str(i1) + "\\dfrac{" + str(f1.numerator) + "}{" + str(f1.denominator) + "} + " + str(i2) + "\\dfrac{" + str(f2.numerator) + "}{" + str(f2.denominator) + "}$")

		tempquestions.write("\n")
#write answer
		if f3.numerator==0:
			tempquestions.write(i3)
		else:
			tempquestions.write("$" + i3 + "\\dfrac{" + str(f3.numerator) + "}{" + str(f3.denominator) + "}$")


def mixednumberssubtract(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		n =  random.randrange(1,6)
		d = n + random.randrange(1,8)
		f1 = Fraction(n,d)
		n =  random.randrange(1,6)
		d = n + random.randrange(1,8)
		f2 = Fraction(n,d)
		i1 = random.randrange(1,4)
		if f1>f2:
			i2 = random.randrange(0,i1+1)
		else:
			i2 = random.randrange(0,i1)
		f3 = f1 - f2
		i3 = f3.numerator//f3.denominator
		f3 = f3 - i3
		i3 = i3 - i2 + i1
		if i2==0:
			i2 = ""
		if i3==0:
			i3 = ""
		else:
			i3 = str(i3) + " "
#write question
		tempquestions.write(explanation + "$" + str(i1) + "\\dfrac{" + str(f1.numerator) + "}{" + str(f1.denominator) + "} - " + str(i2) + "\\dfrac{" + str(f2.numerator) + "}{" + str(f2.denominator) + "}$")

		tempquestions.write("\n")
#write answer
		if f3.numerator==0:
			tempquestions.write(i3)
		else:
			tempquestions.write("$" + i3 + "\\dfrac{" + str(f3.numerator) + "}{" + str(f3.denominator) + "}$")


def mixednumbersmultiply(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		n =  random.randrange(1,6)
		d = n + random.randrange(1,8)
		f1 = Fraction(n,d)
		n =  random.randrange(1,6)
		d = n + random.randrange(1,8)
		f2 = Fraction(n,d)
		i1 = random.randrange(1,4)
		i2 = random.randrange(0,3)
		f3 = (f1 + i1) * (f2 + i2)
		i3 = f3.numerator//f3.denominator
		if i2==0:
			i2 = ""
		if i3==0:
			i3 = ""
		else:
			f3 = f3 - i3
			i3 = str(i3) + " "
#write question
		tempquestions.write(explanation + "$" + str(i1) + "\\dfrac{" + str(f1.numerator) + "}{" + str(f1.denominator) + "} \\times " + str(i2) + "\\dfrac{" + str(f2.numerator) + "}{" + str(f2.denominator) + "}$")

		tempquestions.write("\n")
#write answer
		if f3.numerator==0:
			tempquestions.write(i3)
		else:
			tempquestions.write("$" + i3 + "\\dfrac{" + str(f3.numerator) + "}{" + str(f3.denominator) + "}$")


def mixednumbersdivide(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		n =  random.randrange(1,6)
		d = n + random.randrange(1,8)
		f1 = Fraction(n,d)
		n =  random.randrange(1,6)
		d = n + random.randrange(1,8)
		f2 = Fraction(n,d)
		i1 = random.randrange(1,4)
		i2 = random.randrange(0,3)
		f3 = (f1 + i1) / (f2 + i2)
		i3 = f3.numerator//f3.denominator
		if i2==0:
			i2 = ""
		if i3==0:
			i3 = ""
		else:
			f3 = f3 - i3
			i3 = str(i3) + " "
#write question
		tempquestions.write(explanation + "$" + str(i1) + "\\dfrac{" + str(f1.numerator) + "}{" + str(f1.denominator) + "} \\div " + str(i2) + "\\dfrac{" + str(f2.numerator) + "}{" + str(f2.denominator) + "}$")

		tempquestions.write("\n")
#write answer
		if f3.numerator==0:
			tempquestions.write(i3)
		else:
			tempquestions.write("$" + i3 + "\\dfrac{" + str(f3.numerator) + "}{" + str(f3.denominator) + "}$")
