#!/usr/bin/env python3
import subprocess, os, shutil, random
filename = "Year 9 Number Starter"
topic = "Starter"
title = "Year 9 Number"
hint = ""
from fouroperators.multiplication import twobytwomultiplication, twobythreemultiplication, decimalmultiplication1, decimalmultiplication2
from fouroperators.division import singledigitdivision,twodigitdivision,decimaldivision1,decimaldivision2
from fdp.rounding import round10,round100,round1000,round0dp,round1dp,round2dp,round1sf1,round1sf2,round2sf1,round2sf2,round3sf1,round3sf2
from primes.primefactors import hcflcm
from fdp.percentages import percofamount5,percincdec5
from fdp.fdp import orderdecimals,orderfractions,orderfdp
from fdp.fractionoperations import fractionofamount2, fractionsequivalent, fractionsimplify, fractionconvert1, fractionconvert2, fractionsadd, fractionssubtract, mixednumbersadd, mixednumberssubtract
from measures.metricconversions import mcmass,mccapacity,mcdistance

tempquestions = open("tempquestions","a")
for x in range(0,6):

	question1 = [twobytwomultiplication,twobythreemultiplication,decimalmultiplication1,decimalmultiplication2]
	random.choice(question1)(1,1)

	question2 = [singledigitdivision,twodigitdivision,decimaldivision1,decimaldivision2]
	random.choice(question2)(1,1)

	question3 = [round10,round100,round1000,round0dp,round1dp,round2dp,round1sf1,round1sf2,round2sf1,round2sf2,round3sf1,round3sf2]
	random.choice(question3)(1,1)

	question4 = [mcmass,mccapacity,mcdistance]
	random.choice(question4)(1,1)

	question5 = [fractionofamount2]
	random.choice(question5)(1,1)

	question6 = [percofamount5,percincdec5]
	random.choice(question6)(1,1)

	question7 = [orderdecimals,orderfractions,orderfdp]
	random.choice(question7)(1,1)

	question8 = [hcflcm]
	random.choice(question8)(1,1)

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
