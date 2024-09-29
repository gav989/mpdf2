#!/usr/bin/env python3
#operations.py


def orderdecimals(n,explanationn):
	import random
	from utilities.rounding import rounddp
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
			decimals = [rounddp(0.001*x+int1,3),rounddp(0.01*x+int1,2),rounddp(0.1*x+int1,1),rounddp(0.011*x+int1,3),rounddp(0.101*x+int1,3),rounddp(0.11*x+int1,2),rounddp(0.111*x+int1,3)]
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
			decimals = [rounddp(0.01*x+int1 + 0.001*y,3),rounddp(0.01*y + 0.001*x+int1,3),rounddp(0.1*x+int1 + 0.01*y,2),rounddp(0.1*y + 0.01*x+int1,2),rounddp(0.1*x+int1 + 0.001*y,3),rounddp(0.1*y + 0.001*x+int1,3),rounddp(0.11*x+int1 + 0.001*y,3),rounddp(0.11*y + 0.001*x+int1,3),rounddp(0.1*x+int1 + 0.011*y,3),rounddp(0.1*y + 0.011*x+int1,3),rounddp(0.101*x+int1 + 0.01*y,3),rounddp(0.101*y + 0.01*x+int1,3)]
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



def ordernumbers1(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Order "
		else:
			explanation = ""
		ordered = []
		numlist = list(range(10,100))
		for i in range(0,5):
			x = random.choice(numlist)
			numlist.remove(x)
			ordered.append(x)
		ordered = sorted(ordered)
		shuffled = [ordered[0],ordered[1],ordered[2],ordered[3],ordered[4]]
		random.shuffle(shuffled)
		while ordered[0]==shuffled[0] and ordered[1]==shuffled[1] and ordered[2]==shuffled[2] and ordered[3]==shuffled[3] and ordered[4]==shuffled[4]:
			random.shuffle(shuffled)
#write question
		tempquestions.write(explanation + str(shuffled[0]) + ", " + str(shuffled[1]) + ", " + str(shuffled[2]) + ", " + str(shuffled[3]) + ", " + str(shuffled[4]))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(ordered[0]) + ", " + str(ordered[1]) + ", " + str(ordered[2]) + ", " + str(ordered[3]) + ", " + str(ordered[4]))


def ordernumbers2(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Order "
		else:
			explanation = ""
		ordered = []
		numlist = list(range(10,1000))
		for i in range(0,5):
			x = random.choice(numlist)
			numlist.remove(x)
			ordered.append(x)
		ordered = sorted(ordered)
		shuffled = [ordered[0],ordered[1],ordered[2],ordered[3],ordered[4]]
		random.shuffle(shuffled)
		while ordered[0]==shuffled[0] and ordered[1]==shuffled[1] and ordered[2]==shuffled[2] and ordered[3]==shuffled[3] and ordered[4]==shuffled[4]:
			random.shuffle(shuffled)
#write question
		tempquestions.write(explanation + str(shuffled[0]) + ", " + str(shuffled[1]) + ", " + str(shuffled[2]) + ", " + str(shuffled[3]) + ", " + str(shuffled[4]))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(ordered[0]) + ", " + str(ordered[1]) + ", " + str(ordered[2]) + ", " + str(ordered[3]) + ", " + str(ordered[4]))


def ordernumbers3(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Order "
		else:
			explanation = ""
		ordered = []
		numlist = list(range(10,10000))
		for i in range(0,5):
			x = random.choice(numlist)
			numlist.remove(x)
			ordered.append(x)
		ordered = sorted(ordered)
		shuffled = [ordered[0],ordered[1],ordered[2],ordered[3],ordered[4]]
		random.shuffle(shuffled)
		while ordered[0]==shuffled[0] and ordered[1]==shuffled[1] and ordered[2]==shuffled[2] and ordered[3]==shuffled[3] and ordered[4]==shuffled[4]:
			random.shuffle(shuffled)
#write question
		tempquestions.write(explanation + str(shuffled[0]) + ", " + str(shuffled[1]) + ", " + str(shuffled[2]) + ", " + str(shuffled[3]) + ", " + str(shuffled[4]))

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(ordered[0]) + ", " + str(ordered[1]) + ", " + str(ordered[2]) + ", " + str(ordered[3]) + ", " + str(ordered[4]))



def ordernumbers4(n,explanationn):
	import random
	from utilities.rounding import rounddp
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
			decimals = [rounddp(0.001*x+int1,3),rounddp(0.01*x+int1,2),rounddp(0.1*x+int1,1),rounddp(0.011*x+int1,3),rounddp(0.101*x+int1,3),rounddp(0.11*x+int1,2),rounddp(0.111*x+int1,3)]
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
			decimals = [rounddp(0.01*x+int1 + 0.001*y,3),rounddp(0.01*y + 0.001*x+int1,3),rounddp(0.1*x+int1 + 0.01*y,2),rounddp(0.1*y + 0.01*x+int1,2),rounddp(0.1*x+int1 + 0.001*y,3),rounddp(0.1*y + 0.001*x+int1,3),rounddp(0.11*x+int1 + 0.001*y,3),rounddp(0.11*y + 0.001*x+int1,3),rounddp(0.1*x+int1 + 0.011*y,3),rounddp(0.1*y + 0.011*x+int1,3),rounddp(0.101*x+int1 + 0.01*y,3),rounddp(0.101*y + 0.01*x+int1,3)]
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
		for i in range(0,5):
			shuffled[i] = int(rounddp(shuffled[i]*1000,0))
			ordered[i] = int(rounddp(ordered[i]*1000,0))
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
			explanation = "Write down the reciprocal of "
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

def reciprocal2(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Write down the reciprocal of "
		else:
			explanation = ""
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

def reciprocal1(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Write down the reciprocal of "
		else:
			explanation = ""
		dec = 1
		number = str(random.randrange(2,10))
		reciprocal = "$\\dfrac{1}{" + number + "}$"
		if random.randrange(0,2)==1:
			temp = number
			number = reciprocal
			reciprocal = temp
#write question
		tempquestions.write(explanation + number)

		tempquestions.write("\n")
#write answer
		tempquestions.write(reciprocal)



def reciprocaldec(n,explanationn):
	import random
	from math import floor
	from math import gcd
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Write down the reciprocal of "
		else:
			explanation = ""
		num = random.randrange(1,4)
		decs = [2,4,5,6,8]
		dec = random.choice(decs)
		decimal = num + rounddp(dec/10,1)
		num = num*10 + dec
		den = 10
		hcf = gcd(den,num)
		answer = "$\\dfrac{" + str(int(den/hcf)) + "}{" + str(int(num/hcf)) + "}$"
#write question
		tempquestions.write(explanation + str(decimal))

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def orderfdp(n,explanationn):
	import random
	from utilities.rounding import rounddp
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
		ordered[editor[0]] = str(rounddp(ordered[editor[0]]/100,2))
		ordered[editor[1]] = Fraction(ordered[editor[1]],100)
		ordered[editor[1]] = "$\dfrac{" + str(ordered[editor[1]].numerator) + "}{" + str(ordered[editor[1]].denominator) + "}$"
		ordered[editor[2]] = str(ordered[editor[2]]) + "\%"
		dec = random.randrange(0,3)
		if dec==1:
			ordered[editor[3]] = str(rounddp(ordered[editor[3]]/100,2))
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
		tempquestions.write(explanation + "$\mbox{" + shuffled[0] + " , " + shuffled[1] + " , " + shuffled[2] + " , " + shuffled[3] + "}$")

		tempquestions.write("\n")
#write answer
		tempquestions.write(ordered[0] + " , " + ordered[1] + " , " + ordered[2] + " , " + ordered[3])


def orderfractions(n,explanationn):
	import random
	from math import ceil
	from math import gcd
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Order "
		else:
			explanation = ""
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
	from math import gcd
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
		number = str(inte) + "." + str(extra) + "\\.{" + str(recdec) + "}"
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
	from math import gcd
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
			num = 99*extra + 10*recdec1 + recdec2
			den = 990
		else:
			extra = ""
			num = recdec
			den = 99
		number = str(inte) + "." + str(extra) + "\\.{" + str(recdec1) + "}\\.{" + str(recdec2) + "}"
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
	from math import gcd
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
		pos = 1 #CHANGE IF NEEDED
		if pos==2:
			extras = [0,1,2,3,4,5,6,7,8,9]
			if recdec1==recdec3:
				extras.remove(recdec2)
			extras.remove(recdec3)
			extra = random.choice(extras)
			num = 999*extra + 100*recdec1 + 10*recdec2 + recdec3
			den = 9990
		else:
			extra = ""
			num = recdec
			den = 999
		number = str(inte) + "." + str(extra) + "\\.{" + str(recdec1) + "}" + str(recdec2) + "\\.{" + str(recdec3) + "}"
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

def fractorec(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Convert "
			explanation2 = " to a recurring decimal"
		else:
			explanation1 = ""
			explanation2 = ""
		dens = [3,6,7,9,11]
		den = random.choice(dens)
		if den==6:
			nums = [1,5]
			num = random.choice(nums)
		elif den==9:
			nums = [1,2,4,5,7,8]
			num = random.choice(nums)
		else:
			num = random.randrange(1,den)
		question = "$\\dfrac{" + str(num) + "}{" + str(den) + "}$"
		aden = 9
		if den==6:
			if num==1:
				answer = "0.1\\.{6}"
			else:
				answer = "0.8\\.{3}"
		elif num==1 and den==11:
			answer = "0.\\.{0}\\.{9}"
		else:
			while aden%den!=0:
				aden = aden * 10 + 9
			scaler = int(aden/den)
			answer = num * scaler
			answerl = list(str(answer))
			answer1 = answerl[0]
			if len(answerl)==1:
				answer = "0.\\.{" + str(answer1) + "}"
			else:
				answer = "0.\\.{" + str(answer1) + "}"
				for i in range(1,len(answerl)-1):
					answer = answer + answerl[i]
				answer = answer + "\\.{" + str(answerl[len(answerl)-1]) + "}"
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


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
		if square%1==0:
			square = int(square)
		
		rec = lower * 3 + random.randrange(1,3)
		
		decimal = (lower*100 + random.randrange(1,100))/100
		
		a = "$\\sqrt{" + str(surd) + "}$"
		b = "$\\dfrac{" + str(rec) + "}{3}$"
		c = str(square) + "$^{2}$"
		d = str(decimal)	

		anum = sqrt(surd)
		bnum = rec/3
		cnum = square**2
		dnum = decimal
		texts = [a,b,c,d]
		nums = [anum,bnum,cnum,dnum]
		numssorted = sorted([anum,bnum,cnum,dnum])
		ordered = [texts[nums.index(numssorted[0])],texts[nums.index(numssorted[1])],texts[nums.index(numssorted[2])],texts[nums.index(numssorted[3])]]
		shuffled = [0,1,2,3]
		while shuffled[0]==0 and shuffled[1]==1 and shuffled[2]==2 and shuffled[3]==3:
			random.shuffle(shuffled)
		for i in range(0,4):
			shuffled[i] = ordered[shuffled[i]]
#write question
		tempquestions.write(explanation + shuffled[0] + " , " + shuffled[1] + " , " + shuffled[2] + " , " + shuffled[3])
		#tempquestions.write(explanation + a + " , " + b + " , " + c + " , " + d)
		tempquestions.write("\n")
#write answer
		tempquestions.write(ordered[0] + " , " + ordered[1] + " , " + ordered[2] + " , " + ordered[3])
		#tempquestions.write("not available yet")



def fdpwallfractions(n,explanationn):
	import random
	from math import gcd
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		d4 = [1,3]
		d5 = [1,2,3,4]
		d10 = [1,3,7,9]
		d20 = [1,3,7,9,11,13,17,19]
		d25 = [1,2,3,4,6,7,8,9,11,12,13,14,16,17,18,19,21,22,23,24]
		d50 = [1,3,7,9,11,13,17,19,21,23,27,29,31,33,37,39,41,43,47,49]
		d100 = [1,3,7,9,11,13,17,19,21,23,27,29,31,33,37,39,41,43,47,49,51,53,57,59,61,63,67,69,71,73,77,79,81,83,87,89,91,93,97,99]
		d3 = [1,2]
		n4 = random.choice(d4)
		n5 = random.choice(d5)
		n10 = random.choice(d10)
		n20 = random.choice(d20)
		n25 = random.choice(d25)
		n50 = random.choice(d50)
		n100 = random.choice(d100)
		n3 = random.choice(d3)
		fractions = ["$\\dfrac{" + str(n4) + "}{4}$","$\\dfrac{" + str(n5) + "}{5}$","$\\dfrac{" + str(n10) + "}{10}$","$\\dfrac{" + str(n20) + "}{20}$","$\\dfrac{" + str(n25) + "}{25}$","$\\dfrac{" + str(n50) + "}{50}$","$\\dfrac{" + str(n100) + "}{100}$","$\\dfrac{" + str(n3) + "}{3}$"]
		if n3==1:
			dec3 = "0.\\.3"
			perc3 = "33.\\.3\\%"
		else:
			dec3 = "0.\\.6"
			perc3 = "66.\\.6\\%"
		decimals = [rounddp(n4/4,2),rounddp(n5/5,2),rounddp(n10/10,2),rounddp(n20/20,2),rounddp(n25/25,2),rounddp(n50/50,2),rounddp(n100/100,2),dec3]
		percentages = []
		for i in range(0,7):
			percentages.append(str(int(rounddp(decimals[i]*100,0))) + "\\%")
			decimals[i] = str(decimals[i])
		percentages.append(perc3)
		shuffler = [0,1,2,3,4,5,6,7]
		random.shuffle(shuffler)
		a = shuffler[0]
		b = shuffler[1]
		c = shuffler[2]
		d = shuffler[3]
		e = shuffler[4]
		f = shuffler[5]
		qtable = "\\newcolumntype{C}[1]{>{\\centering\\arraybackslash}p{#1}}\\renewcommand{\\arraystretch}{3}\\begin{tabular}{ | C{2cm} | C{1cm} | C{1cm} | C{1cm} | C{1cm} | C{1cm} | C{1cm} | } \\hline Fraction & " + fractions[a] + " & " + fractions[b] + " & " + fractions[c] + " & " + fractions[d] + " & " + fractions[e] + " & " + fractions[f] + "\\\\ \\hline Decimal &&&&&& \\\\ \\hline Percentage &&&&&& \\\\ \\hline \\end{tabular}"
		atable = "\\newcolumntype{C}[1]{>{\\centering\\arraybackslash}p{#1}}\\renewcommand{\\arraystretch}{3}\\begin{tabular}{ | C{2cm} | C{1cm} | C{1cm} | C{1cm} | C{1cm} | C{1cm} | C{1cm} | } \\hline Fraction & " + fractions[a] + " & " + fractions[b] + " & " + fractions[c] + " & " + fractions[d] + " & " + fractions[e] + " & " + fractions[f] + "\\\\ \\hline Decimal & " + decimals[a] + " & " + decimals[b] + " & " + decimals[c] + " & " + decimals[d] + " & " + decimals[e] + " & " + decimals[f] + "\\\\ \\hline Percentage & " + percentages[a] + " & " + percentages[b] + " & " + percentages[c] + " & " + percentages[d] + " & " + percentages[e] + " & " + percentages[f] + "\\\\ \\hline \\end{tabular}"
		nl = " \\\\[0.3cm] "
		question = "~" + nl + "\\begin{center}" + qtable + "\\end{center}~"
		answer = "\\begin{center}" + atable + "\\end{center}~"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def fdpwalldecimals(n,explanationn):
	import random
	from math import gcd
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question

		d10 = [1,2,3,4,5,6,7,8,9]
		d100 = [1,2,3,4,5,6,7,8,9]
		d20 = [1,3,7,9,11,13,17,19]
		d25 = [1,2,3,4,6,7,8,9,11,12,13,14,16,17,18,19,21,22,23,24]
		d1002 = [11,13,17,19,21,23,27,29,31,33,37,39,41,43,47,49,51,53,57,59,61,63,67,69,71,73,77,79,81,83,87,89,91,93,97,99,6,14,18,22,26,34,38,42,46,53,58,62,66,74,78,82,86,94,98]
		d3 = [1,2]

		n10 = random.choice(d10)
		d10 = 10
		n100 = random.choice(d100)
		d100 = 100
		n20 = random.choice(d20)
		n25 = random.choice(d25)
		n1002 = random.choice(d1002)
		d1002 = 100
		n3 = random.choice(d3)
		hcf = gcd(n10,d10)
		n10 = int(n10/hcf)
		d10 = int(d10/hcf)
		hcf = gcd(n100,d100)
		n100 = int(n100/hcf)
		d100 = int(d100/hcf)
		hcf = gcd(n1002,d1002)
		n1002 = int(n1002/hcf)
		d1002 = int(d1002/hcf)
		fractions = ["$\\dfrac{" + str(n10) + "}{" + str(d10) + "}$","$\\dfrac{" + str(n100) + "}{" + str(d100) + "}$","$\\dfrac{" + str(n20) + "}{20}$","$\\dfrac{" + str(n25) + "}{25}$","$\\dfrac{" + str(n1002) + "}{" + str(d1002) + "}$","$\\dfrac{" + str(n3) + "}{3}$"]
		if n3==1:
			dec3 = "0.\\.3"
			perc3 = "33.\\.3\\%"
		else:
			dec3 = "0.\\.6"
			perc3 = "66.\\.6\\%"
		decimals = [rounddp(n10/d10,2),rounddp(n100/d100,2),rounddp(n20/20,2),rounddp(n25/25,2),rounddp(n1002/d1002,2),dec3]
		percentages = []
		for i in range(0,5):
			percentages.append(str(int(rounddp(decimals[i]*100,0))) + "\\%")
			decimals[i] = str(decimals[i])
		percentages.append(perc3)
		shuffler = [0,1,2,3,4,5]
		random.shuffle(shuffler)
		a = shuffler[0]
		b = shuffler[1]
		c = shuffler[2]
		d = shuffler[3]
		e = shuffler[4]
		f = shuffler[5]
		qtable = "\\newcolumntype{C}[1]{>{\\centering\\arraybackslash}p{#1}}\\renewcommand{\\arraystretch}{3}\\begin{tabular}{ | C{2cm} | C{1cm} | C{1cm} | C{1cm} | C{1cm} | C{1cm} | C{1cm} | } \\hline Fraction &&&&&& \\\\ \\hline Decimal & " + decimals[a] + " & " + decimals[b] + " & " + decimals[c] + " & " + decimals[d] + " & " + decimals[e] + " & " + decimals[f] + "\\\\ \\hline Percentage &&&&&& \\\\ \\hline \\end{tabular}"
		atable = "\\newcolumntype{C}[1]{>{\\centering\\arraybackslash}p{#1}}\\renewcommand{\\arraystretch}{3}\\begin{tabular}{ | C{2cm} | C{1cm} | C{1cm} | C{1cm} | C{1cm} | C{1cm} | C{1cm} | } \\hline Fraction & " + fractions[a] + " & " + fractions[b] + " & " + fractions[c] + " & " + fractions[d] + " & " + fractions[e] + " & " + fractions[f] + "\\\\ \\hline Decimal & " + decimals[a] + " & " + decimals[b] + " & " + decimals[c] + " & " + decimals[d] + " & " + decimals[e] + " & " + decimals[f] + "\\\\ \\hline Percentage & " + percentages[a] + " & " + percentages[b] + " & " + percentages[c] + " & " + percentages[d] + " & " + percentages[e] + " & " + percentages[f] + "\\\\ \\hline \\end{tabular}"
		nl = " \\\\[0.3cm] "
		question = "~" + nl + "\\begin{center}" + qtable + "\\end{center}~"
		answer = "\\begin{center}" + atable + "\\end{center}~"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def fdpwallpercentages(n,explanationn):
	import random
	from math import gcd
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question

		d10 = [1,2,3,4,5,6,7,8,9]
		d100 = [1,2,3,4,5,6,7,8,9]
		d20 = [1,3,7,9,11,13,17,19]
		d25 = [1,2,3,4,6,7,8,9,11,12,13,14,16,17,18,19,21,22,23,24]
		d1002 = [11,13,17,19,21,23,27,29,31,33,37,39,41,43,47,49,51,53,57,59,61,63,67,69,71,73,77,79,81,83,87,89,91,93,97,99,6,14,18,22,26,34,38,42,46,53,58,62,66,74,78,82,86,94,98]
		d3 = [1,2]

		n10 = random.choice(d10)
		d10 = 10
		n100 = random.choice(d100)
		d100 = 100
		n20 = random.choice(d20)
		n25 = random.choice(d25)
		n1002 = random.choice(d1002)
		d1002 = 100
		n3 = random.choice(d3)
		hcf = gcd(n10,d10)
		n10 = int(n10/hcf)
		d10 = int(d10/hcf)
		hcf = gcd(n100,d100)
		n100 = int(n100/hcf)
		d100 = int(d100/hcf)
		hcf = gcd(n1002,d1002)
		n1002 = int(n1002/hcf)
		d1002 = int(d1002/hcf)
		fractions = ["$\\dfrac{" + str(n10) + "}{" + str(d10) + "}$","$\\dfrac{" + str(n100) + "}{" + str(d100) + "}$","$\\dfrac{" + str(n20) + "}{20}$","$\\dfrac{" + str(n25) + "}{25}$","$\\dfrac{" + str(n1002) + "}{" + str(d1002) + "}$","$\\dfrac{" + str(n3) + "}{3}$"]
		if n3==1:
			dec3 = "0.\\.3"
			perc3 = "33.\\.3\\%"
		else:
			dec3 = "0.\\.6"
			perc3 = "66.\\.6\\%"
		decimals = [rounddp(n10/d10,2),rounddp(n100/d100,2),rounddp(n20/20,2),rounddp(n25/25,2),rounddp(n1002/d1002,2),dec3]
		percentages = []
		for i in range(0,5):
			percentages.append(str(int(rounddp(decimals[i]*100,0))) + "\\%")
			decimals[i] = str(decimals[i])
		percentages.append(perc3)
		shuffler = [0,1,2,3,4,5]
		random.shuffle(shuffler)
		a = shuffler[0]
		b = shuffler[1]
		c = shuffler[2]
		d = shuffler[3]
		e = shuffler[4]
		f = shuffler[5]
		qtable = "\\renewcommand{\\arraystretch}{3}\\begin{tabular}{ | C{2cm} | C{1cm} | C{1cm} | C{1cm} | C{1cm} | C{1cm} | C{1cm} | } \\hline Fraction &&&&&& \\\\ \\hline Decimal &&&&&& \\\\ \\hline Percentage & " + percentages[a] + " & " + percentages[b] + " & " + percentages[c] + " & " + percentages[d] + " & " + percentages[e] + " & " + percentages[f] + "\\\\ \\hline \\end{tabular}"
		atable = "\\renewcommand{\\arraystretch}{3}\\begin{tabular}{ | C{2cm} | C{1cm} | C{1cm} | C{1cm} | C{1cm} | C{1cm} | C{1cm} | } \\hline Fraction & " + fractions[a] + " & " + fractions[b] + " & " + fractions[c] + " & " + fractions[d] + " & " + fractions[e] + " & " + fractions[f] + "\\\\ \\hline Decimal & " + decimals[a] + " & " + decimals[b] + " & " + decimals[c] + " & " + decimals[d] + " & " + decimals[e] + " & " + decimals[f] + "\\\\ \\hline Percentage & " + percentages[a] + " & " + percentages[b] + " & " + percentages[c] + " & " + percentages[d] + " & " + percentages[e] + " & " + percentages[f] + "\\\\ \\hline \\end{tabular}"
		atable = "hi"
		qtable = "hi"
		nl = " \\\\[0.3cm] "
		question = qtable
		answer = atable
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def fdpwall(n,explanationn):
	import random
	from math import gcd
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question

		d10 = [1,2,3,4,5,6,7,8,9]
		d100 = [1,2,3,4,5,6,7,8,9]
		d20 = [1,3,7,9,11,13,17,19]
		d25 = [1,2,3,4,6,7,8,9,11,12,13,14,16,17,18,19,21,22,23,24]
		d1002 = [11,13,17,19,21,23,27,29,31,33,37,39,41,43,47,49,51,53,57,59,61,63,67,69,71,73,77,79,81,83,87,89,91,93,97,99,6,14,18,22,26,34,38,42,46,53,58,62,66,74,78,82,86,94,98]
		d3 = [1,2]

		n10 = random.choice(d10)
		d10 = 10
		n100 = random.choice(d100)
		d100 = 100
		n20 = random.choice(d20)
		n25 = random.choice(d25)
		n1002 = random.choice(d1002)
		d1002 = 100
		n3 = random.choice(d3)
		hcf = gcd(n10,d10)
		n10 = int(n10/hcf)
		d10 = int(d10/hcf)
		hcf = gcd(n100,d100)
		n100 = int(n100/hcf)
		d100 = int(d100/hcf)
		hcf = gcd(n1002,d1002)
		n1002 = int(n1002/hcf)
		d1002 = int(d1002/hcf)
		fractions = ["$\\dfrac{" + str(n10) + "}{" + str(d10) + "}$","$\\dfrac{" + str(n100) + "}{" + str(d100) + "}$","$\\dfrac{" + str(n20) + "}{20}$","$\\dfrac{" + str(n25) + "}{25}$","$\\dfrac{" + str(n1002) + "}{" + str(d1002) + "}$","$\\dfrac{" + str(n3) + "}{3}$"]
		if n3==1:
			dec3 = "0.\\.3"
			perc3 = "33.\\.3\\%"
		else:
			dec3 = "0.\\.6"
			perc3 = "66.\\.6\\%"
		decimals = [rounddp(n10/d10,2),rounddp(n100/d100,2),rounddp(n20/20,2),rounddp(n25/25,2),rounddp(n1002/d1002,2),dec3]
		percentages = []
		for i in range(0,5):
			percentages.append(str(int(rounddp(decimals[i]*100,0))) + "\\%")
			decimals[i] = str(decimals[i])
		percentages.append(perc3)
		shuffler = [0,1,2,3,4,5]
		random.shuffle(shuffler)
		a = shuffler[0]
		b = shuffler[1]
		c = shuffler[2]
		d = shuffler[3]
		e = shuffler[4]
		f = shuffler[5]
		qtable = "\\newcolumntype{C}[1]{>{\\centering\\arraybackslash}p{#1}}\\renewcommand{\\arraystretch}{3}\\begin{tabular}{ | C{2cm} | C{1cm} | C{1cm} | C{1cm} | C{1cm} | C{1cm} | C{1cm} | } \\hline Fraction & " + fractions[a] + " &&& " + fractions[d] + " && \\\\ \\hline Decimal && " + decimals[b] + " &&& " + decimals[e] + " & \\\\ \\hline Percentage &&& " + percentages[c] + " &&& " + percentages[f] + "\\\\ \\hline \\end{tabular}"
		atable = "\\newcolumntype{C}[1]{>{\\centering\\arraybackslash}p{#1}}\\renewcommand{\\arraystretch}{3}\\begin{tabular}{ | C{2cm} | C{1cm} | C{1cm} | C{1cm} | C{1cm} | C{1cm} | C{1cm} | } \\hline Fraction & " + fractions[a] + " & " + fractions[b] + " & " + fractions[c] + " & " + fractions[d] + " & " + fractions[e] + " & " + fractions[f] + "\\\\ \\hline Decimal & " + decimals[a] + " & " + decimals[b] + " & " + decimals[c] + " & " + decimals[d] + " & " + decimals[e] + " & " + decimals[f] + "\\\\ \\hline Percentage & " + percentages[a] + " & " + percentages[b] + " & " + percentages[c] + " & " + percentages[d] + " & " + percentages[e] + " & " + percentages[f] + "\\\\ \\hline \\end{tabular}"
		nl = " \\\\[0.3cm] "
		question = "~" + nl + "\\begin{center}" + qtable + "\\end{center}~"
		answer = "\\begin{center}" + atable + "\\end{center}~"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)





def fdpwallstarter(n,explanationn):
	import random
	from math import gcd
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question

		d10 = [1,2,3,4,5,6,7,8,9]
		d100 = [1,2,3,4,5,6,7,8,9]
		d20 = [1,3,7,9,11,13,17,19]
		d25 = [1,2,3,4,6,7,8,9,11,12,13,14,16,17,18,19,21,22,23,24]
		d1002 = [11,13,17,19,21,23,27,29,31,33,37,39,41,43,47,49,51,53,57,59,61,63,67,69,71,73,77,79,81,83,87,89,91,93,97,99,6,14,18,22,26,34,38,42,46,53,58,62,66,74,78,82,86,94,98]
		d3 = [1,2]

		n10 = random.choice(d10)
		d10 = 10
		n100 = random.choice(d100)
		d100 = 100
		n20 = random.choice(d20)
		n25 = random.choice(d25)
		n1002 = random.choice(d1002)
		d1002 = 100
		n3 = random.choice(d3)
		hcf = gcd(n10,d10)
		n10 = int(n10/hcf)
		d10 = int(d10/hcf)
		hcf = gcd(n100,d100)
		n100 = int(n100/hcf)
		d100 = int(d100/hcf)
		hcf = gcd(n1002,d1002)
		n1002 = int(n1002/hcf)
		d1002 = int(d1002/hcf)
		fractions = ["$\\dfrac{" + str(n10) + "}{" + str(d10) + "}$","$\\dfrac{" + str(n100) + "}{" + str(d100) + "}$","$\\dfrac{" + str(n20) + "}{20}$","$\\dfrac{" + str(n25) + "}{25}$","$\\dfrac{" + str(n1002) + "}{" + str(d1002) + "}$","$\\dfrac{" + str(n3) + "}{3}$"]
		if n3==1:
			dec3 = "0.\\.3"
			perc3 = "33.\\.3\\%"
		else:
			dec3 = "0.\\.6"
			perc3 = "66.\\.6\\%"
		decimals = [rounddp(n10/d10,2),rounddp(n100/d100,2),rounddp(n20/20,2),rounddp(n25/25,2),rounddp(n1002/d1002,2),dec3]
		percentages = []
		for i in range(0,5):
			percentages.append(str(int(rounddp(decimals[i]*100,0))) + "\\%")
			decimals[i] = str(decimals[i])
		percentages.append(perc3)
		shuffler = [0,1,2,3,4,5]
		random.shuffle(shuffler)
		a = shuffler[0]
		b = shuffler[1]
		c = shuffler[2]
		d = shuffler[3]
		e = shuffler[4]
		f = shuffler[5]



		qtable = "\\renewcommand{\\arraystretch}{2}\\begin{tabular}{| M{1.3cm} M{1.3cm} M{1.6cm} |} \\hline Fraction & Decimal & Percentage \\\\ \\hline " + fractions[a] + " && \\\\ \\hline & " + decimals[b] + " & \\\\ \\hline && " + percentages[c] + "\\\\ \\hline \\end{tabular}"

		atable = "\\renewcommand{\\arraystretch}{2}\\begin{tabular}{| M{1.3cm} M{1.3cm} M{1.6cm} |} \\hline Fraction & Decimal & Percentage \\\\ \\hline " + fractions[a] + " & " + decimals[a] + " & " + percentages[a] + " \\\\ \\hline " + fractions[b] + " & " + decimals[b] + " & " + percentages[b] + "\\\\ \\hline " + fractions[c] + " & " + decimals[c] + " & " + percentages[c] + "\\\\ \\hline \\end{tabular}"




		nl = " \\\\[0.3cm] "
		question = "\\begin{center}" + qtable + "\\end{center}"
		answer = "\\begin{center}" + atable + "\\end{center}"

#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def fractoperc(n,explanationn):
	import random
	from math import gcd
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Convert "
			explanation2 = " to a percentage"
		else:
			explanation1 = ""
			explanation2 = ""

		d10 = [1,2,3,4,5,6,7,8,9]
		d100 = [1,2,3,4,5,6,7,8,9]
		d20 = [1,3,7,9,11,13,17,19]
		d25 = [1,2,3,4,6,7,8,9,11,12,13,14,16,17,18,19,21,22,23,24]
		d1002 = [11,13,17,19,21,23,27,29,31,33,37,39,41,43,47,49,51,53,57,59,61,63,67,69,71,73,77,79,81,83,87,89,91,93,97,99,6,14,18,22,26,34,38,42,46,53,58,62,66,74,78,82,86,94,98]
		d3 = [1,2]

		n10 = random.choice(d10)
		d10 = 10
		n100 = random.choice(d100)
		d100 = 100
		n20 = random.choice(d20)
		n25 = random.choice(d25)
		n1002 = random.choice(d1002)
		d1002 = 100
		n3 = random.choice(d3)
		hcf = gcd(n10,d10)
		n10 = int(n10/hcf)
		d10 = int(d10/hcf)
		hcf = gcd(n100,d100)
		n100 = int(n100/hcf)
		d100 = int(d100/hcf)
		hcf = gcd(n1002,d1002)
		n1002 = int(n1002/hcf)
		d1002 = int(d1002/hcf)
		fractions = ["$\\dfrac{" + str(n10) + "}{" + str(d10) + "}$","$\\dfrac{" + str(n100) + "}{" + str(d100) + "}$","$\\dfrac{" + str(n20) + "}{20}$","$\\dfrac{" + str(n25) + "}{25}$","$\\dfrac{" + str(n1002) + "}{" + str(d1002) + "}$","$\\dfrac{" + str(n3) + "}{3}$"]
		if n3==1:
			dec3 = "0.\\.3"
			perc3 = "33.\\.3\\%"
		else:
			dec3 = "0.\\.6"
			perc3 = "66.\\.6\\%"
		decimals = [rounddp(n10/d10,2),rounddp(n100/d100,2),rounddp(n20/20,2),rounddp(n25/25,2),rounddp(n1002/d1002,2),dec3]
		percentages = []
		for i in range(0,5):
			percentages.append(str(int(rounddp(decimals[i]*100,0))) + "\\%")
			decimals[i] = str(decimals[i])
		percentages.append(perc3)
		dec = random.randrange(0,6)
		perc = percentages[dec]
		frac = fractions[dec]
		dec = decimals[dec]
		question = frac
		answer = perc
#write question
		tempquestions.write(explanation1 + question + explanation2)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def fractodec(n,explanationn):
	import random
	from math import gcd
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Convert "
			explanation2 = " to a decimal"
		else:
			explanation1 = ""
			explanation2 = ""

		d10 = [1,2,3,4,5,6,7,8,9]
		d100 = [1,2,3,4,5,6,7,8,9]
		d20 = [1,3,7,9,11,13,17,19]
		d25 = [1,2,3,4,6,7,8,9,11,12,13,14,16,17,18,19,21,22,23,24]
		d1002 = [11,13,17,19,21,23,27,29,31,33,37,39,41,43,47,49,51,53,57,59,61,63,67,69,71,73,77,79,81,83,87,89,91,93,97,99,6,14,18,22,26,34,38,42,46,53,58,62,66,74,78,82,86,94,98]
		d3 = [1,2]

		n10 = random.choice(d10)
		d10 = 10
		n100 = random.choice(d100)
		d100 = 100
		n20 = random.choice(d20)
		n25 = random.choice(d25)
		n1002 = random.choice(d1002)
		d1002 = 100
		n3 = random.choice(d3)
		hcf = gcd(n10,d10)
		n10 = int(n10/hcf)
		d10 = int(d10/hcf)
		hcf = gcd(n100,d100)
		n100 = int(n100/hcf)
		d100 = int(d100/hcf)
		hcf = gcd(n1002,d1002)
		n1002 = int(n1002/hcf)
		d1002 = int(d1002/hcf)
		fractions = ["$\\dfrac{" + str(n10) + "}{" + str(d10) + "}$","$\\dfrac{" + str(n100) + "}{" + str(d100) + "}$","$\\dfrac{" + str(n20) + "}{20}$","$\\dfrac{" + str(n25) + "}{25}$","$\\dfrac{" + str(n1002) + "}{" + str(d1002) + "}$","$\\dfrac{" + str(n3) + "}{3}$"]
		if n3==1:
			dec3 = "0.\\.3"
			perc3 = "33.\\.3\\%"
		else:
			dec3 = "0.\\.6"
			perc3 = "66.\\.6\\%"
		decimals = [rounddp(n10/d10,2),rounddp(n100/d100,2),rounddp(n20/20,2),rounddp(n25/25,2),rounddp(n1002/d1002,2),dec3]
		percentages = []
		for i in range(0,5):
			percentages.append(str(int(rounddp(decimals[i]*100,0))) + "\\%")
			decimals[i] = str(decimals[i])
		percentages.append(perc3)
		dec = random.randrange(0,6)
		perc = percentages[dec]
		frac = fractions[dec]
		dec = decimals[dec]
		question = frac
		answer = dec
#write question
		tempquestions.write(explanation1 + question + explanation2)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def perctodec(n,explanationn):
	import random
	from math import gcd
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Convert "
			explanation2 = " to a decimal"
		else:
			explanation1 = ""
			explanation2 = ""

		d10 = [1,2,3,4,5,6,7,8,9]
		d100 = [1,2,3,4,5,6,7,8,9]
		d20 = [1,3,7,9,11,13,17,19]
		d25 = [1,2,3,4,6,7,8,9,11,12,13,14,16,17,18,19,21,22,23,24]
		d1002 = [11,13,17,19,21,23,27,29,31,33,37,39,41,43,47,49,51,53,57,59,61,63,67,69,71,73,77,79,81,83,87,89,91,93,97,99,6,14,18,22,26,34,38,42,46,53,58,62,66,74,78,82,86,94,98]
		d3 = [1,2]

		n10 = random.choice(d10)
		d10 = 10
		n100 = random.choice(d100)
		d100 = 100
		n20 = random.choice(d20)
		n25 = random.choice(d25)
		n1002 = random.choice(d1002)
		d1002 = 100
		n3 = random.choice(d3)
		hcf = gcd(n10,d10)
		n10 = int(n10/hcf)
		d10 = int(d10/hcf)
		hcf = gcd(n100,d100)
		n100 = int(n100/hcf)
		d100 = int(d100/hcf)
		hcf = gcd(n1002,d1002)
		n1002 = int(n1002/hcf)
		d1002 = int(d1002/hcf)
		fractions = ["$\\dfrac{" + str(n10) + "}{" + str(d10) + "}$","$\\dfrac{" + str(n100) + "}{" + str(d100) + "}$","$\\dfrac{" + str(n20) + "}{20}$","$\\dfrac{" + str(n25) + "}{25}$","$\\dfrac{" + str(n1002) + "}{" + str(d1002) + "}$","$\\dfrac{" + str(n3) + "}{3}$"]
		if n3==1:
			dec3 = "0.\\.3"
			perc3 = "33.\\.3\\%"
		else:
			dec3 = "0.\\.6"
			perc3 = "66.\\.6\\%"
		decimals = [rounddp(n10/d10,2),rounddp(n100/d100,2),rounddp(n20/20,2),rounddp(n25/25,2),rounddp(n1002/d1002,2),dec3]
		percentages = []
		for i in range(0,5):
			percentages.append(str(int(rounddp(decimals[i]*100,0))) + "\\%")
			decimals[i] = str(decimals[i])
		percentages.append(perc3)
		dec = random.randrange(0,6)
		perc = percentages[dec]
		frac = fractions[dec]
		dec = decimals[dec]
		question = perc
		answer = dec
#write question
		tempquestions.write(explanation1 + question + explanation2)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def perctofrac(n,explanationn):
	import random
	from math import gcd
	from utilities.rounding import rounddp
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

		d10 = [1,2,3,4,5,6,7,8,9]
		d100 = [1,2,3,4,5,6,7,8,9]
		d20 = [1,3,7,9,11,13,17,19]
		d25 = [1,2,3,4,6,7,8,9,11,12,13,14,16,17,18,19,21,22,23,24]
		d1002 = [11,13,17,19,21,23,27,29,31,33,37,39,41,43,47,49,51,53,57,59,61,63,67,69,71,73,77,79,81,83,87,89,91,93,97,99,6,14,18,22,26,34,38,42,46,53,58,62,66,74,78,82,86,94,98]
		d3 = [1,2]

		n10 = random.choice(d10)
		d10 = 10
		n100 = random.choice(d100)
		d100 = 100
		n20 = random.choice(d20)
		n25 = random.choice(d25)
		n1002 = random.choice(d1002)
		d1002 = 100
		n3 = random.choice(d3)
		hcf = gcd(n10,d10)
		n10 = int(n10/hcf)
		d10 = int(d10/hcf)
		hcf = gcd(n100,d100)
		n100 = int(n100/hcf)
		d100 = int(d100/hcf)
		hcf = gcd(n1002,d1002)
		n1002 = int(n1002/hcf)
		d1002 = int(d1002/hcf)
		fractions = ["$\\dfrac{" + str(n10) + "}{" + str(d10) + "}$","$\\dfrac{" + str(n100) + "}{" + str(d100) + "}$","$\\dfrac{" + str(n20) + "}{20}$","$\\dfrac{" + str(n25) + "}{25}$","$\\dfrac{" + str(n1002) + "}{" + str(d1002) + "}$","$\\dfrac{" + str(n3) + "}{3}$"]
		if n3==1:
			dec3 = "0.\\.3"
			perc3 = "33.\\.3\\%"
		else:
			dec3 = "0.\\.6"
			perc3 = "66.\\.6\\%"
		decimals = [rounddp(n10/d10,2),rounddp(n100/d100,2),rounddp(n20/20,2),rounddp(n25/25,2),rounddp(n1002/d1002,2),dec3]
		percentages = []
		for i in range(0,5):
			percentages.append(str(int(rounddp(decimals[i]*100,0))) + "\\%")
			decimals[i] = str(decimals[i])
		percentages.append(perc3)
		dec = random.randrange(0,6)
		perc = percentages[dec]
		frac = fractions[dec]
		dec = decimals[dec]
		question = perc
		answer = frac
#write question
		tempquestions.write(explanation1 + question + explanation2)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def dectofrac(n,explanationn):
	import random
	from math import gcd
	from utilities.rounding import rounddp
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

		d10 = [1,2,3,4,5,6,7,8,9]
		d100 = [1,2,3,4,5,6,7,8,9]
		d20 = [1,3,7,9,11,13,17,19]
		d25 = [1,2,3,4,6,7,8,9,11,12,13,14,16,17,18,19,21,22,23,24]
		d1002 = [11,13,17,19,21,23,27,29,31,33,37,39,41,43,47,49,51,53,57,59,61,63,67,69,71,73,77,79,81,83,87,89,91,93,97,99,6,14,18,22,26,34,38,42,46,53,58,62,66,74,78,82,86,94,98]
		d3 = [1,2]

		n10 = random.choice(d10)
		d10 = 10
		n100 = random.choice(d100)
		d100 = 100
		n20 = random.choice(d20)
		n25 = random.choice(d25)
		n1002 = random.choice(d1002)
		d1002 = 100
		n3 = random.choice(d3)
		hcf = gcd(n10,d10)
		n10 = int(n10/hcf)
		d10 = int(d10/hcf)
		hcf = gcd(n100,d100)
		n100 = int(n100/hcf)
		d100 = int(d100/hcf)
		hcf = gcd(n1002,d1002)
		n1002 = int(n1002/hcf)
		d1002 = int(d1002/hcf)
		fractions = ["$\\dfrac{" + str(n10) + "}{" + str(d10) + "}$","$\\dfrac{" + str(n100) + "}{" + str(d100) + "}$","$\\dfrac{" + str(n20) + "}{20}$","$\\dfrac{" + str(n25) + "}{25}$","$\\dfrac{" + str(n1002) + "}{" + str(d1002) + "}$","$\\dfrac{" + str(n3) + "}{3}$"]
		if n3==1:
			dec3 = "0.\\.3"
			perc3 = "33.\\.3\\%"
		else:
			dec3 = "0.\\.6"
			perc3 = "66.\\.6\\%"
		decimals = [rounddp(n10/d10,2),rounddp(n100/d100,2),rounddp(n20/20,2),rounddp(n25/25,2),rounddp(n1002/d1002,2),dec3]
		percentages = []
		for i in range(0,5):
			percentages.append(str(int(rounddp(decimals[i]*100,0))) + "\\%")
			decimals[i] = str(decimals[i])
		percentages.append(perc3)
		dec = random.randrange(0,6)
		perc = percentages[dec]
		frac = fractions[dec]
		dec = decimals[dec]
		question = dec
		answer = frac
#write question
		tempquestions.write(explanation1 + question + explanation2)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def dectoperc(n,explanationn):
	import random
	from math import gcd
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Convert "
			explanation2 = " to a percentage"
		else:
			explanation1 = ""
			explanation2 = ""

		d10 = [1,2,3,4,5,6,7,8,9]
		d100 = [1,2,3,4,5,6,7,8,9]
		d20 = [1,3,7,9,11,13,17,19]
		d25 = [1,2,3,4,6,7,8,9,11,12,13,14,16,17,18,19,21,22,23,24]
		d1002 = [11,13,17,19,21,23,27,29,31,33,37,39,41,43,47,49,51,53,57,59,61,63,67,69,71,73,77,79,81,83,87,89,91,93,97,99,6,14,18,22,26,34,38,42,46,53,58,62,66,74,78,82,86,94,98]
		d3 = [1,2]

		n10 = random.choice(d10)
		d10 = 10
		n100 = random.choice(d100)
		d100 = 100
		n20 = random.choice(d20)
		n25 = random.choice(d25)
		n1002 = random.choice(d1002)
		d1002 = 100
		n3 = random.choice(d3)
		hcf = gcd(n10,d10)
		n10 = int(n10/hcf)
		d10 = int(d10/hcf)
		hcf = gcd(n100,d100)
		n100 = int(n100/hcf)
		d100 = int(d100/hcf)
		hcf = gcd(n1002,d1002)
		n1002 = int(n1002/hcf)
		d1002 = int(d1002/hcf)
		fractions = ["$\\dfrac{" + str(n10) + "}{" + str(d10) + "}$","$\\dfrac{" + str(n100) + "}{" + str(d100) + "}$","$\\dfrac{" + str(n20) + "}{20}$","$\\dfrac{" + str(n25) + "}{25}$","$\\dfrac{" + str(n1002) + "}{" + str(d1002) + "}$","$\\dfrac{" + str(n3) + "}{3}$"]
		if n3==1:
			dec3 = "0.\\.3"
			perc3 = "33.\\.3\\%"
		else:
			dec3 = "0.\\.6"
			perc3 = "66.\\.6\\%"
		decimals = [rounddp(n10/d10,2),rounddp(n100/d100,2),rounddp(n20/20,2),rounddp(n25/25,2),rounddp(n1002/d1002,2),dec3]
		percentages = []
		for i in range(0,5):
			percentages.append(str(int(rounddp(decimals[i]*100,0))) + "\\%")
			decimals[i] = str(decimals[i])
		percentages.append(perc3)
		dec = random.randrange(0,6)
		perc = percentages[dec]
		frac = fractions[dec]
		dec = decimals[dec]
		question = dec
		answer = perc
#write question
		tempquestions.write(explanation1 + question + explanation2)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
