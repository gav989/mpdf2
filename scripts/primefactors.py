#!/usr/bin/env python3
import subprocess, os, shutil, random
from utilities.templategen import generatetemplate,generatetitlepage,generatecontentspage
content = ""
starter = "starter"
#####################################

chapter = "Prime Factors"
filename = "Prime Factors"
template = "mpdf2"
from functions.primefactors import *

#####################################

content = content + generatecontentspage(chapter)


title = "Prime Factorisation"
hint = "Write as a product of prime factors:"
section = "Prime Factorisation"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(2,10,3,0,100,100)
tempquestions = primefactorisation1(10,0)
tempquestions += primefactorisation2(10,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(2,10,3,0,100,100)
tempquestions = primefactorisation1(10,0)
tempquestions += primefactorisation2(10,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext


title = "HCF"
hint = "Find the highest common factor of:"
section = "HCF"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,10,4,1,100,100)
tempquestions = hcf(30,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(3,10,4,1,100,100)
tempquestions = hcf(30,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext


title = "LCM"
hint = "Find the lowest common multiple of:"
section = "LCM"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(3,10,4,1,100,100)
tempquestions = lcm(30,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(3,10,4,1,100,100)
tempquestions = lcm(30,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext

title = "HCF and LCM"
hint = "Find the HCF and LCM of:"
section = "HCF and LCM"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(2,10,4,0,100,100)
tempquestions = hcflcm(20,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(2,10,4,0,100,100)
tempquestions = hcflcm(20,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext

title = "Reverse HCF and LCM"
hint = "~"
section = "Reverse HCF and LCM"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(2,3,1,0,100,100)
tempquestions = hcflcmreverse(6,1)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(2,3,1,0,100,100)
tempquestions = hcflcmreverse(6,1)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext

title = "Trains Problem"
hint = "~"
section = "Trains Problem"
description = "~"
examples = "~"
titlepage = generatetitlepage(section,description,examples)
content = content + titlepage
###
frametext = generatetemplate(1,3,1,0,0,100)
tempquestions = trains(10,0)
frametext = frametext.replace("hint",hint)
frametext = frametext.replace("tttitle",title)
for i in range(0, int(len(tempquestions)/2)):
	qterm = "q" + str(i+1) + " "
	aterm = "a" + str(i+1) + " "
	frametext = frametext.replace(qterm,tempquestions[i*2])
	frametext = frametext.replace(aterm,tempquestions[i*2+1])
content = content + frametext
frametext = generatetemplate(1,3,1,0,0,100)
tempquestions = trains(10,0)
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
