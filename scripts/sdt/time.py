#!/usr/bin/env python3
#time.py

def timeadd2451(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "What time will it be "
		else:
			explanation = ""
		time1 = 300 * random.randrange(0,288)
		diff = 300 * random.randrange(3,12)
		time2 = time1 + diff

		hours = int(floor(time1/3600))
		minutes = int((time1 - hours*3600)/60)
		if hours > 23:
			hours = hours - 24
		elif hours<0:
			hours = hours + 24
		if hours < 10:
			hours = "0" + str(hours)
		if minutes < 10:
			minutes = "0" + str(minutes)
		time1 = str(hours) + ":" + str(minutes)

		hours = int(floor(time2/3600))
		minutes = int((time2 - hours*3600)/60)
		if hours > 23:
			hours = hours - 24
		elif hours<0:
			hours = hours + 24
		if hours < 10:
			hours = "0" + str(hours)
		if minutes < 10:
			minutes = "0" + str(minutes)
		time2 = str(hours) + ":" + str(minutes)

		diff = int(diff / 60)
#write question
		tempquestions.write(explanation + str(diff) + " minutes after " + time1 + "?")

		tempquestions.write("\n")
#write answer
		tempquestions.write(time2)



def timeadd2452(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "What time will it be "
		else:
			explanation = ""
		time1 = 300 * random.randrange(0,288)
		diff = 3600 * random.randrange(1,5) + 300 * random.randrange(1,12)
		time2 = time1 + diff

		hours = int(floor(time1/3600))
		minutes = int((time1 - hours*3600)/60)
		if hours > 23:
			hours = hours - 24
		elif hours<0:
			hours = hours + 24
		if hours < 10:
			hours = "0" + str(hours)
		if minutes < 10:
			minutes = "0" + str(minutes)
		time1 = str(hours) + ":" + str(minutes)

		hours = int(floor(time2/3600))
		minutes = int((time2 - hours*3600)/60)
		if hours > 23:
			hours = hours - 24
		elif hours<0:
			hours = hours + 24
		if hours < 10:
			hours = "0" + str(hours)
		if minutes < 10:
			minutes = "0" + str(minutes)
		time2 = str(hours) + ":" + str(minutes)

		hours = int(floor(diff/3600))
		minutes = int((diff - hours*3600)/60)
		if hours==1:
			hora = " hour "
		else:
			hora = " hours "
		if minutes==0:
			diff = str(hours) + hora
		else:
			diff = str(hours) + hora + str(minutes) + " minutes "
#write question
		tempquestions.write(explanation + str(diff) + "after " + time1 + "?")

		tempquestions.write("\n")
#write answer
		tempquestions.write(time2)



def timesubtract2451(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "What time was it "
		else:
			explanation = ""
		time1 = 300 * random.randrange(0,288)
		diff = 300 * random.randrange(3,12)
		time2 = time1 - diff

		hours = int(floor(time1/3600))
		minutes = int((time1 - hours*3600)/60)
		if hours > 23:
			hours = hours - 24
		elif hours<0:
			hours = hours + 24
		if hours < 10:
			hours = "0" + str(hours)
		if minutes < 10:
			minutes = "0" + str(minutes)
		time1 = str(hours) + ":" + str(minutes)

		hours = int(floor(time2/3600))
		minutes = int((time2 - hours*3600)/60)
		if hours > 23:
			hours = hours - 24
		elif hours<0:
			hours = hours + 24
		if hours < 10:
			hours = "0" + str(hours)
		if minutes < 10:
			minutes = "0" + str(minutes)
		time2 = str(hours) + ":" + str(minutes)

		diff = int(diff / 60)
#write question
		tempquestions.write(explanation + str(diff) + " minutes before " + time1 + "?")

		tempquestions.write("\n")
#write answer
		tempquestions.write(time2)



def timesubtract2452(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "What time was it "
		else:
			explanation = ""
		time1 = 300 * random.randrange(0,288)
		diff = 3600 * random.randrange(1,5) + 300 * random.randrange(1,12)
		time2 = time1 - diff

		hours = int(floor(time1/3600))
		minutes = int((time1 - hours*3600)/60)
		if hours > 23:
			hours = hours - 24
		elif hours<0:
			hours = hours + 24
		if hours < 10:
			hours = "0" + str(hours)
		if minutes < 10:
			minutes = "0" + str(minutes)
		time1 = str(hours) + ":" + str(minutes)

		hours = int(floor(time2/3600))
		minutes = int((time2 - hours*3600)/60)
		if hours > 23:
			hours = hours - 24
		elif hours<0:
			hours = hours + 24
		if hours < 10:
			hours = "0" + str(hours)
		if minutes < 10:
			minutes = "0" + str(minutes)
		time2 = str(hours) + ":" + str(minutes)

		hours = int(floor(diff/3600))
		minutes = int((diff - hours*3600)/60)
		if hours==1:
			hora = " hour "
		else:
			hora = " hours "
		if minutes==0:
			diff = str(hours) + hora
		else:
			diff = str(hours) + hora + str(minutes) + " minutes "
#write question
		tempquestions.write(explanation + str(diff) + "before " + time1 + "?")

		tempquestions.write("\n")
#write answer
		tempquestions.write(time2)


def timeadd1251(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "What time will it be "
		else:
			explanation = ""
		time1 = 300 * random.randrange(0,288)
		diff = 300 * random.randrange(3,12)
		time2 = time1 + diff

		hours = int(floor(time1/3600))
		minutes = int((time1 - hours*3600)/60)
		if hours < 0:
			hours = hours + 24
		if hours > 23:
			hours = hours - 24
		if hours==0:
			suffix = " am"
			hours = 12
		elif hours==12:
			suffix = " pm"
		elif hours > 12:
			hours = hours - 12
			suffix = " pm"
		else:
			suffix = " am"
		if minutes < 10:
			minutes = "0" + str(minutes)
		time1 = str(hours) + ":" + str(minutes) + suffix

		hours = int(floor(time2/3600))
		minutes = int((time2 - hours*3600)/60)
		if hours < 0:
			hours = hours + 24
		if hours > 23:
			hours = hours - 24
		if hours==0:
			suffix = " am"
			hours = 12
		elif hours==12:
			suffix = " pm"
		elif hours > 12:
			hours = hours - 12
			suffix = " pm"
		else:
			suffix = " am"
		if minutes < 10:
			minutes = "0" + str(minutes)
		time2 = str(hours) + ":" + str(minutes) + suffix

		diff = int(diff / 60)
#write question
		tempquestions.write(explanation + str(diff) + " minutes after " + time1 + "?")

		tempquestions.write("\n")
#write answer
		tempquestions.write(time2)


def timeadd1252(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "What time will it be "
		else:
			explanation = ""
		time1 = 300 * random.randrange(0,288)
		diff = 3600 * random.randrange(1,5) + 300 * random.randrange(1,12)
		time2 = time1 + diff

		hours = int(floor(time1/3600))
		minutes = int((time1 - hours*3600)/60)
		if hours < 0:
			hours = hours + 24
		if hours > 23:
			hours = hours - 24
		if hours==0:
			suffix = " am"
			hours = 12
		elif hours==12:
			suffix = " pm"
		elif hours > 12:
			hours = hours - 12
			suffix = " pm"
		else:
			suffix = " am"
		if minutes < 10:
			minutes = "0" + str(minutes)
		time1 = str(hours) + ":" + str(minutes) + suffix

		hours = int(floor(time2/3600))
		minutes = int((time2 - hours*3600)/60)
		if hours < 0:
			hours = hours + 24
		if hours > 23:
			hours = hours - 24
		if hours==0:
			suffix = " am"
			hours = 12
		elif hours==12:
			suffix = " pm"
		elif hours > 12:
			hours = hours - 12
			suffix = " pm"
		else:
			suffix = " am"
		if minutes < 10:
			minutes = "0" + str(minutes)
		time2 = str(hours) + ":" + str(minutes) + suffix

		hours = int(floor(diff/3600))
		minutes = int((diff - hours*3600)/60)
		if hours==1:
			hora = " hour "
		else:
			hora = " hours "
		if minutes==0:
			diff = str(hours) + hora
		else:
			diff = str(hours) + hora + str(minutes) + " minutes "
#write question
		tempquestions.write(explanation + str(diff) + "after " + time1 + "?")

		tempquestions.write("\n")
#write answer
		tempquestions.write(time2)


def timesubtract1251(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "What time was it "
		else:
			explanation = ""
		time1 = 300 * random.randrange(0,288)
		diff = 300 * random.randrange(3,12)
		time2 = time1 - diff

		hours = int(floor(time1/3600))
		minutes = int((time1 - hours*3600)/60)
		if hours < 0:
			hours = hours + 24
		if hours > 23:
			hours = hours - 24
		if hours==0:
			suffix = " am"
			hours = 12
		elif hours==12:
			suffix = " pm"
		elif hours > 12:
			hours = hours - 12
			suffix = " pm"
		else:
			suffix = " am"
		if minutes < 10:
			minutes = "0" + str(minutes)
		time1 = str(hours) + ":" + str(minutes) + suffix

		hours = int(floor(time2/3600))
		minutes = int((time2 - hours*3600)/60)
		if hours < 0:
			hours = hours + 24
		if hours > 23:
			hours = hours - 24
		if hours==0:
			suffix = " am"
			hours = 12
		elif hours==12:
			suffix = " pm"
		elif hours > 12:
			hours = hours - 12
			suffix = " pm"
		else:
			suffix = " am"
		if minutes < 10:
			minutes = "0" + str(minutes)
		time2 = str(hours) + ":" + str(minutes) + suffix

		diff = int(diff / 60)
#write question
		tempquestions.write(explanation + str(diff) + " minutes before " + time1 + "?")

		tempquestions.write("\n")
#write answer
		tempquestions.write(time2)


def timesubtract1252(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "What time was it "
		else:
			explanation = ""
		time1 = 300 * random.randrange(0,288)
		diff = 3600 * random.randrange(1,5) + 300 * random.randrange(1,12)
		time2 = time1 - diff

		hours = int(floor(time1/3600))
		minutes = int((time1 - hours*3600)/60)
		if hours < 0:
			hours = hours + 24
		if hours > 23:
			hours = hours - 24
		if hours==0:
			suffix = " am"
			hours = 12
		elif hours==12:
			suffix = " pm"
		elif hours > 12:
			hours = hours - 12
			suffix = " pm"
		else:
			suffix = " am"
		if minutes < 10:
			minutes = "0" + str(minutes)
		time1 = str(hours) + ":" + str(minutes) + suffix

		hours = int(floor(time2/3600))
		minutes = int((time2 - hours*3600)/60)
		if hours < 0:
			hours = hours + 24
		if hours > 23:
			hours = hours - 24
		if hours==0:
			suffix = " am"
			hours = 12
		elif hours==12:
			suffix = " pm"
		elif hours > 12:
			hours = hours - 12
			suffix = " pm"
		else:
			suffix = " am"
		if minutes < 10:
			minutes = "0" + str(minutes)
		time2 = str(hours) + ":" + str(minutes) + suffix

		hours = int(floor(diff/3600))
		minutes = int((diff - hours*3600)/60)
		if hours==1:
			hora = " hour "
		else:
			hora = " hours "
		if minutes==0:
			diff = str(hours) + hora
		else:
			diff = str(hours) + hora + str(minutes) + " minutes "
#write question
		tempquestions.write(explanation + str(diff) + "before " + time1 + "?")

		tempquestions.write("\n")
#write answer
		tempquestions.write(time2)



def timediff(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "What is the difference in time between "
		else:
			explanation = ""
		time1 = 300 * random.randrange(0,288)
		diff = 3600 * random.randrange(1,5) + 300 * random.randrange(1,12)
		time2 = time1 - diff

		hours = int(floor(time1/3600))
		minutes = int((time1 - hours*3600)/60)
		if hours < 0:
			hours = hours + 24
		if hours > 23:
			hours = hours - 24
		if hours==0:
			suffix = " am"
			hours = 12
		elif hours==12:
			suffix = " pm"
		elif hours > 12:
			hours = hours - 12
			suffix = " pm"
		else:
			suffix = " am"
		if minutes < 10:
			minutes = "0" + str(minutes)
		time1 = str(hours) + ":" + str(minutes) + suffix

		hours = int(floor(time2/3600))
		minutes = int((time2 - hours*3600)/60)
		if hours < 0:
			hours = hours + 24
		if hours > 23:
			hours = hours - 24
		if hours==0:
			suffix = " am"
			hours = 12
		elif hours==12:
			suffix = " pm"
		elif hours > 12:
			hours = hours - 12
			suffix = " pm"
		else:
			suffix = " am"
		if minutes < 10:
			minutes = "0" + str(minutes)
		time2 = str(hours) + ":" + str(minutes) + suffix

		hours = int(floor(diff/3600))
		minutes = int((diff - hours*3600)/60)
		if hours==1:
			hora = " hour "
		else:
			hora = " hours "
		if minutes==0:
			diff = str(hours) + hora
		else:
			diff = str(hours) + hora + str(minutes) + " minutes "
#write question
		tempquestions.write(explanation + time2 + " and " + time1 + "?")

		tempquestions.write("\n")
#write answer
		tempquestions.write("\\mbox{" + diff + "}")



def timetodecimal(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Convert "
			explanation2 = " to a number of hours"
		else:
			explanation1 = ""
			explanation2 = ""
		hours = random.randrange(1,4)
		mins = [6,12,18,24,30,36,42,48,54,20,40,10,50,15,45]
		decs = [".1",".2",".3",".4",".5",".6",".7",".8",".9",".\\.{3}",".\\.{6}",".1\\.{6}",".8\\.{3}",".25",".75"]
		fracs = ["$\\dfrac{1}{10}$","$\\dfrac{1}{5}$","$\\dfrac{3}{10}$","$\\dfrac{2}{5}$","$\\dfrac{1}{2}$","$\\dfrac{3}{5}$","$\\dfrac{7}{10}$","$\\dfrac{4}{5}$","$\\dfrac{9}{10}$","$\\dfrac{1}{3}$","$\\dfrac{2}{3}$","$\\dfrac{1}{6}$","$\\dfrac{5}{6}$","$\\dfrac{1}{4}$","$\\dfrac{3}{4}$",]
		choice = random.randrange(0,len(mins))
		mins = mins[choice]
		dec = decs[choice]
		frac = fracs[choice]
		question = str(hours) + " hours " + str(mins) + " minutes"
		answer = str(hours) + dec + " or " + str(hours) + frac
		question = explanation1 + question + explanation2
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def timediffdecimal(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "What is the difference in time between "
			explanation2 = " in hours?"
		else:
			explanation1 = ""
			explanation2 = ""
		hours = random.randrange(1,4)
		mins = [6,12,18,24,30,36,42,48,54,20,40,10,50,15,45]
		decs = [".1",".2",".3",".4",".5",".6",".7",".8",".9",".\\.{3}",".\\.{6}",".1\\.{6}",".8\\.{3}",".25",".75"]
		fracs = ["$\\dfrac{1}{10}$","$\\dfrac{1}{5}$","$\\dfrac{3}{10}$","$\\dfrac{2}{5}$","$\\dfrac{1}{2}$","$\\dfrac{3}{5}$","$\\dfrac{7}{10}$","$\\dfrac{4}{5}$","$\\dfrac{9}{10}$","$\\dfrac{1}{3}$","$\\dfrac{2}{3}$","$\\dfrac{1}{6}$","$\\dfrac{5}{6}$","$\\dfrac{1}{4}$","$\\dfrac{3}{4}$",]
		choice = random.randrange(0,len(mins))
		mins = mins[choice]
		dec = decs[choice]
		frac = fracs[choice]
		answer = str(hours) + dec + " or " + str(hours) + frac
		time1 = 300 * random.randrange(0,288)
		diff = hours*3600 + mins*60
		time2 = time1 - diff

		hours = int(floor(time1/3600))
		minutes = int((time1 - hours*3600)/60)
		if hours < 0:
			hours = hours + 24
		if hours > 23:
			hours = hours - 24
		if hours==0:
			suffix = " am"
			hours = 12
		elif hours==12:
			suffix = " pm"
		elif hours > 12:
			hours = hours - 12
			suffix = " pm"
		else:
			suffix = " am"
		if minutes < 10:
			minutes = "0" + str(minutes)
		time1 = str(hours) + ":" + str(minutes) + suffix

		hours = int(floor(time2/3600))
		minutes = int((time2 - hours*3600)/60)
		if hours < 0:
			hours = hours + 24
		if hours > 23:
			hours = hours - 24
		if hours==0:
			suffix = " am"
			hours = 12
		elif hours==12:
			suffix = " pm"
		elif hours > 12:
			hours = hours - 12
			suffix = " pm"
		else:
			suffix = " am"
		if minutes < 10:
			minutes = "0" + str(minutes)
		time2 = str(hours) + ":" + str(minutes) + suffix

		hours = int(floor(diff/3600))
		minutes = int((diff - hours*3600)/60)
		if hours==1:
			hora = " hour "
		else:
			hora = " hours "
		if minutes==0:
			diff = str(hours) + hora
		else:
			diff = str(hours) + hora + str(minutes) + " minutes "
#write question
		tempquestions.write(explanation1 + time2 + " and " + time1 + explanation2)

		tempquestions.write("\n")
#write answer
		tempquestions.write("\\mbox{" + answer + " hours}")


def sdtspeed3(n,explanationn):
	import random
	from math import floor
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		hours = random.randrange(1,4)
		mins = [6,12,18,24,30,36,42,48,54,20,40,10,50,15,45]
		fracs = [Fraction(1,10),Fraction(2,10),Fraction(3,10),Fraction(4,10),Fraction(5,10),Fraction(6,10),Fraction(7,10),Fraction(8,10),Fraction(9,10),Fraction(1,3),Fraction(2,3),Fraction(1,6),Fraction(2,6),Fraction(1,4),Fraction(3,4)]
		choice = random.randrange(0,len(mins))
		mins = mins[choice]
		frac = fracs[choice]
		b = frac.numerator
		c = frac.denominator
		a = hours
		distance = (a*c + b) * random.randrange(5,31)
		time = a + frac
		speed = distance/time
		answer = str(speed) + "km/h"
		time1 = 300 * random.randrange(0,288)
		diff = hours*3600 + mins*60
		time2 = time1 - diff

		hours = int(floor(time1/3600))
		minutes = int((time1 - hours*3600)/60)
		if hours < 0:
			hours = hours + 24
		if hours > 23:
			hours = hours - 24
		if hours==0:
			suffix = " am"
			hours = 12
		elif hours==12:
			suffix = " pm"
		elif hours > 12:
			hours = hours - 12
			suffix = " pm"
		else:
			suffix = " am"
		if minutes < 10:
			minutes = "0" + str(minutes)
		time1 = str(hours) + ":" + str(minutes) + suffix

		hours = int(floor(time2/3600))
		minutes = int((time2 - hours*3600)/60)
		if hours < 0:
			hours = hours + 24
		if hours > 23:
			hours = hours - 24
		if hours==0:
			suffix = " am"
			hours = 12
		elif hours==12:
			suffix = " pm"
		elif hours > 12:
			hours = hours - 12
			suffix = " pm"
		else:
			suffix = " am"
		if minutes < 10:
			minutes = "0" + str(minutes)
		time2 = str(hours) + ":" + str(minutes) + suffix

		hours = int(floor(diff/3600))
		minutes = int((diff - hours*3600)/60)
		if hours==1:
			hora = " hour "
		else:
			hora = " hours "
		if minutes==0:
			diff = str(hours) + hora
		else:
			diff = str(hours) + hora + str(minutes) + " minutes "
		question = "A cat goes for a " + str(distance) + "km walk at " + time2 + " and arrives home at " + time1 + ". Find the cat's average speed for this journey."
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
