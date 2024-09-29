#!/usr/bin/env python3
import subprocess, os, shutil, random
tempquestions = open("tempquestions","a")
#####################################
#ONLY EDIT THIS PART
#####################################

filename = "Archie|starter|"
hint = "~"
title = "Revision"
template = "mpdf2starter"




from equations.simultaneous import simeqlinadd1,simeqlinadd2,simeqlin3,simeqlinsub1,simeqlinsub2, simeqquad1,simeqquad2
from shape.trig import sinangle,cosangle,tanangle,sinside1,sinside2,cosside1,cosside2,tanside1,tanside2
from algebra.fractions import quaddots,quaddots2,fracadd1,fracsubtract1,fracadd2,fracsubtract2
from algebra.manipulation import rearrange4
from equations.quadratics import factorisequadraticsdots1,factorisequadraticsdots2
from graphs.linear import equationofline3
from data.histograms import histotable,histotablemixer


#tier1
q1 = [factorisequadraticsdots1,factorisequadraticsdots2]
q2 = [quaddots,quaddots2,fracadd1,fracsubtract1,fracadd2,fracsubtract2]
q3 = [simeqlinadd1,simeqlinadd2,simeqlin3,simeqlinsub1,simeqlinsub2, simeqquad1,simeqquad2]

#tier2

q4 = [sinangle,cosangle,tanangle,sinside1,sinside2,cosside1,cosside2,tanside1,tanside2]
q5 = [rearrange4]
#tier3

q6 = [equationofline3]


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