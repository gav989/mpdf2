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
