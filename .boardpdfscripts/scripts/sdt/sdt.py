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
