#!/usr/bin/env python3
import subprocess, os, shutil, random
filename = "KS3 Unit 7 Extension Starter"
topic = "Starter"
title = "Unit 7 Extension"
hint = ""

#TODO
#estimation
#bidmas
#calc typing

from fouroperators.multiplication import twobytwomultiplication,twobythreemultiplication,decimalmultiplication1,decimalmultiplication2
from fouroperators.division import decimaldivision2,decimaldivision1,twodigitdivision,singledigitdivision
from fouroperators.addition import decimaladdition
from fouroperators.subtraction import decimalsubtraction
from fdp.fdp import orderfdp
from fdp.fractionoperations import fractionofamount2,fractionconvert1,fractionconvert2,fractionofamount3,fractionsadd,fractionssubtract,fractionsmultiply,fractionsdivide,mixednumbersadd,mixednumberssubtract,mixednumbersmultiply,mixednumbersdivide
from fdp.percentages import percincdec5
from fdp.rounding import round1dp,round2dp,round1sf1
from indices.laws import indind,divind,multind
from primes.primefactors import factortrees1,factortrees2,hcf,lcm

tempquestions = open("tempquestions","a")
for x in range(0,6):

	question1 = [orderfdp,percincdec5,fractionofamount2,fractionconvert1,fractionconvert2,fractionofamount3]
	question2 = [fractionsadd,fractionssubtract,fractionsmultiply,fractionsdivide,mixednumbersadd,mixednumberssubtract,mixednumbersmultiply,mixednumbersdivide]
	question3 = [factortrees1,factortrees2,hcf,lcm]
	question4 = [indind,divind,multind]
	question5 = [round1dp,round2dp,round1sf1]
	question6 = [decimalsubtraction,decimaldivision2,decimaldivision1,twodigitdivision,singledigitdivision,twobytwomultiplication,twobythreemultiplication,decimalmultiplication1,decimalmultiplication2,decimaladdition]


	questions = [random.choice(question1),random.choice(question2),random.choice(question3),random.choice(question4),random.choice(question5)]
	random.shuffle(questions)
	questions[0](1,1)
	questions[1](1,1)
	questions[2](1,1)
	questions[3](1,1)
	questions[4](1,1)
	random.choice(question6)(1,1)

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
