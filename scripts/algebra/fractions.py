#fractions.py

def quaddots(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		mylist=list(range(-12,13))
		mylist.remove(0)
		d = 1
		e = random.choice(mylist)
		mylist.remove(e*-1)
		f = 1
		g = random.choice(mylist)
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if g<0:
			sign2 = " - "
		else:
			sign2 = " + "
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""
		if b==0:
			qtop = "x^2" + sign4 + str(c)
		else:
			qtop = "x^2" + sign3 + str(b) + "x" + sign4 + str(c)
		qbot = "x^2 - " + str(e**2)
		atop = "x" + sign2 + str(g)
		if sign1==" - ":
			sign5 = " + "
		else:
			sign5 = " - "
		abot = "x" + sign5 + str(e)
		if random.randrange(0,2)==1:
			temp = qtop
			qtop = qbot
			qbot = temp
			temp = atop
			atop = abot
			abot = temp
#write question
		tempquestions.write(explanation + "$\\dfrac{" + qtop + "}{" + qbot + "}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$\\dfrac{" + atop + "}{" + abot + "}$")



def quaddots2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		tailoring1 = list(range(-5,6))
		tailoring1.remove(0)
		tailoring2 = list(range(-5,6))
		tailoring2.remove(0)
		d = random.randrange(1,4)
		if d==1:
			f = random.randrange(2,7)
		else:
			f = random.randrange(1,4)
		if d>1:
			tailoring1.remove(d)
			tailoring1.remove(d*-1)
		if 1<f<6:
			tailoring2.remove(f)
			tailoring2.remove(f*-1)
		if d==2:
			tailoring1.remove(4)
			tailoring1.remove(-4)
		if d==4:
			tailoring1.remove(2)
			tailoring1.remove(-2)
		if f==2:
			tailoring2.remove(4)
			tailoring2.remove(-4)
		if f==4:
			tailoring2.remove(2)
			tailoring2.remove(-2)
		e = random.choice(tailoring1)
		if (0-e) in tailoring2:
			tailoring2.remove(0-e)
		g = random.choice(tailoring2)
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if g<0:
			sign2 = " - "
		else:
			sign2 = " + "
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		temp = d
		if b==1:
			b = ""
		if d==1:
			d = ""
		if f==1:
			f = ""

		if b==0:
			qtop = str(a) + "x^2" + sign4 + str(c)
		else:
			qtop = str(a) + "x^2" + sign3 + str(b) + "x" + sign4 + str(c)
		if temp>1:
			h = d
			i = e
			sign5 = sign1
			atop = str(f) + "x" + sign2 + str(g)
		else:
			h = f
			i = g
			sign5 = sign2
			atop = str(d) + "x" + sign1 + str(e)
		qbot = str(h**2) + "x^{2} - " + str(i**2)
		if sign5== " + ":
			sign6 = " - "
		else:
			sign6 = " + "
		abot = str(h) + "x" + sign6 + str(i)
		if random.randrange(0,2)==1:
			temp = qtop
			qtop = qbot
			qbot = temp
			temp = atop
			atop = abot
			abot = temp
#write question
		tempquestions.write(explanation + "$\\dfrac{" + qtop + "}{" + qbot + "}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$\\dfrac{" + atop + "}{" + abot + "}$")


def fracadd1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Express "
			explanation2 = " as a fraction in its simplest form."
		else:
			explanation1 = ""
			explanation2 = ""
		n1 = random.randrange(1,10)
		n2 = random.randrange(1,10)
		d1 = random.randrange(1,10) * (-1)**random.randrange(1,3)
		d2 = random.randrange(1,10) * (-1)**random.randrange(1,3)
		if d1<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if d2<0:
			sign2 = " - "
		else:
			sign2 = " + "
		question = "$\\dfrac{" + str(n1) + "}{x" + sign1 + str(abs(d1)) + "} + \\dfrac{" + str(n2) + "}{x" + sign2 + str(abs(d2)) + "}$"
		if n1*d2+n2*d1<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if d1 + d2 < 0:
			sign4 = " - "
		else:
			sign4 = " + "
		if d1*d2<0:
			sign5 = " - "
		else:
			sign5 = " + "
		b = abs(d1 + d2)
		if b==1:
			b = ""
		if b==0:
			answer = "$\\dfrac{" +  str(n1 + n2) + "x" + sign3 + str(abs(n1*d2 + n2*d1)) + "}{x^{2}" + sign5 + str(abs(d1*d2)) + "}$"
		else:
			answer = "$\\dfrac{" +  str(n1 + n2) + "x" + sign3 + str(abs(n1*d2 + n2*d1)) + "}{x^{2}" + sign4 + str(b) + "x" + sign5 + str(abs(d1*d2)) + "}$"
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def fracsubtract1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Express "
			explanation2 = " as a fraction in its simplest form."
		else:
			explanation1 = ""
			explanation2 = ""
		n1 = random.randrange(1,10)
		n2 = random.randrange(1,10)
		d1 = random.randrange(1,10) * (-1)**random.randrange(1,3)
		d2 = random.randrange(1,10) * (-1)**random.randrange(1,3)
		if d1<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if d2<0:
			sign2 = " - "
		else:
			sign2 = " + "
		question = "$\\dfrac{" + str(n1) + "}{x" + sign1 + str(abs(d1)) + "} - \\dfrac{" + str(n2) + "}{x" + sign2 + str(abs(d2)) + "}$"
		if n1*d2-n2*d1<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if d1 + d2 < 0:
			sign4 = " - "
		else:
			sign4 = " + "
		if d1*d2<0:
			sign5 = " - "
		else:
			sign5 = " + "
		a = n1 - n2
		if a==1:
			a = "x" + sign3
		elif a==-1:
			a = "-x" + sign3
		elif a==0:
			if sign3==" + ":
				a = ""
			else:
				a = "-"
		else:
			a = str(a) + "x" + sign3
		b = abs(d1 + d2)
		if b==1:
			b = ""
		if b==0:
			answer = "$\\dfrac{" +  str(a) + str(abs(n1*d2 - n2*d1)) + "}{x^{2}" + sign5 + str(abs(d1*d2)) + "}$"
		else:
			answer = "$\\dfrac{" +  str(a) + str(abs(n1*d2 - n2*d1)) + "}{x^{2}" + sign4 + str(b) + "x" + sign5 + str(abs(d1*d2)) + "}$"
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def fracadd2(n,explanationn):
	import random
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Express "
			explanation2 = " as a single fraction"
		else:
			explanation1 = ""
			explanation2 = ""
		nums = (2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,5,5,5,5,5,5,6,6,7,7,7,7,7,8,8,9,9,10,11)
		dens = (3,5,7,9,11,4,5,7,8,10,11,5,7,9,11,6,7,8,9,11,12,7,11,8,9,10,11,12,9,11,10,11,11,12)
		dec1 = random.randrange(0,len(nums))
		dec2 = dec1
		while dec2==dec1:
			dec2 = random.randrange(0,len(nums))
		num1 = nums[dec1]
		num2 = nums[dec2]
		den1 = dens[dec1]
		den2 = dens[dec2]
		letters = ["a","b","c","d","e","f","g","h","j","k","m","n","p","q","r","t","y"]
		letter = random.choice(letters)

		anum = num1*den2 + num2*den1
		aden = den1*den2
		hcf = gcd(anum,aden)
		anum = int(anum/hcf)
		aden = int(aden/hcf)
		question = "$\\dfrac{" + str(num1) + "}{" + str(den1) + letter + "} + \\dfrac{" + str(num2) + "}{" + str(den2) + letter + "}$"
		answer = "$\\dfrac{" + str(anum) + "}{" + str(aden) + letter + "}$"
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def fracsubtract2(n,explanationn):
	import random
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Express "
			explanation2 = " as a single fraction"
		else:
			explanation1 = ""
			explanation2 = ""
		nums = (2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,5,5,5,5,5,5,6,6,7,7,7,7,7,8,8,9,9,10,11)
		dens = (3,5,7,9,11,4,5,7,8,10,11,5,7,9,11,6,7,8,9,11,12,7,11,8,9,10,11,12,9,11,10,11,11,12)
		dec1 = random.randrange(0,len(nums))
		dec2 = dec1
		while dec2==dec1:
			dec2 = random.randrange(0,len(nums))
		num1 = nums[dec1]
		num2 = nums[dec2]
		den1 = dens[dec1]
		den2 = dens[dec2]
		letters = ["a","b","c","d","e","f","g","h","j","k","m","n","p","q","r","t","y"]
		letter = random.choice(letters)
		if num1*den2 - num2*den1<0:
			temp = num1
			num1 = num2
			num2 = temp
			temp = den1
			den1 = den2
			den2 = temp
		anum = num1*den2 - num2*den1
		aden = den1*den2
		hcf = gcd(anum,aden)
		anum = int(anum/hcf)
		aden = int(aden/hcf)
		question = "$\\dfrac{" + str(num1) + "}{" + str(den1) + letter + "} - \\dfrac{" + str(num2) + "}{" + str(den2) + letter + "}$"
		answer = "$\\dfrac{" + str(anum) + "}{" + str(aden) + letter + "}$"
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
