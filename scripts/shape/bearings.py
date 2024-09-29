#bearings.py

def bearingsdistance5(n,explanationn):
	import random
	from math import radians,degrees,sin,cos,tan,sqrt
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		ds = [4,4.5,5,5.5,6,6.5,7,7.5]
		d1 = random.choice(ds)
		ds.remove(d1)
		d2 = random.choice(ds)
		if d1%1==0:
			d1 = int(d1)
		if d2%1==0:
			d2 = int(d1)
		dec = random.randrange(0,4)
		if dec==1:
			b1 = random.randrange(3,16)*5
			b2 = random.randrange(21,34)*5
		elif dec==2:
			b2 = random.randrange(3,16)*5
			b1 = random.randrange(21,34)*5
		elif dec==3:
			b1 = random.randrange(57,70)*5
			b2 = random.randrange(39,52)*5
		else:
			b2 = random.randrange(57,70)*5
			b1 = random.randrange(39,52)*5

		A = abs(180 - b1 + b2)
		d3 = d1**2 + d2**2 - 2*d1*d2*cos(radians(A))
		d3 = sqrt(d3)
		if b1<10:
			b1 = "00" + str(b1)
		elif b1<100:
			b1 = "0" + str(b1)
		else:
			b1 = str(b1)
		if b2<10:
			b2 = "00" + str(b2)
		elif b2<100:
			b2 = "0" + str(b2)
		else:
			b2 = str(b2)
		question = "A cat travels " + str(d1) + "m on a bearing of " + b1 + "\\mydeg and then " + str(d2) + "m on a bearing of " + b2 + "\\mydeg, how far away is the cat from its original location?"
		d3 = rounddp(d3,2)
		if d3%1==0:
			d3 = int(d3)
		answer = str(d3) + "m" 
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def bearingsdistance(n,explanationn):
	import random
	from math import radians,degrees,sin,cos,tan,sqrt
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		ds = [2,3,4,5,6,7]
		d1 = random.choice(ds)
		ds.remove(d1)
		d2 = random.choice(ds)
		b1 = 180 + random.randrange(15,166) * (-1)**random.randrange(1,3)
		b2 = b1 + random.randrange(45,346) * (-1)**random.randrange(1,3)
		if b2>359:
			b2 = b2 - 360
		elif b2<0:
			b2 = b2 + 360
		A = abs(180 - b1 + b2)
		d3 = d1**2 + d2**2 - 2*d1*d2*cos(radians(A))
		d3 = sqrt(d3)
		if b1<10:
			b1 = "00" + str(b1)
		elif b1<100:
			b1 = "0" + str(b1)
		else:
			b1 = str(b1)
		if b2<10:
			b2 = "00" + str(b2)
		elif b2<100:
			b2 = "0" + str(b2)
		else:
			b2 = str(b2)
		question = "A cat travels " + str(d1) + "m on a bearing of " + b1 + "\\mydeg and then " + str(d2) + "m on a bearing of " + b2 + "\\mydeg, how far away is the cat from its original location?"
		d3 = rounddp(d3,2)
		if d3%1==0:
			d3 = int(d3)
		answer = str(d3) + "m" 
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def bearingsangle5(n,explanationn):
	import random
	from math import radians,degrees,sin,cos,tan,sqrt,asin,acos
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		ds = [4,4.5,5,5.5,6,6.5,7,7.5]
		d1 = random.choice(ds)
		ds.remove(d1)
		d2 = random.choice(ds)
		if d1%1==0:
			d1 = int(d1)
		if d2%1==0:
			d2 = int(d1)
		dec = random.randrange(0,4)
		if dec==1:
			b1 = random.randrange(3,16)*5
			b2 = random.randrange(21,34)*5
		elif dec==2:
			b2 = random.randrange(3,16)*5
			b1 = random.randrange(21,34)*5
		elif dec==3:
			b1 = random.randrange(57,70)*5
			b2 = random.randrange(39,52)*5
		else:
			b2 = random.randrange(57,70)*5
			b1 = random.randrange(39,52)*5
		A = abs(180 - b1 + b2)
		d3 = d1**2 + d2**2 - 2*d1*d2*cos(radians(A))
		d3 = sqrt(d3)
		if b1<10:
			b1 = "00" + str(b1)
		elif b1<100:
			b1 = "0" + str(b1)
		else:
			b1 = str(b1)
		C = degrees(acos((d2**2 + d3**2 - d1**2)/(2*d2*d3)))
		if dec==1:
			b3 = 180 + b2 - C
		elif dec==2:
			b3 = 180 + b2 + C
		elif dec==3:
			b3 = b2 - 180 + C
		else:
			b3 = b2 - 180 - C
			
		if b2<10:
			b2 = "00" + str(b2)
		elif b2<100:
			b2 = "0" + str(b2)
		else:
			b2 = str(b2)
		question = "A cat travels " + str(d1) + "m on a bearing of " + b1 + "\\mydeg and then " + str(d2) + "m on a bearing of " + b2 + "\\mydeg, on what bearing should it travel to return to the start?"
		b3 = rounddp(b3,2)
		if b3%1==0:
			b3 = int(b3)
		if b3<10:
			b3 = "00" + str(b3)
		elif b3<100:
			b3 = "0" + str(b3)
		else:
			b3 = str(b3)
		answer = str(b3) + "\\mydeg" 
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def coordinatebearings(n,explanationn):
	import random
	from math import radians,degrees,atan
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		zones = [1,2,3,4,6,7,8,9]
		z1 = random.choice(zones)
		if z1==1:
			z2s = [3,6,9,8,7]
		elif z1==2:
			z2s = [7,8,9]
		elif z1==3:
			z2s = [1,4,7,8,9]
		elif z1==4:
			z2s = [3,6,9]
		elif z1==6:
			z2s = [1,4,7]
		elif z1==7:
			z2s = [1,2,3,6,9]
		elif z1==8:
			z2s = [1,2,3]
		else:
			z2s = [7,4,1,2,3]
		z2 = random.choice(z2s)
		zone = z1
		if zone==1 or zone==4 or zone==7:
			xs = list(range(-8,-2))
		elif zone==2 or zone==8:
			xs = list(range(-3,4))
		else:
			xs = list(range(3,9))
		if zone==1 or zone==2 or zone==3:
			ys = list(range(3,9))
		elif zone==4 or zone==6:
			ys = list(range(-3,4))
		else:
			ys = list(range(-8,-2))
		x1 = random.choice(xs)
		y1 = random.choice(ys)
		zone = z2
		if zone==1 or zone==4 or zone==7:
			xs = list(range(-8,-2))
		elif zone==2 or zone==8:
			xs = list(range(-3,4))
		else:
			xs = list(range(3,9))
		if zone==1 or zone==2 or zone==3:
			ys = list(range(3,9))
		elif zone==4 or zone==6:
			ys = list(range(-3,4))
		else:
			ys = list(range(-8,-2))
		x2 = random.choice(xs)
		y2 = random.choice(ys)
		xdiff = abs(x1 - x2)
		ydiff = abs(y1 - y2)
		if x1==x2:
			if y1>y2:
				answer = 180
			else:
				answer = 0
		elif y1==y2:
			if x1>x2:
				answer = 270
			else:
				answer = 90
		elif x1<x2 and y1<y2:
			answer = rounddp(degrees(atan(xdiff/ydiff)),2)
		elif x1<x2 and y1>y2:
			answer = rounddp(degrees(atan(ydiff/xdiff))+90,2)
		elif x1>x2 and y1>y2:
			answer = rounddp(degrees(atan(xdiff/ydiff))+180,2)
		elif x1>x2 and y1<y2:
			answer = rounddp(degrees(atan(ydiff/xdiff))+270,2)
		if answer%1==0:
			answer = int(answer)
		if answer<10:
			answer = "00" + str(answer)
		elif answer<100:
			answer = "0" + str(answer)
		else:
			answer = str(answer)
		answer = str(answer) + "\\mydeg" 
		if random.randrange(0,2)==1:
			A = "(" + str(x1) + " , " + str(y1) + ")"
			B = "(" + str(x2) + " , " + str(y2) + ")"
			question = "A = " + A + " and B = " + B + ". Calculate the bearing of B from A."
		else:
			B = "(" + str(x1) + " , " + str(y1) + ")"
			A = "(" + str(x2) + " , " + str(y2) + ")"
			question = "A = " + A + " and B = " + B + ". Calculate the bearing of A from B."
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
