#standardform.py

def sfconvertpos1(n,explanationn):
	import random
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
		t = random.randrange(1,3)
		if t==1:
			a = random.randrange(1,10)*10 + random.randrange(1,10)
		else:
			a = random.randrange(1,10)*100 + random.randrange(0,10)*10 + random.randrange(1,10)
		i = random.randrange(3,9)
		num1 = str(a) + ("0" * (abs(i)-t))
		a = a/10**t
#write question
		tempquestions.write(explanation1 + "$" + str(a) + "\\times 10^"+ str(i) + "$" + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write("\\num{" + str(num1)  + "}")

def sfconvertpos2(n,explanationn):
	import random
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
		t = random.randrange(1,3)
		if t==1:
			a = random.randrange(1,10)*10 + random.randrange(1,10)
		else:
			a = random.randrange(1,10)*100 + random.randrange(0,10)*10 + random.randrange(1,10)
		i = random.randrange(3,9)
		num1 = str(a) + ("0" * (abs(i)-t))
		a = a/10**t
#write question
		tempquestions.write(explanation1 + "\\num{" + str(num1)  + "}" + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(a) + "\\times 10^"+ str(i) + "$")

def sfconvertneg1(n,explanationn):
	import random
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
		t = random.randrange(1,3)
		if t==1:
			a = random.randrange(1,10)*10 + random.randrange(1,10)
		else:
			a = random.randrange(1,10)*100 + random.randrange(0,10)*10 + random.randrange(1,10)
		i = random.randrange(-8,-2)
		num1 = "0." + ("0" * (abs(i)-1)) + str(a)
		a = a/10**t
#write question
		tempquestions.write(explanation1 + "$" + str(a) + "\\times 10^{"+ str(i) + "}$" + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write("\\num{" + num1  + "}")

def sfconvertneg2(n,explanationn):
	import random
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
		t = random.randrange(1,3)
		if t==1:
			a = random.randrange(1,10)*10 + random.randrange(1,10)
		else:
			a = random.randrange(1,10)*100 + random.randrange(0,10)*10 + random.randrange(1,10)
		i = random.randrange(-8,-2)
		num1 = "0." + ("0" * (abs(i)-1)) + str(a)
		a = a/10**t
#write question
		tempquestions.write(explanation1 + "\\num{" + num1  + "}" + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(a) + "\\times 10^{"+ str(i) + "}$")

def sfconvert1(n,explanationn):
	import random
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
		t = random.randrange(1,3)
		if t==1:
			a = random.randrange(1,10)*10 + random.randrange(1,10)
		else:
			a = random.randrange(1,10)*100 + random.randrange(0,10)*10 + random.randrange(1,10)
		if pos==1:
			i = random.randrange(3,9)
			num1 = str(a) + ("0" * (abs(i)-t))
			a = a/10**t
		else:
			i = random.randrange(-8,-2)
			num1 = "0." + ("0" * (abs(i)-1)) + str(a)
			a = a/10**t
#write question
		tempquestions.write(explanation1 + "$" + str(a) + "\\times 10^{"+ str(i) + "}$" + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write("\\num{" + str(num1)  + "}")

def sfconvert2(n,explanationn):
	import random
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
		t = random.randrange(1,3)
		if t==1:
			a = random.randrange(1,10)*10 + random.randrange(1,10)
		else:
			a = random.randrange(1,10)*100 + random.randrange(0,10)*10 + random.randrange(1,10)
		if pos==1:
			i = random.randrange(3,9)
			num1 = str(a) + ("0" * (abs(i)-t))
			a = a/10**t
		else:
			i = random.randrange(-8,-2)
			num1 = "0." + ("0" * (abs(i)-1)) + str(a)
			a = a/10**t
#write question
		tempquestions.write(explanation1 + "\\num{" + str(num1)  + "}" + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(a) + "\\times 10^{"+ str(i) + "}$")



def sfmultiplyint(n,explanationn):
	import random
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
		num2 = round(random.randrange(1,10) + random.randrange(1,10)/10,1)
		num3 = round(num1 * num2,1)
		ind2 = random.randrange(2,10)
		ind3 = ind2
		if num3>=10:
			num3 = round(num3/10,2)
			ind3 = ind3 + 1
		#write question
		tempquestions.write(explanation1 + "$(" + str(num2) + " \\times 10^{" + str(ind2) + "})  \\times" + str(num1) + "$" + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(num3) + "\\times 10^{"+ str(ind3) + "}$")



def sfmultiply(n,explanationn):
	import random
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
		num2 = round(random.randrange(1,10) + random.randrange(1,10)/10,1)
		num3 = round(num1 * num2,1)
		if random.randrange(1,3)==2:
			temp = num1
			num1 = num2
			num2 = temp
		ind1 = random.randrange(2,10)*(-1)
		ind2 = random.randrange(2,10)*(-1)
		if ind1!=ind2:
			ind1 = ind1 * (-1)**random.randrange(1,3)
			ind2 = ind2 * (-1)**random.randrange(1,3)
		else:
			temp = random.randrange(1,3)
			ind1 = ind1**temp
			ind2 = ind2**temp
		ind3 = ind1 + ind2
		if num3>=10:
			num3 = round(num3/10,2)
			ind3 = ind3 + 1
		#write question
		tempquestions.write(explanation1 + "$(" + str(num1) + " \\times 10^{" + str(ind1) + "}) \\times (" + str(num2) + " \\times 10^{" + str(ind2) + "})$" + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(num3) + "\\times 10^{"+ str(ind3) + "}$")
		
		
def sfdivide(n,explanationn):
	import random
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
			num1 = round(random.randrange(0,10)/10 + random.randrange(1,10),1)
			num3 = round(num1/num2,3)
		elif num2==6:
			num1 = round(random.randrange(1,33) * 0.3,1)
			num3 = round(num1/num2,3)
		else:
			num3 = random.randrange(2,10)
			num1 = num2 * num3
		ind1 = random.randrange(2,10)
		ind2 = random.randrange(2,10)
		if num1>=10:
			num1 = round(num1/10,3)
			alter = 1
		else:
			alter = 0
		if ind1==ind2:
			if random.randrange(0,2)==1:
				ind1 = ind1 * -1
			else:
				ind2 = ind2 * -1
		else:
			ind1 = ind1 * (-1)**random.randrange(1,3)
			ind2 = ind2 * (-1)**random.randrange(1,3)
		ind3 = ind1 - ind2
		if alter==1:
			ind1 = ind1 + 1
		if num1%1==0:
			num1 = int(num1)
		if num3<1:
			num3 = round(num3*10,3)
			ind3 = ind3 - 1
		if num3%1==0:
			num3 = int(num3)
		#write question
		tempquestions.write(explanation1 + "$(" + str(num1) + " \\times 10^{" + str(ind1) + "}) \\div (" + str(num2) + " \\times 10^{" + str(ind2) + "})$" + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(num3) + "\\times 10^{"+ str(ind3) + "}$")


def sfdividepos(n,explanationn):
	import random
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
			num1 = round(random.randrange(0,10)/10 + random.randrange(1,10),1)
			num3 = round(num1/num2,3)
		elif num2==6:
			num1 = round(random.randrange(1,33) * 0.3,1)
			num3 = round(num1/num2,3)
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
		if num1>=10:
			num1 = round(num1/10,3)
			alter = 1
		else:
			alter = 0
		ind3 = ind1 - ind2
		if alter==1:
			ind1 = ind1 + 1
		if num1%1==0:
			num1 = int(num1)
		if num3<1:
			num3 = round(num3*10,3)
			ind3 = ind3 - 1
		if num3%1==0:
			num3 = int(num3)
		#write question
		tempquestions.write(explanation1 + "$(" + str(num1) + " \\times 10^{" + str(ind1) + "}) \\div (" + str(num2) + " \\times 10^{" + str(ind2) + "})$" + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(num3) + "\\times 10^{"+ str(ind3) + "}$")



def sfaddpos(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			num1 = round(random.randrange(1,10) + random.randrange(1,10)/10,1)
		else:
			num1 = round(random.randrange(1,10) + random.randrange(0,10)/10 + random.randrange(1,10)/100,2)
		if random.randrange(0,2)==1:
			num2 = round(random.randrange(1,10) + random.randrange(1,10)/10,1)
		else:
			num2 = round(random.randrange(1,10) + random.randrange(0,10)/10 + random.randrange(1,10)/100,2)
		signdec = 1
		ind1 = random.randrange(2,6)*signdec
		ind2 = random.randrange(2,6)*signdec
		answer = round(num1*10**ind1 + num2*10**ind2,7)
		if answer%1==0:
			answer = int(answer)
		#write question
		tempquestions.write(explanation + "$(" + str(num1) + " \\times 10^{" + str(ind1) + "}) + (" + str(num2) + " \\times 10^{" + str(ind2) + "})$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def sfaddneg(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			num1 = round(random.randrange(1,10) + random.randrange(1,10)/10,1)
		else:
			num1 = round(random.randrange(1,10) + random.randrange(0,10)/10 + random.randrange(1,10)/100,2)
		if random.randrange(0,2)==1:
			num2 = round(random.randrange(1,10) + random.randrange(1,10)/10,1)
		else:
			num2 = round(random.randrange(1,10) + random.randrange(0,10)/10 + random.randrange(1,10)/100,2)
		signdec = -1
		ind1 = random.randrange(2,6)*signdec
		ind2 = random.randrange(2,6)*signdec
		answer = round(num1*10**ind1 + num2*10**ind2,7)
		if answer%1==0:
			answer = int(answer)
		#write question
		tempquestions.write(explanation + "$(" + str(num1) + " \\times 10^{" + str(ind1) + "}) + (" + str(num2) + " \\times 10^{" + str(ind2) + "})$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def sfadd(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		if random.randrange(0,2)==1:
			num1 = round(random.randrange(1,10) + random.randrange(1,10)/10,1)
		else:
			num1 = round(random.randrange(1,10) + random.randrange(0,10)/10 + random.randrange(1,10)/100,2)
		if random.randrange(0,2)==1:
			num2 = round(random.randrange(1,10) + random.randrange(1,10)/10,1)
		else:
			num2 = round(random.randrange(1,10) + random.randrange(0,10)/10 + random.randrange(1,10)/100,2)
		signdec = (-1)**random.randrange(1,3)
		ind1 = random.randrange(2,6)*signdec
		ind2 = random.randrange(2,6)*signdec
		answer = round(num1*10**ind1 + num2*10**ind2,7)
		if answer%1==0:
			answer = int(answer)
		#write question
		tempquestions.write(explanation + "$(" + str(num1) + " \\times 10^{" + str(ind1) + "}) + (" + str(num2) + " \\times 10^{" + str(ind2) + "})$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))

def sfsubtractpos(n,explanationn):
	import random
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
			num1 = round(random.randrange(1,10) + random.randrange(1,10)/10,1)
		else:
			num1 = round(random.randrange(1,10) + random.randrange(0,10)/10 + random.randrange(1,10)/100,2)
		if random.randrange(0,2)==1:
			num2 = round(random.randrange(1,10) + random.randrange(1,10)/10,1)
		else:
			num2 = round(random.randrange(1,10) + random.randrange(0,10)/10 + random.randrange(1,10)/100,2)
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
		answer = round(num1*10**ind1 - num2*10**ind2,7)
		if answer%1==0:
			answer = int(answer)
		if answer < 0.0001:
			zeros = "0" * abs(ceil(log10(answer)))
			answer = int(answer*10**6)
			while answer%10==0:
				answer = answer / 10
			answer = int(answer)
			answer = "0." + zeros + str(answer)
		#write question
		tempquestions.write(explanation + "$(" + str(num1) + " \\times 10^{" + str(ind1) + "}) - (" + str(num2) + " \\times 10^{" + str(ind2) + "})$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def sfsubtractneg(n,explanationn):
	import random
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
			num1 = round(random.randrange(1,10) + random.randrange(1,10)/10,1)
		else:
			num1 = round(random.randrange(1,10) + random.randrange(0,10)/10 + random.randrange(1,10)/100,2)
		if random.randrange(0,2)==1:
			num2 = round(random.randrange(1,10) + random.randrange(1,10)/10,1)
		else:
			num2 = round(random.randrange(1,10) + random.randrange(0,10)/10 + random.randrange(1,10)/100,2)
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
		answer = round(num1*10**ind1 - num2*10**ind2,7)
		if answer%1==0:
			answer = int(answer)
		if answer < 0.0001:
			zeros = "0" * abs(ceil(log10(answer)))
			answer = int(answer*10**6)
			while answer%10==0:
				answer = answer / 10
			answer = int(answer)
			answer = "0." + zeros + str(answer)
		#write question
		tempquestions.write(explanation + "$(" + str(num1) + " \\times 10^{" + str(ind1) + "}) - (" + str(num2) + " \\times 10^{" + str(ind2) + "})$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def sfsubtract(n,explanationn):
	import random
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
			num1 = round(random.randrange(1,10) + random.randrange(1,10)/10,1)
		else:
			num1 = round(random.randrange(1,10) + random.randrange(0,10)/10 + random.randrange(1,10)/100,2)
		if random.randrange(0,2)==1:
			num2 = round(random.randrange(1,10) + random.randrange(1,10)/10,1)
		else:
			num2 = round(random.randrange(1,10) + random.randrange(0,10)/10 + random.randrange(1,10)/100,2)
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
		answer = round(num1*10**ind1 - num2*10**ind2,7)
		if answer%1==0:
			answer = int(answer)
		if answer < 0.0001:
			zeros = "0" * abs(ceil(log10(answer)))
			answer = int(answer*10**6)
			while answer%10==0:
				answer = answer / 10
			answer = int(answer)
			answer = "0." + zeros + str(answer)
		#write question
		tempquestions.write(explanation + "$(" + str(num1) + " \\times 10^{" + str(ind1) + "}) - (" + str(num2) + " \\times 10^{" + str(ind2) + "})$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))
