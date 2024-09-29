#ven.py

def vennneither(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		justcats = random.randrange(10,50)
		justdogs = random.randrange(10,50)
		catsdogs = random.randrange(10,50)
		cats = justcats + catsdogs
		dogs = justdogs + catsdogs
		neither = random.randrange(10,100)
		total = justcats + justdogs + catsdogs + neither
		intro = "In a school there are " + str(total) + " students."
		fact1 = str(cats) + " students like cats.\\\\"
		fact2 = str(dogs) + " students like dogs.\\\\"
		fact3 = str(catsdogs) + " students like both cats and dogs."
		question = "Work out how many students like neither cats nor dogs."
		question = intro + nl + fact1 + fact2 + fact3 + nl + question
		answer = str(neither)
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def vennboth(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		justcats = random.randrange(10,50)
		justdogs = random.randrange(10,50)
		catsdogs = random.randrange(10,50)
		cats = justcats + catsdogs
		dogs = justdogs + catsdogs
		neither = random.randrange(10,100)
		total = justcats + justdogs + catsdogs + neither
		intro = "In a school there are " + str(total) + " students."
		fact1 = str(cats) + " students like cats.\\\\"
		fact2 = str(dogs) + " students like dogs.\\\\"
		fact3 = str(neither) + " students like neither cats nor dogs."
		question = "Work out how many students like both cats and dogs."
		question = intro + nl + fact1 + fact2 + fact3 + nl + question 
		answer = str(catsdogs)
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def vennone(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		justcats = random.randrange(10,50)
		justdogs = random.randrange(10,50)
		catsdogs = random.randrange(10,50)
		cats = justcats + catsdogs
		dogs = justdogs + catsdogs
		neither = random.randrange(10,100)
		total = justcats + justdogs + catsdogs + neither
		intro = "In a school there are " + str(total) + " students."
		if random.randrange(0,2)==0:
			fact1 = str(cats) + " students like cats.\\\\"
			fact2 = str(catsdogs) + " students like both cats and dogs.\\\\"
			fact3 = str(neither) + " students like neither cats nor dogs."
			question = "Work out how many students like dogs but not cats."
			answer = str(justdogs)
		else:
			fact1 = str(dogs) + " students like dogs.\\\\"
			fact2 = str(catsdogs) + " students like both cats and dogs.\\\\"
			fact3 = str(neither) + " students like neither cats nor dogs."
			question = "Work out how many students like cats but not dogs."
			answer = str(justcats)
		question = intro + nl + fact1 + fact2 + fact3 + nl + question 
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)





def vennexam(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		students = random.randrange(5,16)*10
		neither = random.randrange(3,16)
		intro = str(students) + " students are asked about what pets they have."
		students = students - neither - 15
		distribution = [5,5,5]
		for i in range(0,students):
			dec = random.randrange(0,3)
			distribution[dec] = distribution[dec] + 1
		cats = distribution[0]
		both = distribution[1]
		dogs = distribution[2]

		qimage = "\\begin{overpic}[scale=0.5]{data/images/venn1} \\put(17,49){" + str(cats) + "}  \\put(7,75){cats} \\put(80,75){dogs} \\end{overpic}"
		aimage = "\\begin{overpic}[scale=0.5]{data/images/venn1} \\put(17,49){" + str(cats) + "}  \\put(82,10){" + str(neither) + "}  \\put(46,49){" + str(both) + "}  \\put(75,49){" + str(dogs) + "}     \\put(7,75){cats} \\put(80,75){dogs}  \\end{overpic}"

		point1 = "\\item" + str(cats) + " students have cats but not dogs. \\\\"
		point2 = "\\item" + str(cats + both) + " students have cats.\\\\"
		point3 = "\\item" + str(both + dogs) + " students have dogs.\\\\"
		questiona = "(a) Complete the venn diagram to show this information."
		questionb = "(b) What percentage of students have neither cats nor dogs?"


		question = intro + "\\begin{center}" + qimage  + "\\end{center}" + "\\vspace{-1.5\\topsep}\\begin{itemize}\setlength{\itemsep}{0pt}" + point1 + point2 + point3 + "\\end{itemize}\\vspace{-1.5\\topsep}~" + "\\\\" + questiona + nl + questionb
		perc = rounddp(100* neither / (students+neither+15),2)
		if perc%1==0:
			perc = int(perc)
		answer = aimage + nl + "(b) " + str(perc) + "\\%"
#write question


#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def setnotation1(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		scale = 0.3
		diags = [
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot1}",
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot2}",
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot3}",
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot4}",
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot5}",
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot6}",
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot7}",
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot8}",
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot9}",
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot10}",
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot11}",
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot12}",
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot13}",
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot14}"]
		answers = [
			"A",
			"B",
			"A'",
			"B'",
			"A$\\cap$B",
			"A'$\\cap$B",
			"A$\\cap$B'",
			"A'$\\cap$B'",
			"A$\\cup$B",
			"A'$\\cup$B",
			"A$\\cup$B'",
			"A'$\\cup$B'",
			"(A$\\cap$B)$\\cup$(A'$\\cap$B')",
			"(A$\\cap$B')$\\cup$(A'$\\cap$B)"]
		dec = random.randrange(0,len(answers))
		answer = diags[dec]
		question = answers[dec]
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write("\\begin{center}" + answer + "\\end{center}~")


def setnotation2(n,explanationn):
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		scale = 0.3
		diags = [
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot1}",
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot2}",
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot3}",
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot4}",
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot5}",
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot6}",
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot7}",
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot8}",
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot9}",
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot10}",
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot11}",
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot12}",
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot13}",
			"\\includegraphics[scale=" + str(scale) + "]{data/images/setnot14}"]
		answers = [
			"A",
			"B",
			"A'",
			"B'",
			"A$\\cap$B",
			"A'$\\cap$B",
			"A$\\cap$B'",
			"A'$\\cap$B'",
			"A$\\cup$B",
			"A'$\\cup$B",
			"A$\\cup$B'",
			"A'$\\cup$B'",
			"(A$\\cap$B)$\\cup$(A'$\\cap$B')",
			"(A$\\cap$B')$\\cup$(A'$\\cap$B)"]
		dec = random.randrange(0,len(answers))
		question = diags[dec]
		answer = answers[dec]
#write question
		tempquestions.write("\\begin{center}" + question + "\\end{center}~")

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def venn1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		jcats = random.randrange(10,50)
		jdogs = random.randrange(10,50)
		both = random.randrange(10,50)
		cats = jcats + both
		dogs = jdogs + both
		neither = random.randrange(10,100)
		total = jcats + jdogs + both + neither
		intro = "In a school there are " + str(total) + " students."
		fact1 = str(cats) + " students like cats.\\\\"
		fact2 = str(dogs) + " students like dogs.\\\\"
		fact3 = str(neither) + " students like neither cats nor dogs."
		question = "Work out how many students like both cats and dogs."
		question = intro + nl + fact1 + fact2 + fact3 + nl + question
		aimage = "\\begin{overpic}[scale=0.39]{data/images/venn1} \\put(17,49){" + str(jcats) + "}  \\put(82,10){" + str(neither) + "}  \\put(46,49){" + str(both) + "}  \\put(75,49){" + str(jdogs) + "}     \\put(7,75){cats} \\put(80,75){dogs}  \\end{overpic}"
		answer = "\\centering" + aimage + "\\\\" + str(both) + "\\\\ \\raggedright"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def venn2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		jcats = random.randrange(10,50)
		jdogs = random.randrange(10,50)
		both = random.randrange(10,50)
		cats = jcats + both
		dogs = jdogs + both
		neither = random.randrange(10,100)
		total = jcats + jdogs + both + neither
		intro = "In a school there are " + str(total) + " students."
		fact1 = str(cats) + " students like cats.\\\\"
		fact2 = str(dogs) + " students like dogs.\\\\"
		fact3 = str(neither) + " students like neither cats nor dogs."
		question = "Work out how many students like cats but not dogs"
		question = intro + nl + fact1 + fact2 + fact3 + nl + question
		aimage = "\\begin{overpic}[scale=0.39]{data/images/venn1} \\put(17,49){" + str(jcats) + "}  \\put(82,10){" + str(neither) + "}  \\put(46,49){" + str(both) + "}  \\put(75,49){" + str(jdogs) + "}     \\put(7,75){cats} \\put(80,75){dogs}  \\end{overpic}"
		answer = "\\centering" + aimage + "\\\\" + str(jcats) + "\\\\ \\raggedright"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def venn3(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		jcats = random.randrange(10,50)
		jdogs = random.randrange(10,50)
		both = random.randrange(10,50)
		cats = jcats + both
		dogs = jdogs + both
		neither = random.randrange(10,100)
		total = jcats + jdogs + both + neither
		intro = "In a school there are " + str(total) + " students."
		fact1 = str(cats) + " students like cats.\\\\"
		fact2 = str(dogs) + " students like dogs.\\\\"
		fact3 = str(neither) + " students like neither cats nor dogs."
		question = "Work out how many students like dogs but not cats."
		question = intro + nl + fact1 + fact2 + fact3 + nl + question
		aimage = "\\begin{overpic}[scale=0.39]{data/images/venn1} \\put(17,49){" + str(jcats) + "}  \\put(82,10){" + str(neither) + "}  \\put(46,49){" + str(both) + "}  \\put(75,49){" + str(jdogs) + "}     \\put(7,75){cats} \\put(80,75){dogs}  \\end{overpic}"
		answer = "\\centering" + aimage + "\\\\" + str(jdogs) + "\\\\ \\raggedright"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def venn4(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		jcats = random.randrange(10,50)
		jdogs = random.randrange(10,50)
		both = random.randrange(10,50)
		cats = jcats + both
		dogs = jdogs + both
		neither = random.randrange(10,100)
		total = jcats + jdogs + both + neither
		intro = "In a school there are " + str(total) + " students."
		fact1 = str(cats) + " students like cats.\\\\"
		fact2 = str(dogs) + " students like dogs.\\\\"
		fact3 = str(neither) + " students like neither cats nor dogs."
		question = "Work out how many students like only one animal."
		question = intro + nl + fact1 + fact2 + fact3 + nl + question
		aimage = "\\begin{overpic}[scale=0.39]{data/images/venn1} \\put(17,49){" + str(jcats) + "}  \\put(82,10){" + str(neither) + "}  \\put(46,49){" + str(both) + "}  \\put(75,49){" + str(jdogs) + "}     \\put(7,75){cats} \\put(80,75){dogs}  \\end{overpic}"
		answer = "\\centering" + aimage + "\\\\" + str(jcats + jdogs) + "\\\\ \\raggedright"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def venn5(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		jcats = random.randrange(10,50)
		jdogs = random.randrange(10,50)
		both = random.randrange(10,50)
		cats = jcats + both
		dogs = jdogs + both
		neither = random.randrange(10,100)
		total = jcats + jdogs + both + neither
		intro = "In a school there are " + str(total) + " students."
		fact1 = str(cats) + " students like cats.\\\\"
		fact2 = str(dogs) + " students like dogs.\\\\"
		fact3 = str(both) + " students like both cats and dogs."
		question = "Work out how many students like neither cats nor dogs."
		question = intro + nl + fact1 + fact2 + fact3 + nl + question
		aimage = "\\begin{overpic}[scale=0.39]{data/images/venn1} \\put(17,49){" + str(jcats) + "}  \\put(82,10){" + str(neither) + "}  \\put(46,49){" + str(both) + "}  \\put(75,49){" + str(jdogs) + "}     \\put(7,75){cats} \\put(80,75){dogs}  \\end{overpic}"
		answer = "\\centering" + aimage + "\\\\" + str(neither) + "\\\\ \\raggedright"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def venn6(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		jcats = random.randrange(10,50)
		jdogs = random.randrange(10,50)
		both = random.randrange(10,50)
		cats = jcats + both
		dogs = jdogs + both
		neither = random.randrange(10,100)
		total = jcats + jdogs + both + neither
		intro = "In a school there are " + str(total) + " students."
		fact1 = str(cats) + " students like cats.\\\\"
		fact2 = str(dogs) + " students like dogs.\\\\"
		fact3 = str(both) + " students like both cats and dogs."
		question = "Work out how many students like cats but not dogs."
		question = intro + nl + fact1 + fact2 + fact3 + nl + question
		aimage = "\\begin{overpic}[scale=0.39]{data/images/venn1} \\put(17,49){" + str(jcats) + "}  \\put(82,10){" + str(neither) + "}  \\put(46,49){" + str(both) + "}  \\put(75,49){" + str(jdogs) + "}     \\put(7,75){cats} \\put(80,75){dogs}  \\end{overpic}"
		answer = "\\centering" + aimage + "\\\\" + str(jcats) + "\\\\ \\raggedright"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def venn7(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		jcats = random.randrange(10,50)
		jdogs = random.randrange(10,50)
		both = random.randrange(10,50)
		cats = jcats + both
		dogs = jdogs + both
		neither = random.randrange(10,100)
		total = jcats + jdogs + both + neither
		intro = "In a school there are " + str(total) + " students."
		fact1 = str(cats) + " students like cats.\\\\"
		fact2 = str(dogs) + " students like dogs.\\\\"
		fact3 = str(both) + " students like both cats and dogs."
		question = "Work out how many students like dogs but not cats."
		question = intro + nl + fact1 + fact2 + fact3 + nl + question
		aimage = "\\begin{overpic}[scale=0.39]{data/images/venn1} \\put(17,49){" + str(jcats) + "}  \\put(82,10){" + str(neither) + "}  \\put(46,49){" + str(both) + "}  \\put(75,49){" + str(jdogs) + "}     \\put(7,75){cats} \\put(80,75){dogs}  \\end{overpic}"
		answer = "\\centering" + aimage + "\\\\" + str(jdogs) + "\\\\ \\raggedright"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def venn8(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		jcats = random.randrange(10,50)
		jdogs = random.randrange(10,50)
		both = random.randrange(10,50)
		cats = jcats + both
		dogs = jdogs + both
		neither = random.randrange(10,100)
		total = jcats + jdogs + both + neither
		intro = "In a school there are " + str(total) + " students."
		fact1 = str(cats) + " students like cats.\\\\"
		fact2 = str(dogs) + " students like dogs.\\\\"
		fact3 = str(both) + " students like both cats and dogs."
		question = "Work out how many students like only one animal."
		question = intro + nl + fact1 + fact2 + fact3 + nl + question
		aimage = "\\begin{overpic}[scale=0.39]{data/images/venn1} \\put(17,49){" + str(jcats) + "}  \\put(82,10){" + str(neither) + "}  \\put(46,49){" + str(both) + "}  \\put(75,49){" + str(jdogs) + "}     \\put(7,75){cats} \\put(80,75){dogs}  \\end{overpic}"
		answer = "\\centering" + aimage + "\\\\" + str(jdogs + jcats) + "\\\\ \\raggedright"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def venn9(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		jcats = random.randrange(10,50)
		jdogs = random.randrange(10,50)
		both = random.randrange(10,50)
		cats = jcats + both
		dogs = jdogs + both
		neither = random.randrange(10,100)
		total = jcats + jdogs + both + neither
		intro = "In a school there are " + str(total) + " students."
		fact1 = str(jcats) + " students only like cats.\\\\"
		fact2 = str(jdogs) + " students only like dogs.\\\\"
		fact3 = str(neither) + " students like neither cats nor dogs."
		question = "Work out how many students like both cats and dogs."
		question = intro + nl + fact1 + fact2 + fact3 + nl + question
		aimage = "\\begin{overpic}[scale=0.39]{data/images/venn1} \\put(17,49){" + str(jcats) + "}  \\put(82,10){" + str(neither) + "}  \\put(46,49){" + str(both) + "}  \\put(75,49){" + str(jdogs) + "}     \\put(7,75){cats} \\put(80,75){dogs}  \\end{overpic}"
		answer = "\\centering" + aimage + "\\\\" + str(both) + "\\\\ \\raggedright"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def venn10(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		jcats = random.randrange(10,50)
		jdogs = random.randrange(10,50)
		both = random.randrange(10,50)
		cats = jcats + both
		dogs = jdogs + both
		neither = random.randrange(10,100)
		total = jcats + jdogs + both + neither
		intro = "In a school there are " + str(total) + " students."
		fact1 = str(jcats) + " students only like cats.\\\\"
		fact2 = str(jdogs) + " students only like dogs.\\\\"
		fact3 = str(neither) + " students like neither cats nor dogs."
		question = "Work out how many students like cats."
		question = intro + nl + fact1 + fact2 + fact3 + nl + question
		aimage = "\\begin{overpic}[scale=0.39]{data/images/venn1} \\put(17,49){" + str(jcats) + "}  \\put(82,10){" + str(neither) + "}  \\put(46,49){" + str(both) + "}  \\put(75,49){" + str(jdogs) + "}     \\put(7,75){cats} \\put(80,75){dogs}  \\end{overpic}"
		answer = "\\centering" + aimage + "\\\\" + str(cats) + "\\\\ \\raggedright"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def venn11(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		jcats = random.randrange(10,50)
		jdogs = random.randrange(10,50)
		both = random.randrange(10,50)
		cats = jcats + both
		dogs = jdogs + both
		neither = random.randrange(10,100)
		total = jcats + jdogs + both + neither
		intro = "In a school there are " + str(total) + " students."
		fact1 = str(jcats) + " students only like cats.\\\\"
		fact2 = str(jdogs) + " students only like dogs.\\\\"
		fact3 = str(neither) + " students like neither cats nor dogs."
		question = "Work out how many students like dogs."
		question = intro + nl + fact1 + fact2 + fact3 + nl + question
		aimage = "\\begin{overpic}[scale=0.39]{data/images/venn1} \\put(17,49){" + str(jcats) + "}  \\put(82,10){" + str(neither) + "}  \\put(46,49){" + str(both) + "}  \\put(75,49){" + str(jdogs) + "}     \\put(7,75){cats} \\put(80,75){dogs}  \\end{overpic}"
		answer = "\\centering" + aimage + "\\\\" + str(dogs) + "\\\\ \\raggedright"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def venn12(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		jcats = random.randrange(10,50)
		jdogs = random.randrange(10,50)
		both = random.randrange(10,50)
		cats = jcats + both
		dogs = jdogs + both
		neither = random.randrange(10,100)
		total = jcats + jdogs + both + neither
		intro = "Students in a school were asked which animals they like."
		fact1 = str(cats) + " students liked cats.\\\\"
		fact2 = str(dogs) + " students liked dogs.\\\\"
		fact3 = str(both) + " students liked both cats and dogs.\\\\"
		fact4 = str(neither) + " students liked neither cats nor dogs."
		question = "Work out how many students there are in the school."
		question = intro + nl + fact1 + fact2 + fact3 + fact4 + nl + question
		aimage = "\\begin{overpic}[scale=0.39]{data/images/venn1} \\put(17,49){" + str(jcats) + "}  \\put(82,10){" + str(neither) + "}  \\put(46,49){" + str(both) + "}  \\put(75,49){" + str(jdogs) + "}     \\put(7,75){cats} \\put(80,75){dogs}  \\end{overpic}"
		answer = "\\centering" + aimage + "\\\\" + str(total) + "\\\\ \\raggedright"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

