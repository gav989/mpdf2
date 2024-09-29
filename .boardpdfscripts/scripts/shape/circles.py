#circles.py

def circleareapi(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		radii = (2,3,4,5,6,8,9)
		radius = random.choice(radii)*10
		coeff = radius**2
		pi = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}$"
#write question
		tempquestions.write(explanation + "A circle has a radius of " + str(radius) + "cm. Calculate the area of the circle, giving your answer as a multiple of " + pi)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(coeff) + pi + " cm$^2$")
			

def circlecircumferencerad(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		radius = random.randrange(2,40)*0.25
		pi = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}$"
		circumference = round(math.pi * 2 * radius,2)
		if radius%1==0:
			radius = int(radius)
#write question
		tempquestions.write(explanation + "A circle has a radius of " + str(radius) + "m. Calculate the circumference of the circle")
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(circumference) + "m")
			


def circletablecircumferenceforward(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		circumferences = list(range(10,501))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		c = [0,1,2,3,4,5,6,7]
		for i in range(0,8):
			d[i] = random.choice(diameters)
			diameters.remove(d[i])
			r[i] = d[i]/2
			if r[i]%1==0:
				r[i] = int(r[i])
			c[i] = round(math.pi*d[i],2)
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			c[i] = str(c[i]) + "cm"
		qtable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Circumference \\\\ \\specialrule{1pt}{0pt}{0pt} & " + d[0] + " & \\\\ \\hline & " + d[1] + " & \\\\ \\hline &" + d[2] + " & \\\\ \\hline & " + d[3] + " & \\\\ \\hline " + r[4] + " & & \\\\ \\hline" + r[5] + " & & \\\\ \\hline" + r[6]  + " & & \\\\ \\hline " + r[7] +  " & & \\\\ \\hline \\end{tabular}\\hfill"
		atable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Circumference \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + c[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + c[1] + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + c[2] + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + c[3] + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + c[4] + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + c[5] + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + c[6] + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + c[7] +  " \\\\ \\hline \\end{tabular}\\hfill"
		intro = "Copy and complete this table"
		question = intro + nl + qtable
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def circletablecircumferencebackward(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		circumferences = list(range(10,501))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		c = [0,1,2,3,4,5,6,7]
		for i in range(0,8):
			c[i] = random.choice(circumferences)
			circumferences.remove(c[i])
			d[i] = round(c[i]/math.pi,2)
			r[i] = round((c[i]/math.pi)/2,2)
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			c[i] = str(c[i]) + "cm"
		qtable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Circumference \\\\ \\specialrule{1pt}{0pt}{0pt} & & " + c[0] + "\\\\ \\hline & & " + c[1] + "\\\\ \\hline & &" + c[2] + "\\\\ \\hline & &" + c[3] + "\\\\ \\hline & &" + c[4] + " \\\\ \\hline & & " + c[5] + " \\\\ \\hline & & " + c[6]  + " \\\\ \\hline & & " + c[7]   +  " \\\\ \\hline \\end{tabular}\\hfill"
		atable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Circumference \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + c[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + c[1] + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + c[2] + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + c[3] + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + c[4] + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + c[5] + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + c[6] + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + c[7] +  " \\\\ \\hline \\end{tabular}\\hfill"
		intro = "Copy and complete this table"
		question = intro + nl + qtable
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def circletablecircumferencefull(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		circumferences = list(range(10,501))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		c = [0,1,2,3,4,5,6,7]
		for i in range(0,4):
			d[i] = random.choice(diameters)
			diameters.remove(d[i])
			r[i] = d[i]/2
			if r[i]%1==0:
				r[i] = int(r[i])
			c[i] = round(math.pi*d[i],2)
		for i in range(4,8):
			c[i] = random.choice(circumferences)
			circumferences.remove(c[i])
			d[i] = round(c[i]/math.pi,2)
			r[i] = round((c[i]/math.pi)/2,2)
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			c[i] = str(c[i]) + "cm"
		qtable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Circumference \\\\ \\specialrule{1pt}{0pt}{0pt} & " + d[0] + " & \\\\ \\hline & " + d[1] + " & \\\\ \\hline " + r[2] + " & & \\\\ \\hline " + r[3] + " & & \\\\ \\hline & &" + c[4] + " \\\\ \\hline & & " + c[5] + " \\\\ \\hline & & " + c[6]  + " \\\\ \\hline & & " + c[7]   +  " \\\\ \\hline \\end{tabular}\\hfill"
		atable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Circumference \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + c[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + c[1] + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + c[2] + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + c[3] + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + c[4] + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + c[5] + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + c[6] + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + c[7] +  " \\\\ \\hline \\end{tabular}\\hfill"
		intro = "Copy and complete this table"
		question = intro + nl + qtable
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def circletableareaforward(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		a = [0,1,2,3,4,5,6,7]
		for i in range(0,8):
			d[i] = random.choice(diameters)
			diameters.remove(d[i])
			r[i] = d[i]/2
			if r[i]%1==0:
				r[i] = int(r[i])
			a[i] = round(math.pi*r[i]**2,2)
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			a[i] = str(a[i]) + "cm$^{2}$"
		qtable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + "&  & \\\\ \\hline " + r[1] + "& & \\\\ \\hline " + r[2] + "&  & \\\\ \\hline " + r[3] + " & & \\\\ \\hline &" + d[4] + " & \\\\ \\hline & " + d[5] + "& \\\\ \\hline & " + d[6]  + "& \\\\ \\hline & " + d[7] +  " & \\\\ \\hline \\end{tabular}\\hfill"
		atable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + a[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + a[1] + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + a[2] + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + a[3] + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + a[4] + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + a[5] + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + a[6] + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + a[7] +  " \\\\ \\hline \\end{tabular}\\hfill"
		intro = "Copy and complete this table"
		question = intro + nl + qtable
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def circletableareabackward(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		areas = list(range(10,501))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		a = [0,1,2,3,4,5,6,7]
		for i in range(0,8):
			a[i] = random.choice(areas)
			areas.remove(a[i])
			r[i] = round(math.sqrt(a[i]/math.pi),2)
			d[i] = round(2 * math.sqrt(a[i]/math.pi),2)
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			a[i] = str(a[i]) + "cm$^{2}$"
		qtable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Area \\\\ \\specialrule{1pt}{0pt}{0pt} & & " + a[0] + "\\\\ \\hline & & " + a[1] + "\\\\ \\hline & & " + a[2] + "\\\\ \\hline & & " + a[3] + "\\\\ \\hline & &" + a[4] + " \\\\ \\hline & & " + a[5] + " \\\\ \\hline & & " + a[6]  + " \\\\ \\hline & & " + a[7]   +  " \\\\ \\hline \\end{tabular}\\hfill"
		atable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + a[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + a[1] + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + a[2] + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + a[3] + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + a[4] + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + a[5] + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + a[6] + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + a[7] +  " \\\\ \\hline \\end{tabular}\\hfill"
		intro = "Copy and complete this table"
		question = intro + nl + qtable
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def circletableareafull(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		areas = list(range(10,501))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		a = [0,1,2,3,4,5,6,7]
		for i in range(0,4):
			d[i] = random.choice(diameters)
			diameters.remove(d[i])
			r[i] = d[i]/2
			if r[i]%1==0:
				r[i] = int(r[i])
			a[i] = round(math.pi*r[i]**2,2)
		for i in range(4,8):
			a[i] = random.choice(areas)
			areas.remove(a[i])
			r[i] = round(math.sqrt(a[i]/math.pi),2)
			d[i] = round(2 * math.sqrt(a[i]/math.pi),2)
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			a[i] = str(a[i]) + "cm$^{2}$"
		qtable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + "&  & \\\\ \\hline " + r[1] + "& & \\\\ \\hline & " + d[2] + " & \\\\ \\hline & " + d[3] + " & \\\\ \\hline & &" + a[4] + " \\\\ \\hline & & " + a[5] + " \\\\ \\hline & & " + a[6]  + " \\\\ \\hline & & " + a[7]   +  " \\\\ \\hline \\end{tabular}\\hfill"
		atable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + a[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + a[1] + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + a[2] + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + a[3] + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + a[4] + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + a[5] + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + a[6] + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + a[7] +  " \\\\ \\hline \\end{tabular}\\hfill"
		intro = "Copy and complete this table"
		question = intro + nl + qtable
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def circletablefull(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		circumferences = list(range(10,501))
		areas = list(range(10,501))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		c = [0,1,2,3,4,5,6,7]
		a = [0,1,2,3,4,5,6,7]
		for i in range(0,4):
			d[i] = random.choice(diameters)
			diameters.remove(d[i])
			r[i] = d[i]/2
			if r[i]%1==0:
				r[i] = int(r[i])
			c[i] = round(math.pi*d[i],2)
			a[i] = round(math.pi*r[i]**2,2)
		for i in range(4,6):
			c[i] = random.choice(circumferences)
			circumferences.remove(c[i])
			d[i] = round(c[i]/math.pi,2)
			r[i] = round((c[i]/math.pi)/2,2)
			a[i] = round((c[i]**2)/(4*math.pi),2)
		for i in range(6,8):
			a[i] = random.choice(areas)
			areas.remove(a[i])
			r[i] = round(math.sqrt(a[i]/math.pi),2)
			d[i] = round(2 * math.sqrt(a[i]/math.pi),2)
			c[i] = round(math.sqrt(4 * a[i] * math.pi),2)
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			c[i] = str(c[i]) + "cm"
			a[i] = str(a[i]) + "cm$^{2}$"
		qtable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Circumference & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & & &  \\\\ \\hline " + r[1] + " & & & \\\\ \\hline & " + d[2] + " & & \\\\ \\hline & " + d[3] + " & & \\\\ \\hline & &" + c[4] + " & \\\\ \\hline & & " + c[5] + " & \\\\ \\hline & & & " + a[6]  + " \\\\ \\hline & & & " + a[7]   +  " \\\\ \\hline \\end{tabular}\\hfill"
		atable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Circumference & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + c[0] + " & " + a[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + c[1] + " & " + a[1]  + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + c[2] + " & " + a[2]  + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + c[3] + " & " + a[3]  + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + c[4] + " & " + a[4]  + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + c[5] + " & " + a[5]  + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + c[6] + " & " + a[6]  + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + c[7] + " & " + a[7]   +  " \\\\ \\hline \\end{tabular}\\hfill"
		intro = "Copy and complete this table"
		question = intro + nl + qtable
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def circletablepicircumferenceforward(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		pi = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}$"
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		c = [0,1,2,3,4,5,6,7]
		for i in range(0,8):
			d[i] = random.choice(diameters)
			diameters.remove(d[i])
			r[i] = d[i]/2
			if r[i]%1==0:
				r[i] = int(r[i])
			c[i] = str(d[i]) + pi
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			c[i] = str(c[i]) + "cm"
		qtable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Circumference \\\\ \\specialrule{1pt}{0pt}{0pt} & " + d[0] + " & \\\\ \\hline & " + d[1] + " & \\\\ \\hline &" + d[2] + " & \\\\ \\hline & " + d[3] + " & \\\\ \\hline " + r[4] + " & & \\\\ \\hline" + r[5] + " & & \\\\ \\hline" + r[6]  + " & & \\\\ \\hline " + r[7] +  " & & \\\\ \\hline \\end{tabular}\\hfill"
		atable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Circumference \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + c[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + c[1] + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + c[2] + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + c[3] + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + c[4] + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + c[5] + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + c[6] + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + c[7] +  " \\\\ \\hline \\end{tabular}\\hfill"
		intro = "Copy and complete this table"
		question = intro + nl + qtable
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def circletablepicircumferencebackward(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		pi = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}$"
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		c = [0,1,2,3,4,5,6,7]
		for i in range(0,8):
			d[i] = random.choice(diameters)
			diameters.remove(d[i])
			r[i] = d[i]/2
			if r[i]%1==0:
				r[i] = int(r[i])
			c[i] = str(d[i]) + pi
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			c[i] = str(c[i]) + "cm"
		qtable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Circumference \\\\ \\specialrule{1pt}{0pt}{0pt} & & " + c[0] + "\\\\ \\hline & & " + c[1] + "\\\\ \\hline & &" + c[2] + "\\\\ \\hline & &" + c[3] + "\\\\ \\hline & &" + c[4] + " \\\\ \\hline & & " + c[5] + " \\\\ \\hline & & " + c[6]  + " \\\\ \\hline & & " + c[7]   +  " \\\\ \\hline \\end{tabular}\\hfill"
		atable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Circumference \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + c[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + c[1] + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + c[2] + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + c[3] + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + c[4] + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + c[5] + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + c[6] + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + c[7] +  " \\\\ \\hline \\end{tabular}\\hfill"
		intro = "Copy and complete this table"
		question = intro + nl + qtable
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def circletablepicircumferencefull(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		pi = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}$"
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		c = [0,1,2,3,4,5,6,7]
		for i in range(0,8):
			d[i] = random.choice(diameters)
			diameters.remove(d[i])
			r[i] = d[i]/2
			if r[i]%1==0:
				r[i] = int(r[i])
			c[i] = str(d[i]) + pi
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			c[i] = str(c[i]) + "cm"
		qtable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Circumference \\\\ \\specialrule{1pt}{0pt}{0pt} & " + d[0] + " & \\\\ \\hline & " + d[1] + " & \\\\ \\hline " + r[2] + " & & \\\\ \\hline " + r[3] + " & & \\\\ \\hline & &" + c[4] + " \\\\ \\hline & & " + c[5] + " \\\\ \\hline & & " + c[6]  + " \\\\ \\hline & & " + c[7]   +  " \\\\ \\hline \\end{tabular}\\hfill"
		atable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Circumference \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + c[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + c[1] + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + c[2] + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + c[3] + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + c[4] + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + c[5] + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + c[6] + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + c[7] +  " \\\\ \\hline \\end{tabular}\\hfill"
		intro = "Copy and complete this table"
		question = intro + nl + qtable
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def circletablepiareaforward(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		pi = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}$"
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		areas = list(range(10,501))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		a = [0,1,2,3,4,5,6,7]
		for i in range(0,8):
			d[i] = random.choice(diameters)
			diameters.remove(d[i])
			r[i] = d[i]/2
			if r[i]%1==0:
				r[i] = int(r[i])
			a[i] = str(r[i]**2) + pi
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			a[i] = str(a[i]) + "cm$^{2}$"
		qtable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + "&  & \\\\ \\hline " + r[1] + "& & \\\\ \\hline " + r[2] + "&  & \\\\ \\hline " + r[3] + " & & \\\\ \\hline &" + d[4] + " & \\\\ \\hline & " + d[5] + "& \\\\ \\hline & " + d[6]  + "& \\\\ \\hline & " + d[7] +  " & \\\\ \\hline \\end{tabular}\\hfill"
		atable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + a[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + a[1] + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + a[2] + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + a[3] + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + a[4] + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + a[5] + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + a[6] + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + a[7] +  " \\\\ \\hline \\end{tabular}\\hfill"
		intro = "Copy and complete this table"
		question = intro + nl + qtable
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def circletablepiareabackward(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		pi = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}$"
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		areas = list(range(10,501))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		a = [0,1,2,3,4,5,6,7]
		for i in range(0,8):
			d[i] = random.choice(diameters)
			diameters.remove(d[i])
			r[i] = d[i]/2
			if r[i]%1==0:
				r[i] = int(r[i])
			a[i] = str(r[i]**2) + pi
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			a[i] = str(a[i]) + "cm$^{2}$"
		qtable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Area \\\\ \\specialrule{1pt}{0pt}{0pt} & & " + a[0] + "\\\\ \\hline & & " + a[1] + "\\\\ \\hline & & " + a[2] + "\\\\ \\hline & & " + a[3] + "\\\\ \\hline & &" + a[4] + " \\\\ \\hline & & " + a[5] + " \\\\ \\hline & & " + a[6]  + " \\\\ \\hline & & " + a[7]   +  " \\\\ \\hline \\end{tabular}\\hfill"
		atable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + a[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + a[1] + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + a[2] + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + a[3] + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + a[4] + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + a[5] + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + a[6] + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + a[7] +  " \\\\ \\hline \\end{tabular}\\hfill"
		intro = "Copy and complete this table"
		question = intro + nl + qtable
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def circletablepiareafull(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		pi = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}$"
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		areas = list(range(10,501))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		a = [0,1,2,3,4,5,6,7]
		for i in range(0,8):
			d[i] = random.choice(diameters)
			diameters.remove(d[i])
			r[i] = d[i]/2
			if r[i]%1==0:
				r[i] = int(r[i])
			a[i] = str(r[i]**2) + pi
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			a[i] = str(a[i]) + "cm$^{2}$"
		qtable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + "&  & \\\\ \\hline " + r[1] + "& & \\\\ \\hline & " + d[2] + " & \\\\ \\hline & " + d[3] + " & \\\\ \\hline & &" + a[4] + " \\\\ \\hline & & " + a[5] + " \\\\ \\hline & & " + a[6]  + " \\\\ \\hline & & " + a[7]   +  " \\\\ \\hline \\end{tabular}\\hfill"
		atable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + a[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + a[1] + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + a[2] + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + a[3] + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + a[4] + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + a[5] + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + a[6] + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + a[7] +  " \\\\ \\hline \\end{tabular}\\hfill"
		intro = "Copy and complete this table"
		question = intro + nl + qtable
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def circletablepifull(n,explanationn):
	import random,math
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		pi = "$\\mathlarger{\\mathlarger{\\mathlarger{\\pi}}}$"
		nl = " \\\\[0.3cm] "
		diameters =list(range(2,101))
		r = [0,1,2,3,4,5,6,7]
		d = [0,1,2,3,4,5,6,7]
		c = [0,1,2,3,4,5,6,7]
		a = [0,1,2,3,4,5,6,7]
		for i in range(0,8):
			d[i] = random.choice(diameters)
			diameters.remove(d[i])
			r[i] = d[i]/2
			if r[i]%1==0:
				r[i] = int(r[i])
			c[i] = str(d[i]) + pi
			a[i] = str(r[i]**2) + pi
		for i in range(0,8):
			r[i] = str(r[i]) + "cm"
			d[i] = str(d[i]) + "cm"
			c[i] = str(c[i]) + "cm"
			a[i] = str(a[i]) + "cm$^{2}$"
		qtable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Circumference & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & & &  \\\\ \\hline " + r[1] + " & & & \\\\ \\hline & " + d[2] + " & & \\\\ \\hline & " + d[3] + " & & \\\\ \\hline & &" + c[4] + " & \\\\ \\hline & & " + c[5] + " & \\\\ \\hline & & & " + a[6]  + " \\\\ \\hline & & & " + a[7]   +  " \\\\ \\hline \\end{tabular}\\hfill"
		atable = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{3cm} | p{3cm} | p{3cm} |} \\hline Radius & Diameter & Circumference & Area \\\\ \\specialrule{1pt}{0pt}{0pt} " + r[0] + " & " + d[0] + " & " + c[0] + " & " + a[0] + " \\\\ \\hline " + r[1] + " & " + d[1] + " & " + c[1] + " & " + a[1]  + " \\\\ \\hline " + r[2] + " & " + d[2] + " & " + c[2] + " & " + a[2]  + " \\\\ \\hline " + r[3] + " & " + d[3] + " & " + c[3] + " & " + a[3]  + " \\\\ \\hline " + r[4] + " & " + d[4] + " & " + c[4] + " & " + a[4]  + " \\\\ \\hline " + r[5] + " & " + d[5] + " & " + c[5] + " & " + a[5]  + " \\\\ \\hline " + r[6] + " & " + d[6] + " & " + c[6] + " & " + a[6]  + " \\\\ \\hline " + r[7] + " & " + d[7] + " & " + c[7] + " & " + a[7]   +  " \\\\ \\hline \\end{tabular}\\hfill"
		intro = "Copy and complete this table"
		question = intro + nl + qtable
		answer = intro + nl + atable
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



