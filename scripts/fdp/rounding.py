#!/usr/bin/env python3
#rounding.py
def round10(n,explanationn):
	from utilities.rounding import roundnearest
	import random
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
		roundto=10
		number = random.randrange(0,roundto*10**random.randrange(1,3))*10 + random.randrange(1,10)
		rounded = roundnearest(number,roundto)
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded))


def round100(n,explanationn):
	import random
	from utilities.rounding import roundnearest
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
		rounded = roundnearest(number,roundto)
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded))

def round1000(n,explanationn):
	import random
	from utilities.rounding import roundnearest
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
		rounded = roundnearest(number,roundto)
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded))


def round0dp(n,explanationn):
	import random
	from utilities.rounding import roundnearest,rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Round "
			explanation2 = " to the nearest integer"
		else:
			explanation1 = ""
			explanation2 = ""
		roundto = 1
		if random.randrange(0,2)==1:
			number = random.randrange(0,21) + (random.randrange(0,10) * 10 + random.randrange(1,10))/100
		else:
			number = random.randrange(0,21) + random.randrange(1,10)/10
		rounded = roundnearest(number,roundto)
		number = rounddp(number,2)
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded))

def round1dp(n,explanationn):
	import random
	from utilities.rounding import rounddpstring,rounddp
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
		roundto = 1
		if random.randrange(0,2)==1:
			number = rounddp(random.randrange(0,21) + (random.randrange(0,10) * 10 + random.randrange(1,10))/100,2)
		else:
			number = rounddp(random.randrange(0,21) + (random.randrange(0,100) * 10 + random.randrange(1,10))/1000,3)
		rounded = rounddpstring(number,roundto)
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded))

def round2dp(n,explanationn):
	import random
	from utilities.rounding import rounddpstring,rounddp
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
		roundto = 2
		if random.randrange(0,2)==1:
			number = rounddp(random.randrange(0,21) + (random.randrange(0,100) * 10 + random.randrange(1,10))/1000,3)
		else:
			number = rounddp(random.randrange(0,21) + (random.randrange(0,1000) * 10 + random.randrange(1,10))/10000,4)
		rounded = rounddpstring(number,roundto)
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded))

def round1sf1(n,explanationn):
	import random
	from utilities.rounding import roundsfstring
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
		rounded = roundsfstring(number,roundto)
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded))

def round2sf1(n,explanationn):
	import random
	from utilities.rounding import roundsfstring
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
		rounded = roundsfstring(number,roundto)
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded))

def round3sf1(n,explanationn):
	import random
	from utilities.rounding import roundsfstring
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
		rounded = roundsfstring(number,roundto)
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded))


def round1sf2(n,explanationn):
	import random
	from utilities.rounding import roundsfstring
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
		rounded = roundsfstring(number,roundto)
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded))

def round2sf2(n,explanationn):
	import random
	from utilities.rounding import roundsfstring
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
		rounded = roundsfstring(number,roundto)
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded))

def round3sf2(n,explanationn):
	import random
	from utilities.rounding import roundsfstring
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
		rounded = roundsfstring(number,roundto)
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded))


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

def errorintervals10(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		roundto = 10**random.randrange(1,3)
		letters = ["x","y","z"]
		letter = random.choice(letters)
		explanation1 = "A number, " + letter + ", rounded to the nearest " + str(roundto) + " is "
		explanation2 = ", write down the error interval for " + letter + "."
		num = random.randrange(1,1000)
		num = num * roundto
		diff = roundto/2
		upper = int(num + diff)
		lower = int(num - diff)
		answer = "$" + str(lower) + "\\leq " + letter + " <" + str(upper) + "$"
#write question
		tempquestions.write(explanation1 + str(num) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def boundsdp(n,explanationn):
	import random
	from utilities.rounding import rounddp,rounddpstring,roundnearest
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
				explanation2 = " rounded to the nearest " + unit
			else:
				explanation2 = " rounded to " + str(roundto) + " d.p."
		else:
			explanation1 = ""
			if roundto==0:
				explanation2 = " rounded to the nearest " + unit
			else:
				explanation2 = " rounded to " + str(roundto) + " d.p."
		num = random.randrange(1,1000)
		num = rounddp(num / 10**roundto,roundto)
		diff = 0.5 * 10**(-roundto)
		upper = rounddp(num + diff,roundto+1)
		lower = rounddp(num - diff,roundto+1)
		if roundto==0:
			num = str(roundnearest(num,1))
		else:
			num = rounddpstring(num,roundto)
#write question
		tempquestions.write(explanation1 + str(num) +  unit + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(lower) + unit + " and " + str(upper) + unit)



def errorintervalsdp(n,explanationn):
	import random
	from utilities.rounding import rounddp,rounddpstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		roundto = random.randrange(0,3)
		letters = ["x","y","z"]
		letter = random.choice(letters)
		if roundto==0:
			explanation1 = "A number, " + letter + ", rounded to the nearest whole number is "
			explanation2 = ", write down the error interval for " + letter + "."
		elif roundto==1:
			explanation1 = "A number, " + letter + ", rounded to " + str(roundto) + " decimal place is "
			explanation2 = ", write down the error interval for " + letter + "."
		else:
			explanation1 = "A number, " + letter + ", rounded to " + str(roundto) + " decimal places is "
			explanation2 = ", write down the error interval for " + letter + "."
		num = random.randrange(1,1000)
		num = rounddp(num / 10**roundto,roundto)
		diff = 0.5 * 10**(-roundto)
		upper = rounddp(num + diff,roundto+1)
		lower = rounddp(num - diff,roundto+1)
		if roundto==0:
			num = int(num)
		else:
			num = rounddpstring(num,roundto)
		answer = "$" + str(lower) + "\\leq " + letter + " <" + str(upper) + "$"
#write question
		tempquestions.write(explanation1 + str(num) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def boundssf(n,explanationn):
	import random
	from utilities.rounding import rounddp,roundsfstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		roundto = random.randrange(1,4)
		units = ["mm","m","cm"]
		unit = random.choice(units)
		if explanationn==1:
			explanation1 = "Find the upper and lower bounds for a length measuring "
			explanation2 = " rounded to " + str(roundto) + " s.f."
		else:
			explanation1 = ""
			explanation2 = " to " + str(roundto) + " s.f."
		num = random.randrange(10**(roundto-1),10**roundto)
		adjust = random.randrange(-2,3)
		num = rounddp(num * 10**adjust,2)
		diff = 0.5 * 10**adjust
		upper = rounddp(num + diff,3)
		lower = rounddp(num - diff,3)
		if upper%1==0:
			upper = int(upper)
		if lower%1==0:
			lower = int(lower)
		num = roundsfstring(num,roundto)
#write question
		tempquestions.write(explanation1 + str(num) + unit + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(lower) + unit + " and " + str(upper) + unit)



def errorintervalssf(n,explanationn):
	import random
	from utilities.rounding import rounddp,roundsfstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		roundto = random.randrange(1,4)
		letters = ["x","y","z"]
		letter = random.choice(letters)
		if roundto==1:
			explanation1 = "A number, " + letter + ", rounded to " + str(roundto) + " significant figure is "
		else:
			explanation1 = "A number, " + letter + ", rounded to " + str(roundto) + " significant figures is "
		explanation2 = ", write down the error interval for " + letter + "."
		num = random.randrange(10**(roundto-1),10**roundto)
		adjust = random.randrange(-2,3)
		num = rounddp(num * 10**adjust,2)
		diff = 0.5 * 10**adjust
		upper = rounddp(num + diff,3)
		lower = rounddp(num - diff,3)
		if upper%1==0:
			upper = int(upper)
		if lower%1==0:
			lower = int(lower)
		num = roundsfstring(num,roundto)
		answer = "$" + str(lower) + "\\leq " + letter + " <" + str(upper) + "$"
#write question
		tempquestions.write(explanation1 + str(num) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def trunc1dp(n,explanationn):
	import random
	from utilities.truncating import truncdpstring
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Truncate "
			explanation2 = " to 1 d.p."
		else:
			explanation1 = ""
			explanation2 = ""
		if random.randrange(0,2)==1:
			number = rounddp(random.randrange(0,21) + (random.randrange(0,10) * 10 + random.randrange(1,10))/100,2)
		else:
			number = rounddp(random.randrange(0,21) + (random.randrange(0,100) * 10 + random.randrange(1,10))/1000,3)
		question = str(number)
		answer = truncdpstring(number,1)
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def trunc2dp(n,explanationn):
	import random
	from utilities.truncating import truncdpstring
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Truncate "
			explanation2 = " to 2 d.p."
		else:
			explanation1 = ""
			explanation2 = ""
		if random.randrange(0,2)==1:
			number = rounddp(random.randrange(0,21) + (random.randrange(0,100) * 10 + random.randrange(1,10))/1000,3)
		else:
			number = rounddp(random.randrange(0,21) + (random.randrange(0,1000) * 10 + random.randrange(1,10))/10000,4)
		question = str(number)
		answer = truncdpstring(number,2)
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def trunc1sf(n,explanationn):
	import random
	from utilities.truncating import truncsfstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Truncate "
			explanation2 = " to 1 s.f."
		else:
			explanation1 = ""
			explanation2 = ""
		number = (random.randrange(1,10**random.randrange(2,5))*10 + random.randrange(1,10)) / 10**random.randrange(1,6)
		question = str(number)
		answer = truncsfstring(number,1)
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def trunc2sf(n,explanationn):
	import random
	from utilities.truncating import truncsfstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Truncate "
			explanation2 = " to 2 s.f."
		else:
			explanation1 = ""
			explanation2 = ""
		number = (random.randrange(10,10**random.randrange(2,5))*10 + random.randrange(1,10)) / 10**random.randrange(1,6)
		question = str(number)
		answer = truncsfstring(number,2)
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def errorintervalstruncdp(n,explanationn):
	import random
	from utilities.rounding import rounddp,rounddpstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		roundto = random.randrange(0,3)
		letters = ["x","y","z"]
		letter = random.choice(letters)
		if roundto==0:
			explanation1 = "A number, " + letter + ", truncated to the nearest whole number is "
			explanation2 = ", write down the error interval for " + letter + "."
		elif roundto==1:
			explanation1 = "A number, " + letter + ", truncated to " + str(roundto) + " decimal place is "
			explanation2 = ", write down the error interval for " + letter + "."
		else:
			explanation1 = "A number, " + letter + ", truncated to " + str(roundto) + " decimal places is "
			explanation2 = ", write down the error interval for " + letter + "."
		num = random.randrange(1,1000)
		lower = rounddp(num / 10**roundto,roundto)
		upper = rounddp((num+1) / 10**roundto,roundto)
		num = rounddp(lower,roundto)
		if roundto==0:
			num = int(num)
		else:
			num = rounddpstring(num,roundto)
		if upper%1==0:
			upper = int(upper)
		if lower%1==0:
			lower = int(lower)

		answer = "$" + str(lower) + "\\leq " + letter + " <" + str(upper) + "$"
#write question
		tempquestions.write(explanation1 + str(num) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def errorintervalstruncsf(n,explanationn):
	import random
	from utilities.rounding import rounddp,roundsfstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		roundto = random.randrange(1,4)
		letters = ["x","y","z"]
		letter = random.choice(letters)
		if roundto==1:
			explanation1 = "A number, " + letter + ", truncated to " + str(roundto) + " significant figure is "
		else:
			explanation1 = "A number, " + letter + ", truncated to " + str(roundto) + " significant figures is "
		explanation2 = ", write down the error interval for " + letter + "."
		num = random.randrange(10**(roundto-1),10**roundto)
		adjust = random.randrange(-2,3)
		lower = rounddp(num * 10**adjust,2)
		upper = rounddp((num+1) * 10**adjust,2)
		if upper%1==0:
			upper = int(upper)
		if lower%1==0:
			lower = int(lower)
		num = roundsfstring(lower,roundto)
		answer = "$" + str(lower) + "\\leq " + letter + " <" + str(upper) + "$"
#write question
		tempquestions.write(explanation1 + str(num) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def round10arrow(n,explanationn):
	from utilities.rounding import roundnearest
	import random
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
		roundto=10
		number = random.randrange(0,roundto*10**random.randrange(1,3))*10 + random.randrange(1,10)
		rounded = roundnearest(number,roundto)
		numlist = list(str(number))
		numlist[len(numlist)-2] = "$\\overset{\\downarrow}{" + numlist[len(numlist)-2] + "}$"
		number = ""
		for i in range(0,len(numlist)):
			number += numlist[i]
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded))



def round100arrow(n,explanationn):
	import random
	from utilities.rounding import roundnearest
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
		rounded = roundnearest(number,roundto)
		numlist = list(str(number))
		numlist[len(numlist)-3] = "$\\overset{\\downarrow}{" + numlist[len(numlist)-3] + "}$"
		number = ""
		for i in range(0,len(numlist)):
			number += numlist[i]
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded))

def round1000arrow(n,explanationn):
	import random
	from utilities.rounding import roundnearest
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
		rounded = roundnearest(number,roundto)
		numlist = list(str(number))
		numlist[len(numlist)-4] = "$\\overset{\\downarrow}{" + numlist[len(numlist)-4] + "}$"
		number = ""
		for i in range(0,len(numlist)):
			number += numlist[i]
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded))


def round0dparrow(n,explanationn):
	import random
	from utilities.rounding import roundnearest,rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Round "
			explanation2 = " to the nearest integer"
		else:
			explanation1 = ""
			explanation2 = ""
		roundto = 1
		if random.randrange(0,2)==1:
			number = random.randrange(0,21) + (random.randrange(0,10) * 10 + random.randrange(1,10))/100
		else:
			number = random.randrange(0,21) + random.randrange(1,10)/10
		rounded = roundnearest(number,roundto)
		number = rounddp(number,2)
		numlist = list(str(number))
		decloc = numlist.index(".")
		numlist[decloc-1] = "$\\overset{\\downarrow}{" + numlist[decloc-1] + "}$"
		number = ""
		for i in range(0,len(numlist)):
			number += numlist[i]
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded))

def round1dparrow(n,explanationn):
	import random
	from utilities.rounding import rounddpstring,rounddp
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
		roundto = 1
		if random.randrange(0,2)==1:
			number = rounddp(random.randrange(0,21) + (random.randrange(0,10) * 10 + random.randrange(1,10))/100,2)
		else:
			number = rounddp(random.randrange(0,21) + (random.randrange(0,100) * 10 + random.randrange(1,10))/1000,3)
		rounded = rounddpstring(number,roundto)
		numlist = list(str(number))
		decloc = numlist.index(".")
		numlist[decloc+1] = "$\\overset{\\downarrow}{" + numlist[decloc+1] + "}$"
		number = ""
		for i in range(0,len(numlist)):
			number += numlist[i]
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded))

def round2dparrow(n,explanationn):
	import random
	from utilities.rounding import rounddpstring,rounddp
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
		roundto = 2
		if random.randrange(0,2)==1:
			number = rounddp(random.randrange(0,21) + (random.randrange(0,100) * 10 + random.randrange(1,10))/1000,3)
		else:
			number = rounddp(random.randrange(0,21) + (random.randrange(0,1000) * 10 + random.randrange(1,10))/10000,4)
		rounded = rounddpstring(number,roundto)
		numlist = list(str(number))
		decloc = numlist.index(".")
		numlist[decloc+2] = "$\\overset{\\downarrow}{" + numlist[decloc+2] + "}$"
		number = ""
		for i in range(0,len(numlist)):
			number += numlist[i]
#write question
		tempquestions.write(explanation1 + str(number) + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rounded))
