#!/usr/bin/env python3
import subprocess, os, shutil, random
filename = "Negative Four Rules Torture"
title = "Adding, Subtracting, Multiplying and Dividing Negative Numbers"
from torture.torture import negativeadd1, negativeadd2, negativesubtract1, negativesubtract2, negativesubtract3, negativemultiply1, negativemultiply2, negativedivide1, negativedivide2, negativedivide3
tempquestions = open("tempquestions","a")
for x in range(0,1):
	for y in range(0,25):
		if random.randrange(1,3)==1:
			negativeadd1(1)
		else:
			negativeadd2(1)
	for y in range(0,25):
		dec = random.randrange(1,4)
		if dec==1:
			negativesubtract1(1)
		elif dec==2:
			negativesubtract2(1)
		else:
			negativesubtract3(1)
	for y in range(0,25):
		if random.randrange(1,3)==1:
			negativemultiply1(1)
		else:
			negativemultiply2(1)
	for y in range(0,25):
		dec = random.randrange(1,4)
		if dec==1:
			negativedivide1(1)
		elif dec==2:
			negativedivide2(1)
		else:
			negativedivide3(1)
	for y in range(0,25):
		dec = random.randrange(1,11)
		if dec==1:
			negativeadd1(1)
		elif dec==2:
			negativeadd2(1)
		elif dec==3:
			negativesubtract1(1)
		elif dec==4:
			negativesubtract2(1)
		elif dec==5:
			negativesubtract3(1)
		elif dec==6:
			negativemultiply1(1)
		elif dec==7:
			negativemultiply2(1)
		elif dec==8:
			negativedivide1(1)
		elif dec==9:
			negativedivide2(1)
		else:
			negativedivide3(1)
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

shutil.copyfile("templates/torture.tex", "temp1")
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
	writedoc.write(line.replace("title",title))
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
