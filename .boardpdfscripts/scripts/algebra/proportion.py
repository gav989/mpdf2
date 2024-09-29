#proportion.py


def direct(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "y is directly proportional to x. "
		else:
			explanation = ""
		if random.randrange(0,4)==1:
			k = round(random.randrange(0,13) + random.randrange(1,10)/10,1)
		else:
			k = random.randrange(2,13)
		xs = [2,3,4,5,6,7,8,9,10,11,12]
		x1 = random.choice(xs) 
		y1 = round(x1 * k,1)
		xs.remove(x1)
		x2 = random.choice(xs)
		y2 = round(x2 * k,1)
		if y1%1==0:
			y1 = int(y1)
		if y2%1==0:
			y2 = int(y2)
		if random.randrange(0,2)==1:
			question = "Find x when y = " + str(y2)
			answer = "x = " + str(x2)
		else:
			question = "Find y when x = " + str(x2)
			answer = "y = " + str(y2)
#write question
		tempquestions.write(explanation + "When y = " + str(y1) + ", x = " + str(x1) + ". " + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def directsquare(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "y is directly proportional to the square of x. "
		else:
			explanation = ""
		if random.randrange(0,4)==1:
			k = round(random.randrange(0,13) + random.randrange(1,10)/10,1)
		else:
			k = random.randrange(2,13)
		xs = [2,3,4,5,6,7,8,9,10,11,12]
		x1 = random.choice(xs) 
		y1 = round(x1**2 * k,2)
		xs.remove(x1)
		x2 = random.choice(xs)
		y2 = round(x2**2 * k,2)
		if y1%1==0:
			y1 = int(y1)
		if y2%1==0:
			y2 = int(y2)
		if random.randrange(0,2)==1:
			question = "Find x when y = " + str(y2)
			answer = "x = " + str(x2)
		else:
			question = "Find y when x = " + str(x2)
			answer = "y = " + str(y2)
#write question
		tempquestions.write(explanation + "When y = " + str(y1) + ", x = " + str(x1) + ". " + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def directsquareroot(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "y is directly proportional to the square root of x. "
		else:
			explanation = ""
		if random.randrange(0,4)==1:
			k = round(random.randrange(0,13) + random.randrange(1,10)/10,1)
		else:
			k = random.randrange(2,13)
		xs = [4,9,16,25,36,49,64,81,100,121,144]
		x1 = random.choice(xs) 
		y1 = round(x1**0.5 * k,2)
		xs.remove(x1)
		x2 = random.choice(xs)
		y2 = round(x2**0.5 * k,2)
		if y1%1==0:
			y1 = int(y1)
		if y2%1==0:
			y2 = int(y2)
		if random.randrange(0,2)==1:
			question = "Find x when y = " + str(y2)
			answer = "x = " + str(x2)
		else:
			question = "Find y when x = " + str(x2)
			answer = "y = " + str(y2)
#write question
		tempquestions.write(explanation + "When y = " + str(y1) + ", x = " + str(x1) + ". " + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def inverse(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "y is inversely proportional to x. "
		else:
			explanation = ""
		x1 = random.randrange(2,13) 
		if random.randrange(0,4)==1:
			y1 = round(random.randrange(0,13) + random.randrange(1,10)/10,1)
		else:
			y1 = random.randrange(2,13)
		k = round(x1 * y1,2)
		if k%1==0:
			k = int(k)
		a = random.randrange(0,4)
		if a==0:
			b = random.randrange(1,3)
		else:
			b = random.randrange(0,3)
		x2 = round(x1/(2**a * 5**b),5)
		if x1%1==0:
			x1 = int(x1)
		if x2%1==0:
			x2 = int(x2)
		y2 = round(k/x2,5)
		if y2%1==0:
			y2 = int(y2)
		if random.randrange(0,2)==1:
			question = "Find x when y = " + str(y2)
			answer = "x = " + str(x2)
		else:
			question = "Find y when x = " + str(x2)
			answer = "y = " + str(y2)
#write question
		tempquestions.write(explanation + "When y = " + str(y1) + ", x = " + str(x1) + ". " + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def inversesquare(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "y is inversely proportional to the square of x. "
		else:
			explanation = ""
		x1 = random.randrange(2,13) 
		if random.randrange(0,4)==1:
			y1 = round(random.randrange(0,13) + random.randrange(1,10)/10,1)
		else:
			y1 = random.randrange(2,13)
		k = round(x1**2 * y1,2)
		if k%1==0:
			k = int(k)
		a = random.randrange(0,3)
		if a==0:
			b = random.randrange(1,3)
		else:
			b = random.randrange(0,2)
		x2 = round(x1/(2**a * 5**b),5)
		if x1%1==0:
			x1 = int(x1)
		if x2%1==0:
			x2 = int(x2)
		y2 = round(k/x2**2,5)
		if y2%1==0:
			y2 = int(y2)
		if random.randrange(0,2)==1:
			question = "Find x when y = " + str(y2)
			answer = "x = " + str(x2)
		else:
			question = "Find y when x = " + str(x2)
			answer = "y = " + str(y2)
#write question
		tempquestions.write(explanation + "When y = " + str(y1) + ", x = " + str(x1) + ". " + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def inversesquareroot(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "y is inversely proportional to the square root of x. "
		else:
			explanation = ""
		x1 = random.randrange(2,13)**2 
		if random.randrange(0,4)==1:
			y1 = round(random.randrange(0,13) + random.randrange(1,10)/10,1)
		else:
			y1 = random.randrange(2,13)
		k = round(x1**0.5 * y1,2)
		if k%1==0:
			k = int(k)
		a = random.randrange(0,3)
		if a==0:
			b = random.randrange(1,3)
		else:
			b = random.randrange(0,2)
		x2 = round(round((round(x1**0.5,1))/(2**a * 5**b),5)**2,6)
		if x1%1==0:
			x1 = int(x1)
		if x2%1==0:
			x2 = int(x2)
		y2 = round(k/x2**0.5,5)
		if y2%1==0:
			y2 = int(y2)
		if random.randrange(0,2)==1:
			question = "Find x when y = " + str(y2)
			answer = "x = " + str(x2)
		else:
			question = "Find y when x = " + str(x2)
			answer = "y = " + str(y2)
#write question
		tempquestions.write(explanation + "When y = " + str(y1) + ", x = " + str(x1) + ". " + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
