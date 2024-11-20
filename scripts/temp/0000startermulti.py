#!/usr/bin/env python3
import subprocess, os, shutil, random
hint = "~"
template = "mpdf2starter"
#####################################
#ONLY EDIT THIS PART
#####################################



#██╗███╗   ███╗██████╗  ██████╗ ██████╗ ████████╗███████╗
#██║████╗ ████║██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝
#██║██╔████╔██║██████╔╝██║   ██║██████╔╝   ██║   ███████╗
#██║██║╚██╔╝██║██╔═══╝ ██║   ██║██╔══██╗   ██║   ╚════██║
#██║██║ ╚═╝ ██║██║     ╚██████╔╝██║  ██║   ██║   ███████║
#╚═╝╚═╝     ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝
                                                        

                                                                                                









from shape.angles import polygonanglestable
from graphs.linear import equationoflinepara
from graphs.linear import equationoflineperp
from equations.quadratics import factorisequadratics1
from equations.quadratics import factorisequadratics2
from equations.quadratics import factorisequadraticsdots1
from equations.quadratics import factorisequadraticsdots2
from indices.surds import simplifysurd1
from fdp.fractionoperations import fractionsmultiplysimplifyfirst
from algebra.proportion import direct,directsquare,directsquareroot,inverse,inversesquare,inversesquareroot

from fdp.percentages import percreverse
from shape.trig import sinangle,cosangle,tanangle,sinside1,sinside2,cosside1,cosside2,tanside1,tanside2
from equations.simultaneous import simeqlin1,simeqlin2,simeqlin3
from primes.primefactors import hcf


# ██████╗ ██╗   ██╗███████╗███████╗████████╗██╗ ██████╗ ███╗   ██╗    ██████╗  █████╗  ██████╗██╗  ██╗███████╗
#██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║    ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝
#██║   ██║██║   ██║█████╗  ███████╗   ██║   ██║██║   ██║██╔██╗ ██║    ██████╔╝███████║██║     █████╔╝ ███████╗
#██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║   ██║██║   ██║██║╚██╗██║    ██╔═══╝ ██╔══██║██║     ██╔═██╗ ╚════██║
#╚██████╔╝╚██████╔╝███████╗███████║   ██║   ██║╚██████╔╝██║ ╚████║    ██║     ██║  ██║╚██████╗██║  ██╗███████║
# ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝
             

filename01 = "Starter 01|starter|"
title01 = "Starter 01"
s1q1 = [simplifysurd1]
s1q2 = [simplifysurd1]
s1q3 = [simplifysurd1]
s1q4 = [simplifysurd1]
s1q5 = [simplifysurd1]
s1q6 = [simplifysurd1]
s1 = [s1q1,s1q2,s1q3,s1q4,s1q5,s1q6]

filename02 = "Starter 02|starter|"
title02 = "Starter 02"
s2q1 = [simplifysurd1]
s2q2 = [simplifysurd1]
s2q3 = [simplifysurd1]
s2q4 = [simplifysurd1]
s2q5 = [simplifysurd1]
s2q6 = [simplifysurd1]
s2 = [s2q1,s2q2,s2q3,s2q4,s2q5,s2q6]

filename03 = "Starter 03|starter|"
title03 = "Starter 03"
s3q1 = [simplifysurd1]
s3q2 = [simplifysurd1]
s3q3 = [simplifysurd1]
s3q4 = [simplifysurd1]
s3q5 = [simplifysurd1]
s3q6 = [simplifysurd1]
s3 = [s3q1,s3q2,s3q3,s3q4,s3q5,s3q6]

filename04 = "Starter 04|starter|"
title04 = "Starter 04"
s4q1 = [simplifysurd1]
s4q2 = [simplifysurd1]
s4q3 = [simplifysurd1]
s4q4 = [simplifysurd1]
s4q5 = [simplifysurd1]
s4q6 = [simplifysurd1]
s4 = [s4q1,s4q2,s4q3,s4q4,s4q5,s4q6]

filename05 = "Starter 05|starter|"
title05 = "Starter 05"
s5q1 = [simplifysurd1]
s5q2 = [simplifysurd1]
s5q3 = [simplifysurd1]
s5q4 = [simplifysurd1]
s5q5 = [simplifysurd1]
s5q6 = [simplifysurd1]
s5 = [s5q1,s5q2,s5q3,s5q4,s5q5,s5q6]

filename06 = "Starter 06|starter|"
title06 = "Starter 06"
s6q1 = [simplifysurd1]
s6q2 = [simplifysurd1]
s6q3 = [simplifysurd1]
s6q4 = [simplifysurd1]
s6q5 = [simplifysurd1]
s6q6 = [simplifysurd1]
s6 = [s6q1,s6q2,s6q3,s6q4,s6q5,s6q6]

filename07 = "Starter 07|starter|"
title07 = "Starter 07"
s7q1 = [simplifysurd1]
s7q2 = [simplifysurd1]
s7q3 = [simplifysurd1]
s7q4 = [simplifysurd1]
s7q5 = [simplifysurd1]
s7q6 = [simplifysurd1]
s7 = [s7q1,s7q2,s7q3,s7q4,s7q5,s7q6]

filename08 = "Starter 08|starter|"
title08 = "Starter 08"
s8q1 = [simplifysurd1]
s8q2 = [simplifysurd1]
s8q3 = [simplifysurd1]
s8q4 = [simplifysurd1]
s8q5 = [simplifysurd1]
s8q6 = [simplifysurd1]
s8 = [s8q1,s8q2,s8q3,s8q4,s8q5,s8q6]

filename09 = "Starter 09|starter|"
title09 = "Starter 09"
s9q1 = [simplifysurd1]
s9q2 = [simplifysurd1]
s9q3 = [simplifysurd1]
s9q4 = [simplifysurd1]
s9q5 = [simplifysurd1]
s9q6 = [simplifysurd1]
s9 = [s9q1,s9q2,s9q3,s9q4,s9q5,s9q6]

filename10 = "Starter 10|starter|"
title10 = "Starter 10"
s10q1 = [simplifysurd1]
s10q2 = [simplifysurd1]
s10q3 = [simplifysurd1]
s10q4 = [simplifysurd1]
s10q5 = [simplifysurd1]
s10q6 = [simplifysurd1]
s10 = [s10q1,s10q2,s10q3,s10q4,s10q5,s10q6]

filenames = [filename01,filename02,filename03,filename04,filename05,filename06,filename07,filename08,filename09,filename10]
titles = [title01,title02,title03,title04,title05,title06,title07,title08,title09,title10]
starters = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]


# ██████╗██████╗ ███████╗ █████╗ ████████╗███████╗    ███████╗██╗██╗     ███████╗███████╗
#██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝    ██╔════╝██║██║     ██╔════╝██╔════╝
#██║     ██████╔╝█████╗  ███████║   ██║   █████╗      █████╗  ██║██║     █████╗  ███████╗
#██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██╔══╝      ██╔══╝  ██║██║     ██╔══╝  ╚════██║
#╚██████╗██║  ██║███████╗██║  ██║   ██║   ███████╗    ██║     ██║███████╗███████╗███████║
# ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝    ╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝
                                                                                        

for k in range(0,10):
	tempquestions = open("tempquestions","a")
	
	for i in range(0,8):
		random.choice(starters[k][0])(1,1)
		random.choice(starters[k][1])(1,1)
		random.choice(starters[k][2])(1,1)
		random.choice(starters[k][3])(1,1)
		random.choice(starters[k][4])(1,1)
		random.choice(starters[k][5])(1,1)
	filename = filenames[k]
	title = titles[k]
	
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
#	os.remove(filename + ".vrb")
	os.remove(filename + ".toc")