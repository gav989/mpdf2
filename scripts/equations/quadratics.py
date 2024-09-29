#quadratics.py

def quadprep1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation = "Find a and b: "
		else:
			explanation = ""
		a = random.randrange(1,13)
		b = random.randrange(1,13)
#write question
		tempquestions.write(explanation + "a + b = " + str(a + b) + " and ab = " + str(a*b) )
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a) + " and " + str(b))

def quadprep2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation = "Find a and b: "
		else:
			explanation = ""
		a = random.randrange(1,13)*(-1)**random.randrange(1,3)
		b = random.randrange(1,13)*(-1)**random.randrange(1,3)
#write question
		tempquestions.write(explanation + "a + b = " + str(a + b) + " and ab = " + str(a*b) )
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a) + " and " + str(b))


def quadprep3(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation = "Find a and b: "
		else:
			explanation = ""
		tailoring1 = list(range(-5,6))
		tailoring1.remove(0)
		tailoring2 = list(range(-5,6))
		tailoring2.remove(0)
		d = random.randrange(1,4)
		if d==1:
			f = random.randrange(2,7)
		else:
			f = random.randrange(1,4)
		if d>1:
			tailoring1.remove(d)
			tailoring1.remove(d*-1)
		if 1<f<6:
			tailoring2.remove(f)
			tailoring2.remove(f*-1)
		e = random.choice(tailoring1)
		g = random.choice(tailoring2)
		a = e*f
		b = d*g
#write question
		tempquestions.write(explanation + "a + b = " + str(a + b) + " and ab = " + str(a*b) )
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a) + " and " + str(b))


def expandquadraticspos(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		mylist=list(range(1,13))
		d = 1
		e = random.choice(mylist)
		f = 1
		g = random.choice(mylist)
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if g<0:
			sign2 = " - "
		else:
			sign2 = " + "
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""

#write question
		tempquestions.write(explanation + "$(x" + sign1 + str(e) + ")(x" + sign2 + str(g) + ")$" )
		tempquestions.write("\n")
#write answer
		if b==0:
			tempquestions.write("$x^2" + sign4 + str(c) + "$")
		else:
			tempquestions.write("$x^2" + sign3 + str(b) + "x" + sign4 + str(c) + "$")



def expandquadraticsneg(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		mylist=list(range(-12,13))
		mylist.remove(0)
		d = 1
		e = random.choice(mylist)
		f = 1
		if e>0:
			mylist = list(range(-12,0))
		g = random.choice(mylist)
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if g<0:
			sign2 = " - "
		else:
			sign2 = " + "
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""

#write question
		tempquestions.write(explanation + "$(x" + sign1 + str(e) + ")(x" + sign2 + str(g) + ")$" )
		tempquestions.write("\n")
#write answer
		if b==0:
			tempquestions.write("$x^2" + sign4 + str(c) + "$")
		else:
			tempquestions.write("$x^2" + sign3 + str(b) + "x" + sign4 + str(c) + "$")



def expandquadratics1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		mylist=list(range(-12,13))
		mylist.remove(0)
		d = 1
		e = random.choice(mylist)
		f = 1
		g = random.choice(mylist)
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if g<0:
			sign2 = " - "
		else:
			sign2 = " + "
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""

#write question
		tempquestions.write(explanation + "\\mbox{$(x" + sign1 + str(e) + ")(x" + sign2 + str(g) + ")$}" )
		tempquestions.write("\n")
#write answer
		if b==0:
			tempquestions.write("$x^2" + sign4 + str(c) + "$")
		else:
			tempquestions.write("$x^2" + sign3 + str(b) + "x" + sign4 + str(c) + "$")

def expandquadratics2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		tailoring1 = list(range(-5,6))
		tailoring1.remove(0)
		tailoring2 = list(range(-5,6))
		tailoring2.remove(0)
		d = random.randrange(1,4)
		if d==1:
			f = random.randrange(2,7)
		else:
			f = random.randrange(1,4)
		if d>1:
			tailoring1.remove(d)
			tailoring1.remove(d*-1)
		if 1<f<6:
			tailoring2.remove(f)
			tailoring2.remove(f*-1)
		e = random.choice(tailoring1)
		g = random.choice(tailoring2)
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if g<0:
			sign2 = " - "
		else:
			sign2 = " + "
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""
		if d==1:
			d = ""
		if f==1:
			f = ""
#write question
		tempquestions.write(explanation + "$(" + str(d) + "x" + sign1 + str(e) + ")(" + str(f) + "x" + sign2 + str(g) + ")$" )
		tempquestions.write("\n")
#write answer
		if b==0:
			tempquestions.write("$" + str(a) + "x^2" + sign4 + str(c) + "$")
		else:
			tempquestions.write("$" + str(a) + "x^2" + sign3 + str(b) + "x" + sign4 + str(c) + "$")

def expandquadraticsdots1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		mylist=list(range(-12,13))
		mylist.remove(0)
		d = 1
		e = random.choice(mylist)
		f = 1
		g = e*-1
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if g<0:
			sign2 = " - "
		else:
			sign2 = " + "
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""

#write question
		tempquestions.write(explanation + "$(x" + sign1 + str(e) + ")(x" + sign2 + str(g) + ")$" )
		tempquestions.write("\n")
#write answer
		if b==0:
			tempquestions.write("$x^2" + sign4 + str(c) + "$")
		else:
			tempquestions.write("$x^2" + sign3 + str(b) + "x" + sign4 + str(c) + "$")



def expandquadraticsdots2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		tailoring1 = list(range(-10,11))
		tailoring1.remove(0)
		d = random.randrange(2,11)
		e = random.choice(tailoring1)
		f = d
		g = 0 - e
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if g<0:
			sign2 = " - "
		else:
			sign2 = " + "
		a = d*f
		c = e*e
		e = abs(e)
		g = abs(g)
#write question
		tempquestions.write(explanation + "$(" + str(d) + "x" + sign1 + str(e) + ")(" + str(f) + "x" + sign2 + str(g) + ")$" )
		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(a) + "x^2 - " + str(c) + "$")


def expandquadraticssquared1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		mylist=list(range(-12,13))
		mylist.remove(0)
		d = 1
		e = random.choice(mylist)
		f = 1
		g = e
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""
#write question
		tempquestions.write(explanation + "$(x" + sign1 + str(e) + ")^2$" )
		tempquestions.write("\n")
#write answer
		if b==0:
			tempquestions.write("$x^2" + sign4 + str(c) + "$")
		else:
			tempquestions.write("$x^2" + sign3 + str(b) + "x" + sign4 + str(c) + "$")


def expandquadraticssquared2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		mylist=list(range(-12,13))
		mylist.remove(0)
		d = random.randrange(2,8)
		e = random.choice(mylist)
		f = d
		g = e
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""
#write question
		tempquestions.write(explanation + "$(" + str(d) + "x" + sign1 + str(e) + ")^2$" )
		tempquestions.write("\n")
#write answer
		if b==0:
			tempquestions.write(str(a) + "$x^2" + sign4 + str(c) + "$")
		else:
			tempquestions.write(str(a) + "$x^2" + sign3 + str(b) + "x" + sign4 + str(c) + "$")




def factorisequadratics1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise "
		else:
			explanation = ""
		mylist=list(range(-12,13))
		mylist.remove(0)
		d = 1
		e = random.choice(mylist)
		mylist.remove(e*-1)
		f = 1
		g = random.choice(mylist)
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if g<0:
			sign2 = " - "
		else:
			sign2 = " + "
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""
#write question
		if b==0:
			tempquestions.write(explanation + "$x^2" + sign4 + str(c) + "$")
		else:
			tempquestions.write(explanation + "$x^2" + sign3 + str(b) + "x" + sign4 + str(c) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$(x" + sign1 + str(e) + ")(x" + sign2 + str(g) + ")$" )



def factorisequadratics1pospos(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise "
		else:
			explanation = ""
		mylist=list(range(1,13))
		d = 1
		e = random.choice(mylist)
		f = 1
		g = random.choice(mylist)
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if g<0:
			sign2 = " - "
		else:
			sign2 = " + "
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""
#write question
		if b==0:
			tempquestions.write(explanation + "$x^2" + sign4 + str(c) + "$")
		else:
			tempquestions.write(explanation + "$x^2" + sign3 + str(b) + "x" + sign4 + str(c) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$(x" + sign1 + str(e) + ")(x" + sign2 + str(g) + ")$" )



def factorisequadratics1posneg(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise "
		else:
			explanation = ""
		mylist=list(range(1,13))
		d = 1
		e = random.choice(mylist)
		mylist.remove(e)
		f = 1
		g = random.choice(mylist) * (-1)
		if random.randrange(0,2)==1:
			temp = g
			g = e
			e = temp
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if g<0:
			sign2 = " - "
		else:
			sign2 = " + "
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""
#write question
		if b==0:
			tempquestions.write(explanation + "$x^2" + sign4 + str(c) + "$")
		else:
			tempquestions.write(explanation + "$x^2" + sign3 + str(b) + "x" + sign4 + str(c) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$(x" + sign1 + str(e) + ")(x" + sign2 + str(g) + ")$" )



def factorisequadratics1negneg(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise "
		else:
			explanation = ""
		mylist=list(range(-12,0))
		d = 1
		e = random.choice(mylist)
		f = 1
		g = random.choice(mylist)
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if g<0:
			sign2 = " - "
		else:
			sign2 = " + "
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""
#write question
		if b==0:
			tempquestions.write(explanation + "$x^2" + sign4 + str(c) + "$")
		else:
			tempquestions.write(explanation + "$x^2" + sign3 + str(b) + "x" + sign4 + str(c) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$(x" + sign1 + str(e) + ")(x" + sign2 + str(g) + ")$" )



def factorisequadratics2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise "
		else:
			explanation = ""
		tailoring1 = list(range(-5,6))
		tailoring1.remove(0)
		tailoring2 = list(range(-5,6))
		tailoring2.remove(0)
		d = random.randrange(1,4)
		if d==1:
			f = random.randrange(2,7)
		else:
			f = random.randrange(1,4)
		if d>1:
			tailoring1.remove(d)
			tailoring1.remove(d*-1)
		if 1<f<6:
			tailoring2.remove(f)
			tailoring2.remove(f*-1)
		if d==2:
			tailoring1.remove(4)
			tailoring1.remove(-4)
		if d==4:
			tailoring1.remove(2)
			tailoring1.remove(-2)
		if f==2:
			tailoring2.remove(4)
			tailoring2.remove(-4)
		if f==4:
			tailoring2.remove(2)
			tailoring2.remove(-2)
		e = random.choice(tailoring1)
		if (0-e) in tailoring2:
			tailoring2.remove(0-e)
		g = random.choice(tailoring2)
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if g<0:
			sign2 = " - "
		else:
			sign2 = " + "
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""
		if d==1:
			d = ""
		if f==1:
			f = ""
#write question
		if b==0:
			tempquestions.write(explanation + "$" + str(a) + "x^2" + sign4 + str(c) + "$")
		else:
			tempquestions.write(explanation + "$" + str(a) + "x^2" + sign3 + str(b) + "x" + sign4 + str(c) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$(" + str(d) + "x" + sign1 + str(e) + ")(" + str(f) + "x" + sign2 + str(g) + ")$" )



def factorisequadratics2pospos(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise "
		else:
			explanation = ""
		tailoring1 = list(range(1,6))
		tailoring2 = list(range(1,6))
		d = random.randrange(1,4)
		if d==1:
			f = random.randrange(2,7)
		else:
			f = random.randrange(1,4)
		if d>1:
			tailoring1.remove(d)
		if 1<f<6:
			tailoring2.remove(f)
		if d==2:
			tailoring1.remove(4)
		if d==4:
			tailoring1.remove(2)
		if f==2:
			tailoring2.remove(4)
		if f==4:
			tailoring2.remove(2)
		e = random.choice(tailoring1)
		g = random.choice(tailoring2)
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if g<0:
			sign2 = " - "
		else:
			sign2 = " + "
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""
		if d==1:
			d = ""
		if f==1:
			f = ""
#write question
		if b==0:
			tempquestions.write(explanation + "$" + str(a) + "x^2" + sign4 + str(c) + "$")
		else:
			tempquestions.write(explanation + "$" + str(a) + "x^2" + sign3 + str(b) + "x" + sign4 + str(c) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$(" + str(d) + "x" + sign1 + str(e) + ")(" + str(f) + "x" + sign2 + str(g) + ")$" )



def factorisequadratics2posneg(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise "
		else:
			explanation = ""
		tailoring1 = list(range(-5,0))
		tailoring2 = list(range(1,6))
		d = random.randrange(1,4)
		if d==1:
			f = random.randrange(2,7)
		else:
			f = random.randrange(1,4)
		if d>1:
			tailoring1.remove(d*-1)
		if 1<f<6:
			tailoring2.remove(f)
		if d==2:
			tailoring1.remove(-4)
		if d==4:
			tailoring1.remove(-2)
		if f==2:
			tailoring2.remove(4)
		if f==4:
			tailoring2.remove(2)
		e = random.choice(tailoring1)
		if (0-e) in tailoring2:
			tailoring2.remove(0-e)
		g = random.choice(tailoring2)
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if g<0:
			sign2 = " - "
		else:
			sign2 = " + "
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""
		if d==1:
			d = ""
		if f==1:
			f = ""
#write question
		if b==0:
			tempquestions.write(explanation + "$" + str(a) + "x^2" + sign4 + str(c) + "$")
		else:
			tempquestions.write(explanation + "$" + str(a) + "x^2" + sign3 + str(b) + "x" + sign4 + str(c) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$(" + str(d) + "x" + sign1 + str(e) + ")(" + str(f) + "x" + sign2 + str(g) + ")$" )





def factorisequadratics2negneg(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise "
		else:
			explanation = ""
		tailoring1 = list(range(-5,0))
		tailoring2 = list(range(-5,0))
		d = random.randrange(1,4)
		if d==1:
			f = random.randrange(2,7)
		else:
			f = random.randrange(1,4)
		if d>1:
			tailoring1.remove(d*-1)
		if 1<f<6:
			tailoring2.remove(f*-1)
		if d==2:
			tailoring1.remove(-4)
		if d==4:
			tailoring1.remove(-2)
		if f==2:
			tailoring2.remove(-4)
		if f==4:
			tailoring2.remove(-2)
		e = random.choice(tailoring1)
		g = random.choice(tailoring2)
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if g<0:
			sign2 = " - "
		else:
			sign2 = " + "
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""
		if d==1:
			d = ""
		if f==1:
			f = ""
#write question
		if b==0:
			tempquestions.write(explanation + "$" + str(a) + "x^2" + sign4 + str(c) + "$")
		else:
			tempquestions.write(explanation + "$" + str(a) + "x^2" + sign3 + str(b) + "x" + sign4 + str(c) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$(" + str(d) + "x" + sign1 + str(e) + ")(" + str(f) + "x" + sign2 + str(g) + ")$" )





def factorisequadraticsdots1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation = "Factorise "
		else:
			explanation = ""
		mylist=list(range(-12,13))
		mylist.remove(0)
		d = 1
		e = random.choice(mylist)
		f = 1
		g = e*-1
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if g<0:
			sign2 = " - "
		else:
			sign2 = " + "
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""

#write question
		if b==0:
			tempquestions.write(explanation + "$x^2" + sign4 + str(c) + "$")
		else:
			tempquestions.write(explanation + "$x^2" + sign3 + str(b) + "x" + sign4 + str(c) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$(x" + sign1 + str(e) + ")(x" + sign2 + str(g) + ")$" )



def factorisequadraticsdots2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise "
		else:
			explanation = ""
		tailoring1 = list(range(-10,11))
		tailoring1.remove(0)
		d = random.randrange(2,11)
		e = random.choice(tailoring1)
		f = d
		g = 0 - e
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if g<0:
			sign2 = " - "
		else:
			sign2 = " + "
		a = d*f
		c = e*e
		e = abs(e)
		g = abs(g)
#write question
		tempquestions.write(explanation + "$" + str(a) + "x^2 - " + str(c) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$(" + str(d) + "x" + sign1 + str(e) + ")(" + str(f) + "x" + sign2 + str(g) + ")$" )



def dotswithnumbers(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate "
		else:
			explanation = ""
		base = random.randrange(2,10)*10
		bond = random.randrange(1,10)
		num1 = base + bond
		num2 = base - bond
		question = str(num1) + "$^{2}$ - " + str(num2) + "$^{2}$"
		answer = num1**2 - num2**2
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def solvequadratics1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise and solve "
		else:
			explanation = ""
		mylist=list(range(-12,13))
		mylist.remove(0)
		d = 1
		e = random.choice(mylist)
		mylist.remove(e*-1)
		f = 1
		g = random.choice(mylist)
		if e<0:
			sign1 = 1 
		else:
			sign1 = -1
		if g<0:
			sign2 = 1
		else:
			sign2 = -1
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""
#write question
		if b==0:
			tempquestions.write(explanation + "$x^2" + sign4 + str(c) + " = 0$")
		else:
			tempquestions.write(explanation + "$x^2" + sign3 + str(b) + "x" + sign4 + str(c) + " = 0$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$x = " + str(sign1*e) + "$ and $x = " + str(sign2*g) + "$")



def solvequadraticinequalities1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the range of values for which "
		else:
			explanation = ""
		mylist=list(range(-12,13))
		mylist.remove(0)
		d = 1
		e = random.choice(mylist)
		mylist.remove(e*-1)
		f = 1
		g = random.choice(mylist)
		if e<0:
			sign1 = 1 
		else:
			sign1 = -1
		if g<0:
			sign2 = 1
		else:
			sign2 = -1
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""
		equation = "$x^2" + sign3 + str(b) + "x" + sign4 + str(c)
		x1 = sign1*e
		x2 = sign2*g
		if x2<x1:
			temp = x2
			x2 = x1
			x1 = temp
		dec = random.randrange(0,4)
		if dec==0:
			question = equation + "<0$"
			answer = "$" + str(x1) + "< x <" + str(x2) + "$"
		elif dec==1:
			question = equation + "\\leq0$"
			answer = "$" + str(x1) + "\\leq x \\leq" + str(x2) + "$"
		elif dec==3:
			question = equation + ">0$"
			answer = "$x<" + str(x1) + "$, $x >" + str(x2) + "$"
		else:
			question = equation + "\\geq0$"
			answer = "$ x \\leq" + str(x1) + "$, $ x \\geq" + str(x2) + "$"
#write question
		tempquestions.write(explanation + "\\mbox{" + question + "}")
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def solvequadraticsrearrange1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise and solve "
		else:
			explanation = ""
		mylist=list(range(-12,13))
		mylist.remove(0)
		d = 1
		e = random.choice(mylist)
		mylist.remove(e*-1)
		f = 1
		g = random.choice(mylist)
		if e<0:
			sign1 = 1 
		else:
			sign1 = -1
		if g<0:
			sign2 = 1
		else:
			sign2 = -1
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = ""
		else:
			sign4 = "-"
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""
#write question
		if b==0:
			tempquestions.write(explanation + "$x^2" + " = " + sign4 + str(c) + "$")
		else:
			tempquestions.write(explanation + "$x^2" + sign3 + str(b) + "x = " + sign4 + str(c) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$x = " + str(sign1*e) + "$ and $x = " + str(sign2*g) + "$")

def solvequadratics2(n,explanationn):
	import random
	from fractions import Fraction
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise and solve "
		else:
			explanation = ""
		tailoring1 = list(range(-5,6))
		tailoring1.remove(0)
		tailoring2 = list(range(-5,6))
		tailoring2.remove(0)
		d = random.randrange(1,4)
		if d==1:
			f = random.randrange(2,7)
		else:
			f = random.randrange(1,4)
		if d>1:
			tailoring1.remove(d)
			tailoring1.remove(d*-1)
		if 1<f<6:
			tailoring2.remove(f)
			tailoring2.remove(f*-1)
		e = random.choice(tailoring1)
		g = random.choice(tailoring2)
		if e<0:
			sign1 = ""
		else:
			sign1 = "-"
		if g<0:
			sign2 = ""
		else:
			sign2 = "-"
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		int1 = ""
		int2 = ""
		if e%d==0:
			x1 = str(int(e/d))
		else:
			x1 = Fraction(e,d)
			if x1>1:
				int1 = int(floor(x1))
				x1 = x1 - int1
			x1 = "\\dfrac{" + str(x1.numerator) + "}{" + str(x1.denominator) + "}"
		if g%f==0:
			x2 = str(int(g/f))
		else:
			x2 = Fraction(g,f)
			if x2>1:
				int2 = int(floor(x2))
				x2 = x2 - int2
			x2 = "\\dfrac{" + str(x2.numerator) + "}{" + str(x2.denominator) + "}"
		if b==1:
			b = ""
		if d==1:
			d = ""
		if f==1:
			f = ""

#write question
		if b==0:
			tempquestions.write(explanation + "$" + str(a) + "x^2" + sign4 + str(c) + " = 0$")
		else:
			tempquestions.write(explanation + "$" + str(a) + "x^2" + sign3 + str(b) + "x" + sign4 + str(c) + " = 0$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$x = " + sign1 + str(int1) + x1 + "$ and $x = " + sign2 + str(int2) + x2 + "$")



def solvequadratics2pospos(n,explanationn):
	import random
	from fractions import Fraction
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise and solve "
		else:
			explanation = ""
		tailoring1 = list(range(0,6))
		tailoring1.remove(0)
		tailoring2 = list(range(0,6))
		tailoring2.remove(0)
		d = random.randrange(1,4)
		if d==1:
			f = random.randrange(2,7)
		else:
			f = random.randrange(1,4)
		if d>1:
			tailoring1.remove(d)

		if 1<f<6:
			tailoring2.remove(f)

		e = random.choice(tailoring1)
		g = random.choice(tailoring2)
		if e<0:
			sign1 = ""
		else:
			sign1 = "-"
		if g<0:
			sign2 = ""
		else:
			sign2 = "-"
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		int1 = ""
		int2 = ""
		if e%d==0:
			x1 = str(int(e/d))
		else:
			x1 = Fraction(e,d)
			if x1>1:
				int1 = int(floor(x1))
				x1 = x1 - int1
			x1 = "\\dfrac{" + str(x1.numerator) + "}{" + str(x1.denominator) + "}"
		if g%f==0:
			x2 = str(int(g/f))
		else:
			x2 = Fraction(g,f)
			if x2>1:
				int2 = int(floor(x2))
				x2 = x2 - int2
			x2 = "\\dfrac{" + str(x2.numerator) + "}{" + str(x2.denominator) + "}"
		if b==1:
			b = ""
		if d==1:
			d = ""
		if f==1:
			f = ""

#write question
		if b==0:
			tempquestions.write(explanation + "$" + str(a) + "x^2" + sign4 + str(c) + " = 0$")
		else:
			tempquestions.write(explanation + "$" + str(a) + "x^2" + sign3 + str(b) + "x" + sign4 + str(c) + " = 0$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$x = " + sign1 + str(int1) + x1 + "$ and $x = " + sign2 + str(int2) + x2 + "$")

def solvequadratics2posneg(n,explanationn):
	import random
	from fractions import Fraction
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise and solve "
		else:
			explanation = ""
		tailoring1 = list(range(-5,1))
		tailoring1.remove(0)
		tailoring2 = list(range(0,6))
		tailoring2.remove(0)
		d = random.randrange(1,4)
		if d==1:
			f = random.randrange(2,7)
		else:
			f = random.randrange(1,4)


		if 1<f<6:
			tailoring2.remove(f)

		e = random.choice(tailoring1)
		g = random.choice(tailoring2)
		if e<0:
			sign1 = ""
		else:
			sign1 = "-"
		if g<0:
			sign2 = ""
		else:
			sign2 = "-"
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		int1 = ""
		int2 = ""
		if e%d==0:
			x1 = str(int(e/d))
		else:
			x1 = Fraction(e,d)
			if x1>1:
				int1 = int(floor(x1))
				x1 = x1 - int1
			x1 = "\\dfrac{" + str(x1.numerator) + "}{" + str(x1.denominator) + "}"
		if g%f==0:
			x2 = str(int(g/f))
		else:
			x2 = Fraction(g,f)
			if x2>1:
				int2 = int(floor(x2))
				x2 = x2 - int2
			x2 = "\\dfrac{" + str(x2.numerator) + "}{" + str(x2.denominator) + "}"
		if b==1:
			b = ""
		if d==1:
			d = ""
		if f==1:
			f = ""

#write question
		if b==0:
			tempquestions.write(explanation + "$" + str(a) + "x^2" + sign4 + str(c) + " = 0$")
		else:
			tempquestions.write(explanation + "$" + str(a) + "x^2" + sign3 + str(b) + "x" + sign4 + str(c) + " = 0$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$x = " + sign1 + str(int1) + x1 + "$ and $x = " + sign2 + str(int2) + x2 + "$")

def solvequadratics2negneg(n,explanationn):
	import random
	from fractions import Fraction
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise and solve "
		else:
			explanation = ""
		tailoring1 = list(range(-5,1))
		tailoring1.remove(0)
		tailoring2 = list(range(-5,1))
		tailoring2.remove(0)
		d = random.randrange(1,4)
		if d==1:
			f = random.randrange(2,7)
		else:
			f = random.randrange(1,4)


		e = random.choice(tailoring1)
		g = random.choice(tailoring2)
		if e<0:
			sign1 = ""
		else:
			sign1 = "-"
		if g<0:
			sign2 = ""
		else:
			sign2 = "-"
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		int1 = ""
		int2 = ""
		if e%d==0:
			x1 = str(int(e/d))
		else:
			x1 = Fraction(e,d)
			if x1>1:
				int1 = int(floor(x1))
				x1 = x1 - int1
			x1 = "\\dfrac{" + str(x1.numerator) + "}{" + str(x1.denominator) + "}"
		if g%f==0:
			x2 = str(int(g/f))
		else:
			x2 = Fraction(g,f)
			if x2>1:
				int2 = int(floor(x2))
				x2 = x2 - int2
			x2 = "\\dfrac{" + str(x2.numerator) + "}{" + str(x2.denominator) + "}"
		if b==1:
			b = ""
		if d==1:
			d = ""
		if f==1:
			f = ""

#write question
		if b==0:
			tempquestions.write(explanation + "$" + str(a) + "x^2" + sign4 + str(c) + " = 0$")
		else:
			tempquestions.write(explanation + "$" + str(a) + "x^2" + sign3 + str(b) + "x" + sign4 + str(c) + " = 0$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$x = " + sign1 + str(int1) + x1 + "$ and $x = " + sign2 + str(int2) + x2 + "$")



















def quadraticformula(n,explanationn):
	import random
	from utilities.rounding import rounddp,rounddpstring
	from fractions import Fraction
	from math import floor,ceil,sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Solve "
			explanation2 = ", giving your answer to 2 d.p."
		else:
			explanation1 = ""
			explanation2 = ""
		a = random.randrange(1,6)
		b = random.randrange(1,13) * (-1)**random.randrange(1,3)
		c = random.randrange(floor(b**2/(4*a)) - 8,floor(b**2/(4*a)))
		while c==0:
			c = random.randrange(floor(b**2/(4*a)) - 8,floor(b**2/(4*a)))
		while sqrt(b**2 - 4*a*c)%1==0:
			a = random.randrange(1,6)
			b = random.randrange(1,13) * (-1)**random.randrange(1,3)
			c = random.randrange(floor(b**2/(4*a)) - 8,floor(b**2/(4*a)))
			while c==0:
				c = random.randrange(floor(b**2/(4*a)) - 8,floor(b**2/(4*a)))
		x1 = rounddpstring((-b + sqrt(b**2 - 4*a*c))/(2*a),2)
		x2 = rounddpstring((-b - sqrt(b**2 - 4*a*c))/(2*a),2)
		if b<0:
			sign1 = " - "
			b = abs(b)
		else:
			sign1 = " + "
		if c<0:
			sign2 = " - "
			c = abs(c)
		else:
			sign2 = " + "
		if b==1:
			b = ""
		if a==1:
			a = ""
#write question
		tempquestions.write(explanation1 + "$" + str(a) + "x^2" + sign1 + str(b) + "x" + sign2 + str(c) + " = 0$" + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write("x = " + x1 + " and " + x2)


def completesquare(n,explanationn):
	import random
	from fractions import Fraction
	from math import floor,ceil,sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Write in the form $(x + a)^2 + b$: "
		else:
			explanation = ""
		a = 1
		b = random.randrange(1,7) * 2 * (-1)**random.randrange(1,3)
		c = list(range(-8,20))
		c.remove(0)
		c = random.choice(c) 
		adjuster = int(c - (b/2)**2)
		if b<0:
			sign1 = " - "
			b = abs(b)
		else:
			sign1 = " + "
		if c<0:
			sign2 = " - "
			c = abs(c)
		else:
			sign2 = " + "
		if b==1:
			b = ""
		if a==1:
			a = ""
		if adjuster<0:
			sign3 = " - "
			adjuster = abs(adjuster)
		else:
			sign3 = " + "
#write question
		tempquestions.write(explanation + "$" + str(a) + "x^2" + sign1 + str(b) + "x" + sign2 + str(c) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$(x" + sign1 + str(int(b/2)) + ")^2" + sign3 + str(adjuster) + "$")




def completesquare2(n,explanationn):
	import random
	from fractions import Fraction
	from math import floor,ceil,sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Write in the form $a(x + b)^2 + c$: "
		else:
			explanation = ""
		a = random.randrange(2,4)
		b = random.randrange(1,5) * 2 * (-1)**random.randrange(1,3) * a
		c = list(range(-8,20))
		c.remove(0)
		c = random.choice(c)
		d = b/(2*a)
		e = c - a*d**2 
		if b<0:
			sign1 = " - "
			b = abs(b)
		else:
			sign1 = " + "
		if c<0:
			sign2 = " - "
			c = abs(c)
		else:
			sign2 = " + "
		if b==1:
			b = ""
		if a==1:
			a = ""
		if e<0:
			sign3 = " - "
			e = abs(e)
		else:
			sign3 = " + "
		if d%1==0:
			d = int(d)
		if e%1==0:
			e = int(e)
#write question
		tempquestions.write(explanation + "$" + str(a) + "x^2" + sign1 + str(b) + "x" + sign2 + str(c) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(a) + "(x" + sign1 + str(abs(d)) + ")^2" + sign3 + str(e) + "$")



def completesquaresolve(n,explanationn):
	import random
	from utilities.rounding import rounddp
	from fractions import Fraction
	from math import floor,ceil,sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve by completing the square and state the minimum point of "
		else:
			explanation = ""
		a = 1
		b = random.randrange(1,7) * 2 * (-1)**random.randrange(1,3)
		cs = list(range(floor((b/2)**2)-8,floor((b/2)**2)))
		c = random.choice(cs) 
		while c==0:
			c = random.choice(cs) 
		adjuster = int(c - (b/2)**2)
		x1 = rounddp((-b + sqrt(b**2 - 4*a*c))/(2*a),2)
		x2 = rounddp((-b - sqrt(b**2 - 4*a*c))/(2*a),2)
		if x1%1==0:
			x1 = int(x1)
		if x2%1==0:
			x2 = int(x2)
		minim = "(" + str(int(-b/2)) + " , " + str(adjuster) + ")"
		if b<0:
			sign1 = " - "
			b = abs(b)
		else:
			sign1 = " + "
		if c<0:
			sign2 = " - "
			c = abs(c)
		else:
			sign2 = " + "
		if b==1:
			b = ""
		if a==1:
			a = ""
		if adjuster<0:
			sign3 = " - "
			adjuster = abs(adjuster)
		else:
			sign3 = " + "
#write question
		tempquestions.write(explanation + "\\mbox{$" + str(a) + "x^2" + sign1 + str(b) + "x" + sign2 + str(c) + " = 0$}")
		tempquestions.write("\n")
#write answer
		tempquestions.write("x = " + str(x1) + " and " + str(x2) + ", min = " + minim)


def quadcourse1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		nums=list(range(1,13))
		a = random.choice(nums)
		b = random.choice(nums)
		if a<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if b<0:
			sign2 = " - "
		else:
			sign2 = " + "
		if a+b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if a*b<0:
			sign4 = " - "
		else:
			sign4 = " + "
		brackets = "$(x" + sign1 + str(abs(a)) + ")(x" + sign2 + str(abs(b)) + ")$"
		t = a+b
		if t==1 or t==-1:
			t = ""
		else:
			t = abs(t)
		if t==0:
			expanded = "$x^{2}" + sign4 + str(abs(a*b)) + "$"
		else:
			expanded = "$x^{2}" + sign3 + str(t) + "x" + sign4 + str(abs(a*b)) + "$"
		question = brackets
		answer = expanded
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def quadcourse2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation = "Find a and b: "
		else:
			explanation = ""
		a = random.randrange(1,13)
		b = random.randrange(1,13)
#write question
		tempquestions.write(explanation + "a + b = $" + str(a + b) + "$ and ab = $" + str(a*b) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(a) + "$ and $" + str(b) + "$")

def quadcourse3(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise "
		else:
			explanation = ""
		nums=list(range(1,13))
		a = random.choice(nums)
		b = random.choice(nums)
		if a<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if b<0:
			sign2 = " - "
		else:
			sign2 = " + "
		if a+b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if a*b<0:
			sign4 = " - "
		else:
			sign4 = " + "
		brackets = "$(x" + sign1 + str(abs(a)) + ")(x" + sign2 + str(abs(b)) + ")$"
		t = a+b
		if t==1 or t==-1:
			t = ""
		else:
			t = abs(t)
		if t==0:
			expanded = "$x^{2}" + sign4 + str(abs(a*b)) + "$"
		else:
			expanded = "$x^{2}" + sign3 + str(t) + "x" + sign4 + str(abs(a*b)) + "$"
		question = expanded
		answer = brackets
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def quadcourse4(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		nums = list(range(-12,0))
		a = random.choice(nums)
		b = random.choice(nums)
		if a<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if b<0:
			sign2 = " - "
		else:
			sign2 = " + "
		if a+b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if a*b<0:
			sign4 = " - "
		else:
			sign4 = " + "
		brackets = "$(x" + sign1 + str(abs(a)) + ")(x" + sign2 + str(abs(b)) + ")$"
		t = a+b
		if t==1 or t==-1:
			t = ""
		else:
			t = abs(t)
		if t==0:
			expanded = "$x^{2}" + sign4 + str(abs(a*b)) + "$"
		else:
			expanded = "$x^{2}" + sign3 + str(t) + "x" + sign4 + str(abs(a*b)) + "$"
		question = brackets
		answer = expanded
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def quadcourse5(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation = "Find a and b: "
		else:
			explanation = ""
		a = random.randrange(1,13) * (-1)
		b = random.randrange(1,13) * (-1)
#write question
		tempquestions.write(explanation + "a + b = $" + str(a + b) + "$ and ab = $" + str(a*b) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(a) + "$ and $" + str(b) + "$")


def quadcourse6(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise "
		else:
			explanation = ""
		nums = list(range(-12,0))
		a = random.choice(nums)
		b = random.choice(nums)
		if a<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if b<0:
			sign2 = " - "
		else:
			sign2 = " + "
		if a+b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if a*b<0:
			sign4 = " - "
		else:
			sign4 = " + "
		brackets = "$(x" + sign1 + str(abs(a)) + ")(x" + sign2 + str(abs(b)) + ")$"
		t = a+b
		if t==1 or t==-1:
			t = ""
		else:
			t = abs(t)
		if t==0:
			expanded = "$x^{2}" + sign4 + str(abs(a*b)) + "$"
		else:
			expanded = "$x^{2}" + sign3 + str(t) + "x" + sign4 + str(abs(a*b)) + "$"
		question = expanded
		answer = brackets
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def quadcourse9(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		nums = list(range(1,13))
		a = random.choice(nums)
		b = random.choice(nums) * (-1)
		if random.randrange(0,2)==1:
			temp = a
			a = b
			b = temp
		if a<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if b<0:
			sign2 = " - "
		else:
			sign2 = " + "
		if a+b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if a*b<0:
			sign4 = " - "
		else:
			sign4 = " + "
		brackets = "$(x" + sign1 + str(abs(a)) + ")(x" + sign2 + str(abs(b)) + ")$"
		t = a+b
		if t==1 or t==-1:
			t = ""
		else:
			t = abs(t)
		if t==0:
			expanded = "$x^{2}" + sign4 + str(abs(a*b)) + "$"
		else:
			expanded = "$x^{2}" + sign3 + str(t) + "x" + sign4 + str(abs(a*b)) + "$"
		question = brackets
		answer = expanded
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def quadcourse91(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		nums = list(range(1,13))
		a = random.choice(nums)
		b = random.choice(nums)
		if a<b:
			a = 0 - a
		else:
			b = 0 - b
		if random.randrange(0,2)==1:
			temp = a
			a = b
			b = temp
		if a<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if b<0:
			sign2 = " - "
		else:
			sign2 = " + "
		if a+b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if a*b<0:
			sign4 = " - "
		else:
			sign4 = " + "
		brackets = "$(x" + sign1 + str(abs(a)) + ")(x" + sign2 + str(abs(b)) + ")$"
		t = a+b
		if t==1 or t==-1:
			t = ""
		else:
			t = abs(t)
		if t==0:
			expanded = "$x^{2}" + sign4 + str(abs(a*b)) + "$"
		else:
			expanded = "$x^{2}" + sign3 + str(t) + "x" + sign4 + str(abs(a*b)) + "$"
		question = brackets
		answer = expanded
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def quadcourse92(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		nums = list(range(1,13))
		a = random.choice(nums)
		b = random.choice(nums)
		if a>b:
			a = 0 - a
		else:
			b = 0 - b
		if random.randrange(0,2)==1:
			temp = a
			a = b
			b = temp
		if a<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if b<0:
			sign2 = " - "
		else:
			sign2 = " + "
		if a+b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if a*b<0:
			sign4 = " - "
		else:
			sign4 = " + "
		brackets = "$(x" + sign1 + str(abs(a)) + ")(x" + sign2 + str(abs(b)) + ")$"
		t = a+b
		if t==1 or t==-1:
			t = ""
		else:
			t = abs(t)
		if t==0:
			expanded = "$x^{2}" + sign4 + str(abs(a*b)) + "$"
		else:
			expanded = "$x^{2}" + sign3 + str(t) + "x" + sign4 + str(abs(a*b)) + "$"
		question = brackets
		answer = expanded
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def quadcourse10(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")

#create question
		if explanationn==1:
			explanation = "Find a and b: "
		else:
			explanation = ""
		nums = list(range(1,13))
		a = random.choice(nums)
		nums.remove(a)
		b = random.choice(nums)
		if b>a:
			temp = a
			a = b
			b = temp
#write question
		tempquestions.write(explanation + "a $-$ b = $" + str(a - b) + "$ and ab = $" + str(a*b) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(a) + "$ and $" + str(b) + "$")


def quadcourse11(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise "
		else:
			explanation = ""
		nums = list(range(1,13))
		a = random.choice(nums)
		nums.remove(a)
		b = random.choice(nums)
		if a>b:
			b = b * (-1)
		else:
			a = a * (-1)
		if a<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if b<0:
			sign2 = " - "
		else:
			sign2 = " + "
		if a+b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if a*b<0:
			sign4 = " - "
		else:
			sign4 = " + "
		brackets = "$(x" + sign1 + str(abs(a)) + ")(x" + sign2 + str(abs(b)) + ")$"
		t = a+b
		if t==1 or t==-1:
			t = ""
		else:
			t = abs(t)
		if t==0:
			expanded = "$x^{2}" + sign4 + str(abs(a*b)) + "$"
		else:
			expanded = "$x^{2}" + sign3 + str(t) + "x" + sign4 + str(abs(a*b)) + "$"
		question = expanded
		answer = brackets
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def quadcourse12(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise "
		else:
			explanation = ""
		nums = list(range(1,13))
		a = random.choice(nums)
		nums.remove(a)
		b = random.choice(nums)
		if a<b:
			b = b * (-1)
		else:
			a = a * (-1)
		if a<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if b<0:
			sign2 = " - "
		else:
			sign2 = " + "
		if a+b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if a*b<0:
			sign4 = " - "
		else:
			sign4 = " + "
		brackets = "$(x" + sign1 + str(abs(a)) + ")(x" + sign2 + str(abs(b)) + ")$"
		t = a+b
		if t==1 or t==-1:
			t = ""
		else:
			t = abs(t)
		if t==0:
			expanded = "$x^{2}" + sign4 + str(abs(a*b)) + "$"
		else:
			expanded = "$x^{2}" + sign3 + str(t) + "x" + sign4 + str(abs(a*b)) + "$"
		question = expanded
		answer = brackets
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def quadcourse15pospos(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve "
		else:
			explanation = ""
		nums = list(range(1,13))
		a = random.choice(nums)
		b = random.choice(nums)
		if a<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if b<0:
			sign2 = " - "
		else:
			sign2 = " + "
		if a+b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if a*b<0:
			sign4 = " - "
		else:
			sign4 = " + "
		brackets = "$(x" + sign1 + str(abs(a)) + ")(x" + sign2 + str(abs(b)) + ") = 0$"
		t = a+b
		if t==1 or t==-1:
			t = ""
		else:
			t = abs(t)
		if t==0:
			expanded = "$x^{2}" + sign4 + str(abs(a*b)) + "$ = 0"
		else:
			expanded = "$x^{2}" + sign3 + str(t) + "x" + sign4 + str(abs(a*b)) + "$ = 0"
		question = brackets
		answer = "$x = " + str(-a) + "$ and $x = " + str(-b) + "$"
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def quadcourse15posneg(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve "
		else:
			explanation = ""
		nums = list(range(1,13))
		a = random.choice(nums)
		nums.remove(a)
		b = random.choice(nums)
		if a<b:
			b = b * (-1)
		else:
			a = a * (-1)
		if a<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if b<0:
			sign2 = " - "
		else:
			sign2 = " + "
		if a+b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if a*b<0:
			sign4 = " - "
		else:
			sign4 = " + "
		brackets = "$(x" + sign1 + str(abs(a)) + ")(x" + sign2 + str(abs(b)) + ") = 0$"
		t = a+b
		if t==1 or t==-1:
			t = ""
		else:
			t = abs(t)
		if t==0:
			expanded = "$x^{2}" + sign4 + str(abs(a*b)) + "$ = 0"
		else:
			expanded = "$x^{2}" + sign3 + str(t) + "x" + sign4 + str(abs(a*b)) + "$ = 0"
		question = brackets
		answer = "$x = " + str(-a) + "$ and $x = " + str(-b) + "$"
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def quadcourse15negpos(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve "
		else:
			explanation = ""
		nums = list(range(1,13))
		a = random.choice(nums)
		nums.remove(a)
		b = random.choice(nums)
		if a>b:
			b = b * (-1)
		else:
			a = a * (-1)
		if a<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if b<0:
			sign2 = " - "
		else:
			sign2 = " + "
		if a+b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if a*b<0:
			sign4 = " - "
		else:
			sign4 = " + "
		brackets = "$(x" + sign1 + str(abs(a)) + ")(x" + sign2 + str(abs(b)) + ") = 0$"
		t = a+b
		if t==1 or t==-1:
			t = ""
		else:
			t = abs(t)
		if t==0:
			expanded = "$x^{2}" + sign4 + str(abs(a*b)) + "$ = 0"
		else:
			expanded = "$x^{2}" + sign3 + str(t) + "x" + sign4 + str(abs(a*b)) + "$ = 0"
		question = brackets
		answer = "$x = " + str(-a) + "$ and $x = " + str(-b) + "$"
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def quadcourse15negneg(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Solve "
		else:
			explanation = ""
		nums = list(range(1,13))
		a = random.choice(nums) * (-1)
		b = random.choice(nums) * (-1)
		if a<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if b<0:
			sign2 = " - "
		else:
			sign2 = " + "
		if a+b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if a*b<0:
			sign4 = " - "
		else:
			sign4 = " + "
		brackets = "$(x" + sign1 + str(abs(a)) + ")(x" + sign2 + str(abs(b)) + ") = 0$"
		t = a+b
		if t==1 or t==-1:
			t = ""
		else:
			t = abs(t)
		if t==0:
			expanded = "$x^{2}" + sign4 + str(abs(a*b)) + "$ = 0"
		else:
			expanded = "$x^{2}" + sign3 + str(t) + "x" + sign4 + str(abs(a*b)) + "$ = 0"
		question = brackets
		answer = "$x = " + str(-a) + "$ and $x = " + str(-b) + "$"
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def quadcourse16pospos(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise and solve "
		else:
			explanation = ""
		nums = list(range(1,13))
		a = random.choice(nums)
		b = random.choice(nums)
		if a<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if b<0:
			sign2 = " - "
		else:
			sign2 = " + "
		if a+b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if a*b<0:
			sign4 = " - "
		else:
			sign4 = " + "
		brackets = "$(x" + sign1 + str(abs(a)) + ")(x" + sign2 + str(abs(b)) + ") = 0$"
		t = a+b
		if t==1 or t==-1:
			t = ""
		else:
			t = abs(t)
		if t==0:
			expanded = "$x^{2}" + sign4 + str(abs(a*b)) + "$ = 0"
		else:
			expanded = "$x^{2}" + sign3 + str(t) + "x" + sign4 + str(abs(a*b)) + "$ = 0"
		question = expanded
		answer = "$x = " + str(-a) + "$ and $x = " + str(-b) + "$"
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def quadcourse16posneg(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise and solve "
		else:
			explanation = ""
		nums = list(range(1,13))
		a = random.choice(nums)
		nums.remove(a)
		b = random.choice(nums)
		if a<b:
			b = b * (-1)
		else:
			a = a * (-1)
		if a<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if b<0:
			sign2 = " - "
		else:
			sign2 = " + "
		if a+b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if a*b<0:
			sign4 = " - "
		else:
			sign4 = " + "
		brackets = "$(x" + sign1 + str(abs(a)) + ")(x" + sign2 + str(abs(b)) + ") = 0$"
		t = a+b
		if t==1 or t==-1:
			t = ""
		else:
			t = abs(t)
		if t==0:
			expanded = "$x^{2}" + sign4 + str(abs(a*b)) + "$ = 0"
		else:
			expanded = "$x^{2}" + sign3 + str(t) + "x" + sign4 + str(abs(a*b)) + "$ = 0"
		question = expanded
		answer = "$x = " + str(-a) + "$ and $x = " + str(-b) + "$"
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def quadcourse16negpos(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise and solve "
		else:
			explanation = ""
		nums = list(range(1,13))
		a = random.choice(nums)
		nums.remove(a)
		b = random.choice(nums)
		if a>b:
			b = b * (-1)
		else:
			a = a * (-1)
		if a<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if b<0:
			sign2 = " - "
		else:
			sign2 = " + "
		if a+b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if a*b<0:
			sign4 = " - "
		else:
			sign4 = " + "
		brackets = "$(x" + sign1 + str(abs(a)) + ")(x" + sign2 + str(abs(b)) + ") = 0$"
		t = a+b
		if t==1 or t==-1:
			t = ""
		else:
			t = abs(t)
		if t==0:
			expanded = "$x^{2}" + sign4 + str(abs(a*b)) + "$ = 0"
		else:
			expanded = "$x^{2}" + sign3 + str(t) + "x" + sign4 + str(abs(a*b)) + "$ = 0"
		question = expanded
		answer = "$x = " + str(-a) + "$ and $x = " + str(-b) + "$"
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def quadcourse16negneg(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise and solve "
		else:
			explanation = ""
		nums = list(range(1,13))
		a = random.choice(nums) * (-1)
		b = random.choice(nums) * (-1)
		if a<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if b<0:
			sign2 = " - "
		else:
			sign2 = " + "
		if a+b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if a*b<0:
			sign4 = " - "
		else:
			sign4 = " + "
		brackets = "$(x" + sign1 + str(abs(a)) + ")(x" + sign2 + str(abs(b)) + ") = 0$"
		t = a+b
		if t==1 or t==-1:
			t = ""
		else:
			t = abs(t)
		if t==0:
			expanded = "$x^{2}" + sign4 + str(abs(a*b)) + "$ = 0"
		else:
			expanded = "$x^{2}" + sign3 + str(t) + "x" + sign4 + str(abs(a*b)) + "$ = 0"
		question = expanded
		answer = "$x = " + str(-a) + "$ and $x = " + str(-b) + "$"
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def factoriseexperiment(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		tailoring1 = list(range(-5,6))
		tailoring1.remove(0)
		tailoring2 = list(range(-5,6))
		tailoring2.remove(0)
		d = random.randrange(1,4)
		if d==1:
			f = random.randrange(2,7)
		else:
			f = random.randrange(1,4)
		if d>1:
			tailoring1.remove(d)
			tailoring1.remove(d*-1)
		if 1<f<6:
			tailoring2.remove(f)
			tailoring2.remove(f*-1)
		e = random.choice(tailoring1)
		g = random.choice(tailoring2)
		if e<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if g<0:
			sign2 = " - "
		else:
			sign2 = " + "
		a = d*f
		b = d*g + e*f
		c = e*g
		if b<0:
			sign3 = " - "
		else:
			sign3 = " + "
		if c<0:
			sign4 = " - "
		else:
			sign4 = " + "
		e = abs(e)
		g = abs(g)
		b = abs(b)
		c = abs(c)		
		if b==1:
			b = ""
		if d==1:
			d = ""
		if f==1:
			f = ""
		if b==0:
			question = str(a) + "x^2" + sign4 + str(c)
		else:
			question = str(a) + "x^2" + sign3 + str(b) + "x" + sign4 + str(c)
		question = "$(" + str(d) + "x" + sign1 + str(e) + ")(\\hspace{1cm}) = " + question + "$" 
		answer = "$(" + str(f) + "x" + sign2 + str(g) + ")$" 
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
