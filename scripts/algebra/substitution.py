#substitution.py


def subs1pos(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the value of "
		else:
			explanation = ""
		num = random.randrange(2,6)
		letters = ["a","b","c","x","y"]
		a = random.randrange(2,11)
		letter = random.choice(letters)
		expressions = [letter + "$^{2}$",str(num) + letter,str(num) + letter + "$^{2}$","(" + str(num) + letter + ")$^{2}$"]
		answers = [a**2,num * a,num * a**2,(num*a)**2]
		choice = random.randrange(0,len(expressions))
#write question
		tempquestions.write(explanation + expressions[choice] + " when " + letter + " = " + str(a))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answers[choice]))



def subs1neg(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the value of "
		else:
			explanation = ""
		num = random.randrange(2,6)
		letters = ["a","b","c","x","y"]
		a = 0 - random.randrange(2,11)
		letter = random.choice(letters)
		expressions = [letter + "$^{2}$",str(num) + letter,str(num) + letter + "$^{2}$","(" + str(num) + letter + ")$^{2}$"]
		answers = [a**2,num * a,num * a**2,(num*a)**2]
		choice = random.randrange(0,len(expressions))
#write question
		tempquestions.write(explanation + expressions[choice] + " when " + letter + " = " + str(a))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answers[choice]))



def subs2pos(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the value of "
		else:
			explanation = ""
		num1 = random.randrange(2,6)
		num2 = random.randrange(2,6)
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		letters.remove(letter1)
		letter2 = random.choice(letters)
		nums = list(range(2,7))
		a = random.choice(nums)
		nums.remove(a)
		b = random.choice(nums)
		sf = random.randrange(2,7)
		c = b * sf
		if random.randrange(0,6)==1:
			expressions = [str(num1) + letter1 + " + " + letter2,str(num1) + letter1 + " - " + letter2,str(num1) + letter1 + " + " + str(num2) + letter2,str(num1) + letter1 + " - " + str(num2) + letter2,letter1 + " + " + str(num2) + letter2,letter1 + " - " + str(num2) + letter2]
			answers = [num1*a + b,num1*a - b,num1*a + num2*b,num1*a - num2*b,a + num2*b,a - num2*b]
			choice = random.randrange(0,len(expressions))
		else:
			expressions = [letter1 + " + " + letter2,letter1 + " - " + letter2,letter1 + letter2,"$\\dfrac{" + letter1 + "}{" + letter2 + "}$",letter1 + letter2 + "$^{2}$","(" + letter1 + letter2 + ")$^{2}$"]
			choice = random.randrange(0,len(expressions))
			if choice==3:
				a = c
			answers = [a + b,a - b,a * b,int(a/b),a * b**2,(a*b)**2]
#write question
		tempquestions.write(explanation + expressions[choice] + " when " + letter1 + " = " + str(a) + " and " + letter2 + " = " + str(b))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answers[choice]))



def subs2neg(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the value of "
		else:
			explanation = ""
		num1 = random.randrange(2,6)
		num2 = random.randrange(2,6)
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		letters.remove(letter1)
		letter2 = random.choice(letters)
		if letter2<letter1:
			temp = letter1
			letter1 = letter2
			letter2 = temp
		nums = list(range(2,7))
		a = random.choice(nums)
		nums.remove(a)
		b = random.choice(nums)
		dec = random.randrange(0,4)
		sf = random.randrange(2,7)
		c = b * sf
		if dec==1:
			a = 0-a
			c = 0-c
		elif dec==2:
			b = 0-b
		elif dec==3:
			a = 0-a
			b = 0-b
		else:
			a = 0-a
			b = 0-b
			c = 0-c
		if random.randrange(0,6)==1:
			expressions = [str(num1) + letter1 + " + " + letter2,str(num1) + letter1 + " - " + letter2,str(num1) + letter1 + " + " + str(num2) + letter2,str(num1) + letter1 + " - " + str(num2) + letter2,letter1 + " + " + str(num2) + letter2,letter1 + " - " + str(num2) + letter2]
			answers = [num1*a + b,num1*a - b,num1*a + num2*b,num1*a - num2*b,a + num2*b,a - num2*b]
			choice = random.randrange(0,len(expressions))
		else:
			expressions = [letter1 + " + " + letter2,letter1 + " - " + letter2,letter1 + letter2,"$\\dfrac{" + letter1 + "}{" + letter2 + "}$",letter1 + letter2 + "$^{2}$","(" + letter1 + letter2 + ")$^{2}$"]
			choice = random.randrange(0,len(expressions))
			if choice==3:
				a = c
			answers = [a + b,a - b,a * b,int(a/b),a * b**2,(a*b)**2]
#write question
		tempquestions.write(explanation + expressions[choice] + " when " + letter1 + " = " + str(a) + " and " + letter2 + " = " + str(b))
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answers[choice]))



def subswallpos(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		expressions = []
		answers = []
		b = random.randrange(2,6)
		c = b * random.randrange(2,6)
		aas = [2,3,4,5,6,7,8,9]
		if b<10:
			aas.remove(b)
		if c<10:
			aas.remove(c)
		a = random.choice(aas)
		ds = [2,3,4,5,6,7,8,9,10,11,12,13,14,15]
		if a<16:
			ds.remove(a)
		if b<16:
			ds.remove(b)
		if c<16:
			ds.remove(c)
		d = random.choice(ds)

		expressions.append("a + d")
		answers.append(str(a+d))

		expressions.append("c - a")
		answers.append(str(c-a))

		expressions.append("ab")
		answers.append(str(a * b))

		expressions.append("$\\dfrac{c}{b}$")
		answers.append(str(int(c/b)))

		expressions.append("c + ab")
		answers.append(str(c + a*b))

		expressions.append("ac - d")
		answers.append(str(a*c - d))

		expressions.append("d$^{2}$")
		answers.append(str(d**2))

		expressions.append("ab$^{2}$")
		answers.append(str(a * b**2))
		
		expressions.append("(ab)$^{2}$")
		answers.append(str((a * b)**2))

		expressions.append("$\\dfrac{ac}{b}$")
		answers.append(str(int(a*c/b)))
		
		expressions.append("abd")
		answers.append(str(a*b*d))

		expressions.append("a$^{2}$ + b$^{2}$")
		answers.append(str(a**2 + b**2))

		expressions.append("ab$^{2}$d")
		answers.append(str(a * b**2 * d))

		expressions.append("b$^{2}$ - 4ac")
		answers.append(str(b**2 - 4*a*c))

		expressions.append("2d$^{2}$ + (bc)$^{2}$")
		answers.append(str(2*d**2 + (b*c)**2))

		qtable = "\\renewcommand{\\arraystretch}{3}\\begin{tabular}{ p{3.5cm} p{3.5cm} p{4cm} } \\circled{1} " + expressions[0] + " & \\circled{6} " + expressions[5] + " & \\circled{11} " + expressions[10] + " \\\\ \\circled{2} " + expressions[1] + " & \\circled{7} " + expressions[6] + " & \\circled{12} " + expressions[11] + " \\\\ \\circled{3} " + expressions[2] + " & \\circled{8} " + expressions[7] + " & \\circled{13} " + expressions[12] + " \\\\ \\circled{4} " + expressions[3] + " & \\circled{9} " + expressions[8] + " & \\circled{14} " + expressions[13] + " \\\\ \\circled{5} " + expressions[4] + " & \\circled{10} " + expressions[9] + " & \\circled{15} " + expressions[14] + " \\\\ \\end{tabular}"
		for i in range(0,15):
			expressions[i] = expressions[i] + " = " + answers[i]
		answer = "\\renewcommand{\\arraystretch}{3}\\begin{tabular}{ p{3.5cm} p{3.5cm} p{4cm} } \\circled{1} " + expressions[0] + " & \\circled{6} " + expressions[5] + " & \\circled{11} " + expressions[10] + " \\\\ \\circled{2} " + expressions[1] + " & \\circled{7} " + expressions[6] + " & \\circled{12} " + expressions[11] + " \\\\ \\circled{3} " + expressions[2] + " & \\circled{8} " + expressions[7] + " & \\circled{13} " + expressions[12] + " \\\\ \\circled{4} " + expressions[3] + " & \\circled{9} " + expressions[8] + " & \\circled{14} " + expressions[13] + " \\\\ \\circled{5} " + expressions[4] + " & \\circled{10} " + expressions[9] + " & \\circled{15} " + expressions[14] + " \\\\ \\end{tabular}"
#write question
		tempquestions.write("\\centering a = " + str(a) + "\\hspace{1cm} b = " + str(b) + "\\hspace{1cm} c = " + str(c) + "\\hspace{1cm} d = " + str(d) + "\\\\[1cm] " + qtable)
		tempquestions.write("\n")
#write answer
		tempquestions.write("\\centering a = " + str(a) + "\\hspace{1cm} b = " + str(b) + "\\hspace{1cm} c = " + str(c) + "\\hspace{1cm} d = " + str(d) + "\\\\[1cm] " + answer)



def subswall(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		expressions = []
		answers = []
		b = random.randrange(2,6)*(-1)**random.randrange(0,2)
		c = b * random.randrange(2,6) * (-1)**random.randrange(0,2)
		aas = [2,3,4,5,6,7,8,9,-2,-3,-4,-5,-6,-7,-8,-9]
		if b<10 and b>-10:
			aas.remove(b)
		if c<10 and c>-10:
			aas.remove(c)
		a = random.choice(aas)
		ds = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15]
		if a<16 and a>-16:
			ds.remove(a)
		if b<16 and b>-16:
			ds.remove(b)
		if c<16 and c>-16:
			ds.remove(c)
		d = random.choice(ds)

		expressions.append("a + d")
		answers.append(str(a+d))

		expressions.append("c - a")
		answers.append(str(c-a))

		expressions.append("ab")
		answers.append(str(a * b))

		expressions.append("$\\dfrac{c}{b}$")
		answers.append(str(int(c/b)))

		expressions.append("c + ab")
		answers.append(str(c + a*b))

		expressions.append("ac - d")
		answers.append(str(a*c - d))

		expressions.append("d$^{2}$")
		answers.append(str(d**2))

		expressions.append("ab$^{2}$")
		answers.append(str(a * b**2))
		
		expressions.append("(ab)$^{2}$")
		answers.append(str((a * b)**2))

		expressions.append("$\\dfrac{ac}{b}$")
		answers.append(str(int(a*c/b)))
		
		expressions.append("abd")
		answers.append(str(a*b*d))

		expressions.append("a$^{2}$ + b$^{2}$")
		answers.append(str(a**2 + b**2))

		expressions.append("ab$^{2}$d")
		answers.append(str(a * b**2 * d))

		expressions.append("b$^{2}$ - 4ac")
		answers.append(str(b**2 - 4*a*c))

		expressions.append("2d$^{2}$ + (bc)$^{2}$")
		answers.append(str(2*d**2 + (b*c)**2))

		qtable = "\\renewcommand{\\arraystretch}{3}\\begin{tabular}{ p{3.5cm} p{3.5cm} p{4cm} } \\circled{1} " + expressions[0] + " & \\circled{6} " + expressions[5] + " & \\circled{11} " + expressions[10] + " \\\\ \\circled{2} " + expressions[1] + " & \\circled{7} " + expressions[6] + " & \\circled{12} " + expressions[11] + " \\\\ \\circled{3} " + expressions[2] + " & \\circled{8} " + expressions[7] + " & \\circled{13} " + expressions[12] + " \\\\ \\circled{4} " + expressions[3] + " & \\circled{9} " + expressions[8] + " & \\circled{14} " + expressions[13] + " \\\\ \\circled{5} " + expressions[4] + " & \\circled{10} " + expressions[9] + " & \\circled{15} " + expressions[14] + " \\\\ \\end{tabular}"
		for i in range(0,15):
			expressions[i] = expressions[i] + " = " + answers[i]
		answer = "\\renewcommand{\\arraystretch}{3}\\begin{tabular}{ p{3.5cm} p{3.5cm} p{4cm} } \\circled{1} " + expressions[0] + " & \\circled{6} " + expressions[5] + " & \\circled{11} " + expressions[10] + " \\\\ \\circled{2} " + expressions[1] + " & \\circled{7} " + expressions[6] + " & \\circled{12} " + expressions[11] + " \\\\ \\circled{3} " + expressions[2] + " & \\circled{8} " + expressions[7] + " & \\circled{13} " + expressions[12] + " \\\\ \\circled{4} " + expressions[3] + " & \\circled{9} " + expressions[8] + " & \\circled{14} " + expressions[13] + " \\\\ \\circled{5} " + expressions[4] + " & \\circled{10} " + expressions[9] + " & \\circled{15} " + expressions[14] + " \\\\ \\end{tabular}"
#write question
		tempquestions.write("\\centering a = " + str(a) + "\\hspace{1cm} b = " + str(b) + "\\hspace{1cm} c = " + str(c) + "\\hspace{1cm} d = " + str(d) + "\\\\[1cm] " + qtable)
		tempquestions.write("\n")
#write answer
		tempquestions.write("\\centering a = " + str(a) + "\\hspace{1cm} b = " + str(b) + "\\hspace{1cm} c = " + str(c) + "\\hspace{1cm} d = " + str(d) + "\\\\[1cm] " + answer)


def subsnegdec(n,explanationn):
#from hia8/9
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Find the value of "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		a = random.randrange(2,11)
		letter1 = random.choice(letters)
		letters.remove(letter1)
		letter2 = random.choice(letters)
		num1 = (random.randrange(1,10) + random.randrange(1,10)/10)*(-1)**random.randrange(1,3)
		num2 = (random.randrange(1,10) + random.randrange(1,10)/10)*(-1)**random.randrange(1,3)
		coeff1 = random.randrange(2,10)
		coeff2 = random.randrange(2,10)
		if random.randrange(0,2)==0:
			question = str(coeff1) + letter1 + " + " + str(coeff2) + letter2
			answer = rounddp(coeff1*num1 + coeff2 * num2,2)
		else:
			question = str(coeff1) + letter1 + " - " + str(coeff2) + letter2
			answer = rounddp(coeff1*num1 - coeff2 * num2,2)
		question = question + " when \\mbox{" + letter1 + " = " + str(num1) + "} and \\mbox{" + letter2 + " = " + str(num2) + "}"
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))
