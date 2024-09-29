#!/usr/bin/env python3
import subprocess, os, shutil, random
filename = "KS4 Intermediate Unit 3 Starter"
topic = "Starter"
title = "Unit 3"
hint = ""

from algebra.manipulation import rearrange1,rearrange2,singlebracketexpansion7showthat

from fouroperators.multiplication import twobythreemultiplication

from fouroperators.subtraction import fullsubtraction

from fdp.estimation import estimation1

from fdp.rounding import round1dp,round1sf2,round1sf1

from examquestions.shape import pythaggrid

from sdt.sdt import journey

from indices.standardform import sfconvertpos2,sfconvertneg2

from calculator.typing import squareroot1

from fdp.percentages import compoundinterest

from algebra.manipulation import singlebracketexpansion7showthat,singlebracketexpansion2,singlebracketfactorise8

from equations.linear import threestep1,threestep2,fourstep1

from equations.quadratics import expandquadraticspos

from graphs.quadratic import substitution3pos,substitution3neg,substitution4pos

from graphs.linear import writegradient,writeintercept

from algebra.sequences import nthtermpos,genseqquad1

tempquestions = open("tempquestions","a")
for x in range(0,6):

	question1 = [rearrange1,rearrange2,nthtermpos,genseqquad1,expandquadraticspos]
	question2 = [sfconvertpos2,sfconvertneg2,squareroot1,pythaggrid,journey]
	question3 = [substitution3pos,substitution3neg,substitution4pos,singlebracketexpansion7showthat,singlebracketexpansion2,singlebracketfactorise8]
	question4 = [twobythreemultiplication,fullsubtraction,writegradient,writeintercept]
	question5 = [estimation1,round1dp,round1sf2,round1sf1,compoundinterest]
	question6 = [threestep1,threestep2,fourstep1]


	questions = [random.choice(question1),random.choice(question2),random.choice(question3),random.choice(question4),random.choice(question5)]
	random.shuffle(questions)
	questions[0](1,1)
	questions[1](1,1)
	questions[2](1,1)
	questions[3](1,1)
	questions[4](1,1)
	random.choice(question6)(1,1,0)



tempquestions.close()

#Don't edit this chunk
tempquestions = open("tempquestions","r")
all = tempquestions.read().splitlines()
lines = sum(1 for line in open('tempquestions'))
lines=int((lines - 1)/2)
#lines is now the total number of questions
questions = []
answers = []
for x in range(0, lines):
	questions.append(str(all[2*x+1]))
	answers.append(str(all[2*x+2]))
tempquestions.close()
os.remove("tempquestions")

shutil.copyfile("templates/boardtallwide2.tex", "temp1")
decision = 1


for x in range(0, lines):
	if decision==1:
		readdoc=open("temp1","r")
		writedoc=open("temp2","w")	
	else:
		readdoc=open("temp2","r")
		writedoc=open("temp1","w")	
	qterm = "q" + str(x+1) + " "
	for line in readdoc:
		writedoc.write(line.replace(qterm, questions[x]))
	decision*=-1
	readdoc.close()
	writedoc.close()


for x in range(0, lines):
	if decision==1:
		readdoc=open("temp1","r")
		writedoc=open("temp2","w")	
	else:
		readdoc=open("temp2","r")
		writedoc=open("temp1","w")	
	aterm = "a" + str(x+1) + " "
	for line in readdoc:
		writedoc.write(line.replace(aterm, answers[x]))
	decision*=-1
	readdoc.close()
	writedoc.close()


if decision==1:
	shutil.copyfile("temp1","temp2")

readdoc=open("temp2","r")
writedoc=open("temp1","w")	
for line in readdoc:
	writedoc.write(line.replace("topic",topic))
readdoc.close()
writedoc.close()
shutil.copyfile("temp1",filename+".tex")

readdoc=open("temp1","r")
writedoc=open("temp2","w")	
for line in readdoc:
	writedoc.write(line.replace("title",title ))
readdoc.close()
writedoc.close()

readdoc=open("temp2","r")
writedoc=open("temp1","w")	
for line in readdoc:
	writedoc.write(line.replace("hint",hint))
readdoc.close()
writedoc.close()
shutil.copyfile("temp1",filename+".tex")


subprocess.call(["pdflatex", filename+".tex"])
os.remove(filename + ".aux")
os.remove(filename + ".log")
os.remove(filename + ".tex")
os.remove(filename + ".nav")
os.remove(filename + ".out")
os.remove(filename + ".snm")
os.remove(filename + ".toc")
os.remove("temp1")
os.remove("temp2")
