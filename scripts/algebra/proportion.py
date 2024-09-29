#proportion.py


def direct(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "y is directly proportional to x. "
		else:
			explanation = ""
		if random.randrange(0,4)==1:
			k = rounddp(random.randrange(0,13) + random.randrange(1,10)/10,1)
		else:
			k = random.randrange(2,13)
		xs = [2,3,4,5,6,7,8,9,10,11,12]
		x1 = random.choice(xs) 
		y1 = rounddp(x1 * k,1)
		xs.remove(x1)
		x2 = random.choice(xs)
		y2 = rounddp(x2 * k,1)
		if y1%1==0:
			y1 = int(y1)
		if y2%1==0:
			y2 = int(y2)
		if random.randrange(0,2)==1:
			question = "Find x when \\mbox{y = " + str(y2) + "}"
			answer = "x = " + str(x2)
		else:
			question = "Find y when \\mbox{x = " + str(x2) + "}"
			answer = "y = " + str(y2)
#write question
		tempquestions.write(explanation + "When \\mbox{y = " + str(y1) + "}, \\mbox{x = " + str(x1) + "}. " + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def directtable(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "y is directly proportional to x. Complete this table."
		else:
			explanation = ""
		if random.randrange(0,4)==1:
			k = rounddp(random.randrange(0,13) + random.randrange(1,10)/10,1)
		else:
			k = random.randrange(2,13)
		xs = [2,3,4,5,6,7,8,9,10,11,12]
		x1 = random.choice(xs) 
		y1 = rounddp(x1 * k,1)
		xs.remove(x1)
		x2 = random.choice(xs)
		y2 = rounddp(x2 * k,1)
		if y1%1==0:
			y1 = int(y1)
		if y2%1==0:
			y2 = int(y2)
		if random.randrange(0,2)==1:
			answer = "x = " + str(x2)
			x2 = "?"
		else:
			answer = "y = " + str(y2)
			y2 = "?"
		table = "\\renewcommand{\\arraystretch}{1}\\begin{tabular}{ | c | c | c |} \\hline x & " + str(x1) + " & " + str(x2) + " \\\\ \\hline y & " + str(y1) + " & " + str(y2) + " \\\\ \\hline \\end{tabular}"
#write question
		tempquestions.write(explanation + table)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def directsquare(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "y is directly proportional to the square of x. "
		else:
			explanation = ""
		if random.randrange(0,4)==1:
			k = rounddp(random.randrange(0,13) + random.randrange(1,10)/10,1)
		else:
			k = random.randrange(2,13)
		xs = [2,3,4,5,6,7,8,9,10,11,12]
		x1 = random.choice(xs) 
		y1 = rounddp(x1**2 * k,2)
		xs.remove(x1)
		x2 = random.choice(xs)
		y2 = rounddp(x2**2 * k,2)
		if y1%1==0:
			y1 = int(y1)
		if y2%1==0:
			y2 = int(y2)
		if random.randrange(0,2)==1:
			question = "Find x when \\mbox{y = " + str(y2) + "}"
			answer = "x = " + str(x2)
		else:
			question = "Find y when \\mbox{x = " + str(x2) + "}"
			answer = "y = " + str(y2)
#write question
		tempquestions.write(explanation + "When \\mbox{y = " + str(y1) + "}, \\mbox{x = " + str(x1) + "}. " + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def directsquaretable(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "y is directly proportional to  the square of x. Complete this table."
		else:
			explanation = ""
		if random.randrange(0,4)==1:
			k = rounddp(random.randrange(0,13) + random.randrange(1,10)/10,1)
		else:
			k = random.randrange(2,13)
		xs = [2,3,4,5,6,7,8,9,10,11,12]
		x1 = random.choice(xs) 
		y1 = rounddp(x1**2 * k,2)
		xs.remove(x1)
		x2 = random.choice(xs)
		y2 = rounddp(x2**2 * k,2)
		if y1%1==0:
			y1 = int(y1)
		if y2%1==0:
			y2 = int(y2)
		if random.randrange(0,2)==1:
			answer = "x = " + str(x2)
			x2 = "?"
		else:
			answer = "y = " + str(y2)
			y2 = "?"
		table = "\\renewcommand{\\arraystretch}{1}\\begin{tabular}{ | c | c | c |} \\hline x & " + str(x1) + " & " + str(x2) + " \\\\ \\hline y & " + str(y1) + " & " + str(y2) + " \\\\ \\hline \\end{tabular}"
#write question
		tempquestions.write(explanation + table)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def directsquareroot(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "y is directly proportional to the square root of x. "
		else:
			explanation = ""
		if random.randrange(0,4)==1:
			k = rounddp(random.randrange(0,13) + random.randrange(1,10)/10,1)
		else:
			k = random.randrange(2,13)
		xs = [4,9,16,25,36,49,64,81,100,121,144]
		x1 = random.choice(xs) 
		y1 = rounddp(x1**0.5 * k,2)
		xs.remove(x1)
		x2 = random.choice(xs)
		y2 = rounddp(x2**0.5 * k,2)
		if y1%1==0:
			y1 = int(y1)
		if y2%1==0:
			y2 = int(y2)
		if random.randrange(0,2)==1:
			question = "Find x when \\mbox{y = " + str(y2) + "}"
			answer = "x = " + str(x2)
		else:
			question = "Find y when \\mbox{x = " + str(x2) + "}"
			answer = "y = " + str(y2)
#write question
		tempquestions.write(explanation + "When \\mbox{y = " + str(y1) + "}, \\mbox{x = " + str(x1) + "}. " + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def directsquareroottable(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "y is directly proportional to the square root of x. Complete this table."
		else:
			explanation = ""
		if random.randrange(0,4)==1:
			k = rounddp(random.randrange(0,13) + random.randrange(1,10)/10,1)
		else:
			k = random.randrange(2,13)
		xs = [4,9,16,25,36,49,64,81,100,121,144]
		x1 = random.choice(xs) 
		y1 = rounddp(x1**0.5 * k,2)
		xs.remove(x1)
		x2 = random.choice(xs)
		y2 = rounddp(x2**0.5 * k,2)
		if y1%1==0:
			y1 = int(y1)
		if y2%1==0:
			y2 = int(y2)
		if random.randrange(0,2)==1:
			answer = "x = " + str(x2)
			x2 = "?"
		else:
			answer = "y = " + str(y2)
			y2 = "?"
		table = "\\renewcommand{\\arraystretch}{1}\\begin{tabular}{ | c | c | c |} \\hline x & " + str(x1) + " & " + str(x2) + " \\\\ \\hline y & " + str(y1) + " & " + str(y2) + " \\\\ \\hline \\end{tabular}"
#write question
		tempquestions.write(explanation + table)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def inverse(n,explanationn):
	import random
	from utilities.rounding import rounddp
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
			y1 = rounddp(random.randrange(0,13) + random.randrange(1,10)/10,1)
		else:
			y1 = random.randrange(2,13)
		k = rounddp(x1 * y1,2)
		if k%1==0:
			k = int(k)
		a = random.randrange(0,4)
		if a==0:
			b = random.randrange(1,3)
		else:
			b = random.randrange(0,3)
		x2 = rounddp(x1/(2**a * 5**b),5)
		if x1%1==0:
			x1 = int(x1)
		if x2%1==0:
			x2 = int(x2)
		y2 = rounddp(k/x2,5)
		if y2%1==0:
			y2 = int(y2)
		if random.randrange(0,2)==1:
			question = "Find x when \\mbox{y = " + str(y2) + "}"
			answer = "x = " + str(x2)
		else:
			question = "Find y when \\mbox{x = " + str(x2) + "}"
			answer = "y = " + str(y2)
#write question
		tempquestions.write(explanation + "When \\mbox{y = " + str(y1) + "}, \\mbox{x = " + str(x1) + "}. " + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def inversetable(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "y is inversely proportional to x. Complete this table."
		else:
			explanation = ""
		x1 = random.randrange(2,13) 
		if random.randrange(0,4)==1:
			y1 = rounddp(random.randrange(0,13) + random.randrange(1,10)/10,1)
		else:
			y1 = random.randrange(2,13)
		k = rounddp(x1 * y1,2)
		if k%1==0:
			k = int(k)
		a = random.randrange(0,4)
		if a==0:
			b = random.randrange(1,3)
		else:
			b = random.randrange(0,3)
		x2 = rounddp(x1/(2**a * 5**b),5)
		if x1%1==0:
			x1 = int(x1)
		if x2%1==0:
			x2 = int(x2)
		y2 = rounddp(k/x2,5)
		if y2%1==0:
			y2 = int(y2)
		if random.randrange(0,2)==1:
			answer = "x = " + str(x2)
			x2 = "?"
		else:
			answer = "y = " + str(y2)
			y2 = "?"
		table = "\\renewcommand{\\arraystretch}{1}\\begin{tabular}{ | c | c | c |} \\hline x & " + str(x1) + " & " + str(x2) + " \\\\ \\hline y & " + str(y1) + " & " + str(y2) + " \\\\ \\hline \\end{tabular}"
#write question
		tempquestions.write(explanation + table)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def inversesquare(n,explanationn):
	import random
	from utilities.rounding import rounddp
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
			y1 = rounddp(random.randrange(0,13) + random.randrange(1,10)/10,1)
		else:
			y1 = random.randrange(2,13)
		k = rounddp(x1**2 * y1,2)
		if k%1==0:
			k = int(k)
		a = random.randrange(0,3)
		if a==0:
			b = random.randrange(1,3)
		else:
			b = random.randrange(0,2)
		x2 = rounddp(x1/(2**a * 5**b),5)
		if x1%1==0:
			x1 = int(x1)
		if x2%1==0:
			x2 = int(x2)
		y2 = rounddp(k/x2**2,5)
		if y2%1==0:
			y2 = int(y2)
		if random.randrange(0,2)==1:
			question = "Find x when \\mbox{y = " + str(y2) + "}"
			answer = "x = " + str(x2)
		else:
			question = "Find y when \\mbox{x = " + str(x2) + "}"
			answer = "y = " + str(y2)
#write question
		tempquestions.write(explanation + "When \\mbox{y = " + str(y1) + "}, \\mbox{x = " + str(x1) + "}. " + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def inversesquaretable(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "y is inversely proportional to the square of x. Complete this table."
		else:
			explanation = ""
		x1 = random.randrange(2,13) 
		if random.randrange(0,4)==1:
			y1 = rounddp(random.randrange(0,13) + random.randrange(1,10)/10,1)
		else:
			y1 = random.randrange(2,13)
		k = rounddp(x1**2 * y1,2)
		if k%1==0:
			k = int(k)
		a = random.randrange(0,3)
		if a==0:
			b = random.randrange(1,3)
		else:
			b = random.randrange(0,2)
		x2 = rounddp(x1/(2**a * 5**b),5)
		if x1%1==0:
			x1 = int(x1)
		if x2%1==0:
			x2 = int(x2)
		y2 = rounddp(k/x2**2,5)
		if y2%1==0:
			y2 = int(y2)
		if random.randrange(0,2)==1:
			answer = "x = " + str(x2)
			x2 = "?"
		else:
			answer = "y = " + str(y2)
			y2 = "?"
		table = "\\renewcommand{\\arraystretch}{1}\\begin{tabular}{ | c | c | c |} \\hline x & " + str(x1) + " & " + str(x2) + " \\\\ \\hline y & " + str(y1) + " & " + str(y2) + " \\\\ \\hline \\end{tabular}"
#write question
		tempquestions.write(explanation + table)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def inversesquareroot(n,explanationn):
	import random
	from utilities.rounding import rounddp
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
			y1 = rounddp(random.randrange(0,13) + random.randrange(1,10)/10,1)
		else:
			y1 = random.randrange(2,13)
		k = rounddp(x1**0.5 * y1,2)
		if k%1==0:
			k = int(k)
		a = random.randrange(0,3)
		if a==0:
			b = random.randrange(1,3)
		else:
			b = random.randrange(0,2)
		x2 = rounddp(rounddp((rounddp(x1**0.5,1))/(2**a * 5**b),5)**2,6)
		if x1%1==0:
			x1 = int(x1)
		if x2%1==0:
			x2 = int(x2)
		y2 = rounddp(k/x2**0.5,5)
		if y2%1==0:
			y2 = int(y2)
		if random.randrange(0,2)==1:
			question = "Find x when \\mbox{y = " + str(y2) + "}"
			answer = "x = " + str(x2)
		else:
			question = "Find y when \\mbox{x = " + str(x2) + "}"
			answer = "y = " + str(y2)
#write question
		tempquestions.write(explanation + "When \\mbox{y = " + str(y1) + "}, \\mbox{x = " + str(x1) + "}. " + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def inversesquareroottable(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "y is inversely proportional to the square root of x. Complete this table."
		else:
			explanation = ""
		x1 = random.randrange(2,13)**2 
		if random.randrange(0,4)==1:
			y1 = rounddp(random.randrange(0,13) + random.randrange(1,10)/10,1)
		else:
			y1 = random.randrange(2,13)
		k = rounddp(x1**0.5 * y1,2)
		if k%1==0:
			k = int(k)
		a = random.randrange(0,3)
		if a==0:
			b = random.randrange(1,3)
		else:
			b = random.randrange(0,2)
		x2 = rounddp(rounddp((rounddp(x1**0.5,1))/(2**a * 5**b),5)**2,6)
		if x1%1==0:
			x1 = int(x1)
		if x2%1==0:
			x2 = int(x2)
		y2 = rounddp(k/x2**0.5,5)
		if y2%1==0:
			y2 = int(y2)
		if random.randrange(0,2)==1:
			answer = "x = " + str(x2)
			x2 = "?"
		else:
			answer = "y = " + str(y2)
			y2 = "?"
		table = "\\renewcommand{\\arraystretch}{1}\\begin{tabular}{ | c | c | c |} \\hline x & " + str(x1) + " & " + str(x2) + " \\\\ \\hline y & " + str(y1) + " & " + str(y2) + " \\\\ \\hline \\end{tabular}"
#write question
		tempquestions.write(explanation + table)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def proportionwall(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		people1 = random.randrange(3,7)
		people2 = people1 + random.randrange(1,people1-1)*(-1)**random.randrange(1,3)
		time1 = random.randrange(3,13) * people2
		time2 = time1/(people2/people1)
		question = "It takes " + str(people1) + " workers " + str(time1) + " hours to build a wall. How long would it take " + str(people2) + " workers?"
		answer = str(int(time2)) + " hours"
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def proportioncatbowls(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		baserates = [6,9,10,12,16,18,20,24,28,30,32]
		baserate = random.choice(baserates)
		bs = [2,3,4,5,6,7,8,9,10]
		b1 = random.choice(bs)
		bs.remove(b1)
		m1 = baserate*b1
		factors = []
		for i in range(2,m1):
			if m1%i==0:
				factors.append(i)
		c1 = random.choice(factors)
		m1 = int(m1/c1)
		b2 = random.choice(bs)
		m2 = baserate*b2
		factors = []
		for i in range(2,m2):
			if m2%i==0:
				factors.append(i)
		c2 = random.choice(factors)
		m2 = int(m2/c2)
		question = "If it takes " + str(m1) + " minutes for " + str(c1) + " cats to eat " + str(b1) + " bowls of cat food, how long will it take " + str(c2) + " cats to eat " + str(b2) + " bowls of food?"
		answer = str(m2) + " minutes"

#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def directeq(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "y is directly proportional to x. "
		else:
			explanation = ""
		if random.randrange(0,4)==1:
			k = rounddp(random.randrange(0,13) + random.randrange(1,10)/10,1)
		else:
			k = random.randrange(2,13)
		xs = [2,3,4,5,6,7,8,9,10,11,12]
		x1 = random.choice(xs) 
		y1 = rounddp(x1 * k,1)
		xs.remove(x1)
		x2 = random.choice(xs)
		y2 = rounddp(x2 * k,1)
		if y1%1==0:
			y1 = int(y1)
		if y2%1==0:
			y2 = int(y2)
		if random.randrange(0,2)==1:
			question = "Find x when \\mbox{y = " + str(y2) + "}"
			answer = "x = " + str(x2)
		else:
			question = "Find y when \\mbox{x = " + str(x2) + "}"
			answer = "y = " + str(y2)
		question = explanation + "When \\mbox{y = " + str(y1) + "}, \\mbox{x = " + str(x1) + "}. Find a formula linking x and y."
		answer = "$y = " + str(k) + "x$"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def directsquareeq(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "y is directly proportional to the square of x. "
		else:
			explanation = ""
		if random.randrange(0,4)==1:
			k = rounddp(random.randrange(0,13) + random.randrange(1,10)/10,1)
		else:
			k = random.randrange(2,13)
		xs = [2,3,4,5,6,7,8,9,10,11,12]
		x1 = random.choice(xs) 
		y1 = rounddp(x1**2 * k,2)
		xs.remove(x1)
		x2 = random.choice(xs)
		y2 = rounddp(x2**2 * k,2)
		if y1%1==0:
			y1 = int(y1)
		if y2%1==0:
			y2 = int(y2)
		if random.randrange(0,2)==1:
			question = "Find x when \\mbox{y = " + str(y2) + "}"
			answer = "x = " + str(x2)
		else:
			question = "Find y when \\mbox{x = " + str(x2) + "}"
			answer = "y = " + str(y2)
		question = explanation + "When \\mbox{y = " + str(y1) + "}, \\mbox{x = " + str(x1) + "}. Find a formula linking x and y."
		answer = "$y = " + str(k) + "x^{2}$"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def directsquarerooteq(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "y is directly proportional to the square root of x. "
		else:
			explanation = ""
		if random.randrange(0,4)==1:
			k = rounddp(random.randrange(0,13) + random.randrange(1,10)/10,1)
		else:
			k = random.randrange(2,13)
		xs = [4,9,16,25,36,49,64,81,100,121,144]
		x1 = random.choice(xs) 
		y1 = rounddp(x1**0.5 * k,2)
		xs.remove(x1)
		x2 = random.choice(xs)
		y2 = rounddp(x2**0.5 * k,2)
		if y1%1==0:
			y1 = int(y1)
		if y2%1==0:
			y2 = int(y2)
		if random.randrange(0,2)==1:
			question = "Find x when \\mbox{y = " + str(y2) + "}"
			answer = "x = " + str(x2)
		else:
			question = "Find y when \\mbox{x = " + str(x2) + "}"
			answer = "y = " + str(y2)
		question = explanation + "When \\mbox{y = " + str(y1) + "}, \\mbox{x = " + str(x1) + "}. Find a formula linking x and y."
		answer = "$y = " + str(k) + "\\sqrt{x}$"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def inverseeq(n,explanationn):
	import random
	from utilities.rounding import rounddp
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
			y1 = rounddp(random.randrange(0,13) + random.randrange(1,10)/10,1)
		else:
			y1 = random.randrange(2,13)
		k = rounddp(x1 * y1,2)
		if k%1==0:
			k = int(k)
		a = random.randrange(0,4)
		if a==0:
			b = random.randrange(1,3)
		else:
			b = random.randrange(0,3)
		x2 = rounddp(x1/(2**a * 5**b),5)
		if x1%1==0:
			x1 = int(x1)
		if x2%1==0:
			x2 = int(x2)
		y2 = rounddp(k/x2,5)
		if y2%1==0:
			y2 = int(y2)
		if random.randrange(0,2)==1:
			question = "Find x when \\mbox{y = " + str(y2) + "}"
			answer = "x = " + str(x2)
		else:
			question = "Find y when \\mbox{x = " + str(x2) + "}"
			answer = "y = " + str(y2)
		question = explanation + "When \\mbox{y = " + str(y1) + "}, \\mbox{x = " + str(x1) + "}. Find a formula linking x and y."
		answer = "$y = \\dfrac{" + str(k) + "}{x}$"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def inversesquareeq(n,explanationn):
	import random
	from utilities.rounding import rounddp
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
			y1 = rounddp(random.randrange(0,13) + random.randrange(1,10)/10,1)
		else:
			y1 = random.randrange(2,13)
		k = rounddp(x1**2 * y1,2)
		if k%1==0:
			k = int(k)
		a = random.randrange(0,3)
		if a==0:
			b = random.randrange(1,3)
		else:
			b = random.randrange(0,2)
		x2 = rounddp(x1/(2**a * 5**b),5)
		if x1%1==0:
			x1 = int(x1)
		if x2%1==0:
			x2 = int(x2)
		y2 = rounddp(k/x2**2,5)
		if y2%1==0:
			y2 = int(y2)
		if random.randrange(0,2)==1:
			question = "Find x when \\mbox{y = " + str(y2) + "}"
			answer = "x = " + str(x2)
		else:
			question = "Find y when \\mbox{x = " + str(x2) + "}"
			answer = "y = " + str(y2)
		question = explanation + "When \\mbox{y = " + str(y1) + "}, \\mbox{x = " + str(x1) + "}. Find a formula linking x and y."
		answer = "$y = \\dfrac{" + str(k) + "}{x^{2}}$"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def inversesquarerooteq(n,explanationn):
	import random
	from utilities.rounding import rounddp
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
			y1 = rounddp(random.randrange(0,13) + random.randrange(1,10)/10,1)
		else:
			y1 = random.randrange(2,13)
		k = rounddp(x1**0.5 * y1,2)
		if k%1==0:
			k = int(k)
		a = random.randrange(0,3)
		if a==0:
			b = random.randrange(1,3)
		else:
			b = random.randrange(0,2)
		x2 = rounddp(rounddp((rounddp(x1**0.5,1))/(2**a * 5**b),5)**2,6)
		if x1%1==0:
			x1 = int(x1)
		if x2%1==0:
			x2 = int(x2)
		y2 = rounddp(k/x2**0.5,5)
		if y2%1==0:
			y2 = int(y2)
		if random.randrange(0,2)==1:
			question = "Find x when \\mbox{y = " + str(y2) + "}"
			answer = "x = " + str(x2)
		else:
			question = "Find y when \\mbox{x = " + str(x2) + "}"
			answer = "y = " + str(y2)
		question = explanation + "When \\mbox{y = " + str(y1) + "}, \\mbox{x = " + str(x1) + "}. Find a formula linking x and y."
		answer = "$y = \\dfrac{" + str(k) + "}{\sqrt{x}}$"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
