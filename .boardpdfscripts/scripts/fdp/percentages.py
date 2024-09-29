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
			n = round(a*(1-p/100),2)
			if n%1!=0:
				n = "{0:.2f}".format(n)
			else:
				n = str(int(n))
			tempquestions.write("The price of an item has decreased by "  + str(p) + "\%. It now costs \pounds" + n + ", find its original price.")
		else:
			n = round(a*(1+p/100),2)
			if n%1!=0:
				n = "{0:.2f}".format(n)
			else:
				n = str(int(n))
			tempquestions.write("The price of an item has increased by "  + str(p) + "\%. It now costs \pounds" + n + ", find its original price.")
		tempquestions.write("\n")
#write answer
		tempquestions.write("\pounds" + str(a))

def percreverse(n,explanationn):
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
			n = round(a*(1-p/100),2)
			if n%1!=0:
				n = "{0:.2f}".format(n)
			else:
				n = str(int(n))
			tempquestions.write("The price of an item has decreased by "  + str(p) + "\%. It now costs \pounds" + n + ", find its original price.")
		else:
			n = round(a*(1+p/100),2)
			if n%1!=0:
				n = "{0:.2f}".format(n)
			else:
				n = str(int(n))
			tempquestions.write("The price of an item has increased by "  + str(p) + "\%. It now costs \pounds" + n + ", find its original price.")
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
		if d==0:
			r = round(a * (1 - p/100),2)
		else:
			r = round(a * (1 + p/100),2)
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
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		d = random.randrange(0,2)
		p = random.randrange(1,6)*random.randrange(1,20)
		a = random.randrange(1,6)*random.randrange(1,51)
		if d==0:
			r = round(a * (1 - p/100),2)
		else:
			r = round(a * (1 + p/100),2)
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
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		d = 0
		p = random.randrange(1,6)*random.randrange(1,20)
		a = random.randrange(1,6)*random.randrange(1,51)
		if d==0:
			r = round(a * (1 - p/100),2)
		else:
			r = round(a * (1 + p/100),2)
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
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		p = random.randrange(1,6)*random.randrange(1,20)
		a = random.randrange(1,6)*random.randrange(1,51)
		b = round(a * (1 - p/100),2)
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


def compoundinterest(n,explanationn):
	import random
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
				ans = str(int(round(a * (1-p/100)**(year2 - year),0)))
				t4 = "decreases by "
			else:
				ans = str(int(round(a * (1+p/100)**(year2 - year),0)))
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
				ans = str(int(round(a * (1-p/100)**(year2 - year),0)))
				t4 = "decreases by "
			else:
				ans = str(int(round(a * (1+p/100)**(year2 - year),0)))
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
