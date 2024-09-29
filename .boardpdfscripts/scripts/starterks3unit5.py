#!/usr/bin/env python3
import subprocess, os, shutil, random
filename = "KS3 Unit 5 Starter"
topic = "Starter"
title = "Unit 5"
hint = ""

#TODO
#list factors
#bidmas
#given that x /
#substitution

from fouroperators.addition import fulladdition,decimaladdition
from fouroperators.subtraction import fullsubtraction,decimalsubtraction
from fouroperators.multiplication import twobytwomultiplication,twobythreemultiplication
from fouroperators.division import singledigitdivision,twodigitdivision,twodigittables
from fdp.fdp import orderdecimals,orderfractions,orderfdp
from fdp.fractionoperations import fractionofamount2,fractionsadd,fractionssubtract,mixednumbersadd,mixednumberssubtract
from algebra.manipulation import collect1,collect2
from algebra.sequences import seqnext

tempquestions = open("tempquestions","a")
for x in range(0,6):

	question1 = [fulladdition,decimaladdition,fullsubtraction,decimalsubtraction]
	question2 = [twobytwomultiplication,twobythreemultiplication]
	question3 = [singledigitdivision,twodigitdivision,twodigittables]
	question4 = [fractionofamount2]
	question5 = [fractionsadd,fractionssubtract,mixednumbersadd,mixednumberssubtract]
	question6 = [orderdecimals,orderfractions,orderfdp]
	question7 = [collect1,collect2]
	question8 = [seqnext]


	questions = [random.choice(question1),random.choice(question2),random.choice(question3),random.choice(question4),random.choice(question5),random.choice(question6),random.choice(question7),random.choice(question8)]
	random.shuffle(questions)
	questions[0](1,1)
	questions[1](1,1)
	questions[2](1,1)
	questions[3](1,1)
	questions[4](1,1)
	questions[5](1,1)
	questions[6](1,1)
	questions[7](1,1)
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

shutil.copyfile("templates/boardtallwide.tex", "temp1")
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
