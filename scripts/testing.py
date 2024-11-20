#!/usr/bin/env python3
import subprocess, os, shutil, random
from utilities.templategen import generatetemplate,generatetitlepage,generatecontentspage
content = ""
starter = "starter"
bycolumn = "bycolumn"
#####################################

chapter = "Test File"
filename = "Test File"
template = "mpdf2"
from functions.writcalc import *

#####################################

content = content + generatecontentspage(chapter)


title = "Division"
hint = "~"
section = "Decimal Division 2"
description = "Divisor is a decimal"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(4,9,bycolumn,0,100,100)
tempquestions = divisionbydecimal(9,0)
tempquestions += decimaldivision3(9,0)
tempquestions += divisionbydecimal2(9,0)
tempquestions += decimaldivision4(9,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext



#####################################
with open("templates/"+template+".tex", 'r') as file :
	templatetext = file.read()
templatetext = templatetext.replace("CONTENT",content)
with open(filename+".tex", 'w') as file:
	file.write(templatetext)
subprocess.call(["pdflatex", filename+".tex"])
subprocess.call(["pdflatex", filename+".tex"])
os.remove(filename + ".aux")
os.remove(filename + ".log")
os.remove(filename + ".tex")
os.remove(filename + ".nav")
os.remove(filename + ".out")
os.remove(filename + ".snm")
os.remove(filename + ".toc")
os.remove(filename + ".vrb")
