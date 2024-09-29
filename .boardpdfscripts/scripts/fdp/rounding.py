#!/usr/bin/env python3
#rounding.py
def round10(n,explanationn):
	import random
	from math import log10, floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Round "
			explanation2 = " to the nearest 10"
		else:
			explanation1 = ""
			explanation2 = ""
		roundto = 10
		number = random.randrange(0,roundto*10**random.randrange(1,3))*10 + random.randrange(1,10)
		length = len(str(floor(number)))
		number = number * 10**(10-length)
		roundto = 10**(10-(length-(log10(roundto))))
		remainder = number%roundto
		if remainder < 0.5*roundto:
			rounded = number - remainder
		else:
			rounded = number + (roundto-remainder)
		number = number / 10**(10-length)
		rounded = rounded / 10**(10-length)
		if number%1==0:
			number = int(number)
		else:
			number = round(number,6)
		if rounded%1==0:
			rounded = int(rounded)
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded))


def round100(n,explanationn):
	import random
	from math import log10, floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Round "
			explanation2 = " to the nearest 100"
		else:
			explanation1 = ""
			explanation2 = ""
		roundto = 100
		number = random.randrange(0,roundto*10**random.randrange(1,3))*10 + random.randrange(1,10)
		length = len(str(floor(number)))
		number = number * 10**(10-length)
		roundto = 10**(10-(length-(log10(roundto))))
		remainder = number%roundto
		if remainder < 0.5*roundto:
			rounded = number - remainder
		else:
			rounded = number + (roundto-remainder)
		number = number / 10**(10-length)
		rounded = rounded / 10**(10-length)
		if number%1==0:
			number = int(number)
		else:
			number = round(number,6)
		if rounded%1==0:
			rounded = int(rounded)
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded))

def round1000(n,explanationn):
	import random
	from math import log10, floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Round "
			explanation2 = " to the nearest 1000"
		else:
			explanation1 = ""
			explanation2 = ""
		roundto = 1000
		number = random.randrange(0,roundto*10**random.randrange(1,3))*10 + random.randrange(1,10)
		length = len(str(floor(number)))
		number = number * 10**(10-length)
		roundto = 10**(10-(length-(log10(roundto))))
		remainder = number%roundto
		if remainder < 0.5*roundto:
			rounded = number - remainder
		else:
			rounded = number + (roundto-remainder)
		number = number / 10**(10-length)
		rounded = rounded / 10**(10-length)
		if number%1==0:
			number = int(number)
		else:
			number = round(number,6)
		if rounded%1==0:
			rounded = int(rounded)
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded))


def round0dp(n,explanationn):
	import random
	from math import log10, floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Round "
			explanation2 = " to a whole number"
		else:
			explanation1 = ""
			explanation2 = ""
		roundto = 1
		if random.randrange(0,2)==1:
			number = random.randrange(0,21) + (random.randrange(0,10) * 10 + random.randrange(1,10))/100
		else:
			number = random.randrange(0,21) + random.randrange(1,10)/10
		length = len(str(floor(number)))
		number = number * 10**(10-length)
		roundto = 10**(10-(length-(log10(roundto))))
		remainder = number%roundto
		if remainder < 0.5*roundto:
			rounded = number - remainder
		else:
			rounded = number + (roundto-remainder)
		number = number / 10**(10-length)
		rounded = rounded / 10**(10-length)
		if number%1==0:
			number = int(number)
		else:
			number = round(number,6)
		if rounded%1==0:
			rounded = int(rounded)
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded))

def round1dp(n,explanationn):
	import random
	from math import log10, floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Round "
			explanation2 = " to 1 d.p."
		else:
			explanation1 = ""
			explanation2 = ""
		roundto = 0.1
		if random.randrange(0,2)==1:
			number = random.randrange(0,21) + (random.randrange(0,10) * 10 + random.randrange(1,10))/100
		else:
			number = random.randrange(0,21) + (random.randrange(0,100) * 10 + random.randrange(1,10))/1000
		length = len(str(floor(number)))
		number = number * 10**(10-length)
		roundto = 10**(10-(length-(log10(roundto))))
		remainder = number%roundto
		if remainder < 0.5*roundto:
			rounded = number - remainder
		else:
			rounded = number + (roundto-remainder)
		number = number / 10**(10-length)
		rounded = rounded / 10**(10-length)
		if number%1==0:
			number = int(number)
		else:
			number = round(number,6)
		if rounded%1==0:
			zeros = ".0"
			rounded = int(rounded)
		else:
			zeros = ""
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded) + zeros)

def round2dp(n,explanationn):
	import random
	from math import log10, floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Round "
			explanation2 = " to 2 d.p."
		else:
			explanation1 = ""
			explanation2 = ""
		roundto = 0.01
		if random.randrange(0,2)==1:
			number = random.randrange(0,21) + (random.randrange(0,100) * 10 + random.randrange(1,10))/1000
		else:
			number = random.randrange(0,21) + (random.randrange(0,1000) * 10 + random.randrange(1,10))/10000
		length = len(str(floor(number)))
		number = number * 10**(10-length)
		roundto = 10**(10-(length-(log10(roundto))))
		remainder = number%roundto
		if remainder < 0.5*roundto:
			rounded = number - remainder
		else:
			rounded = number + (roundto-remainder)
		number = number / 10**(10-length)
		rounded = rounded / 10**(10-length)
		if number%1==0:
			number = int(number)
		else:
			number = round(number,6)
		if rounded%1==0:
			zeros = ".00"
			rounded = int(rounded)
		elif (rounded*10)%1==0:
			zeros = "0"
		else:
			zeros = ""
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded) + zeros)

def round1sf1(n,explanationn):
	import random
	from math import log10, floor, ceil
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Round "
			explanation2 = " to 1 s.f."
		else:
			explanation1 = ""
			explanation2 = ""
		roundto = 1
		number = random.randrange(1,10**random.randrange(2,5))*10 + random.randrange(1,10)
		firstsig = ceil(log10(number))
		number = number * 10**(10-firstsig)
		roundto = 10**(10-roundto)
		remainder = number%roundto
		if remainder < 0.5*roundto:
			rounded = number - remainder
		else:
			rounded = number + (roundto-remainder)
		number = number / 10**(10-firstsig)
		rounded = rounded / 10**(10-firstsig)
		if number%1==0:
			number = int(number)
		else:
			number = round(number,6)
		if rounded%1==0:
			rounded = int(rounded)
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded))

def round2sf1(n,explanationn):
	import random
	from math import log10, floor, ceil
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Round "
			explanation2 = " to 2 s.f."
		else:
			explanation1 = ""
			explanation2 = ""
		roundto = 2
		number = random.randrange(10,10**random.randrange(2,5))*10 + random.randrange(1,10)
		firstsig = ceil(log10(number))
		number = number * 10**(10-firstsig)
		roundto = 10**(10-roundto)
		remainder = number%roundto
		if remainder < 0.5*roundto:
			rounded = number - remainder
		else:
			rounded = number + (roundto-remainder)
		number = number / 10**(10-firstsig)
		rounded = rounded / 10**(10-firstsig)
		if number%1==0:
			number = int(number)
		else:
			number = round(number,6)
		if rounded%1==0:
			rounded = int(rounded)
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded))

def round3sf1(n,explanationn):
	import random
	from math import log10, floor, ceil
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Round "
			explanation2 = " to 3 s.f."
		else:
			explanation1 = ""
			explanation2 = ""
		roundto = 3
		number = random.randrange(100,10**random.randrange(3,6))*10 + random.randrange(1,10)
		firstsig = ceil(log10(number))
		number = number * 10**(10-firstsig)
		roundto = 10**(10-roundto)
		remainder = number%roundto
		if remainder < 0.5*roundto:
			rounded = number - remainder
		else:
			rounded = number + (roundto-remainder)
		number = number / 10**(10-firstsig)
		rounded = rounded / 10**(10-firstsig)
		if number%1==0:
			number = int(number)
		else:
			number = round(number,6)
		if rounded%1==0:
			rounded = int(rounded)
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded))


def round1sf2(n,explanationn):
	import random
	from math import log10, floor, ceil
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Round "
			explanation2 = " to 1 s.f."
		else:
			explanation1 = ""
			explanation2 = ""
		roundto = 1
		number = (random.randrange(1,10**random.randrange(2,5))*10 + random.randrange(1,10)) / 10**random.randrange(1,6)
		firstsig = ceil(log10(number))
		number = number * 10**(10-firstsig)
		roundto = 10**(10-roundto)
		remainder = number%roundto
		if remainder < 0.5*roundto:
			rounded = number - remainder
		else:
			rounded = number + (roundto-remainder)
		number = number / 10**(10-firstsig)
		rounded = rounded / 10**(10-firstsig)
		if number%1==0:
			number = int(number)
		else:
			number = round(number,6)
		if rounded%1==0:
			rounded = int(rounded)
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded))

def round2sf2(n,explanationn):
	import random
	from math import log10, floor, ceil
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Round "
			explanation2 = " to 2 s.f."
		else:
			explanation1 = ""
			explanation2 = ""
		roundto = 2
		number = (random.randrange(10,10**random.randrange(2,5))*10 + random.randrange(1,10)) / 10**random.randrange(1,6)
		firstsig = ceil(log10(number))
		number = number * 10**(10-firstsig)
		roundto = 10**(10-roundto)
		remainder = number%roundto
		if remainder < 0.5*roundto:
			rounded = number - remainder
		else:
			rounded = number + (roundto-remainder)
		number = number / 10**(10-firstsig)
		rounded = rounded / 10**(10-firstsig)
		if number%1==0:
			number = int(number)
		else:
			number = round(number,6)
		if rounded%1==0:
			rounded = int(rounded)
			if rounded < 10:
				zeros = ".0"
			else:
				zeros = ""
		elif rounded<1 and rounded*10**(abs(firstsig)+1)%1==0:
			zeros = "0"
		else:
			zeros = ""
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded) + zeros)

def round3sf2(n,explanationn):
	import random
	from math import log10, floor, ceil
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Round "
			explanation2 = " to 3 s.f."
		else:
			explanation1 = ""
			explanation2 = ""
		roundto = 3
		number = (random.randrange(100,10**random.randrange(3,6))*10 + random.randrange(1,10)) / 10**random.randrange(1,6)
		firstsig = ceil(log10(number))
		number = number * 10**(10-firstsig)
		roundto = 10**(10-roundto)
		remainder = number%roundto
		if remainder < 0.5*roundto:
			rounded = number - remainder
		else:
			rounded = number + (roundto-remainder)
		number = number / 10**(10-firstsig)
		rounded = rounded / 10**(10-firstsig)
		if number%1==0:
			number = int(number)
		else:
			number = round(number,6)
		if rounded%1==0:
			rounded = int(rounded)
			if rounded < 10:
				zeros = ".00"
			elif rounded < 100:
				zeros = ".0"
			else:
				zeros = ""
		elif rounded<1 and rounded*10**(abs(firstsig)+1)%1==0:
			zeros = "00"
		elif rounded<1 and rounded*10**(abs(firstsig)+2)%1==0:
			zeros = "0"
		elif rounded<10 and rounded*10%1==0:
			zeros = "0"
		else:
			zeros = ""
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded) + zeros)


def bounds10(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		roundto = 10**random.randrange(1,3)
		units = ["mm","m","cm"]
		unit = random.choice(units)
		if explanationn==1:
			explanation1 = "Find the upper and lower bounds for a length measuring "
			explanation2 = " to the nearest " + str(roundto) + unit
		else:
			explanation1 = ""
			explanation2 = " to the nearest " + str(roundto) + unit
		num = random.randrange(1,1000)
		num = num * roundto
		diff = roundto/2
		upper = int(num + diff)
		lower = int(num - diff)
#write question
		tempquestions.write(explanation1 + str(num) + unit + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(lower) + unit + " and " + str(upper) + unit)

def boundsdp(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		roundto = random.randrange(0,3)
		units = ["mm","m","cm"]
		unit = random.choice(units)
		if explanationn==1:
			explanation1 = "Find the upper and lower bounds for a length measuring "
			if roundto==0:
				explanation2 = " to the nearest " + unit
			else:
				explanation2 = " to " + str(roundto) + " d.p."
		else:
			explanation1 = ""
			if roundto==0:
				explanation2 = " to the nearest " + unit
			else:
				explanation2 = " to " + str(roundto) + " d.p."
		num = random.randrange(1,1000)
		num = round(num / 10**roundto,roundto)
		diff = 0.5 * 10**(-roundto)
		upper = round(num + diff,roundto+1)
		lower = round(num - diff,roundto+1)
		if roundto==0:
			num = int(num)
			zeros = ""
		elif roundto==2 and num%1==0:
			zeros = "00"
		elif roundto==2 and (num*10)%1==0:
			zeros = "0"
		else:
			zeros = ""
#write question
		tempquestions.write(explanation1 + str(num) + zeros + unit + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(lower) + unit + " and " + str(upper) + unit)


def boundssf(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		roundto = random.randrange(1,4)
		units = ["mm","m","cm"]
		unit = random.choice(units)
		if explanationn==1:
			explanation1 = "Find the upper and lower bounds for a length measuring "
			explanation2 = " to " + str(roundto) + " s.f."
		else:
			explanation1 = ""
			explanation2 = " to " + str(roundto) + " s.f."
		num = random.randrange(10**(roundto-1),10**roundto)
		adjust = random.randrange(-2,3)
		num = round(num * 10**adjust,2)
		diff = 0.5 * 10**adjust
		upper = round(num + diff,3)
		lower = round(num - diff,3)
		if upper%1==0:
			upper = int(upper)
		if lower%1==0:
			lower = int(lower)
		if num%1==0:
			num = int(num)
			if num < 10 and roundto==2:
				zeros = ".0"
			elif num < 10 and roundto==3:
				zeros = ".00"
			elif num < 100 and roundto==3:
				zeros = ".0"
			else:
				zeros = ""
		elif num<1 and (num*10)%1==0 and roundto==3:
			zeros = "00"
		elif num<1 and (num*10)%1==0 and roundto==2:
			zeros = "0"
		elif num<1 and (num*100)%1==0 and roundto==3:
			zeros = "0"
		else:
			zeros = ""
#write question
		tempquestions.write(explanation1 + str(num) + zeros + unit + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(lower) + unit + " and " + str(upper) + unit)
