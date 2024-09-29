#sequences.py


def seqnext(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "What number comes next in the sequence "
		else:
			explanation = ""
		m = random.randrange(1,10)
		if m==1:
			c = random.randrange(1,10)
		else:
			c = random.randrange(0,10)
		if random.randrange(0,2)==1:
			sign = " - "
		else:
			sign = " + "
		if random.randrange(0,2)==1:
			if sign==" - ":
				t1 = m * 1 - c
				t2 = m * 2 - c
				t3 = m * 3 - c
				t4 = m * 4 - c
				t5 = m * 5 - c
			else:
				t1 = m * 1 + c
				t2 = m * 2 + c
				t3 = m * 3 + c
				t4 = m * 4 + c
				t5 = m * 5 + c
		else:
			if sign==" - ":
				t1 = c - m * 1
				t2 = c - m * 2
				t3 = c - m * 3
				t4 = c - m * 4
				t5 = c - m * 5
			else:
				t1 = c + m * 1
				t2 = c + m * 2
				t3 = c + m * 3
				t4 = c + m * 4
				t5 = c + m * 5
		sequence = str(t1) + ", " + str(t2) + ", " + str(t3) + ", " + str(t4)	
#write question
		tempquestions.write(explanation + sequence)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(t5))

def genseq(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Write out the first 5 terms of the sequence "
		else:
			explanation = ""
		m = random.randrange(1,7)
		if m==1:
			c = random.randrange(1,7)
		else:
			c = random.randrange(0,7)
		if random.randrange(0,2)==1:
			sign = " - "
		else:
			sign = " + "
		if random.randrange(0,2)==1:
			if sign==" - ":
				t1 = m * 1 - c
				t2 = m * 2 - c
				t3 = m * 3 - c
				t4 = m * 4 - c
				t5 = m * 5 - c
			else:
				t1 = m * 1 + c
				t2 = m * 2 + c
				t3 = m * 3 + c
				t4 = m * 4 + c
				t5 = m * 5 + c
			if m==1:
				m = ""
			if c==0:
				expression = str(m) + "n"
			else:
				expression = str(m) + "n" + sign + str(c)
		else:
			if sign==" - ":
				t1 = c - m * 1
				t2 = c - m * 2
				t3 = c - m * 3
				t4 = c - m * 4
				t5 = c - m * 5
			else:
				t1 = c + m * 1
				t2 = c + m * 2
				t3 = c + m * 3
				t4 = c + m * 4
				t5 = c + m * 5
			if m==1:
				m = ""
			if c==0:
				if sign==" - ":
					sign = "-"
				else:
					sign = ""
				expression = sign + str(m) + "n"
			else:
				expression = str(c) + sign + str(m) + "n"
		sequence = str(t1) + ", " + str(t2) + ", " + str(t3) + ", " + str(t4) + ", " + str(t5)	
#write question
		tempquestions.write(explanation + expression)
		tempquestions.write("\n")
#write answer
		tempquestions.write(sequence)


def genseqsubs(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		m = random.randrange(1,7)
		if m==1:
			c = random.randrange(1,7)
		else:
			c = random.randrange(0,7)
		if random.randrange(0,2)==1:
			sign = " - "
		else:
			sign = " + "
		if random.randrange(0,2)==1:
			if sign==" - ":
				t1 = m * 1 - c
				t2 = m * 2 - c
				t3 = m * 3 - c
				t4 = m * 4 - c
				t5 = m * 5 - c
			else:
				t1 = m * 1 + c
				t2 = m * 2 + c
				t3 = m * 3 + c
				t4 = m * 4 + c
				t5 = m * 5 + c
			if m==1:
				m = ""
			if c==0:
				expression = str(m) + "n"
			else:
				expression = str(m) + "n" + sign + str(c)
		else:
			if sign==" - ":
				t1 = c - m * 1
				t2 = c - m * 2
				t3 = c - m * 3
				t4 = c - m * 4
				t5 = c - m * 5
			else:
				t1 = c + m * 1
				t2 = c + m * 2
				t3 = c + m * 3
				t4 = c + m * 4
				t5 = c + m * 5
			if m==1:
				m = ""
			if c==0:
				if sign==" - ":
					sign = "-"
				else:
					sign = ""
				expression = sign + str(m) + "n"
			else:
				expression = str(c) + sign + str(m) + "n"
		sequence = [t1,t2,t3,t4,t5]
		n = random.randrange(1,6)
#write question
		tempquestions.write("Calculate " +  expression + " when \\mbox{n = " + str(n) + "}")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(sequence[n-1]))



def nthtermpos(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the nth term of the sequence "
		else:
			explanation = ""
		m = random.randrange(1,7)
		if m==1:
			c = random.randrange(1,7) * (-1)**random.randrange(1,3)
		else:
			c = random.randrange(0,7) * (-1)**random.randrange(1,3)
		if c<0:
			sign = " - "
		else:
			sign = " + "
		t1 = m * 1 + c
		t2 = m * 2 + c
		t3 = m * 3 + c
		t4 = m * 4 + c
		t5 = m * 5 + c
		if m==1:
			m = ""
		elif m==-1:
			m = "-"
		if c==0:
			expression = str(m) + "n"
		else:
			expression = str(m) + "n" + sign + str(abs(c))

		sequence = str(t1) + ", " + str(t2) + ", " + str(t3) + ", " + str(t4) + ", " + str(t5)	
#write question
		tempquestions.write(explanation + sequence)
		tempquestions.write("\n")
#write answer
		tempquestions.write(expression)


def nthtermneg(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the nth term of the sequence "
		else:
			explanation = ""
		m = random.randrange(1,7) * (-1)
		if m==1:
			c = random.randrange(1,7) * (-1)**random.randrange(1,3)
		else:
			c = random.randrange(0,7) * (-1)**random.randrange(1,3)
		if c<0:
			sign = " - "
		else:
			sign = " + "
		t1 = m * 1 + c
		t2 = m * 2 + c
		t3 = m * 3 + c
		t4 = m * 4 + c
		t5 = m * 5 + c
		if m==1:
			m = ""
		elif m==-1:
			m = "-"
		if c==0:
			expression = str(m) + "n"
		else:
			expression = str(m) + "n" + sign + str(abs(c))

		sequence = "\\mbox{" + str(t1) + ", " + str(t2) + ", " + str(t3) + ", " + str(t4) + ", " + str(t5) + "}"	
#write question
		tempquestions.write(explanation + sequence)
		tempquestions.write("\n")
#write answer
		tempquestions.write(expression)



def nthterm(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the nth term of the sequence "
		else:
			explanation = ""
		m = random.randrange(1,7) * (-1)**random.randrange(1,3)
		if m==1:
			c = random.randrange(1,7) * (-1)**random.randrange(1,3)
		else:
			c = random.randrange(0,7) * (-1)**random.randrange(1,3)
		if c<0:
			sign = " - "
		else:
			sign = " + "
		t1 = m * 1 + c
		t2 = m * 2 + c
		t3 = m * 3 + c
		t4 = m * 4 + c
		t5 = m * 5 + c
		if m==1:
			m = ""
		elif m==-1:
			m = "-"
		if c==0:
			expression = str(m) + "n"
		else:
			expression = str(m) + "n" + sign + str(abs(c))

		sequence = "\\mbox{" + str(t1) + ", " + str(t2) + ", " + str(t3) + ", " + str(t4) + ", " + str(t5) + "}"	
#write question
		tempquestions.write(explanation + sequence)
		tempquestions.write("\n")
#write answer
		tempquestions.write(expression)


def genseqquad1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Write out the first three terms of the sequence "
		else:
			explanation = ""
		a = random.randrange(1,7)
		c = random.randrange(1,10) * (-1)**random.randrange(1,3)
		if c<0:
			sign = " - "
		else:
			sign = " + "
		t1 = a * 1 + c
		t2 = a * 4 + c
		t3 = a * 9 + c
		if a==1:
			a = ""
		elif a==-1:
			a = "-"
		expression = str(a) + "n$^{2}$" + sign + str(abs(c))
		sequence = str(t1) + ", " + str(t2) + ", " + str(t3)
#write question
		tempquestions.write(explanation + expression)
		tempquestions.write("\n")
#write answer
		tempquestions.write(sequence)


def genseqquad2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Write out the first three terms of the sequence "
		else:
			explanation = ""
		a = 1
		b = random.randrange(1,10) * (-1)**random.randrange(1,3)
		if b<0:
			sign = " - "
		else:
			sign = " + "
		t1 = a * 1 + b
		t2 = a * 4 + b * 2
		t3 = a * 9 + b * 3
		if a==1:
			a = ""
		elif a==-1:
			a = "-"
		b = abs(b)
		if b==1:
			b = ""
		expression = str(a) + "n$^{2}$" + sign + str(b) + "n"
		sequence = str(t1) + ", " + str(t2) + ", " + str(t3)
#write question
		tempquestions.write(explanation + expression)
		tempquestions.write("\n")
#write answer
		tempquestions.write(sequence)


def genseqquad3(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Write out the first three terms of the sequence "
		else:
			explanation = ""
		a = random.randrange(1,7)
		b = random.randrange(1,10) * (-1)**random.randrange(1,3)
		if b<0:
			sign = " - "
		else:
			sign = " + "
		t1 = a * 1 + b
		t2 = a * 4 + b * 2
		t3 = a * 9 + b * 3
		if a==1:
			a = ""
		elif a==-1:
			a = "-"
		b = abs(b)
		if b==1:
			b = ""
		expression = str(a) + "n$^{2}$" + sign + str(b) + "n"
		sequence = str(t1) + ", " + str(t2) + ", " + str(t3)
#write question
		tempquestions.write(explanation + expression)
		tempquestions.write("\n")
#write answer
		tempquestions.write(sequence)


def genseqquad4(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Write out the first three terms of the sequence "
		else:
			explanation = ""
		a = 1
		b = random.randrange(1,10) * (-1)**random.randrange(1,3)
		c = random.randrange(1,10) * (-1)**random.randrange(1,3)
		if b<0:
			sign = " - "
		else:
			sign = " + "
		if c<0:
			sign2 = " - "
		else:
			sign2 = " + "
		t1 = a * 1 + b + c
		t2 = a * 4 + b * 2 + c
		t3 = a * 9 + b * 3 + c
		if a==1:
			a = ""
		elif a==-1:
			a = "-"
		b = abs(b)
		c = abs(c)
		if b==1:
			b = ""
		expression = str(a) + "n$^{2}$" + sign + str(b) + "n" + sign2 + str(c)
		sequence = str(t1) + ", " + str(t2) + ", " + str(t3)
#write question
		tempquestions.write(explanation + expression)
		tempquestions.write("\n")
#write answer
		tempquestions.write(sequence)


def genseqquad5(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Write out the first three terms of the sequence "
		else:
			explanation = ""
		a = random.randrange(1,7)
		b = random.randrange(1,10) * (-1)**random.randrange(1,3)
		c = random.randrange(1,10) * (-1)**random.randrange(1,3)
		if b<0:
			sign = " - "
		else:
			sign = " + "
		if c<0:
			sign2 = " - "
		else:
			sign2 = " + "
		t1 = a * 1 + b + c
		t2 = a * 4 + b * 2 + c
		t3 = a * 9 + b * 3 + c
		if a==1:
			a = ""
		elif a==-1:
			a = "-"
		b = abs(b)
		c = abs(c)
		if b==1:
			b = ""
		expression = str(a) + "n$^{2}$" + sign + str(b) + "n" + sign2 + str(c)
		sequence = str(t1) + ", " + str(t2) + ", " + str(t3)
#write question
		tempquestions.write(explanation + expression)
		tempquestions.write("\n")
#write answer
		tempquestions.write(sequence)


def nthtermquad1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the nth term of "
		else:
			explanation = ""
		a = random.randrange(1,7)
		c = random.randrange(1,10) * (-1)**random.randrange(1,3)
		if c<0:
			sign = " - "
		else:
			sign = " + "
		t1 = a * 1 + c
		t2 = a * 4 + c
		t3 = a * 9 + c
		t4 = a * 16 + c
		t5 = a * 25 + c
		if a==1:
			a = ""
		elif a==-1:
			a = "-"
		expression = str(a) + "n$^{2}$" + sign + str(abs(c))
		sequence = str(t1) + ", " + str(t2) + ", " + str(t3) + ", " + str(t4) + ", " + str(t5)
#write question
		tempquestions.write(explanation + sequence)
		tempquestions.write("\n")
#write answer
		tempquestions.write(expression)


def nthtermquad2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the nth term of "
		else:
			explanation = ""
		a = 1
		b = random.randrange(1,10) * (-1)**random.randrange(1,3)
		if b<0:
			sign = " - "
		else:
			sign = " + "
		t1 = a * 1 + b
		t2 = a * 4 + b * 2
		t3 = a * 9 + b * 3
		t4 = a * 16 + b * 4
		t5 = a * 25 + b * 5
		if a==1:
			a = ""
		elif a==-1:
			a = "-"
		b = abs(b)
		if b==1:
			b = ""
		expression = str(a) + "n$^{2}$" + sign + str(b) + "n"
		sequence = str(t1) + ", " + str(t2) + ", " + str(t3) + ", " + str(t4) + ", " + str(t5)
#write question
		tempquestions.write(explanation + sequence)
		tempquestions.write("\n")
#write answer
		tempquestions.write(expression)


def nthtermquad3(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the nth term of "
		else:
			explanation = ""
		a = random.randrange(1,7)
		b = random.randrange(1,10) * (-1)**random.randrange(1,3)
		if b<0:
			sign = " - "
		else:
			sign = " + "
		t1 = a * 1 + b
		t2 = a * 4 + b * 2
		t3 = a * 9 + b * 3
		t4 = a * 16 + b * 4
		t5 = a * 25 + b * 5
		if a==1:
			a = ""
		elif a==-1:
			a = "-"
		b = abs(b)
		if b==1:
			b = ""
		expression = str(a) + "n$^{2}$" + sign + str(b) + "n"
		sequence = str(t1) + ", " + str(t2) + ", " + str(t3) + ", " + str(t4) + ", " + str(t5)
#write question
		tempquestions.write(explanation + sequence)
		tempquestions.write("\n")
#write answer
		tempquestions.write(expression)


def nthtermquad4(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the nth term of "
		else:
			explanation = ""
		a = 1
		b = random.randrange(1,10) * (-1)**random.randrange(1,3)
		c = random.randrange(1,10) * (-1)**random.randrange(1,3)
		if b<0:
			sign = " - "
		else:
			sign = " + "
		if c<0:
			sign2 = " - "
		else:
			sign2 = " + "
		t1 = a * 1 + b + c
		t2 = a * 4 + b * 2 + c
		t3 = a * 9 + b * 3 + c
		t4 = a * 16 + b * 4 + c
		t5 = a * 25 + b * 5 + c
		if a==1:
			a = ""
		elif a==-1:
			a = "-"
		b = abs(b)
		c = abs(c)
		if b==1:
			b = ""
		expression = str(a) + "n$^{2}$" + sign + str(b) + "n" + sign2 + str(c)
		sequence = str(t1) + ", " + str(t2) + ", " + str(t3) + ", " + str(t4) + ", " + str(t5)
#write question
		tempquestions.write(explanation + sequence)
		tempquestions.write("\n")
#write answer
		tempquestions.write(expression)


def nthtermquad5(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the nth term of "
		else:
			explanation = ""
		a = random.randrange(1,7)
		b = random.randrange(1,10) * (-1)**random.randrange(1,3)
		c = random.randrange(1,10) * (-1)**random.randrange(1,3)
		if b<0:
			sign = " - "
		else:
			sign = " + "
		if c<0:
			sign2 = " - "
		else:
			sign2 = " + "
		t1 = a * 1 + b + c
		t2 = a * 4 + b * 2 + c
		t3 = a * 9 + b * 3 + c
		t4 = a * 16 + b * 4 + c
		t5 = a * 25 + b * 5 + c
		if a==1:
			a = ""
		elif a==-1:
			a = "-"
		b = abs(b)
		c = abs(c)
		if b==1:
			b = ""
		expression = str(a) + "n$^{2}$" + sign + str(b) + "n" + sign2 + str(c)
		sequence = str(t1) + ", " + str(t2) + ", " + str(t3) + ", " + str(t4) + ", " + str(t5)
#write question
		tempquestions.write(explanation + sequence)
		tempquestions.write("\n")
#write answer
		tempquestions.write(expression)


def geoseqnthterm(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the nth term of "
		else:
			explanation = ""
		num = random.randrange(2,9)
		ratio = random.randrange(2,6)
		t1 = str(num)
		t2 = str(num*ratio)
		t3 = str(num*ratio**2)
		t4 = str(num*ratio**3)
		t5 = str(num*ratio**4)
		answer = str(num) + "$\\times " + str(ratio) + "^{(n-1)}$"
		question = str(t1) + ", " + str(t2) + ", " + str(t3) + ", " + str(t4) + ", " + str(t5)
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def geosurdseqnthterm(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the nth term of "
		else:
			explanation = ""
		num = random.randrange(2,7)
		surds = [2,3,5,6,7]
		surd = random.choice(surds)
		t1 = str(num)
		t2 = str(num) + "$\\sqrt{" + str(surd) + "}$"
		t3 = str(num*surd)
		t4 = str(num*surd) + "$\\sqrt{" + str(surd) + "}$"
		t5 = str(num*surd*surd)
		answer = str(num) + "$\\sqrt{" + str(surd) + "}^{(n-1)}$"
		question = str(t1) + ", " + str(t2) + ", " + str(t3) + ", " + str(t4) + ", " + str(t5)
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def nthtermtest(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		explanation = ""
		m = random.randrange(2,7) * (-1)**random.randrange(1,3)
		c = random.randrange(1,10) * (-1)**random.randrange(1,3)
		testnum = random.randrange(15,40)
		test = testnum * m + c
		dec = random.randrange(0,2)
		if dec==0:
			answer = "No"
			diff = random.randrange(1,abs(m))
			test = test + diff * (-1)**random.randrange(1,3)
		else:
			answer = "Yes (" + str(testnum) + ")"
		if c<0:
			sign = " - "
		else:
			sign = " + "
		if m<0 and c>0:
			expression = str(c) + " - " + str(abs(m)) + "n"
		else:
			expression = str(m) + "n" + sign + str(abs(c))
		question = "Is " + str(test) + " a number in the sequence " + expression + "?"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def termtotermiteration(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "The term-to-term rule for a sequence is "
		else:
			explanation = ""
		b = random.randrange(1,10)*(-1)**random.randrange(1,3)
		if b<0:
			sign1 = " - "
		else:
			sign1 = " + "
		c = random.randrange(1,10)*(-1)**random.randrange(1,3)
		if c<0:
			sign2 = " - "
		else:
			sign2 = " + "
		rule = "\\mbox{u$_{n+1}$ = u$_{n}\\hspace{0pt}^{2}$" + sign1 + str(abs(b)) + "u$_{n}$" + sign2 + str(abs(c)) + "}"
		u1 = random.randrange(1,6)
		u2 = u1**2 + u1*b + c
		u3 = u2**2 + u2*b + c
		question = explanation + rule + ". Given that \\mbox{u$_{1}$ = " + str(u1) + "}, find u$_{2}$ and u$_{3}$."
		answer = "u$_{2}$ = " + str(u2) + " and u$_{3}$ = " + str(u3)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def nthtermbuild1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		m = random.randrange(1,7) * (-1)**random.randrange(1,3)
		if m==1:
			c = random.randrange(1,7) * (-1)**random.randrange(1,3)
		else:
			c = random.randrange(0,7) * (-1)**random.randrange(1,3)
		if c<0:
			sign = " - "
		else:
			sign = " + "
		t1 = m * 1 + c
		t2 = m * 2 + c
		t3 = m * 3 + c
		t4 = m * 4 + c
		t5 = m * 5 + c

		if c==0:
			expression = str(m) + "n"
			gap = "$\\rule[-1.5mm]{1cm}{0.15mm}$n"
		else:
			expression = str(m) + "n" + sign + str(abs(c))
			gap = "$\\rule[-1.5mm]{1cm}{0.15mm}$n" + sign + str(abs(c))

		sequence = "\\mbox{" + str(t1) + ", " + str(t2) + ", " + str(t3) + ", " + str(t4) + ", " + str(t5) + "}"
		question = sequence + " $\\rightarrow$  " + gap
		answer = expression
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def nthtermbuild2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		m = random.randrange(1,7) * (-1)**random.randrange(1,3)
		if m==1:
			c = random.randrange(1,7) * (-1)**random.randrange(1,3)
		else:
			c = random.randrange(1,7) * (-1)**random.randrange(1,3)
		if c<0:
			sign = " - "
		else:
			sign = " + "
		t1 = m * 1 + c
		t2 = m * 2 + c
		t3 = m * 3 + c
		t4 = m * 4 + c
		t5 = m * 5 + c

		if c==0:
			expression = str(m) + "n"
			gap = "$\\rule[-1.5mm]{1cm}{0.15mm}$n"
		else:
			expression = str(m) + "n" + sign + str(abs(c))
			if sign==" - ":
				sign = ""
			gap = str(m) + "n" + sign + "$\\rule[-1.5mm]{1cm}{0.15mm}$"

		sequence = "\\mbox{" + str(t1) + ", " + str(t2) + ", " + str(t3) + ", " + str(t4) + ", " + str(t5) + "}"
		question = sequence + " $\\rightarrow$  " + gap
		answer = expression
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def nthtermbuild3(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		m = random.randrange(1,7) * (-1)**random.randrange(1,3)
		if m==1:
			c = random.randrange(1,7) * (-1)**random.randrange(1,3)
		else:
			c = random.randrange(1,7) * (-1)**random.randrange(1,3)
		if c<0:
			sign = " - "
		else:
			sign = " + "
		t1 = m * 1 + c
		t2 = m * 2 + c
		t3 = m * 3 + c
		t4 = m * 4 + c
		t5 = m * 5 + c

		if c==0:
			expression = str(m) + "n"
			gap = "$\\rule[-1.5mm]{1cm}{0.15mm}$n"
		else:
			expression = str(m) + "n" + sign + str(abs(c))
			if sign==" - ":
				sign = ""
			gap = "$\\rule[-1.5mm]{1cm}{0.15mm}$n" + sign + "$\\rule[-1.5mm]{1cm}{0.15mm}$"

		sequence = "\\mbox{" + str(t1) + ", " + str(t2) + ", " + str(t3) + ", " + str(t4) + ", " + str(t5) + "}"
		question = sequence + " $\\rightarrow$  " + gap
		answer = expression
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def nthtermbuild4(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		m = random.randrange(1,7) * (-1)**random.randrange(1,3)
		if m==1:
			c = random.randrange(1,7) * (-1)**random.randrange(1,3)
		else:
			c = random.randrange(1,7) * (-1)**random.randrange(1,3)
		if c<0:
			sign = " - "
		else:
			sign = " + "
		t1 = m * 1 + c
		t2 = m * 2 + c
		t3 = m * 3 + c
		t4 = m * 4 + c
		t5 = m * 5 + c

		if c==0:
			expression = str(m) + "n"
		else:
			expression = str(m) + "n" + sign + str(abs(c))
		sequence = "\\mbox{" + str(t1) + ", " + str(t2) + ", " + str(t3) + ", " + str(t4) + ", " + str(t5) + "}"
		gap = "$\\rule[-1.5mm]{2cm}{0.15mm}$"
		question = sequence + " $\\rightarrow$  " + gap
		answer = expression
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def genseq1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		m = random.randrange(1,7)
		if m==1:
			c = random.randrange(1,7)
		else:
			c = random.randrange(0,7)
		if random.randrange(0,2)==1:
			sign = " - "
		else:
			sign = " + "
		if random.randrange(0,2)==1:
			if sign==" - ":
				t1 = m * 1 - c
				t2 = m * 2 - c
				t3 = m * 3 - c
				t4 = m * 4 - c
				t5 = m * 5 - c
			else:
				t1 = m * 1 + c
				t2 = m * 2 + c
				t3 = m * 3 + c
				t4 = m * 4 + c
				t5 = m * 5 + c
			if m==1:
				m = ""
			if c==0:
				expression = str(m) + "n"
			else:
				expression = str(m) + "n" + sign + str(c)
		else:
			if sign==" - ":
				t1 = c - m * 1
				t2 = c - m * 2
				t3 = c - m * 3
				t4 = c - m * 4
				t5 = c - m * 5
			else:
				t1 = c + m * 1
				t2 = c + m * 2
				t3 = c + m * 3
				t4 = c + m * 4
				t5 = c + m * 5
			if m==1:
				m = ""
			if c==0:
				if sign==" - ":
					sign = "-"
				else:
					sign = ""
				expression = sign + str(m) + "n"
			else:
				expression = str(c) + sign + str(m) + "n"
		sequence = str(t1) + ", " + str(t2) + ", " + str(t3) + ", " + str(t4) + ", " + str(t5)
		question = "Find the value of " + expression + " when: \\\\ a) n = 1 \\\\ b) n = 2 \\\\ c) n = 3 \\\\ d) n = 4 \\\\ e) n = 5"
		answer = "a) " + str(t1) + "\\\\ b) " + str(t2) + "\\\\ c) " + str(t3) + "\\\\ d) " + str(t4) + "\\\\ e) " + str(t5)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
