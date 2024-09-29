#!/usr/bin/env python3
#torture.py

def timestables1(n,q=1):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = random.randrange(2,13)
		b = random.randrange(2,13)
#write question
		tempquestions.write("$" + str(a) + " \\times " + str(b) + " = \\rule[-1.5mm]{1cm}{0.15mm}$")

		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(a) + " \\times " + str(b) + " = \\underline{" + str(a*b) +"}$")


def timestables2(n,q=1):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = random.randrange(2,13)
		b = random.randrange(2,13)
#write question
		tempquestions.write("$" + str(a*b) + " \\div " + str(b) + " = \\rule[-1.5mm]{1cm}{0.15mm}$")

		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(a*b) + " \\div " + str(b) + " = \\underline{" + str(a) +"}$")


def timestables3(n,q=1):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = random.randrange(2,13)
		b = random.randrange(2,13)
		dec = random.randrange(0,2)
#write question
		if dec==1:
			tempquestions.write("$\\rule[-1.5mm]{1cm}{0.15mm} \\times " + str(b) + " = " + str(a*b) + "$")
		else:
			tempquestions.write("$" + str(a) + "\\times " + "\\rule[-1.5mm]{1cm}{0.15mm} = " + str(a*b) + "$")

		tempquestions.write("\n")
#write answer
		
		if dec==1:
			tempquestions.write("$\\underline{" + str(a) + "} \\times " + str(b) + " = " + str(a*b) + "$")
		else:
			tempquestions.write("$" + str(a) + "\\times " + "\\underline{" + str(b) + "} = " + str(a*b) + "$")

def timestables4(n,q=1):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = random.randrange(2,13)
		b = random.randrange(2,13)
#write question
		tempquestions.write("$" + str(a*b) + " \\div " + "\\rule[-1.5mm]{1cm}{0.15mm} = " + str(a) + "$")

		tempquestions.write("\n")
#write answer
		
		tempquestions.write("$" + str(a*b) + " \\div " + "\\underline{" + str(b) + "} = " + str(a) + "$")

def timestables5(n,q=1):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = random.randrange(2,13)
		b = random.randrange(2,13)
#write question
		tempquestions.write("$\\rule[-1.5mm]{1cm}{0.15mm} \\div " + str(b) + " = " + str(a) + "$")

		tempquestions.write("\n")
#write answer
		
		tempquestions.write("$ \\underline{" + str(a*b) + "} \\div " + str(b) + " = " + str(a) + "$")

def negativeadd1(n,q=1):
    import random
    for x in range(0, n):
        tempquestions = open("tempquestions","a")
        tempquestions.write("\n")
#create question
        decision=random.randrange(1,4)
        if decision<3:
                a = random.randrange(2,16) * (-1)
        else:
                a = random.randrange(2,16)
        if decision>1:
                b = random.randrange(2,16) * (-1)
        else:
                b = random.randrange(2,16)
#write question
        tempquestions.write("$" + str(a) + " + " + str(b) + " = \\rule[-1.5mm]{1cm}{0.15mm}$")
 
        tempquestions.write("\n")
#write answer
        tempquestions.write("$" + str(a) + " + " + str(b) + " = \\underline{" + str(a+b) +"}$")


def negativeadd2(n,q=1):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		decision=random.randrange(1,4)
		if decision<3:
			a = random.randrange(2,16) * (-1)
		else:
			a = random.randrange(2,16)
		if decision>1:
			b = random.randrange(2,16) * (-1)
		else:
			b = random.randrange(2,16)
#write question
		decision=random.randrange(1,3)
		if decision==1:
			tempquestions.write("$" + str(a) + " + \\rule[-1.5mm]{1cm}{0.15mm}" + " = " + str(a+b) + "$")
		else:
			tempquestions.write("$\\rule[-1.5mm]{1cm}{0.15mm} + " + str(b) + " = " + str(a+b) + "$")
	
		tempquestions.write("\n")
#write answer
		if decision==1:
			tempquestions.write("$" + str(a) + " + \\underline{" + str(b) + "} = " + str(a+b) + "$")
		else:
			tempquestions.write("$\\underline{" + str(a) + "} + " + str(b) + " = " + str(a+b) + "$")


def negativesubtract1(n,q=1):
    import random
    for x in range(0, n):
        tempquestions = open("tempquestions","a")
        tempquestions.write("\n")
#create question
        decision=random.randrange(1,4)
        if decision<3:
                a = random.randrange(2,16) * (-1)
        else:
                a = random.randrange(2,16)
        if decision>1:
                b = random.randrange(2,16) * (-1)
        else:
                b = random.randrange(2,16)
#write question
        tempquestions.write(str(a) + " - " + str(b) + " = $\\rule[-1.5mm]{1cm}{0.15mm}$")
 
        tempquestions.write("\n")
#write answer
        tempquestions.write("$" + str(a) + " - " + str(b) + " = \\underline{" + str(a-b) +"}$")


def negativesubtract2(n,q=1):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		decision=random.randrange(1,4)
		if decision<3:
			a = random.randrange(2,16) * (-1)
		else:
			a = random.randrange(2,16)
		if decision>1:
			b = random.randrange(2,16) * (-1)
		else:
			b = random.randrange(2,16)
#write question
		tempquestions.write("$" + str(a) + " - \\rule[-1.5mm]{1cm}{0.15mm}" + " = " + str(a-b) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(a) + " - \\underline{" + str(b) + "} = " + str(a-b) + "$")


def negativesubtract3(n,q=1):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		decision=random.randrange(1,4)
		if decision<3:
			a = random.randrange(2,16) * (-1)
		else:
			a = random.randrange(2,16)
		if decision>1:
			b = random.randrange(2,16) * (-1)
		else:
			b = random.randrange(2,16)
#write question
		tempquestions.write("$\\rule[-1.5mm]{1cm}{0.15mm} - " + str(b) + " = " + str(a-b) + "$")
	
		tempquestions.write("\n")
#write answer
		tempquestions.write("$\\underline{" + str(a) + "} - " + str(b) + " = " + str(a-b) + "$")


def negativemultiply1(n,q=1):
    import random
    for x in range(0, n):
        tempquestions = open("tempquestions","a")
        tempquestions.write("\n")
#create question
        decision=random.randrange(1,4)
        if decision<3:
                a = random.randrange(2,13) * (-1)
        else:
                a = random.randrange(2,13)
        if decision>1:
                b = random.randrange(2,13) * (-1)
        else:
                b = random.randrange(2,13)
#write question
        tempquestions.write("$" + str(a) + " \\times " + str(b) + " = \\rule[-1.5mm]{1cm}{0.15mm}$")
 
        tempquestions.write("\n")
#write answer
        tempquestions.write("$" + str(a) + " \\times " + str(b) + " = \\underline{" + str(a*b) +"}$")

def negativemultiply2(n,q=1):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		decision=random.randrange(1,4)
		if decision<3:
			a = random.randrange(2,13) * (-1)
		else:
			a = random.randrange(2,13)
		if decision>1:
			b = random.randrange(2,13) * (-1)
		else:
			b = random.randrange(2,13)
#write question
		decision=random.randrange(1,3)
		if decision==1:
			tempquestions.write("$" + str(a) + " \\times \\rule[-1.5mm]{1cm}{0.15mm}" + " = " + str(a*b) + "$")
		else:
			tempquestions.write("$\\rule[-1.5mm]{1cm}{0.15mm} \\times " + str(b) + " = " + str(a*b) + "$")
	
		tempquestions.write("\n")
#write answer
		if decision==1:
			tempquestions.write("$" + str(a) + " \\times \\underline{" + str(b) + "} = " + str(a*b) + "$")
		else:
			tempquestions.write("$\\underline{" + str(a) + "} \\times " + str(b) + " = " + str(a*b) + "$")

def negativedivide1(n,q=1):
    import random
    for x in range(0, n):
        tempquestions = open("tempquestions","a")
        tempquestions.write("\n")
#create question
        decision=random.randrange(1,4)
        if decision<3:
                a = random.randrange(2,13) * (-1)
        else:
                a = random.randrange(2,13)
        if decision>1:
                b = random.randrange(2,13) * (-1)
        else:
                b = random.randrange(2,13)
#write question
        tempquestions.write("$" + str(a*b) + " \\div " + str(b) + " = \\rule[-1.5mm]{1cm}{0.15mm}$")
 
        tempquestions.write("\n")
#write answer
        tempquestions.write("$" + str(a*b) + " \\div " + str(b) + " = \\underline{" + str(a) +"}$")


def negativedivide2(n,q=1):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		decision=random.randrange(1,4)
		if decision<3:
			a = random.randrange(2,13) * (-1)
		else:
			a = random.randrange(2,13)
		if decision>1:
			b = random.randrange(2,13) * (-1)
		else:
			b = random.randrange(2,13)
#write question
		tempquestions.write("$" + str(a*b) + " \\div \\rule[-1.5mm]{1cm}{0.15mm}" + " = " + str(a) + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(a*b) + " \\div \\underline{" + str(b) + "} = " + str(a) + "$")


def negativedivide3(n,q=1):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		decision=random.randrange(1,4)
		if decision<3:
			a = random.randrange(2,13) * (-1)
		else:
			a = random.randrange(2,13)
		if decision>1:
			b = random.randrange(2,13) * (-1)
		else:
			b = random.randrange(2,13)
#write question
		tempquestions.write("$\\rule[-1.5mm]{1cm}{0.15mm} " + "\\div " + str(b) + " = " + str(a) + "$")
	
		tempquestions.write("\n")
#write answer
		tempquestions.write("$\\underline{" + str(a*b) + "} " + "\\div " + str(b) + " = " + str(a) + "$")


def multten(n,q=1):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = round(random.randrange(1,1000)/10**random.randrange(0,3),2)
		if a%1==0:
			a = int(a)
		b = 10
		sign = " $\\times$ "
		c = round(a*b,5)
		if random.randrange(1,3)==1:
			d = a
			a = b
			b = d
		if c%1==0:
			c = int(c)
#write question
		tempquestions.write(str(a) + sign + str(b) + " = $\\rule[-1.5mm]{1cm}{0.15mm}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a) + sign + str(b) + " = $\\underline{" + str(c) +"}$")


def multhundred(n,q=1):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = round(random.randrange(1,1000)/10**random.randrange(0,3),2)
		if a%1==0:
			a = int(a)
		b = 100
		sign = " $\\times$ "
		c = round(a*b,5)
		if random.randrange(1,3)==1:
			d = a
			a = b
			b = d
		if c%1==0:
			c = int(c)
#write question
		tempquestions.write(str(a) + sign + str(b) + " = $\\rule[-1.5mm]{1cm}{0.15mm}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a) + sign + str(b) + " = $\\underline{" + str(c) +"}$")

def multthousand(n,q=1):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = round(random.randrange(1,1000)/10**random.randrange(0,3),2)
		if a%1==0:
			a = int(a)
		b = 1000
		sign = " $\\times$ "
		c = round(a*b,5)
		if random.randrange(1,3)==1:
			d = a
			a = b
			b = d
		if c%1==0:
			c = int(c)
#write question
		tempquestions.write(str(a) + sign + str(b) + " = $\\rule[-1.5mm]{1cm}{0.15mm}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a) + sign + str(b) + " = $\\underline{" + str(c) +"}$")


def divten(n,q=1):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = round(random.randrange(1,1000)/10**random.randrange(0,3),2)
		if a%1==0:
			a = int(a)
		b = 10
		sign = " $\\div$ "
		c = round(a/b,5)
		if c%1==0:
			c = int(c)
#write question
		tempquestions.write(str(a) + sign + str(b) + " = $\\rule[-1.5mm]{1cm}{0.15mm}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a) + sign + str(b) + " = $\\underline{" + str(c) +"}$")


def divhundred(n,q=1):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = round(random.randrange(1,1000)/10**random.randrange(0,3),2)
		if a%1==0:
			a = int(a)
		b = 100
		sign = " $\\div$ "
		c = round(a/b,5)
		if c%1==0:
			c = int(c)
#write question
		tempquestions.write(str(a) + sign + str(b) + " = $\\rule[-1.5mm]{1cm}{0.15mm}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a) + sign + str(b) + " = $\\underline{" + str(c) +"}$")

def divthousand(n,q=1):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = round(random.randrange(1,1000)/10**random.randrange(0,3),2)
		if a%1==0:
			a = int(a)
		b = 1000
		sign = " $\\div$ "
		c = round(a/b,5)
		if c%1==0:
			c = int(c)
#write question
		tempquestions.write(str(a) + sign + str(b) + " = $\\rule[-1.5mm]{1cm}{0.15mm}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a) + sign + str(b) + " = $\\underline{" + str(c) +"}$")


def multdivtht1(n,q=1):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = round(random.randrange(1,1000)/10**random.randrange(0,3),2)
		if a%1==0:
			a = int(a)
		b = 10**random.randrange(1,4)
		decision = random.randrange(1,3)
		if decision==1:
			sign = " $\\times$ "
			c = round(a*b,5)
			if random.randrange(1,3)==1:
				d = a
				a = b
				b = d
		else:
			sign = " $\\div$ "
			c = round(a/b,5)
		if c%1==0:
			c = int(c)
#write question
		tempquestions.write(str(a) + sign + str(b) + " = $\\rule[-1.5mm]{1cm}{0.15mm}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a) + sign + str(b) + " = $\\underline{" + str(c) +"}$")

def multdivtht2(n,q=1):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = round(random.randrange(1,1000)/10**random.randrange(0,3),2)
		if a%1==0:
			a = int(a)
		b = 10**random.randrange(1,4)
		swap = 0
		decision = random.randrange(1,3)
		if decision==1:
			sign = " $\\times$ "
			c = round(a*b,5)
			swap = random.randrange(1,3)
			if swap==1:
				d = b
				b = a
				a = d
		else:
			sign = " $\\div$ "
			c = round(a/b,5)
		if c%1==0:
			c = int(c)
#write question
		if swap==1:
			tempquestions.write("$\\rule[-1.5mm]{1cm}{0.15mm}$" + sign + str(b) + " = " + str(c))
		else:
			tempquestions.write(str(a) + sign + "$\\rule[-1.5mm]{1cm}{0.15mm}$" + " = " + str(c))
		tempquestions.write("\n")
#write answer
		if swap==1:
			tempquestions.write("$\\underline{" + str(a) +"}$" + sign + str(b) + " = " + str(c))
		else:
			tempquestions.write(str(a) + sign + "$\\underline{" + str(b) +"}$" + " = " + str(c))

def multdivtht3(n,q=1):
	from utilities.rounding import rounddp
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = round(random.randrange(1,1000)/10**random.randrange(0,3),2)
		b = 10**random.randrange(1,4)
		swap = 0
		if a%1==0:
			a = int(a)
		decision = random.randrange(1,3)
		if decision==1:
			sign = " $\\times$ "
			c = round(a*b,5)
			swap = random.randrange(1,3)
			if swap==1:
				d = b
				b = a
				a = d
		else:
			sign = " $\\div$ "
			c = round(a/b,5)
		if c%1==0:
			c = int(c)
#write question
		if swap!=1:
			tempquestions.write("$\\rule[-1.5mm]{1cm}{0.15mm}$" + sign + str(b) + " = " + str(c))
		else:
			tempquestions.write(str(a) + sign + "$\\rule[-1.5mm]{1cm}{0.15mm}$" + " = " + str(c))
		tempquestions.write("\n")
#write answer
		if swap!=1:
			tempquestions.write("$\\underline{" + str(a) +"}$" + sign + str(b) + " = " + str(c))
		else:
			tempquestions.write(str(a) + sign + "$\\underline{" + str(b) +"}$" + " = " + str(c))

def singledigitdivision(n,q=1):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = random.randrange(2,10)
		b = random.randrange(13,10**(random.randrange(2,3)))
#write question
		tempquestions.write(str(a*b) + " $\\div$ " + str(a) + " = " + "$\\rule[-1.5mm]{1cm}{0.15mm}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a*b) + " $\\div$ " + str(a) + " = " + "$\\underline{" + str(b) +"}$")

def twodigitdivisioneasy(n,q=1):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = random.randrange(11,20)
		if random.randrange(0,2)==1:
			b = random.randrange(1,7) + random.randrange(0,7)*10 + random.randrange(1,7)*100
		else:
			b = random.randrange(1,7) + random.randrange(1,7)*10
#write question
		tempquestions.write(str(a*b) + " $\\div$ " + str(a) + " = " + "$\\rule[-1.5mm]{1cm}{0.15mm}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a*b) + " $\\div$ " + str(a) + " = " + "$\\underline{" + str(b) +"}$")


def twodigitdivision(n,q=1):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = random.randrange(11,40)
		if random.randrange(0,2)==1:
			b = random.randrange(1,7) + random.randrange(0,7)*10 + random.randrange(1,7)*100
		else:
			b = random.randrange(1,7) + random.randrange(1,7)*10
#write question
		tempquestions.write(str(a*b) + " $\\div$ " + str(a) + " = " + "$\\rule[-1.5mm]{1cm}{0.15mm}$")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a*b) + " $\\div$ " + str(a) + " = " + "$\\underline{" + str(b) +"}$")


def fulladdition(n,q=1):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		selection = (2,3,3,4,4)
		c = random.choice(selection)
		d = random.choice(selection)
		a = random.randrange(10**(c-1),10**c)
		b = random.randrange(10**(d-1),10**d)
#write question
		tempquestions.write("$" + str(a) + " + " + str(b) + " = " + "\\rule[-1.5mm]{1cm}{0.15mm}$")

		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(a) + " + " + str(b) + " = " + "\\underline{" + str(a+b) +"}$")


def fullsubtraction(n,q=1):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		selection = (2,3,3,4,4)
		c = random.choice(selection)
		d = random.choice(selection)
		a = random.randrange(10**(c-1),10**c)
		b = random.randrange(10**(d-1),10**d)
		if a<b:
			c = a
			a = b
			b = c
#write question
		tempquestions.write("$" + str(a) + " - " + str(b) +  " = " + "\\rule[-1.5mm]{1cm}{0.15mm}$")

		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(a) + " - " + str(b) +  " = " + "\\underline{" + str(a-b)+"}$")



def simpleaddition1(n,q=1):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = random.randrange(1,10)
		b = random.randrange(1,10)
		c = a + b
#write question
		tempquestions.write("$" + str(a) + " + " + "\\rule[-1.5mm]{1cm}{0.15mm} = " + str(c) + "$")

		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(a) + " + " + "\\underline{" + str(b) +"} = " + str(c) + "$")

def simpleaddition2(n,q=1):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		a = random.randrange(1,20)
		b = random.randrange(1,20)
		c = a + b
#write question
		tempquestions.write("$" + str(a) + " + " + "\\rule[-1.5mm]{1cm}{0.15mm} = " + str(c) + "$")

		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + str(a) + " + " + "\\underline{" + str(b) +"} = " + str(c) + "$")
