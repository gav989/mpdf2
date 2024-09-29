#standardform.py

def sfconvertpos1(n,explanationn):
	import random
	from utilities.sf import sftonum,sftosf
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Write "
			explanation2 = " as a number"
		else:
			explanation1 = ""
			explanation2 = ""
		t = random.randrange(0,2)
		if t==1:
			a = rounddp((random.randrange(1,10)*10 + random.randrange(1,10))/10,1)
		else:
			a = rounddp((random.randrange(1,10)*100 + random.randrange(0,10)*10 + random.randrange(1,10))/100,2)
		i = random.randrange(3,9)
		question = sftosf(str(a),i)
		answer = sftonum(str(a),i)
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def sfconvertpos2(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from utilities.sf import sftonum,sftosf
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation1 = "Write "
			explanation2 = " in standard form"
		else:
			explanation1 = ""
			explanation2 = ""
		t = random.randrange(0,2)
		if t==1:
			a = rounddp((random.randrange(1,10)*10 + random.randrange(1,10))/10,1)
		else:
			a = rounddp((random.randrange(1,10)*100 + random.randrange(0,10)*10 + random.randrange(1,10))/100,2)
		i = random.randrange(3,9)
		answer = sftosf(str(a),i)
		question = sftonum(str(a),i)
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def sfconvertneg1(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from utilities.sf import sftonum,sftosf
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation1 = "Write "
			explanation2 = " as a number"
		else:
			explanation1 = ""
			explanation2 = ""
		t = random.randrange(0,2)
		if t==1:
			a = rounddp((random.randrange(1,10)*10 + random.randrange(1,10))/10,1)
		else:
			a = rounddp((random.randrange(1,10)*100 + random.randrange(0,10)*10 + random.randrange(1,10))/100,2)
		i = random.randrange(-8,-2)
		question = sftosf(str(a),i)
		answer = sftonum(str(a),i)
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def sfconvertneg2(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from utilities.sf import sftonum,sftosf
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation1 = "Write "
			explanation2 = " in standard form"
		else:
			explanation1 = ""
			explanation2 = ""
		t = random.randrange(0,2)
		if t==1:
			a = rounddp((random.randrange(1,10)*10 + random.randrange(1,10))/10,1)
		else:
			a = rounddp((random.randrange(1,10)*100 + random.randrange(0,10)*10 + random.randrange(1,10))/100,2)
		i = random.randrange(-8,-2)
		answer = sftosf(str(a),i)
		question = sftonum(str(a),i)
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def sfconvert1(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from utilities.sf import sftonum,sftosf
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation1 = "Write "
			explanation2 = " as a number"
		else:
			explanation1 = ""
			explanation2 = ""
		pos = random.randrange(0,2)
		t = random.randrange(0,2)
		if t==1:
			a = rounddp((random.randrange(1,10)*10 + random.randrange(1,10))/10,1)
		else:
			a = rounddp((random.randrange(1,10)*100 + random.randrange(0,10)*10 + random.randrange(1,10))/100,2)
		if pos==1:
			i = random.randrange(3,9)
		else:
			i = random.randrange(-8,-2)
		question = sftosf(str(a),i)
		answer = sftonum(str(a),i)
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def sfconvert2(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from utilities.sf import sftonum,sftosf
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation1 = "Write "
			explanation2 = " in standard form"
		else:
			explanation1 = ""
			explanation2 = ""
		pos = random.randrange(0,2)
		t = random.randrange(0,2)
		if t==1:
			a = rounddp((random.randrange(1,10)*10 + random.randrange(1,10))/10,1)
		else:
			a = rounddp((random.randrange(1,10)*100 + random.randrange(0,10)*10 + random.randrange(1,10))/100,2)
		if pos==1:
			i = random.randrange(3,9)
		else:
			i = random.randrange(-8,-2)
		answer = sftosf(str(a),i)
		question = sftonum(str(a),i)
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def sfconvert3(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from utilities.sf import sftonum,sftosf
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation1 = "Write "
			explanation2 = " in standard form"
		else:
			explanation1 = ""
			explanation2 = ""
		pos = random.randrange(0,2)
		t = random.randrange(0,2)
		if t==1:
			a = rounddp((random.randrange(1,10)*10 + random.randrange(1,10))/10,1)
		else:
			a = rounddp((random.randrange(1,10)*100 + random.randrange(0,10)*10 + random.randrange(1,10))/100,2)
		if pos==1:
			i = random.randrange(3,9)
		else:
			i = random.randrange(-8,-2)
		a = a * 10**(random.randrange(1,4)*(-1)**random.randrange(0,2))
		if a%1==0:
			a = int(a)
		else:
			a = rounddp(a,5)
		answer = sftosf(str(a),i)
		question = "$" + str(a) + " \\times 10^{" + str(i) + "}$"
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def sfconvert3pos(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from utilities.sf import sftonum,sftosf
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation1 = "Write "
			explanation2 = " in standard form"
		else:
			explanation1 = ""
			explanation2 = ""
		pos = random.randrange(0,2)
		t = random.randrange(0,2)
		if t==1:
			a = rounddp((random.randrange(1,10)*10 + random.randrange(1,10))/10,1)
		else:
			a = rounddp((random.randrange(1,10)*100 + random.randrange(0,10)*10 + random.randrange(1,10))/100,2)
		if pos==1:
			i = random.randrange(3,9)
		else:
			i = random.randrange(-8,-2)
		a = a * 10**random.randrange(1,4)
		if a%1==0:
			a = int(a)
		else:
			a = rounddp(a,5)
		answer = sftosf(str(a),i)
		question = "$" + str(a) + " \\times 10^{" + str(i) + "}$"
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def sfconvert3neg(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from utilities.sf import sftonum,sftosf
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation1 = "Write "
			explanation2 = " in standard form"
		else:
			explanation1 = ""
			explanation2 = ""
		pos = random.randrange(0,2)
		t = random.randrange(0,2)
		if t==1:
			a = rounddp((random.randrange(1,10)*10 + random.randrange(1,10))/10,1)
		else:
			a = rounddp((random.randrange(1,10)*100 + random.randrange(0,10)*10 + random.randrange(1,10))/100,2)
		if pos==1:
			i = random.randrange(3,9)
		else:
			i = random.randrange(-8,-2)
		a = a * 10**(random.randrange(1,4)*(-1))
		if a%1==0:
			a = int(a)
		else:
			a = rounddp(a,5)
		answer = sftosf(str(a),i)
		question = "$" + str(a) + " \\times 10^{" + str(i) + "}$"
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def sfmultiplyint(n,explanationn):
	import random
	from utilities.sf import sftonum,sftosf
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Calculate "
			explanation2 = ", giving your answer in standard form"
		else:
			explanation1 = ""
			explanation2 = ""
		num1 = random.randrange(2,10)
		num2 = rounddp(random.randrange(1,10) + random.randrange(1,10)/10,1)
		num3 = rounddp(num1 * num2,1)
		ind2 = random.randrange(2,10)
		question = sftosf(str(num2),ind2) + " $\\times$ " + str(num1)
		answer = sftosf(str(num3),ind2)
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def sfmultiply(n,explanationn):
	import random
	from utilities.sf import sftonum,sftosf
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Calculate "
			explanation2 = ", giving your answer in standard form"
		else:
			explanation1 = ""
			explanation2 = ""
		num1 = random.randrange(2,10)
		num2 = rounddp(random.randrange(1,10) + random.randrange(1,10)/10,1)
		num3 = rounddp(num1 * num2,1)
		if random.randrange(1,3)==2:
			temp = num1
			num1 = num2
			num2 = temp
		ind1 = random.randrange(2,10)*(-1)**random.randrange(1,3)
		ind2 = random.randrange(2,10)*(-1)**random.randrange(1,3)
		ind3 = ind1 + ind2
		question = sftosf(str(num1),ind1) + " $\\times$ " + sftosf(str(num2),ind2)
		answer = sftosf(str(num3),ind3)

#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
		

def sfmultiplypos(n,explanationn):
	import random
	from utilities.sf import sftonum,sftosf
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Calculate "
			explanation2 = ", giving your answer in standard form"
		else:
			explanation1 = ""
			explanation2 = ""
		num1 = random.randrange(2,10)
		num2 = rounddp(random.randrange(1,10) + random.randrange(1,10)/10,1)
		num3 = rounddp(num1 * num2,1)
		if random.randrange(1,3)==2:
			temp = num1
			num1 = num2
			num2 = temp
		ind1 = random.randrange(2,10)
		ind2 = random.randrange(2,10)
		ind3 = ind1 + ind2
		question = sftosf(str(num1),ind1) + " $\\times$ " + sftosf(str(num2),ind2)
		answer = sftosf(str(num3),ind3)

#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def sfmultiplyposint(n,explanationn):
	import random
	from utilities.sf import sftonum,sftosf
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Calculate "
			explanation2 = ", giving your answer in standard form"
		else:
			explanation1 = ""
			explanation2 = ""
		num1 = random.randrange(2,10)
		num2 = random.randrange(2,10)
		num3 = num1 * num2
		ind1 = random.randrange(2,10)
		ind2 = random.randrange(2,10)
		ind3 = ind1 + ind2
		question = sftosf(str(num1),ind1) + " $\\times$ " + sftosf(str(num2),ind2)
		answer = sftosf(str(num3),ind3)

#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

		
def sfdivide(n,explanationn):
	import random
	from utilities.sf import sftonum,sftosf
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Calculate "
			explanation2 = ", giving your answer in standard form"
		else:
			explanation1 = ""
			explanation2 = ""
		num2 = random.randrange(2,10)
		if num2==2 or num2==5 or num2==4:
			num1 = rounddp(random.randrange(0,10)/10 + random.randrange(1,10),1)
			num3 = rounddp(num1/num2,3)
		elif num2==6:
			num1 = rounddp(random.randrange(1,33) * 0.3,1)
			num3 = rounddp(num1/num2,3)
		else:
			num3 = random.randrange(2,10)
			num1 = num2 * num3
		ind1 = random.randrange(2,10)*(-1)**random.randrange(1,3)
		ind2 = random.randrange(2,10)*(-1)**random.randrange(1,3)
		ind3 = ind1-ind2
		question = "(" + sftosf(str(num1),ind1) + ") $\\div$ (" + sftosf(str(num2),ind2) + ")"
		answer = sftosf(str(num3),ind3)
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def sfdividepos(n,explanationn):
	import random
	from utilities.sf import sftonum,sftosf
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Calculate "
			explanation2 = ", giving your answer in standard form"
		else:
			explanation1 = ""
			explanation2 = ""
		num2 = random.randrange(2,10)
		if num2==2 or num2==5 or num2==4:
			num1 = rounddp(random.randrange(0,10)/10 + random.randrange(1,10),1)
			num3 = rounddp(num1/num2,3)
		elif num2==6:
			num1 = rounddp(random.randrange(1,33) * 0.3,1)
			num3 = rounddp(num1/num2,3)
		else:
			num3 = random.randrange(2,10)
			num1 = num2 * num3
		ind1 = random.randrange(2,10)
		inds = [2,3,4,5,6,7,8,9]
		inds.remove(ind1)
		ind2 = random.choice(inds)
		if ind1<ind2:
			temp = ind1
			ind1 = ind2
			ind2 = temp
		ind3 = ind1-ind2
		question = "(" + sftosf(str(num1),ind1) + ") $\\div$ (" + sftosf(str(num2),ind2) + ")"
		answer = sftosf(str(num3),ind3)
#write question
		tempquestions.write(explanation1 + question + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def sfadd(n,explanationn):
	import random
	from utilities.sf import sftonum,sftosf
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			num1 = rounddp(random.randrange(1,10) + random.randrange(1,10)/10,1)
		else:
			num1 = rounddp(random.randrange(1,10) + random.randrange(0,10)/10 + random.randrange(1,10)/100,2)
		if random.randrange(0,2)==1:
			num2 = rounddp(random.randrange(1,10) + random.randrange(1,10)/10,1)
		else:
			num2 = rounddp(random.randrange(1,10) + random.randrange(0,10)/10 + random.randrange(1,10)/100,2)
		signdec = (-1)**random.randrange(1,3)
		ind1 = random.randrange(2,6)*signdec
		ind2 = random.randrange(2,6)*signdec
		answer = rounddp(num1*10**ind1 + num2*10**ind2,7)
		if answer%1==0:
			answer = int(answer)
		question = sftosf(str(num1),ind1) + " + " + sftosf(str(num2),ind2)
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def sfaddpos(n,explanationn):
	import random
	from utilities.sf import sftonum,sftosf
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			num1 = rounddp(random.randrange(1,10) + random.randrange(1,10)/10,1)
		else:
			num1 = rounddp(random.randrange(1,10) + random.randrange(0,10)/10 + random.randrange(1,10)/100,2)
		if random.randrange(0,2)==1:
			num2 = rounddp(random.randrange(1,10) + random.randrange(1,10)/10,1)
		else:
			num2 = rounddp(random.randrange(1,10) + random.randrange(0,10)/10 + random.randrange(1,10)/100,2)
		signdec = 1
		ind1 = random.randrange(2,6)*signdec
		ind2 = random.randrange(2,6)*signdec
		answer = rounddp(num1*10**ind1 + num2*10**ind2,7)
		if answer%1==0:
			answer = int(answer)
		question = sftosf(str(num1),ind1) + " + " + sftosf(str(num2),ind2)
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def sfaddneg(n,explanationn): #THIS AND OTHERS NEED UPDATING WITH SF UTILITIES INSTEAD OF MANUAL CALCS
	import random
	from utilities.sf import sftonum,sftosf
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			num1 = rounddp(random.randrange(1,10) + random.randrange(1,10)/10,1)
		else:
			num1 = rounddp(random.randrange(1,10) + random.randrange(0,10)/10 + random.randrange(1,10)/100,2)
		if random.randrange(0,2)==1:
			num2 = rounddp(random.randrange(1,10) + random.randrange(1,10)/10,1)
		else:
			num2 = rounddp(random.randrange(1,10) + random.randrange(0,10)/10 + random.randrange(1,10)/100,2)
		signdec = -1
		ind1 = random.randrange(2,6)*signdec
		ind2 = random.randrange(2,6)*signdec
		answer = rounddp(num1*10**ind1 + num2*10**ind2,7)
		if answer%1==0:
			answer = int(answer)
		question = sftosf(str(num1),ind1) + " + " + sftosf(str(num2),ind2)
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))




def sfsubtract(n,explanationn):
	import random
	from utilities.sf import sftonum,sftosf
	from utilities.rounding import rounddp
	from math import ceil,log10
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			num1 = rounddp(random.randrange(1,10) + random.randrange(1,10)/10,1)
		else:
			num1 = rounddp(random.randrange(1,10) + random.randrange(0,10)/10 + random.randrange(1,10)/100,2)
		if random.randrange(0,2)==1:
			num2 = rounddp(random.randrange(1,10) + random.randrange(1,10)/10,1)
		else:
			num2 = rounddp(random.randrange(1,10) + random.randrange(0,10)/10 + random.randrange(1,10)/100,2)
		signdec = (-1)**random.randrange(1,3)
		ind1 = random.randrange(2,6)*signdec
		ind2 = random.randrange(2,6)*signdec
		if num2*10**ind2>num1*10**ind1:
			tempnum = num1
			tempind = ind1
			num1 = num2
			ind1 = ind2
			num2 = tempnum
			ind2 = tempind
		answer = rounddp(num1*10**ind1 - num2*10**ind2,7)
		answer = sftonum(str(answer),0)
		question = sftosf(str(num1),ind1) + " $-$ " + sftosf(str(num2),ind2)
#write question
		tempquestions.write(explanation + "$" + str(num1) + " \\times 10^{" + str(ind1) + "} - " + str(num2) + " \\times 10^{" + str(ind2) + "}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def sfsubtractpos(n,explanationn):
	import random
	from utilities.sf import sftonum,sftosf
	from utilities.rounding import rounddp
	from math import ceil,log10
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		num1 = 2
		num2 = num1
		while num1==num2:
			if random.randrange(0,2)==1:
				num1 = rounddp(random.randrange(1,10) + random.randrange(1,10)/10,1)
			else:
				num1 = rounddp(random.randrange(1,10) + random.randrange(0,10)/10 + random.randrange(1,10)/100,2)
			if random.randrange(0,2)==1:
				num2 = rounddp(random.randrange(1,10) + random.randrange(1,10)/10,1)
			else:
				num2 = rounddp(random.randrange(1,10) + random.randrange(0,10)/10 + random.randrange(1,10)/100,2)
		signdec = 1
		ind1 = random.randrange(2,6)*signdec
		ind2 = random.randrange(2,6)*signdec
		if num2*10**ind2>num1*10**ind1:
			tempnum = num1
			tempind = ind1
			num1 = num2
			ind1 = ind2
			num2 = tempnum
			ind2 = tempind
		answer = rounddp(num1*10**ind1 - num2*10**ind2,7)
		answer = sftonum(str(answer),0)
		question = sftosf(str(num1),ind1) + " $-$ " + sftosf(str(num2),ind2)
#write question
		tempquestions.write(explanation + "$" + str(num1) + " \\times 10^{" + str(ind1) + "} - " + str(num2) + " \\times 10^{" + str(ind2) + "}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def sfsubtractneg(n,explanationn):
	import random
	from utilities.sf import sftonum,sftosf
	from utilities.rounding import rounddp
	from math import ceil,log10
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			num1 = rounddp(random.randrange(1,10) + random.randrange(1,10)/10,1)
		else:
			num1 = rounddp(random.randrange(1,10) + random.randrange(0,10)/10 + random.randrange(1,10)/100,2)
		if random.randrange(0,2)==1:
			num2 = rounddp(random.randrange(1,10) + random.randrange(1,10)/10,1)
		else:
			num2 = rounddp(random.randrange(1,10) + random.randrange(0,10)/10 + random.randrange(1,10)/100,2)
		signdec = -1
		ind1 = random.randrange(2,6)*signdec
		ind2 = random.randrange(2,6)*signdec
		if num2*10**ind2>num1*10**ind1:
			tempnum = num1
			tempind = ind1
			num1 = num2
			ind1 = ind2
			num2 = tempnum
			ind2 = tempind
		answer = rounddp(num1*10**ind1 - num2*10**ind2,7)
		answer = sftonum(str(answer),0)
		question = sftosf(str(num1),ind1) + " $-$ " + sftosf(str(num2),ind2)
#write question
		tempquestions.write(explanation + "$" + str(num1) + " \\times 10^{" + str(ind1) + "} - " + str(num2) + " \\times 10^{" + str(ind2) + "}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))
