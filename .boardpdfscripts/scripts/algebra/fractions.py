#fractions.py

def quaddots(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
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
		if b==0:
			qtop = "x^2" + sign4 + str(c)
		else:
			qtop = "x^2" + sign3 + str(b) + "x" + sign4 + str(c)
		qbot = "x^2 - " + str(e**2)
		atop = "x" + sign2 + str(g)
		if sign1==" - ":
			sign5 = " + "
		else:
			sign5 = " - "
		abot = "x" + sign5 + str(e)
		if random.randrange(0,2)==1:
			temp = qtop
			qtop = qbot
			qbot = temp
			temp = atop
			atop = abot
			abot = temp
#write question
		tempquestions.write(explanation + "$\\dfrac{" + qtop + "}{" + qbot + "}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$\\dfrac{" + atop + "}{" + abot + "}$")
