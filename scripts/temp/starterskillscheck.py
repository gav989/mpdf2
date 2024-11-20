#!/usr/bin/env python3
import subprocess, os, shutil, random
tempquestions = open("tempquestions","a")
#####################################
#ONLY EDIT THIS PART
#####################################

filename = "Skills Check"
hint = "~"
title = "Skills Check"
template = "mpdf2starter"






from fouroperators.addition import threedigitaddition,decimaladdition,fulladdition
from fouroperators.subtraction import threedigitsubtraction,decimalsubtraction,fullsubtraction
from fouroperators.ten import multten,multhundred,multthousand,divten,divhundred,divthousand

from torture.torture import multdivtht3



from fouroperators.addition import threedigitaddition,decimaladdition,fulladdition
from fouroperators.subtraction import threedigitsubtraction,decimalsubtraction
from fouroperators.multiplication import threebyonemultiplication,twobythreemultiplication,decimalmultiplication1,timestables,decimalmultiplication2
from fouroperators.division import singledigitdivision,twodigitdivisioneasy,twodigitdivision,decimaldivision2,decimaldivision1
from fouroperators.ten import multten,multhundred,multthousand,divten,divhundred,divthousand
from sdt.time import timeadd2451,timeadd2452,timesubtract2451,timesubtract2452,timeadd1251,timeadd1252,timesubtract1251,timesubtract1252,timediff
from starters.starters import skillscheckreversefourops,skillscheckdoublehalve


#tier1
q1 = [timestables,timestables,timestables,timestables,timestables,timestables,multten,multhundred,multthousand,divten,divhundred,divthousand]
q2 = [fulladdition,fullsubtraction,decimaladdition,decimalsubtraction]
q3 = [threebyonemultiplication,twobythreemultiplication,decimalmultiplication1,decimalmultiplication2]

#tier2

q4 = [singledigitdivision,twodigitdivisioneasy,twodigitdivision,decimaldivision2,decimaldivision1]
q5 = [skillscheckreversefourops,skillscheckdoublehalve]
#tier3

q6 = [timeadd2451,timeadd2452,timesubtract2451,timesubtract2452,timeadd1251,timeadd1252,timesubtract1251,timesubtract1252,timediff]


for i in range(0,8):
	random.choice(q1)(1,0)
	random.choice(q2)(1,0)
	random.choice(q3)(1,0)
	random.choice(q4)(1,0)
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