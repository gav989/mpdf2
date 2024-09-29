#!/usr/bin/env python3
#questiontemplate.py

def percofamount5(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		p = random.randrange(1,20)*5
		if p%10==0:
			a = random.randrange(10,201)
		else:
			a = random.randrange(1,13)*10
#write question
		tempquestions.write(explanation + str(p) + "\% of " + str(a))
		tempquestions.write("\n")
#write answer
		tempquestions.write("{0:g}".format(float(a*p/100)))

def percofamount5gym(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		ps = [15,20,30,35,40,45,55,60,65,70,75,80,85,90,95]
		p = random.choice(ps)
		if p%10==0:
			a = random.randrange(10,201)
		else:
			a = random.randrange(1,13)*10
#write question
		tempquestions.write(explanation + str(p) + "\% of " + str(a))
		tempquestions.write("\n")
#write answer
		tempquestions.write("{0:g}".format(float(a*p/100)))

def percofamount(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		p = random.randrange(1,6)*random.randrange(1,20)
		a = random.randrange(1,6)*random.randrange(1,51)
#write question
		tempquestions.write(explanation + str(p) + "\% of " + str(a))
		tempquestions.write("\n")
#write answer
		tempquestions.write("{0:g}".format(float(a*p/100)))

def percincdec5(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		d = random.randrange(0,2)
		p = random.randrange(1,20)*5
		if p%10==0:
			a = random.randrange(10,201)
		else:
			a = random.randrange(1,13)*10
#write question
		if d==0:
			tempquestions.write("Decrease " + str(a) + " by " + str(p) + "\%")
		else:
			tempquestions.write("Increase " + str(a) + " by " + str(p) + "\%")
		tempquestions.write("\n")
#write answer
		if d==0:
			tempquestions.write("{0:g}".format(float(a*(1-p/100))))
		else:
			tempquestions.write("{0:g}".format(float(a*(1+p/100))))


def percinc5(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		p = random.randrange(1,20)*5
		if p%10==0:
			a = random.randrange(10,201)
		else:
			a = random.randrange(1,13)*10
#write question
		tempquestions.write("Increase " + str(a) + " by " + str(p) + "\%")
		tempquestions.write("\n")
#write answer
		tempquestions.write("{0:g}".format(float(a*(1+p/100))))

def percinc5easy(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		d = 1
		ps = (5,10,25,50)
		p = random.randrange(1,20)*5
		a = random.randrange(2,9)*10
#write question
		if d==0:
			tempquestions.write("Decrease " + str(a) + " by " + str(p) + "\%")
		else:
			tempquestions.write("Increase " + str(a) + " by " + str(p) + "\%")
		tempquestions.write("\n")
#write answer
		if d==0:
			tempquestions.write("{0:g}".format(float(a*(1-p/100))))
		else:
			tempquestions.write("{0:g}".format(float(a*(1+p/100))))


def percincdec(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		d = random.randrange(0,2)
		p = random.randrange(1,6)*random.randrange(1,20)
		a = random.randrange(1,6)*random.randrange(1,51)
#write question
		if d==0:
			tempquestions.write("Decrease " + str(a) + " by " + str(p) + "\%")
		else:
			tempquestions.write("Increase " + str(a) + " by " + str(p) + "\%")
		tempquestions.write("\n")
#write answer
		if d==0:
			tempquestions.write("{0:g}".format(float(a*(1-p/100))))
		else:
			tempquestions.write("{0:g}".format(float(a*(1+p/100))))

def percdec(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		d = 0
		p = random.randrange(1,6)*random.randrange(1,20)
		a = random.randrange(1,6)*random.randrange(1,51)
#write question
		tempquestions.write("Decrease " + str(a) + " by " + str(p) + "\%")
		tempquestions.write("\n")
#write answer
		tempquestions.write("{0:g}".format(float(a*(1-p/100))))


def percreverse5(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		d = random.randrange(0,2)
		p = random.randrange(1,20)*5
		if p%10==0:
			a = random.randrange(10,201)
		else:
			a = random.randrange(1,13)*10
#write question
		if d==0:
			n = rounddp(a*(1-p/100),2)
			if n%1!=0:
				n = "{0:.2f}".format(n)
			else:
				n = str(int(n))
			tempquestions.write("The price of an item has decreased by "  + str(p) + "\%. It now costs \pounds" + n + ", find its original price.")
		else:
			n = rounddp(a*(1+p/100),2)
			if n%1!=0:
				n = "{0:.2f}".format(n)
			else:
				n = str(int(n))
			tempquestions.write("The price of an item has increased by "  + str(p) + "\%. It now costs \pounds" + n + ", find its original price.")
		tempquestions.write("\n")
#write answer
		tempquestions.write("\pounds" + str(a))

def percreverse52(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		answer = random.randrange(3,31) * 100
		perc = random.randrange(1,13)*5
		question = int(answer * (perc/100))
		question = str(perc) + "\\% = " + str(question) + ", find 100\\%"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))

def percreverse53(n,explanationn):
	import random
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		perc = random.randrange(1,13)*5
		hcf = gcd(perc,100)
		base = int(perc/hcf)
		multiplier = random.randrange(4,13)
		number = base * multiplier
		answer = multiplier * int(100/hcf)
		question = str(perc) + "\\% = " + str(number) + ", find 100\\%"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def percreverse54(n,explanationn):
	import random
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		percs = [105,110,120,125,135,140,150,160,165,175,180]
		divisors = [21,[11,22],[12,6],[5,25],27,[14,7],[15,3],[16,8],33,[7,35],[18,9]]
		choice = random.randrange(0,len(percs))
		divisor = divisors[choice]
		try:
			divisor = random.choice(divisor)
		except:
			divisor = divisor
		perc = percs[choice]
		number = random.randrange(3,12)
		number = number * divisor
		answer = int(100*(number/perc))
		question = str(perc) + "\\% = " + str(number) + ", find 100\\%"
		
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))

def percreverse(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		d = random.randrange(0,2)
		p = random.randrange(1,6)*random.randrange(1,20)
		a = random.randrange(1,6)*random.randrange(1,51)
#write question
		if d==0:
			n = rounddp(a*(1-p/100),2)
			if n%1!=0:
				n = "{0:.2f}".format(n)
			else:
				n = str(int(n))
			tempquestions.write("The price of an item has decreased by "  + str(p) + "\%. It now costs \pounds" + n + ", find its original price.")
		else:
			n = rounddp(a*(1+p/100),2)
			if n%1!=0:
				n = "{0:.2f}".format(n)
			else:
				n = str(int(n))
			tempquestions.write("The price of an item has increased by "  + str(p) + "\%. It now costs \pounds" + n + ", find its original price.")
		tempquestions.write("\n")
#write answer
		tempquestions.write("\pounds" + str(a))



def percreverseice(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		p = random.randrange(3,21)
		a = random.randrange(2,21)*100
		n = int(a*(1+p/100))
		question = "When a liquid freezes its volume increases by " + str(p) + "\%. What volume of the liquid freezes to make " + str(n) + "cm$^{3}$ of ice?"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a) + "cm$^{2}$")



def percreversetip(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		p = random.randrange(1,6)*random.randrange(1,6)
		a = random.randrange(1,6)*random.randrange(10,20)
#write question
		n = rounddp(a*(1+p/100),2)
		if n%1!=0:
			n = "{0:.2f}".format(n)
		else:
			n = str(int(n))
		tempquestions.write("A meal costs \\pounds " + n + " including a " + str(p) + "\% service charge. Calculate the cost of the meal without the service charge.")
		tempquestions.write("\n")
#write answer
		tempquestions.write("\pounds" + str(a))


def perc50(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		p = 50
		if random.randrange(1,5)==1:
			a = random.randrange(10,201)
		else:
			a = random.randrange(1,100)*2
#write question
		tempquestions.write(explanation + str(p) + "\% of " + str(a))
		tempquestions.write("\n")
#write answer
		tempquestions.write("{0:g}".format(float(a*p/100)))

def perc25(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		p = 25
		if random.randrange(1,5)==1:
			a = random.randrange(10,100) * 2
		else:
			a = random.randrange(1,50)*4
#write question
		tempquestions.write(explanation + str(p) + "\% of " + str(a))
		tempquestions.write("\n")
#write answer
		tempquestions.write("{0:g}".format(float(a*p/100)))

def perc10(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		p = 10
		a = random.randrange(10,201)
#write question
		tempquestions.write(explanation + str(p) + "\% of " + str(a))
		tempquestions.write("\n")
#write answer
		tempquestions.write("{0:g}".format(float(a*p/100)))

def perc5(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		p = 5
		if random.randrange(1,5)==1:
			a = random.randrange(10,201)
		else:
			a = random.randrange(1,100)*2
#write question
		tempquestions.write(explanation + str(p) + "\% of " + str(a))
		tempquestions.write("\n")
#write answer
		tempquestions.write("{0:g}".format(float(a*p/100)))


def percchange5(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		d = random.randrange(0,2)
		p = random.randrange(1,15)*5
		if p%10==0:
			a = random.randrange(10,201)
		else:
			a = random.randrange(1,13)*10
		if d==0:
			r = rounddp(a * (1 - p/100),2)
		else:
			r = rounddp(a * (1 + p/100),2)
		if r%1!=0:
			r = "{0:.2f}".format(r)
		else:
			r = str(int(r))
#write question
		if d==0:
			tempquestions.write("The price of an item has been reduced from \pounds" + str(a) + " to \pounds" + r + ", by what percentage has it changed?")
		else:
			tempquestions.write("The price of an item has increased from \pounds" + str(a) + " to \pounds" + r + ", by what percentage has it changed?")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(p) + "\%")


def percchange(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		d = random.randrange(0,2)
		p = random.randrange(1,6)*random.randrange(1,20)
		a = random.randrange(1,6)*random.randrange(1,51)
		if d==0:
			r = rounddp(a * (1 - p/100),2)
		else:
			r = rounddp(a * (1 + p/100),2)
		if r%1!=0:
			r = "{0:.2f}".format(r)
		else:
			r = str(int(r))
#write question
		if d==0:
			tempquestions.write("The price of an item has been reduced from \pounds" + str(a) + " to \pounds" + r + ", by what percentage has it changed?")
		else:
			tempquestions.write("The price of an item has increased from \pounds" + str(a) + " to \pounds" + r + ", by what percentage has it changed?")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(p) + "\%")

def percchangeinc(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		d = 0
		p = random.randrange(1,6)*random.randrange(1,20)
		a = random.randrange(1,6)*random.randrange(1,51)
		if d==0:
			r = rounddp(a * (1 - p/100),2)
		else:
			r = rounddp(a * (1 + p/100),2)
		if r%1!=0:
			r = "{0:.2f}".format(r)
		else:
			r = str(int(r))
#write question
		if d==0:
			tempquestions.write("The price of an item has been reduced from \pounds" + str(a) + " to \pounds" + r + ", by what percentage has it changed?")
		else:
			tempquestions.write("The price of an item has increased from \pounds" + str(a) + " to \pounds" + r + ", by what percentage has it changed?")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(p) + "\%")


def numberasperc(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		p = random.randrange(1,6)*random.randrange(1,20)
		a = random.randrange(1,6)*random.randrange(1,51)
		b = rounddp(a * (1 - p/100),2)
		if b%1!=0:
			b = "{0:.2f}".format(b)
		else:
			b = str(int(b))
		p = 100 - p
#write question
		tempquestions.write("What percentage of \pounds" + str(a) + " is \pounds" + b + "?")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(p) + "\%")

def numberaspercnc(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if random.randrange(1,3)==1:
			p = 25*random.randrange(1,4)
			a = 4 * random.randrange(3,21)
		else:
			p = 10*random.randrange(1,10)
			a =10 * random.randrange(2,10)
		b = rounddp(a * (1 - p/100),2)
		if b%1!=0:
			b = "{0:.2f}".format(b)
		else:
			b = str(int(b))
		p = 100 - p
#write question
		tempquestions.write("What percentage of \pounds" + str(a) + " is \pounds" + b + "?")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(p) + "\%")



def percconcentrate(n,explanationn):
#from intermediate unit 2
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		perc = random.randrange(1,10)*10
		mult = random.randrange(2,10)
		lemon = perc*mult
		water = (100-perc)*mult
		if random.randrange(0,2)==0:
			question = "A drink is made by mixing " + str(lemon) + "ml of concentrate with " + str(water) + "ml of water. What percentage of the drink is water?"
			answer = str(100-perc) + "\%"
		else:
			question = "A drink is made by mixing " + str(lemon) + "ml of concentrate with " + str(water) + "ml of water. What percentage of the drink is concentrate?"
			answer = str(perc) + "\%"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def perctestscore(n,explanationn):
#from intermediate unit 2
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		outofs = [20,30,40,60,70,80,90,35,45,55,65,75,85,95]
		outof = random.choice(outofs)
		score = random.randrange(2,outof-1)
		perc = rounddp((score*100)/outof,2)
		if perc%1==0:
			perc = int(perc)
		question = "If you score " + str(score) + " out of " + str(outof) + " on a test, what is your percentage?"
		answer = str(perc) + "\%"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def compoundinterest(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		d1 = random.randrange(0,2)
		a = random.randrange(1,51)*500
		t2 = " at the start of "
		year = random.randrange(2010,2021)
		d2 = random.randrange(0,2)
		p = random.randrange(2,31)/2
		if p%1==0:
			p = int(p)
		t5 = "\% per year. What is "
		year2 = year + random.randrange(2,10)
		if d1==0:
			t1 = "The population of a place is "
			t3 = ". The population "
			t6 = "the population at the start of "
			if d2==0:
				ans = str(int(rounddp(a * (1-p/100)**(year2 - year),0)))
				t4 = "decreases by "
			else:
				ans = str(int(rounddp(a * (1+p/100)**(year2 - year),0)))
				t4 = "increases by "
		else:
			t1 = "The value of a thing is \pounds"
			t3 = ". Its value "
			t6 = " its value at the start of "
			if d2==0:
				ans = "\pounds" + str("{0:.2f}".format(a * (1-p/100)**(year2 - year)))
				t4 = "decreases by "
			else:
				ans = "\pounds" + str("{0:.2f}".format(a * (1+p/100)**(year2 - year)))
				t4 = "increases by "
#write question
		tempquestions.write(t1 + str(a) + t2 + str(year) + t3 + t4 + str(p) + t5 + t6 + str(year2) + "?")
		tempquestions.write("\n")
#write answer
		tempquestions.write(ans)

def compoundinterestincmon(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		d1 = 1
		a = random.randrange(1,51)*500
		t2 = " at the start of "
		year = random.randrange(2010,2021)
		d2 = 1
		p = random.randrange(2,31)/2
		if p%1==0:
			p = int(p)
		t5 = "\% per year. What is "
		year2 = year + random.randrange(2,10)
		if d1==0:
			t1 = "The population of a place is "
			t3 = ". The population "
			t6 = "the population at the start of "
			if d2==0:
				ans = str(int(rounddp(a * (1-p/100)**(year2 - year),0)))
				t4 = "decreases by "
			else:
				ans = str(int(rounddp(a * (1+p/100)**(year2 - year),0)))
				t4 = "increases by "
		else:
			t1 = "The value of a thing is \pounds"
			t3 = ". Its value "
			t6 = " its value at the start of "
			if d2==0:
				ans = "\pounds" + str("{0:.2f}".format(a * (1-p/100)**(year2 - year)))
				t4 = "decreases by "
			else:
				ans = "\pounds" + str("{0:.2f}".format(a * (1+p/100)**(year2 - year)))
				t4 = "increases by "
#write question
		tempquestions.write(t1 + str(a) + t2 + str(year) + t3 + t4 + str(p) + t5 + t6 + str(year2) + "?")
		tempquestions.write("\n")
#write answer
		tempquestions.write(ans)



def decimalmultiplier(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "What decimal multipler would you use to "
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			perc = random.randrange(1,50)
			question = "increase by " + str(perc) + "\\%?"
			answer = str(rounddp(1 + perc/100,2))
		else:
			perc = random.randrange(1,50)
			question = "decrease by " + str(perc) + "\\%?"
			answer = str(rounddp(1 - perc/100,2))
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def percchangenc(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		bases = [10,20,25,50]
		base = random.choice(bases)
		mults = list(range(1,6))
		remov = int(100/base)
		if remov in mults:
			mults.remove(remov)
		mult = random.choice(mults)
		diff = random.randrange(1,int(base/2.5))
		base = base * mult
		diff = diff * mult
		if random.randrange(0,2)==0:
			result = base + diff
			question = str(base) + " cats were sat in a hat. The next day, there were " + str(result) + " cats sat in the hat. By what percentage has the number of cats increased?"
		else:
			result = base - diff
			question = str(base) + " cats were sat in a hat. The next day, there were " + str(result) + " cats sat in the hat. By what percentage has the number of cats decreased?"
		answer = str(int(rounddp(100 * diff/base,0))) + "\\%"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def percchangencstarter(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find "
		else:
			explanation = ""
		bases = [10,20,25,50]
		base = random.choice(bases)
		mults = list(range(1,6))
		remov = int(100/base)
		if remov in mults:
			mults.remove(remov)
		mult = random.choice(mults)
		diff = random.randrange(1,int(base/2.5))
		base = base * mult
		diff = diff * mult
		if random.randrange(0,2)==0:
			result = base + diff
			question = "Yesterday there were " + str(base) + " cats, today there are " + str(result) + ". What is the percentage increase?"
		else:
			result = base - diff
			question = "Yesterday there were " + str(base) + " cats, today there are " + str(result) + ". What is the percentage decrease?"
		answer = str(int(rounddp(100 * diff/base,0))) + "\\%"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def percchangedivision(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		d = random.randrange(0,2)
		p = random.randrange(1,6)*random.randrange(1,20)
		a = random.randrange(1,6)*random.randrange(1,51)
		if d==0:
			answer = str(rounddp(1 - p/100,2))
			r = rounddp(a * (1 - p/100),2)
		else:
			answer = str(rounddp(1 + p/100,2))
			r = rounddp(a * (1 + p/100),2)
		if r%1!=0:
			r = "{0:.2f}".format(r)
		else:
			r = str(int(r))
		question = "$" + str(a) + " \\times \\rule[-1.5mm]{1cm}{0.15mm} = " + str(r) + "$"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)





def doublepercchange(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		p1 = random.randrange(3,51) * (-1)**random.randrange(1,3)
		p2 = random.randrange(3,51) * (-1)**random.randrange(1,3)
		if p1>0:
			word1 = "increases"
		else:
			word1 = "decreases"
		if p2>0:
			word2 = "increases"
		else:
			word2 = "decreases"
		dm1 = 1 + rounddp(p1/100,2)
		dm2 = 1 + rounddp(p2/100,2)
		answer = rounddp((dm1*dm2-1)*100,2)
		if answer==0:
			answer = "0\% - no change"
		elif answer<0:
			answer = str(abs(answer)) + "\% decrease"
		else:
			answer = str(answer) + "\% increase"
		question = "The value of a product " + word1 + " by " + str(abs(p1)) + "\%, and then " + word2 + " by " + str(abs(p2)) + "\%. What is the overall percentage change from the original value?"
		
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def perctriangle1(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		ov = random.randrange(11,200)
		dm = rounddp(1 + random.randrange(1,80)/100*(-1)**random.randrange(0,2),2)
		nv = rounddp(ov*dm,2)
		question = "Old \\mbox{value = " + str(ov) + "}, decimal \\mbox{multiplier = " + str(dm) + "}, find new value"
		answer = str(nv)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def perctriangle2(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		ov = random.randrange(11,200)
		dm = rounddp(1 + random.randrange(1,80)/100*(-1)**random.randrange(0,2),2)
		nv = rounddp(ov*dm,2)
		question = "New \\mbox{value = " + str(nv) + "}, decimal \\mbox{multiplier = " + str(dm) + "}, find old value"
		answer = str(ov)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def perctriangle3(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		ov = random.randrange(11,200)
		dm = rounddp(1 + random.randrange(1,80)/100*(-1)**random.randrange(0,2),2)
		nv = rounddp(ov*dm,2)
		question = "Old \\mbox{value = " + str(ov) + "}, new \\mbox{value = " + str(nv) + "}, find decimal multiplier"
		answer = str(dm)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
