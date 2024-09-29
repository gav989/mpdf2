#!/usr/bin/env python3
#operations.py


def orderdecimals(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Order "
		else:
			explanation = ""
		list = [1,2,3,4,5,6,7,8,9]
		x = random.choice(list)
		list.remove(x)
		y = random.choice(list)
		dec = random.randrange(0,2)
		if random.randrange(0,2)==1:
			int1 = random.randrange(1,10)
		else:
			int1 = 0
		if dec==1:
			decimals = [round(0.001*x+int1,3),round(0.01*x+int1,2),round(0.1*x+int1,1),round(0.011*x+int1,3),round(0.101*x+int1,3),round(0.11*x+int1,2),round(0.111*x+int1,3)]
			a = random.choice(decimals)
			decimals.remove(a)
			b = random.choice(decimals)
			decimals.remove(b)
			c = random.choice(decimals)
			decimals.remove(c)
			d = random.choice(decimals)
			decimals.remove(d)
			e = random.choice(decimals)
		else:
			decimals = [round(0.01*x+int1 + 0.001*y,3),round(0.01*y + 0.001*x+int1,3),round(0.1*x+int1 + 0.01*y,2),round(0.1*y + 0.01*x+int1,2),round(0.1*x+int1 + 0.001*y,3),round(0.1*y + 0.001*x+int1,3),round(0.11*x+int1 + 0.001*y,3),round(0.11*y + 0.001*x+int1,3),round(0.1*x+int1 + 0.011*y,3),round(0.1*y + 0.011*x+int1,3),round(0.101*x+int1 + 0.01*y,3),round(0.101*y + 0.01*x+int1,3)]
			a = random.choice(decimals)
			decimals.remove(a)
			b = random.choice(decimals)
			decimals.remove(b)
			c = random.choice(decimals)
			decimals.remove(c)
			d = random.choice(decimals)
			decimals.remove(d)
			e = random.choice(decimals)
		ordered = sorted([a,b,c,d,e])
		shuffled = [ordered[0],ordered[1],ordered[2],ordered[3],ordered[4]]
		random.shuffle(shuffled)
		while ordered[0]==shuffled[0] and ordered[1]==shuffled[1] and ordered[2]==shuffled[2] and ordered[3]==shuffled[3] and ordered[4]==shuffled[4]:
			random.shuffle(shuffled)
#write question
		tempquestions.write(explanation + str(shuffled[0]) + ", " + str(shuffled[1]) + ", " + str(shuffled[2]) + ", " + str(shuffled[3]) + ", " + str(shuffled[4]))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(ordered[0]) + ", " + str(ordered[1]) + ", " + str(ordered[2]) + ", " + str(ordered[3]) + ", " + str(ordered[4]))

def reciprocal(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Write down the reciprical of "
		else:
			explanation = ""
		dec = random.randrange(0,2)
		if dec==1:
			number = str(random.randrange(2,10))
			reciprocal = "$\\dfrac{1}{" + number + "}$"
		else:
			nums = (2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,5,5,5,5,5,5,6,6,7,7,7,7,7,8,8,9,9,10,11)
			dens = (3,5,7,9,11,4,5,7,8,10,11,5,7,9,11,6,7,8,9,11,12,7,11,8,9,10,11,12,9,11,10,11,11,12)
			choice = random.randrange(0,34)
			num = nums[choice]
			den = dens[choice]
			number = "$\\dfrac{" + str(num) + "}{" + str(den) + "}$"
			integer = floor(den/num)
			den = den%num
			reciprocal = "$" + str(integer) + "\\dfrac{" + str(den) + "}{" + str(num) + "}$"
		if random.randrange(0,2)==1:
			temp = number
			number = reciprocal
			reciprocal = temp
#write question
		tempquestions.write(explanation + number)

		tempquestions.write("\n")
#write answer
		tempquestions.write(reciprocal)


def orderfdp(n,explanationn):
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Order "
		else:
			explanation = ""
		fracs = [2,4,5,6,8,10,12,14,15,16,18,20,22,24,25,26,28,30,32,34,35,36,38,40,42,44,45,46,48,50,52,54,55,56,58,60,62,64,65,66,68,70,72,74,75,76,78,80,82,84,85,86,88,90,92,94,95,96,98]
		dec = random.randrange(0,4)
		a = random.randrange(1,56)
		b = a + 1
		c = b + 1
		d = c + 1
		a = fracs[a]
		b = fracs[b]
		c = fracs[c]
		d = fracs[d] 
		ordered = [a,b,c,d]
		editor = [0,1,2,3]
		random.shuffle(editor)
		ordered[editor[0]] = str(round(ordered[editor[0]]/100,2))
		ordered[editor[1]] = Fraction(ordered[editor[1]],100)
		ordered[editor[1]] = "$\dfrac{" + str(ordered[editor[1]].numerator) + "}{" + str(ordered[editor[1]].denominator) + "}$"
		ordered[editor[2]] = str(ordered[editor[2]]) + "\%"
		dec = random.randrange(0,3)
		if dec==1:
			ordered[editor[3]] = str(round(ordered[editor[3]]/100,2))
		elif dec==2:
			ordered[editor[3]] = Fraction(ordered[editor[3]],100)
			ordered[editor[3]] = "$\dfrac{" + str(ordered[editor[3]].numerator) + "}{" + str(ordered[editor[3]].denominator) + "}$"
		else:
			ordered[editor[3]] = str(ordered[editor[3]]) + "\%"
		shuffled = [0,1,2,3]
		while shuffled[0]==0 and shuffled[1]==1 and shuffled[2]==2 and shuffled[3]==3:
			random.shuffle(shuffled)
		for i in range(0,4):
			shuffled[i] = ordered[shuffled[i]]
#write question
		tempquestions.write(explanation + shuffled[0] + " , " + shuffled[1] + " , " + shuffled[2] + " , " + shuffled[3])

		tempquestions.write("\n")
#write answer
		tempquestions.write(ordered[0] + " , " + ordered[1] + " , " + ordered[2] + " , " + ordered[3])


def orderfractions(n,explanationn):
	import random
	from math import ceil
	from fractions import gcd,Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		explanation = "Order "
		dens = [24,30,36,40,42,48,54,56,60,66,70,72,80,84,88,90,96,100,108,120,128,150,160,180,200]
		den = random.choice(dens)
		factors = []
		for i in range(3,ceil(den/2)+1):
			if den%i==0:
				factors.append(i)
		den1 = random.choice(factors)
		factors.remove(den1)
		den2 = random.choice(factors)
		factors.remove(den2)
		den3 = random.choice(factors)
		factors.remove(den3)
		den4 = random.choice(factors)
		nums = []
		for i in range(1,den1):
			if gcd(i,den1)==1:
				nums.append(i)
		num1 = random.choice(nums)
		nums = []
		for i in range(1,den2):
			if gcd(i,den2)==1:
				nums.append(i)
		num2 = random.choice(nums)
		nums = []
		for i in range(1,den3):
			if gcd(i,den3)==1:
				nums.append(i)
		num3 = random.choice(nums)
		nums = []
		for i in range(1,den4):
			if gcd(i,den4)==1:
				nums.append(i)
		num4 = random.choice(nums)
		frac1 = Fraction(num1,den1)
		frac2 = Fraction(num2,den2)
		frac3 = Fraction(num3,den3)
		frac4 = Fraction(num4,den4)
		ordered = [frac1,frac2,frac3,frac4]
		ordered.sort()
		a1 = "\dfrac{" + str(ordered[0].numerator) + "}{" + str(ordered[0].denominator) + "}"
		a2 = "\dfrac{" + str(ordered[1].numerator) + "}{" + str(ordered[1].denominator) + "}"
		a3 = "\dfrac{" + str(ordered[2].numerator) + "}{" + str(ordered[2].denominator) + "}"
		a4 = "\dfrac{" + str(ordered[3].numerator) + "}{" + str(ordered[3].denominator) + "}"
		shuffled = [frac1,frac2,frac3,frac4]
		while ordered[0]==shuffled[0] and ordered[1]==shuffled[1] and ordered[2]==shuffled[2] and ordered[3]==shuffled[3]:
			random.shuffle(shuffled)
		f1 = "\dfrac{" + str(shuffled[0].numerator) + "}{" + str(shuffled[0].denominator) + "}"
		f2 = "\dfrac{" + str(shuffled[1].numerator) + "}{" + str(shuffled[1].denominator) + "}"
		f3 = "\dfrac{" + str(shuffled[2].numerator) + "}{" + str(shuffled[2].denominator) + "}"
		f4 = "\dfrac{" + str(shuffled[3].numerator) + "}{" + str(shuffled[3].denominator) + "}"
		
#write question
		tempquestions.write(explanation + "$" + f1 + " , " + f2 + " , " + f3 + " , " + f4 + "$")

		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + a1 + " , " + a2 + " , " + a3 + " , " + a4 + "$")



def recurringdec1(n,explanationn):
	import random
	from fractions import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Convert "
			explanation2 = " to a fraction"
		else:
			explanation1 = ""
			explanation2 = ""
		recdec = random.randrange(1,9)
		pos = random.randrange(1,3)
		if pos==2:
			extras = [0,1,2,3,4,5,6,7,8,9]
			extras.remove(recdec)
			extra = random.choice(extras)
			num = 9*extra + recdec
			den = 90
		else:
			extra = ""
			num = recdec
			den = 9
		if random.randrange(0,2)==1:
			inte = 0
		else:
			inte = random.randrange(1,10)
		number = "$" + str(inte) + "." + str(extra) + "\\dot{" + str(recdec) + "}$"
		hcf = gcd(num,den)
		num = int(num/hcf)
		den = int(den/hcf)
		if inte==0:
			inte = ""
		frac = "$" + str(inte) + "\\dfrac{" + str(num) + "}{" + str(den) + "}$"
#write question
		tempquestions.write(explanation1 + number + explanation2)

		tempquestions.write("\n")
#write answer
		tempquestions.write(frac)


def recurringdec2(n,explanationn):
	import random
	from fractions import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Convert "
			explanation2 = " to a fraction"
		else:
			explanation1 = ""
			explanation2 = ""
		recdec1 = random.randrange(0,10)
		recs = [0,1,2,3,4,5,6,7,8,9]
		recs.remove(recdec1)
		recdec2 = random.choice(recs)
		recdec = recdec1*10 + recdec2
		if random.randrange(0,2)==1:
			inte = 0
		else:
			inte = random.randrange(1,10)
		pos = random.randrange(1,3)
		if pos==2:
			extras = [0,1,2,3,4,5,6,7,8,9]
			extras.remove(recdec2)
			extra = random.choice(extras)
			num = 100*extra + 10*recdec1 + recdec2 - (10*inte + extra)
			den = 990
		else:
			extra = ""
			num = recdec
			den = 99
		number = "$" + str(inte) + "." + str(extra) + "\\dot{" + str(recdec1) + "} \\dot{" + str(recdec2) + "}$"
		hcf = gcd(num,den)
		num = int(num/hcf)
		den = int(den/hcf)
		if inte==0:
			inte = ""
		frac = "$" + str(inte) + "\\dfrac{" + str(num) + "}{" + str(den) + "}$"
#write question
		tempquestions.write(explanation1 + number + explanation2)

		tempquestions.write("\n")
#write answer
		tempquestions.write(frac)


def recurringdec3(n,explanationn):
	import random
	from fractions import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Convert "
			explanation2 = " to a fraction"
		else:
			explanation1 = ""
			explanation2 = ""
		recdec1 = random.randrange(0,10)
		recs = [0,1,2,3,4,5,6,7,8,9]
		recdec2 = random.randrange(0,10)
		if recdec1==recdec2:
			recs.remove(recdec2)
		recdec3 = random.choice(recs)
		recdec = recdec1*100 + recdec2*10 + recdec3
		if random.randrange(0,2)==1:
			inte = 0
		else:
			inte = random.randrange(1,10)
		pos = random.randrange(1,3)
		if pos==2:
			extras = [0,1,2,3,4,5,6,7,8,9]
			if recdec1==recdec3:
				extras.remove(recdec2)
			extra = random.choice(extras)
			num = 1000*extra + 100*recdec1 + 10*recdec2 + recdec3 - (10*inte + extra)
			den = 9990
		else:
			extra = ""
			num = recdec
			den = 999
		number = "$" + str(inte) + "." + str(extra) + "\\dot{" + str(recdec1) + "}" + str(recdec2) + "\\dot{" + str(recdec3) + "}$"
		hcf = gcd(num,den)
		num = int(num/hcf)
		den = int(den/hcf)
		if inte==0:
			inte = ""
		frac = "$" + str(inte) + "\\dfrac{" + str(num) + "}{" + str(den) + "}$"
#write question
		tempquestions.write(explanation1 + number + explanation2)

		tempquestions.write("\n")
#write answer
		tempquestions.write(frac)


def ordermixhard(n,explanationn):
	import random
	from fractions import Fraction
	from math import floor,ceil,sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Order "
		else:
			explanation = ""
		surd = random.randrange(2,7)
		lower = surd
		surd = surd**2
		dec = random.randrange(0,2)
		if dec==1:
			surd = surd + random.randrange(1,3)
			lower = lower - 1
		else:
			surd = surd - random.randrange(1,3)

		square = floor(sqrt(lower*100))
		while square**2<lower*100:
			square = square + 1
		squares = [square]
		for i in range(1,7):
			if (squares[0] + i)**2 < (lower+1)*100:
				squares.append(squares[0]+i)
		square = random.choice(squares)/10
		
		
		rec = lower * 3 + random.randrange(1,3)
		
		#NEED TO FIX
		decimal = (lower*100 + random.randrange(1,100))/100
		
		a = "$\\sqrt{" + str(surd) + "}$"
		b = "$\\dfrac{" + str(rec) + "}{3}$"
		c = str(square) + "$^{2}$"
		d = str(decimal)	

		#ordered = [a,b,c,d]
		#shuffled = [0,1,2,3]
		#while shuffled[0]==0 and shuffled[1]==1 and shuffled[2]==2 and shuffled[3]==3:
		#	random.shuffle(shuffled)
		#for i in range(0,4):
		#	shuffled[i] = ordered[shuffled[i]]
#write question
		#tempquestions.write(explanation + shuffled[0] + " , " + shuffled[1] + " , " + shuffled[2] + " , " + shuffled[3])
		tempquestions.write(explanation + a + " , " + b + " , " + c + " , " + d)
		tempquestions.write("\n")
#write answer
		#tempquestions.write(ordered[0] + " , " + ordered[1] + " , " + ordered[2] + " , " + ordered[3])
		tempquestions.write("not available yet")
