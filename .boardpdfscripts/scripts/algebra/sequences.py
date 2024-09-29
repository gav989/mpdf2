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

		sequence = str(t1) + ", " + str(t2) + ", " + str(t3) + ", " + str(t4) + ", " + str(t5)	
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
