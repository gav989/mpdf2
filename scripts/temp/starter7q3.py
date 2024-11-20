#!/usr/bin/env python3
import subprocess, os, shutil, random
tempquestions = open("tempquestions","a")
#####################################
#ONLY EDIT THIS PART
#####################################

filename = "7Q3"
hint = "~"
title = "Revision"
template = "mpdf2starter"



from starters.starters import shapenamesstarter, subs1
from probability.simple import simpleprobstarter
from shape.angles import straightline,aroundapoint,inatriangle,opposite
from fdp.fractionoperations import fractionsmultiply,fractionsequivalent
from facts.fmp import fmpscwall
from fdp.fdp import fdpwallstarter
from fdp.rounding import round1dp,round2dp
from fdp.fdp import orderfractions,orderfdp
from primes.primefactors import hcf
from fdp.percentages import percincdec

#tier1
q1 = [fractionsmultiply,fractionsequivalent]
q2 = [round1dp,round2dp]
q3 = [orderfractions,orderfdp]

#tier2
q4 = [shapenamesstarter,fmpscwall,fdpwallstarter]
q5 = [straightline,aroundapoint,inatriangle,opposite,subs1,subs1,subs1,subs1,simpleprobstarter,simpleprobstarter,simpleprobstarter,simpleprobstarter]

#tier3
q6 = [hcf,percincdec]


for i in range(0,8):
	random.choice(q1)(1,1)
	random.choice(q2)(1,1)
	random.choice(q3)(1,1)
	random.choice(q4)(1,1)
	random.choice(q5)(1,1)
	random.choice(q6)(1,1)



#####################################
tempquestions.close()
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

# Read template to RAM
filedata = None
with open("templates/"+template+".tex", 'r') as file :
	filedata = file.read()

# Replace text strings
filedata = filedata.replace("hint",hint)
filedata = filedata.replace("tttitle",title)
for x in range(0, lines):
	qterm = "q" + str(x+1) + " "
	aterm = "a" + str(x+1) + " "
	filedata = filedata.replace(qterm,questions[x])
	filedata = filedata.replace(aterm,answers[x])

# Write to tex file
with open(filename+".tex", 'w') as file:
	file.write(filedata)

subprocess.call(["pdflatex", filename+".tex"])
os.remove(filename + ".aux")
os.remove(filename + ".log")
os.remove(filename + ".tex")
os.remove(filename + ".nav")
os.remove(filename + ".out")
os.remove(filename + ".snm")
os.remove(filename + ".toc")
os.remove(filename + ".vrb")