#cubis.py
def expandcubics1pos(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		e = random.randrange(1,13)
		f = random.randrange(1,13)
		g = random.randrange(1,13)
		b = e + f + g
		c = e*f + e*g + f*g
		d = e*f*g
		question = "(x + " + str(e) + ")(x + " + str(f) + ")(x + " + str(g) + ")"
		if b==1:
			b = ""
		if c==1:
			c = ""
		answer = "$x^{3} + " + str(b) + "x^{2} + " + str(c) + "x + " + str(d) + "$"
		
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def expandcubics1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		e = random.randrange(1,13) * (-1)**random.randrange(1,3)
		f = random.randrange(1,13) * (-1)**random.randrange(1,3)
		g = random.randrange(1,13) * (-1)**random.randrange(1,3)
		b = e + f + g
		c = e*f + e*g + f*g
		d = e*f*g
		aterm = "x^{3}"
		if b==0:
			bterm = ""
		elif b==1:
			bterm = " + x^{2}"
		elif b==-1:
			bterm = " - x^{2}"
		elif b>0:
			bterm = " + "  + str(b) + "x^{2}"
		else:
			bterm = " - " + str(abs(b)) + "x^{2}"
		if c==0:
			cterm = ""
		elif c==1:
			cterm = " + x^{2}"
		elif c==-1:
			cterm = " - x^{2}"
		elif c>0:
			cterm = " + " + str(c) + "x"
		else:
			cterm = " - " + str(abs(c)) + "x"
		if d>0:
			dterm = " + " + str(d)
		else:
			dterm = " - "+  str(abs(d))
		if e<0:
			ebrac = "(x - " + str(abs(e)) + ")"
		else:
			ebrac = "(x + " + str(e) + ")"
		if f<0:
			fbrac = "(x - " + str(abs(f)) + ")"
		else:
			fbrac = "(x + " + str(f) + ")"
		if g<0:
			gbrac = "(x - " + str(abs(g)) + ")"
		else:
			gbrac = "(x + " + str(g) + ")"
		question = ebrac + fbrac + gbrac
		answer = "$" + aterm + bterm + cterm + dterm + "$"
		
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def expandcubics2pos(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		e = random.randrange(1,5)
		f = random.randrange(1,7)
		g = random.randrange(1,5)
		h = random.randrange(1,7)
		i = random.randrange(1,5)
		j = random.randrange(1,7)
		if e==1 and g==1 and i==1:
			e = random.randrange(2,6)
		a = e*g*i
		b = i*f*g + e*h*i + e*g*j
		c = f*h*i + j*f*g + e*h*j
		d = f*h*j
		if a==1:
			b = ""
		if b==1:
			b = ""
		if c==1:
			c = ""
		if e==1:
			e = ""
		if g==1:
			g = ""
		if i==1:
			i = ""
		question = "(" + str(e) + "x + " + str(f) + ")(" + str(g) + "x + " + str(h) + ")(" + str(i) + "x + " + str(j) + ")"
		answer = str(a) + "$x^{3} + " + str(b) + "x^{2} + " + str(c) + "x + " + str(d) + "$"
		
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def expandcubics2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		e = random.randrange(1,5)
		f = random.randrange(1,7) * (-1)**random.randrange(1,3)
		g = random.randrange(1,5)
		h = random.randrange(1,7) * (-1)**random.randrange(1,3)
		i = random.randrange(1,5)
		j = random.randrange(1,7) * (-1)**random.randrange(1,3)
		if e==1 and g==1 and i==1:
			e = random.randrange(2,6)
		a = e*g*i
		b = i*f*g + e*h*i + e*g*j
		c = f*h*i + j*f*g + e*h*j
		d = f*h*j
		aterm = str(a) + "x^{3}"
		if b==0:
			bterm = ""
		elif b==1:
			bterm = " + x^{2}"
		elif b==-1:
			bterm = " - x^{2}"
		elif b>0:
			bterm = " + "  + str(b) + "x^{2}"
		else:
			bterm = " - " + str(abs(b)) + "x^{2}"
		if c==0:
			cterm = ""
		elif c==1:
			cterm = " + x^{2}"
		elif c==-1:
			cterm = " - x^{2}"
		elif c>0:
			cterm = " + " + str(c) + "x"
		else:
			cterm = " - " + str(abs(c)) + "x"
		if d>0:
			dterm = " + " + str(d)
		else:
			dterm = " - "+  str(abs(d))
		if e==1:
			e = ""
		if g==1:
			g = ""
		if i==1:
			i = ""
		if f<1:
			ebrac = "(" + str(e) + "x - " + str(abs(f)) + ")"
		else:
			ebrac = "(" + str(e) + "x + " + str(f) + ")"
		if h<1:
			gbrac = "(" + str(g) + "x - " + str(abs(h)) + ")"
		else:
			gbrac = "(" + str(g) + "x + " + str(h) + ")"
		if j<1:
			ibrac = "(" + str(i) + "x - " + str(abs(j)) + ")"
		else:
			ibrac = "(" + str(i) + "x + " + str(j) + ")"
		question = ebrac + gbrac + ibrac
		answer = "$" + aterm + bterm + cterm + dterm + "$"
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
