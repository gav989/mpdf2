#!/usr/bin/env python3
#sdt.py

def journey(n,explanationn):
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
		speeds = [30,40,50,60]
		speed = random.choice(speeds)
		time = random.randrange(6,21)/4
		distance = speed * time
		time2 = time1 - time*3600

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
		if distance%1==0:
			distance = int(distance)
#write question
		tempquestions.write("To travel " + str(distance) + " miles at " + str(speed) + "mph and arrive at " + time1 + ", what time do I need to leave?")

		tempquestions.write("\n")
#write answer
		tempquestions.write(time2)



def sdtspeed(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the average speed of someone travelling "
		else:
			explanation = ""
		duns = ["m","km"]
		tuns = ["seconds","hours"]
		suns = ["m/s","km/h"]
		dec = random.randrange(0,len(suns))
		sun = suns[dec]
		dun = duns[dec]
		tun = tuns[dec]
		s = random.randrange(1,21)*5
		t = random.randrange(2,13)
		d = s * t
		question = str(d) + dun + " in " + str(t) +  " " + tun + "?"
		answer = str(s) + sun
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def sdtdistance(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "How far would you go if you travelled at "
		else:
			explanation = ""
		duns = ["m","km"]
		tuns = ["seconds","hours"]
		suns = ["m/s","km/h"]
		dec = random.randrange(0,len(suns))
		sun = suns[dec]
		dun = duns[dec]
		tun = tuns[dec]
		s = random.randrange(1,21)*5
		t = random.randrange(2,13)
		d = s * t
		question = str(s) + sun + " for " + str(t) + " " + tun + "?"
		answer = str(d) + dun
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def sdttime(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "How long would it take to travel "
		else:
			explanation = ""
		duns = ["m","km"]
		tuns = ["seconds","hours"]
		suns = ["m/s","km/h"]
		dec = random.randrange(0,len(suns))
		sun = suns[dec]
		dun = duns[dec]
		tun = tuns[dec]
		s = random.randrange(1,21)*5
		t = random.randrange(2,13)
		d = s * t
		question = str(d) + dun + " at " + str(s) + sun + "?"
		answer = str(t) + " " + tun
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def sdtspeed2(n,explanationn):
	import random
	from math import floor
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the average speed of someone travelling "
		else:
			explanation = ""
		dun = "km"
		sun = "km/h"
		hours = random.randrange(0,4)
		minutes = [12,15,20,24,30,36,40,45,48]
		minutes = random.choice(minutes)
		if hours==0:
			t = str(minutes) + " minutes"
		elif hours==1:
			t = str(hours) + " hour " + str(minutes) + " minutes"
		else:
			t = str(hours) + " hours " + str(minutes) + " minutes"
		if minutes==20 or minutes==40:
			s = random.randrange(2,35) * 3
		elif minutes==15 or minutes==45:
			s = random.randrange(1,16)*4
		elif minutes==30:
			s = random.randrange(2,53)*2
		else:
			s = random.randrange(1,12)*5
		d = s * Fraction(60*hours + minutes,60)
		question = str(d) + dun + " in " + t + "?"
		answer = str(s) + sun
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def sdtdistance2(n,explanationn):
	import random
	from math import floor
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "How far would you go if you travelled at "
		else:
			explanation = ""
		dun = "km"
		sun = "km/h"
		hours = random.randrange(0,4)
		minutes = [12,15,20,24,30,36,40,45,48]
		minutes = random.choice(minutes)
		if hours==0:
			t = str(minutes) + " minutes"
		elif hours==1:
			t = str(hours) + " hour " + str(minutes) + " minutes"
		else:
			t = str(hours) + " hours " + str(minutes) + " minutes"
		if minutes==20 or minutes==40:
			s = random.randrange(2,35) * 3
		elif minutes==15 or minutes==45:
			s = random.randrange(1,16)*4
		elif minutes==30:
			s = random.randrange(2,53)*2
		else:
			s = random.randrange(1,12)*5
		d = s * Fraction(60*hours + minutes,60)
		question = str(s) + sun + " for " + t + "?"
		answer = str(d) + dun
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def sdttime2(n,explanationn):
	import random
	from math import floor
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "How long would it take to travel "
		else:
			explanation = ""
		dun = "km"
		sun = "km/h"
		hours = random.randrange(0,4)
		minutes = [12,15,20,24,30,36,40,45,48]
		minutes = random.choice(minutes)
		if hours==0:
			t = str(minutes) + " minutes"
		elif hours==1:
			t = str(hours) + " hour " + str(minutes) + " minutes"
		else:
			t = str(hours) + " hours " + str(minutes) + " minutes"
		if minutes==20 or minutes==40:
			s = random.randrange(2,35) * 3
		elif minutes==15 or minutes==45:
			s = random.randrange(1,16)*4
		elif minutes==30:
			s = random.randrange(2,53)*2
		else:
			s = random.randrange(1,12)*5
		d = s * Fraction(60*hours + minutes,60)
		question = str(d) + dun + " at " + str(s) + " " + sun + "?"
		answer = t
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
