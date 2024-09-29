#!/usr/bin/env python3
#quadratics.py



def substitution1pos(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Find the value of "
			explanation2 = " when x = "
		else:
			explanation = ""
		num = random.randrange(1,10)
		x = random.randrange(1,10)
		if random.randrange(0,2)==1:
			sign = " + "
			answer = x**2 + num
		else:
			sign = " - "
			answer = x**2 - num
		expression = "$x^{2}" + sign + str(num) + "$"
		question = explanation1 + expression + explanation2 + str(x)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def substitution1neg(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Find the value of "
			explanation2 = " when x = "
		else:
			explanation = ""
		num = random.randrange(1,10)
		x = 0 - random.randrange(1,10)
		if random.randrange(0,2)==1:
			sign = " + "
			answer = x**2 + num
		else:
			sign = " - "
			answer = x**2 - num
		expression = "$x^{2}" + sign + str(num) + "$"
		question = explanation1 + expression + explanation2 + str(x)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))

def substitution2pos(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Find the value of "
			explanation2 = " when x = "
		else:
			explanation = ""
		coeff = random.randrange(1,10)
		x = random.randrange(1,10)
		if random.randrange(0,2)==1:
			sign = " + "
			answer = x**2 + coeff * x
		else:
			sign = " - "
			answer = x**2 - coeff * x
		if coeff==1:
			coeff = ""
		expression = "$x^{2}" + sign + str(coeff) + "x$"
		question = explanation1 + expression + explanation2 + str(x)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def substitution3pos(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Find the value of "
			explanation2 = " when x = "
		else:
			explanation = ""
		coeff = random.randrange(1,10)
		x = random.randrange(1,10)
		num = random.randrange(1,10)
		if random.randrange(0,2)==1:
			sign1 = " + "
			answer = x**2 + coeff * x
		else:
			sign1 = " - "
			answer = x**2 - coeff * x
		if coeff==1:
			coeff = ""
		if random.randrange(0,2)==1:
			sign2 = " + "
			answer = answer + num
		else:
			sign2 = " - "
			answer = answer - num
		expression = "$x^{2}" + sign1 + str(coeff) + "x" + sign2 + str(num) + "$"
		question = explanation1 + expression + explanation2 + str(x)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def substitution3neg(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Find the value of "
			explanation2 = " when x = "
		else:
			explanation = ""
		coeff = random.randrange(1,10)
		x = 0 -random.randrange(1,10)
		num = random.randrange(1,10)
		if random.randrange(0,2)==1:
			sign1 = " + "
			answer = x**2 + coeff * x
		else:
			sign1 = " - "
			answer = x**2 - coeff * x
		if coeff==1:
			coeff = ""
		if random.randrange(0,2)==1:
			sign2 = " + "
			answer = answer + num
		else:
			sign2 = " - "
			answer = answer - num
		expression = "$x^{2}" + sign1 + str(coeff) + "x" + sign2 + str(num) + "$"
		question = explanation1 + expression + explanation2 + str(x)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))

def substitution2neg(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Find the value of "
			explanation2 = " when x = "
		else:
			explanation = ""
		coeff = random.randrange(1,10)
		x = 0 - random.randrange(1,10)
		if random.randrange(0,2)==1:
			sign = " + "
			answer = x**2 + coeff * x
		else:
			sign = " - "
			answer = x**2 - coeff * x
		if coeff==1:
			coeff = ""
		expression = "$x^{2}" + sign + str(coeff) + "x$"
		question = explanation1 + expression + explanation2 + str(x)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def substitution4pos(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Find the value of "
			explanation2 = " when x = "
		else:
			explanation1 = ""
			explanation2 = ""
		a = random.randrange(2,7)
		b = random.randrange(2,7)
		x = random.randrange(1,7)
		if random.randrange(0,2)==1:
			sign = " + "
			answer = a * x**2 + b * x
		else:
			sign = " - "
			answer = a * x**2 - b * x
		expression = "$" + str(a) + "x^{2}" + sign + str(b) + "x$"
		question = explanation1 + expression + explanation2 + str(x)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def substitution4neg(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Find the value of "
			explanation2 = " when x = "
		else:
			explanation1 = ""
			explanation2 = ""
		a = random.randrange(2,7)
		b = random.randrange(2,7)
		x = random.randrange(-6,0)
		if random.randrange(0,2)==1:
			sign = " + "
			answer = a * x**2 + b * x
		else:
			sign = " - "
			answer = a * x**2 - b * x
		expression = "$" + str(a) + "x^{2}" + sign + str(b) + "x$"
		question = explanation1 + expression + explanation2 + str(x)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))

def plotquad1(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		a = 1
		b = 0
		c = random.randrange(-5,6)
		mid = 0 - b/(2*a)
		if mid%1==0:
			mid = int(mid)
			if random.randrange(0,3)==1:
				xs = [mid-2,mid-1,mid,mid+1,mid+2,mid+3,mid+4]
			else:
				xs = [mid-4,mid-3,mid-2,mid-1,mid,mid+1,mid+2]
		else:
			mid = int(floor(mid))
			if random.randrange(0,3)==1:
				xs = [mid-2,mid-1,mid,mid+1,mid+2,mid+3,mid+4]
			else:
				xs = [mid-3,mid-2,mid-1,mid,mid+1,mid+2,mid+3]
		xmin = xs[0]
		xmax = xs[6]
		if xmin>1:
			xmin = -1
		if xmax<-1:
			xmax = 1
		ys = []
		for i in range(0,7):
			ys.append(a*xs[i]**2 + b*xs[i] + c)
		atable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{1cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		ymin = floor(c - ((b**2)/(4*a)))
		if abs(ys[0])>abs(ys[6]):
			ymax = ys[0]
		else:
			ymax = ys[6]
		if a<0:
			temp = ymin
			ymin = ymax
			ymax = temp
		if ymin>-1:
			ymin = -1
		if ymax<1:
			ymax = 1
		del1 = random.randrange(0,2)
		del2 = random.randrange(2,5)
		del3 = random.randrange(5,7)
		ys[del1] = ""
		ys[del2] = ""
		ys[del3] = ""
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{1cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		if b<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if c<0:
			sign2 = " - "
		else:
			sign2 = " + "
		graph = "\\begin{gnuplot}[terminal=pdf] set nokey; set grid; set border 0; set xtics axis 1; set ytics axis 1; set size ratio 2; set size 1,1; set zeroaxis linewidth 2 linetype 1; set yrange [" + str(ymin) + ":" + str(ymax) + "]; set xrange [" + str(xmin) + ":" + str(xmax) + "]; plot " + str(a) + "*x**2+" + str(b) + "*x+" + str(c) + " \end{gnuplot}"
		b = abs(b)
		c = abs(c)
		if a==1:
			a = ""
		if b==1:
			b = ""
		if b==0 and c==0:
			equation = "$y = " + str(a) + "x^{2}$"
		elif b==0:
			equation = "$y = " + str(a) + "x^{2}" + sign2 + str(c) + "$"
		elif c==0:
			equation = "$y = " + str(a) + "x^{2}" + sign1 + str(b) + "x$"
		else:
			equation = "$y = " + str(a) + "x^{2}" + sign1 + str(b) + "x" + sign2 + str(c) + "$"
		question =  " Complete this table for " + equation + " and draw the graph." + nl + qtable
		answer = atable + graph
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def plotquad2(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		a = 1
		b = random.randrange(1,6) * (-1)**random.randrange(1,3)
		c = 0
		mid = 0 - b/(2*a)
		if mid%1==0:
			mid = int(mid)
			if random.randrange(0,3)==1:
				xs = [mid-2,mid-1,mid,mid+1,mid+2,mid+3,mid+4]
			else:
				xs = [mid-4,mid-3,mid-2,mid-1,mid,mid+1,mid+2]
		else:
			mid = int(floor(mid))
			if random.randrange(0,3)==1:
				xs = [mid-2,mid-1,mid,mid+1,mid+2,mid+3,mid+4]
			else:
				xs = [mid-3,mid-2,mid-1,mid,mid+1,mid+2,mid+3]
		xmin = xs[0]
		xmax = xs[6]
		if xmin>1:
			xmin = -1
		if xmax<-1:
			xmax = 1
		ys = []
		for i in range(0,7):
			ys.append(a*xs[i]**2 + b*xs[i] + c)
		atable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{1cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		ymin = floor(c - ((b**2)/(4*a)))
		if abs(ys[0])>abs(ys[6]):
			ymax = ys[0]
		else:
			ymax = ys[6]
		if a<0:
			temp = ymin
			ymin = ymax
			ymax = temp
		if ymin>-1:
			ymin = -1
		if ymax<1:
			ymax = 1
		del1 = random.randrange(0,2)
		del2 = random.randrange(2,5)
		del3 = random.randrange(5,7)
		ys[del1] = ""
		ys[del2] = ""
		ys[del3] = ""
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{1cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		if b<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if c<0:
			sign2 = " - "
		else:
			sign2 = " + "
		graph = "\\begin{gnuplot}[terminal=pdf] set nokey; set grid; set border 0; set xtics axis 1; set ytics axis 1; set size ratio 2; set size 1,1; set zeroaxis linewidth 2 linetype 1; set yrange [" + str(ymin) + ":" + str(ymax) + "]; set xrange [" + str(xmin) + ":" + str(xmax) + "]; plot " + str(a) + "*x**2+" + str(b) + "*x+" + str(c) + " \end{gnuplot}"
		b = abs(b)
		c = abs(c)
		if a==1:
			a = ""
		if b==1:
			b = ""
		if b==0 and c==0:
			equation = "$y = " + str(a) + "x^{2}$"
		elif b==0:
			equation = "$y = " + str(a) + "x^{2}" + sign2 + str(c) + "$"
		elif c==0:
			equation = "$y = " + str(a) + "x^{2}" + sign1 + str(b) + "x$"
		else:
			equation = "$y = " + str(a) + "x^{2}" + sign1 + str(b) + "x" + sign2 + str(c) + "$"
		question =  " Complete this table for " + equation + " and draw the graph." + nl + qtable
		answer = atable + graph
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def plotquad3(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		a = 1
		b = random.randrange(1,6) * (-1)**random.randrange(1,3)
		c = random.randrange(1,6) * (-1)**random.randrange(1,3)
		mid = 0 - b/(2*a)
		if mid%1==0:
			mid = int(mid)
			if random.randrange(0,3)==1:
				xs = [mid-2,mid-1,mid,mid+1,mid+2,mid+3,mid+4]
			else:
				xs = [mid-4,mid-3,mid-2,mid-1,mid,mid+1,mid+2]
		else:
			mid = int(floor(mid))
			if random.randrange(0,3)==1:
				xs = [mid-2,mid-1,mid,mid+1,mid+2,mid+3,mid+4]
			else:
				xs = [mid-3,mid-2,mid-1,mid,mid+1,mid+2,mid+3]
		xmin = xs[0]
		xmax = xs[6]
		if xmin>1:
			xmin = -1
		if xmax<-1:
			xmax = 1
		ys = []
		for i in range(0,7):
			ys.append(a*xs[i]**2 + b*xs[i] + c)
		atable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{1cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		ymin = floor(c - ((b**2)/(4*a)))
		if abs(ys[0])>abs(ys[6]):
			ymax = ys[0]
		else:
			ymax = ys[6]
		if a<0:
			temp = ymin
			ymin = ymax
			ymax = temp
		if ymin>-1:
			ymin = -1
		if ymax<1:
			ymax = 1
		del1 = random.randrange(0,2)
		del2 = random.randrange(2,5)
		del3 = random.randrange(5,7)
		ys[del1] = ""
		ys[del2] = ""
		ys[del3] = ""
		qtable = "\\renewcommand{\\arraystretch}{1.2}\\newcolumntype{C}{>{\centering\\arraybackslash} m{1cm} }\\begin{tabular}{|C|C|C|C|C|C|C|C|} \\hline x & " + str(xs[0]) + " & " + str(xs[1]) + " & " + str(xs[2]) + " & " + str(xs[3]) + " & " + str(xs[4]) + " & " + str(xs[5]) + " & " + str(xs[6]) + " \\\\ \\hline y & " + str(ys[0]) + " & " + str(ys[1]) + " & " + str(ys[2]) + " & " + str(ys[3]) + " & " + str(ys[4]) + " & " + str(ys[5]) + " & " + str(ys[6]) + "\\\\ \\hline \\end{tabular}"
		if b<0:
			sign1 = " - "
		else:
			sign1 = " + "
		if c<0:
			sign2 = " - "
		else:
			sign2 = " + "
		graph = "\\begin{gnuplot}[terminal=pdf] set nokey; set grid; set border 0; set xtics axis 1; set ytics axis 1; set size ratio 2; set size 1,1; set zeroaxis linewidth 2 linetype 1; set yrange [" + str(ymin) + ":" + str(ymax) + "]; set xrange [" + str(xmin) + ":" + str(xmax) + "]; plot " + str(a) + "*x**2+" + str(b) + "*x+" + str(c) + " \end{gnuplot}"
		b = abs(b)
		c = abs(c)
		if a==1:
			a = ""
		if b==1:
			b = ""
		if b==0 and c==0:
			equation = "$y = " + str(a) + "x^{2}$"
		elif b==0:
			equation = "$y = " + str(a) + "x^{2}" + sign2 + str(c) + "$"
		elif c==0:
			equation = "$y = " + str(a) + "x^{2}" + sign1 + str(b) + "x$"
		else:
			equation = "$y = " + str(a) + "x^{2}" + sign1 + str(b) + "x" + sign2 + str(c) + "$"
		question =  " Complete this table for " + equation + " and draw the graph." + nl + qtable
		answer = atable + graph
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))
