#starters.py

def writcalc(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Calculate:"
		linebreak = 0.2

		from fouroperators.addition import fulladdition
		from fouroperators.subtraction import fullsubtraction
		from fouroperators.multiplication import threebyonemultiplication,fourbyonemultiplication,twobytwomultiplication,twobythreemultiplication,threebythreemultiplication
		from fouroperators.division import singledigitdivision,twodigitdivision,twodigitdivisioneasy

		mults = [threebyonemultiplication,fourbyonemultiplication,twobytwomultiplication,twobythreemultiplication,threebythreemultiplication]
		divs = [singledigitdivision,twodigitdivision,twodigitdivisioneasy]

		fulladdition(1,0)
		fullsubtraction(1,0)
		random.choice(mults)(1,0)
		random.choice(divs)(1,0)

#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)


def placevalue(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Calculate:"
		linebreak = 0.15

		from fouroperators.ten import multten,multhundred,multthousand,divten,divhundred,divthousand

		qs = [multten,multhundred,multthousand,divten,divhundred,divthousand]
		random.shuffle(qs)
		for i in range(0,6):
			qs[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)


def fracops1(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Calculate:"
		linebreak = 0.15
		from fdp.fractionoperations import fractionsadd,fractionssubtract,fractionsmultiply,fractionsdivide,fractionsdivideinteger,fractionsmultiplyinteger
		mults = [fractionsmultiply,fractionsmultiplyinteger]
		divs = [fractionsdivide,fractionsdivideinteger]
		qs = [fractionsadd,fractionssubtract,random.choice(mults),random.choice(divs)]
		random.shuffle(qs)
		for i in range(0,4):
			qs[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)

def fracops2(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Calculate:"
		linebreak = 0.15
		from fdp.fractionoperations import mixednumbersadd,mixednumberssubtract,mixednumbersmultiply,mixednumbersdivide
		qs = [mixednumbersadd,mixednumberssubtract,mixednumbersmultiply,mixednumbersdivide]
		random.shuffle(qs)
		for i in range(0,4):
			qs[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)



def negstarter(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Calculate:"
		linebreak = 0.15

		from fouroperators.negatives import negadd,negsubtract,negdivide,negmultiply

		qs = [negadd,negsubtract,negdivide,negmultiply]
		random.shuffle(qs)
		for i in range(0,4):
			qs[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)

def lineq1(n,explanationn):	#REPEATED LATER?
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Calculate:"
		linebreak = 0.15

		from equations.linear import twostep1,twostep4,twostep6,threestep1


		qs = [twostep1,twostep4,twostep6,threestep1]
#		random.shuffle(qs)
		for i in range(0,4):
			qs[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)

def hcalc(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Use a calculator to work out (to 2dp):"
		linebreak = 0.15

		from gym.gym import calc1,calc2,calc3,calc4,calc5,calc6,calc7,calc8,calc9,calc10,calc11,calc12,calc13
		calca = [calc3,calc4]
		calcb = [calc5,calc10]
		calcc = [calc6,calc8]
		calcd = [calc7,calc9]
		calce = [calc1,calc2]
		calcf = [calc12,calc2]
		qs = [random.choice(calca),random.choice(calcb),random.choice(calcc),random.choice(calcd),random.choice(calce), random.choice(calcf)]
		random.shuffle(qs)
		for i in range(0,4):
			qs[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)


def fcalc(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Use a calculator to work out (to 2dp):"
		linebreak = 0.2

		from gym.gym import calc1,calc2,calc3,calc4,calc5,calc6,calc7,calc8,calc9,calc10,calc11,calc12,calc13
		calca = [calc3,calc4]
		calcb = [calc5,calc10]
		calcc = [calc6,calc8]
		calcd = [calc7,calc9]
		calce = [calc1,calc2]
		calcf = [calc12,calc2]
		qs = [calc1,random.choice(calcf),calc11,random.choice(calca)]
		random.shuffle(qs)
		for i in range(0,4):
			qs[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)



def sfconversions(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = ""
		linebreak = 0.3

		from indices.standardform import sfconvertpos1,sfconvertpos2,sfconvertneg1,sfconvertneg2, sfconvert3pos,sfconvert3neg 
		combo1 = [sfconvertpos1,sfconvertneg2]
		combo2 = [sfconvertneg1,sfconvertpos2]
		combos = [combo1,combo2]
		combo = random.choice(combos)
		qs = [combo[0],combo[1],sfconvert3pos,sfconvert3neg]
#		random.shuffle(qs)
		for i in range(0,4):
			qs[i](1,1)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)

def sfcalcs(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Calculate:"
		linebreak = 0.3

		from indices.standardform import sfmultiply,sfdivide,sfadd,sfsubtract
		qs = [sfmultiply,sfdivide,sfadd,sfsubtract]
		random.shuffle(qs)
		for i in range(0,4):
			qs[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)




def ncperc(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Non-calc:"
		linebreak = 0.1


		from fdp.percentages import percofamount5gym,percincdec5,percreverse52,percreverse53,percreverse54,numberaspercnc,percchangencstarter
		revs = [percreverse52,percreverse53,percreverse54]
		qs = [percofamount5gym,percincdec5,random.choice(revs),numberaspercnc,percchangencstarter]
#		random.shuffle(qs)
		for i in range(0,5):
			qs[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)

def calcperc(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = ""
		linebreak = 0.15


		from fdp.percentages import percofamount,percincdec,percreverse,percchange
		qs = [percofamount,percincdec,percreverse,percchange]
#		random.shuffle(qs)
		for i in range(0,4):
			qs[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)


def rounding(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = ""
		linebreak = 0.15

		from fdp.rounding import round1sf2, round2sf2, round3sf2, round10, round100, round1000, round1sf1, round2sf1, round3sf1, round1dp, round2dp, round0dp
		r1 = [round1sf2, round2sf2, round3sf2]
		r2 = [round10, round100, round1000]
		r3 = [round1sf1, round2sf1, round3sf1]
		r4 = [round0dp]
		r5 = [round1dp, round2dp]
		qs = [random.choice(r2),random.choice(r4),random.choice(r5),random.choice(r3),random.choice(r1)]
#		random.shuffle(qs)
		for i in range(0,5):
			qs[i](1,1)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)



def rounding10(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = ""
		linebreak = 0.15

		from fdp.rounding import round1sf2, round2sf2, round3sf2, round10, round100, round1000, round1sf1, round2sf1, round3sf1, round1dp, round2dp, round0dp
		qs = [round10, round100, round1000]
#		random.shuffle(qs)
		for i in range(0,3):
			qs[i](1,1)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)




def linearnthterm(n,explanationn):
#DON'T USE - REPLACED LATER, KEEPING JUST IN CASE
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = ""
		linebreak = 0.15

		from algebra.sequences import seqnext,genseq,nthterm
		qs = [seqnext,genseq,nthterm]
#		random.shuffle(qs)
		for i in range(0,3):
			qs[i](1,1)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)



def indexlaws(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = ""
		linebreak = 0.15

		from indices.laws import multindpos,divindpos,indindpos,multindneg,divindneg,indindneg
		qs = [multindpos,divindpos,indindpos,multindneg,divindneg,indindneg]
		random.shuffle(qs)
		for i in range(0,len(qs)):
			qs[i](1,1)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)



def reciprocals(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = ""
		linebreak = 0.15

		from fdp.fdp import reciprocal1,reciprocal2,reciprocaldec
		qs = [reciprocal1,reciprocal2,reciprocaldec]
#		random.shuffle(qs)
		for i in range(0,len(qs)):
			qs[i](1,1)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)


def singlebracketexpansion(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Expand:"
		linebreak = 0.15

		from algebra.manipulation import singlebracketexpansion1,singlebracketexpansion2,singlebracketexpansion3, singlebracketexpansion4,singlebracketexpansion5
		qs = [singlebracketexpansion1,singlebracketexpansion2,singlebracketexpansion3, singlebracketexpansion4,singlebracketexpansion5]
#		random.shuffle(qs)
		for i in range(0,len(qs)):
			qs[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)

def sinlgebracketfactorisation(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Factorise fully:"
		linebreak = 0.15

		from algebra.manipulation import singlebracketfactorise1,singlebracketfactorise2,singlebracketfactorise3, singlebracketfactorise4,singlebracketfactorise5
		qs = [singlebracketfactorise1,singlebracketfactorise2,singlebracketfactorise3, singlebracketfactorise4,singlebracketfactorise5]
#		random.shuffle(qs)
		for i in range(0,len(qs)):
			qs[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)


def solveequations1(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Solve:"
		linebreak = 0.15

		from equations.linear import onestepadd,onestepsubtract,onestepmultiply,onestepdivide,twostep1,twostep4,twostep6,threestep1
		ones = [onestepadd,onestepsubtract,onestepmultiply,onestepdivide]
		qs = [random.choice(ones),twostep1,twostep4,twostep6,threestep1]
#		random.shuffle(qs)
		for i in range(0,len(qs)):
			qs[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)

def quadexpansion1(n,explanationn):
#NEED TO FIX AQUADCOURSE 9 X 2
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Expand and simplify:"
		linebreak = 0.15
		from equations.quadratics import quadcourse1,quadcourse4,quadcourse91,quadcourse92
		qs = [quadcourse1,quadcourse4,quadcourse91,quadcourse92]
		random.shuffle(qs)
		for i in range(0,len(qs)):
			qs[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)


def simeqs(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Solve:"
		linebreak = 0.15
		from equations.simultaneous import simeqlin1,simeqlin2,simeqlin3
		qs = [simeqlin1,simeqlin2,simeqlin3]
#		random.shuffle(qs)
		for i in range(0,len(qs)):
			qs[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)


def quadfactorise1(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Factorise:"
		linebreak = 0.15
		from equations.quadratics import quadcourse3,quadcourse6,quadcourse11,quadcourse12
		qs = [quadcourse3,quadcourse6,quadcourse11,quadcourse12]
		random.shuffle(qs)
		for i in range(0,len(qs)):
			qs[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)


def quadfactorise2(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = ""
		linebreak = 0.15
		from equations.quadratics import factorisequadratics2pospos,factorisequadratics2posneg, factorisequadratics2negneg,solvequadratics2
		qs = [factorisequadratics2pospos,factorisequadratics2posneg, factorisequadratics2negneg,solvequadratics2]
		random.shuffle(qs)
		for i in range(0,len(qs)):
			qs[i](1,1)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)





def quadfactorisesolve1(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Factorise and solve :"
		linebreak = 0.15
		from equations.quadratics import quadcourse16pospos,quadcourse16negpos,quadcourse16posneg,quadcourse16negneg
		qs = [quadcourse16pospos,quadcourse16negpos,quadcourse16posneg,quadcourse16negneg]
		random.shuffle(qs)
		for i in range(0,len(qs)):
			qs[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)




def quadfactorisesolve2(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Factorise and solve :"
		linebreak = 0.15
		from equations.quadratics import solvequadratics2pospos,solvequadratics2negneg,solvequadratics2posneg
		qs = [solvequadratics2pospos,solvequadratics2negneg,solvequadratics2posneg]
		random.shuffle(qs)
		for i in range(0,len(qs)):
			qs[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)





def subs1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		expressions = []
		answers = []
		b = random.randrange(2,6)*(-1)**random.randrange(0,2)
		c = b * random.randrange(2,6) * (-1)**random.randrange(0,2)
		aas = [2,3,4,5,6,7,8,9,-2,-3,-4,-5,-6,-7,-8,-9]
		if b<10 and b>-10:
			aas.remove(b)
		if c<10 and c>-10:
			aas.remove(c)
		a = random.choice(aas)
		x = random.randrange(2,10)
		y = random.randrange(2,10)
		if random.randrange(0,2)==1:
			sign1 = " - "
			answera = str(x*a - y*b)
		else:
			sign1 = " + "
			answera = str(x*a + y*b)
		questiona = "$" + str(x) + "\\text{a}" + sign1 + str(y) + "\\text{b}$"
		questionb = "$\\dfrac{\\text{ac}}{\\text{b}}$"
		answerb = str(int(a*c/b))
		questionc = "$\\text{ab}^{2}$"
		answerc = str(a * b**2)
		questiond = "$(\\text{ab})^{2}$"
		answerd = str((a*b)**2)
		nl = "\\\\[0.15cm]"
		question = "a = " + str(a) + "\\hspace{1cm}" + "b = " + str(b) + "\\hspace{1cm}" + "c = " + str(c) + nl + "Calculate:" + nl + "a) " + questiona + nl + "b) " + questionb + nl + "c) " + questionc + nl + "d) " + questiond
		answer = "a) " + answera + nl + "b) " + answerb + nl + "c) " + answerc + nl + "d) " + answerd
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def nthtermlinear(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = "\\\\[0.15cm]"
		m = random.randrange(1,7) * (-1)**random.randrange(1,3)
		if m>0:
			m2 = random.randrange(2,7) * (-1)**random.randrange(1,3)
		else:
			m2 = random.randrange(2,7)
		if m==1:
			c = random.randrange(1,7) * (-1)**random.randrange(1,3)
		else:
			c = random.randrange(0,7) * (-1)**random.randrange(1,3)
		if c<0:
			sign = " - "
		else:
			sign = " + "
		t1 = m * 1 + c
		t2 = m * 2 + c
		t3 = m * 3 + c
		t4 = m * 4 + c
		t5 = m * 5 + c
		if m==1:
			m = ""
		elif m==-1:
			m = "-"
		if c==0:
			expressiona = "\\mbox{" + str(m) + "n}"
		else:
			expressiona = "\\mbox{" + str(m) + "n" + sign + str(abs(c)) + "}"

		sequencea = "\\mbox{" + str(t1) + ", " + str(t2) + ", " + str(t3) + ", " + str(t4) + ", " + str(t5) + "}"	
		questiona = "a) Write down the first five terms of the sequence " + expressiona
		answera = "a) " + sequencea
		m = m2
		cs = list(range(2,7))
		cs.remove(abs(m))
		c = random.choice(cs) * (-1)**random.randrange(1,3)
		if c<0:
			sign = " - "
		else:
			sign = " + "
		t1 = m * 1 + c
		t2 = m * 2 + c
		t3 = m * 3 + c
		t4 = m * 4 + c
		t5 = m * 5 + c
		qc = random.randrange(6,11)*10
		t100 = m * qc + c
		if m==1:
			m = ""
		elif m==-1:
			m = "-"
		if c==0:
			expressionb = "\\mbox{" + str(m) + "n}"
		else:
			expressionb = "\\mbox{" + str(m) + "n" + sign + str(abs(c)) + "}"

		sequenceb = "\\mbox{" + str(t1) + ", " + str(t2) + ", " + str(t3) + ", " + str(t4) + ", " + str(t5) + "}"	
		questionb = "b) Find the nth term of " + sequenceb
		answerb = "b) " + expressionb
		questionc = "c) Write down the " + str(qc) + "th term of the sequence in part b"
		answerc = "c) " + str(t100)
		qd = random.randrange(25,50)
		t50 = m * qd + c
		qdcheck = [31,32,33,41,42,43]
		if qd in qdcheck:
			if qd==31 or qd==41:
				qd = str(qd) + "st"
			elif qd==32 or qd==42:
				qd = str(qd) + "nd"
			elif qd==33 or qd==43:
				qd = str(qd) + "rd"
		else:
			qd = str(qd) + "th"
		if random.randrange(0,2)==1:
			answerd = "d) Yes, " + qd + " term"
		else:
			t50 = t50 + random.randrange(1,abs(m))
			answerd = "d) No"
		questiond = "d) Is " + str(t50) + " a number in the sequence in part b?"
		question = questiona + nl + questionb + nl + questionc + nl + questiond
		answer = answera + nl + answerb + nl + answerc + nl + answerd
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def nthtermlineargym(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = "\\\\[0.15cm]"
		m = random.randrange(1,7) * (-1)**random.randrange(1,3)
		if m>0:
			m2 = random.randrange(2,7) * (-1)**random.randrange(1,3)
		else:
			m2 = random.randrange(2,7)
		if m==1:
			c = random.randrange(1,7) * (-1)**random.randrange(1,3)
		else:
			c = random.randrange(0,7) * (-1)**random.randrange(1,3)
		if c<0:
			sign = " - "
		else:
			sign = " + "
		t1 = m * 1 + c
		t2 = m * 2 + c
		t3 = m * 3 + c
		t4 = m * 4 + c
		t5 = m * 5 + c
		if m==1:
			m = ""
		elif m==-1:
			m = "-"
		if c==0:
			expressiona = "\\mbox{" + str(m) + "n}"
		else:
			expressiona = "\\mbox{" + str(m) + "n" + sign + str(abs(c)) + "}"

		sequencea = "\\mbox{" + str(t1) + ", " + str(t2) + ", " + str(t3) + ", " + str(t4) + ", " + str(t5) + "}"	
		questiona = "Write down the first five terms of the sequence " + expressiona
		answera = sequencea
		m = m2
		cs = list(range(2,7))
		cs.remove(abs(m))
		c = random.choice(cs) * (-1)**random.randrange(1,3)
		if c<0:
			sign = " - "
		else:
			sign = " + "
		t1 = m * 1 + c
		t2 = m * 2 + c
		t3 = m * 3 + c
		t4 = m * 4 + c
		t5 = m * 5 + c
		t6 = m * 6 + c
		t7 = m * 7 + c
		qc = random.randrange(6,11)*10
		t100 = m * qc + c
		if m==1:
			m = ""
		elif m==-1:
			m = "-"
		if c==0:
			expressionb = "\\mbox{" + str(m) + "n}"
		else:
			expressionb = "\\mbox{" + str(m) + "n" + sign + str(abs(c)) + "}"

		sequenceb = "\\mbox{" + str(t1) + ", " + str(t2) + ", " + str(t3) + ", " + str(t4) + ", " + str(t5) + "}"	
		questionb = "Find the nth term of the sequence in question 2"
		answerb = expressionb
		questionc = "Write down the " + str(qc) + "th term of the sequence in question 2"
		answerc = str(t100)
		qd = random.randrange(25,50)
		t50 = m * qd + c
		qdcheck = [31,32,33,41,42,43]
		if qd in qdcheck:
			if qd==31 or qd==41:
				qd = str(qd) + "st"
			elif qd==32 or qd==42:
				qd = str(qd) + "nd"
			elif qd==33 or qd==43:
				qd = str(qd) + "rd"
		else:
			qd = str(qd) + "th"
		if random.randrange(0,2)==1:
			answerd = "Yes, " + qd + " term"
		else:
			t50 = t50 + random.randrange(1,abs(m))
			answerd = "No"
		questiond = "Is " + str(t50) + " a number in the sequence in question 2?"
		question2 = "Write down the next two terms in the sequence " + sequenceb
		answer2 = str(t6) + " and " + str(t7)
#write question
		tempquestions.write(questiona)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answera)
		tempquestions.write("\n")
#write question
		tempquestions.write(question2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer2)
		tempquestions.write("\n")
#write question
		tempquestions.write(questionb)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answerb)
		tempquestions.write("\n")
#write question
		tempquestions.write(questionc)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answerc)
		tempquestions.write("\n")
#write question
		tempquestions.write(questiond)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answerd)

def nthtermquadratic(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = ""
		linebreak = 0.15

		from algebra.sequences import genseqquad1,genseqquad2,genseqquad3,genseqquad4,genseqquad5, nthtermquad1,nthtermquad2,nthtermquad3,nthtermquad4,nthtermquad5
		choices1 = [0,1,2]
		choices2 = [3,4]
		gens = [genseqquad1,genseqquad2,genseqquad3,genseqquad4,genseqquad5]
		seqs = [nthtermquad1,nthtermquad2,nthtermquad3,nthtermquad4,nthtermquad5]
		choice1 = random.choice(choices1)
		choices1.remove(choice1)
		choice2 = random.choice(choices2)
		choices2.remove(choice2)
		seqs = [seqs[choice1],seqs[choice2]]
		random.shuffle(seqs)
		random.shuffle(choices1)
		qs = [gens[choices1[0]],gens[choices2[0]],seqs[0],seqs[1]]
#		random.shuffle(qs)
		for i in range(0,4):
			qs[i](1,1)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)


def fibseq(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = "\\\\[0.15cm]"
		t1 = random.randrange(1,6)
		t2 = t1 + random.randrange(1,6)
		t3 = t1 + t2
		t4 = t2 + t3
		t5 = t3 + t4
		t6 = t4 + t5
		t7 = t5 + t6
		sequencea = "\\mbox{" + str(t1) + ", " + str(t2) + ", " + str(t3) + ", " + str(t4) + ", " + str(t5) + "}"	
		questiona = "a) The first five terms of a Fibonacci sequence are " + sequencea + ". Write down the next two terms in the sequence."
		answera = "a) " + str(t6) + ", " + str(t7)
		ts = list(range(1,6))
		ts.remove(t1)
		diffs = list(range(1,6))
		diffs.remove(t2-t1)
		t1 = random.choice(ts)
		t2 = t1 + random.choice(diffs)
		t3 = t1 + t2
		t4 = t2 + t3
		t5 = t3 + t4
		questionb = "b) In a different Fibonacci sequence the fourth term is " + str(t4) + " and the fifth term is " + str(t5) + ". Work out the first term in this sequence."
		answerb = "b) " + str(t1)
		question = questiona + nl + questionb
		answer = answera + nl + answerb
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def bidmas(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Calculate:"
		linebreak = 0.2
		from fouroperators.bidmas import bidmas1,bidmas2,bidmas3,bidmas4,bidmas5,bidmas6,bidmas7, bidmas8,bidmas9,bidmas10,bidmas11,bidmas12,bidmas13,bidmas14, bidmas15,bidmas16,bidmas17,bidmas18,bidmas19,bidmas20, bidmas21,bidmas22,bidmas23,bidmas24,bidmas25
		
		a = [bidmas1,bidmas2,bidmas3,bidmas4,bidmas8,bidmas10,bidmas12,bidmas20,bidmas22,bidmas24]
		bb = [bidmas5,bidmas6,bidmas7,bidmas9]
		b = [bidmas11,bidmas13,bidmas16,bidmas21,bidmas23,random.choice(bb)]
		c = [bidmas14,bidmas15,bidmas17,bidmas18,bidmas19,bidmas25]
		random.shuffle(a)
		random.shuffle(b)
		random.shuffle(c)
		for i in range(0,2):
			a[i](1,0)
		for i in range(0,2):
			b[i](1,0)
		for i in range(0,1):
			c[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)






def bidmasbracseasy(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Add brackets to make these correct:"
		linebreak = 0.2
		from fouroperators.bidmas import bidmasbracs1,bidmasbracs2,bidmasbracs3,bidmasbracs4,bidmasbracs5, bidmasbracs6,bidmasbracs7,bidmasbracs8,bidmasbracs9,bidmasbracs10, bidmasbracs11,bidmasbracs12,bidmasbracs13,bidmasbracs14,bidmasbracs15, bidmasbracs16,bidmasbracs17,bidmasbracs18,bidmasbracs19,bidmasbracs20, bidmasbracs21,bidmasbracs22,bidmasbracs23,bidmasbracs24,bidmasbracs25, bidmasbracs26,bidmasbracs27,bidmasbracs28,bidmasbracs29
		qs1 = [bidmasbracs8,bidmasbracs9,bidmasbracs10,bidmasbracs11,bidmasbracs12,bidmasbracs24,bidmasbracs25,bidmasbracs27]
		qs2 = [bidmasbracs13,bidmasbracs14,bidmasbracs15,bidmasbracs18]
		random.shuffle(qs1)
		random.shuffle(qs2)
		for i in range(0,4):
			qs1[i](1,0)
		for i in range(0,1):
			qs2[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)


def bidmasbracs(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Add brackets to make these correct:"
		linebreak = 0.2
		from fouroperators.bidmas import bidmasbracs1,bidmasbracs2,bidmasbracs3,bidmasbracs4,bidmasbracs5, bidmasbracs6,bidmasbracs7,bidmasbracs8,bidmasbracs9,bidmasbracs10, bidmasbracs11,bidmasbracs12,bidmasbracs13,bidmasbracs14,bidmasbracs15, bidmasbracs16,bidmasbracs17,bidmasbracs18,bidmasbracs19,bidmasbracs20, bidmasbracs21,bidmasbracs22,bidmasbracs23,bidmasbracs24,bidmasbracs25, bidmasbracs26,bidmasbracs27,bidmasbracs28,bidmasbracs29
		
		qs1 = [bidmasbracs8,bidmasbracs9,bidmasbracs10,bidmasbracs11,bidmasbracs12,bidmasbracs24,bidmasbracs25,bidmasbracs27]
		qs22 = [bidmasbracs1,bidmasbracs2,bidmasbracs3,bidmasbracs15,bidmasbracs18,bidmasbracs19, bidmasbracs20,bidmasbracs21,bidmasbracs22,bidmasbracs23,bidmasbracs26]
		qs222 = [bidmasbracs13,bidmasbracs14]
		qs3 = [bidmasbracs4,bidmasbracs5,bidmasbracs6,bidmasbracs7,bidmasbracs16,bidmasbracs17,bidmasbracs28,bidmasbracs29]
		random.shuffle(qs1)
		qs2 = qs22
		qs2.append(random.choice(qs222))
		random.shuffle(qs2)
		random.shuffle(qs3)
		
		for i in range(0,2):
			qs1[i](1,0)
		for i in range(0,2):
			qs2[i](1,0)
		for i in range(0,1):
			qs3[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)


def negsfillblanks(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Copy and complete:"
		linebreak = 0.2
		from torture.torture import negativeadd2,negativesubtract2,negativesubtract3,negativemultiply2,negativedivide2,negativedivide3
		subs = [negativesubtract2,negativesubtract3]
		divs = [negativedivide2,negativedivide3]
		qs = [negativeadd2,negativemultiply2,random.choice(subs),random.choice(divs)]
		random.shuffle(qs)
		for i in range(0,len(qs)):
			qs[i](1)
			
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)

def estimation(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Estimate:"
		linebreak = 0.2
		from fdp.estimation import estimation1,estimation2,estimation3,estimation4
		qs = [estimation3,estimation2,estimation4,estimation1]
		for i in range(0,len(qs)):
			qs[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)




def decimalcalcs(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Calculate:"
		linebreak = 0.2
		from fouroperators.addition import decimaladdition
		from fouroperators.subtraction import decimalsubtraction
		from fouroperators.multiplication import decimalmultiplication0,decimalmultiplication1,decimalmultiplication2
		from fouroperators.division import decimaldivision1,decimaldivision2,divisionbydecimal,divisionbydecimal2
		mults = [decimalmultiplication0,decimalmultiplication1,decimalmultiplication2]
		divs = [decimaldivision1,decimaldivision2,divisionbydecimal,divisionbydecimal2]
		qs = [decimaladdition,decimalsubtraction,random.choice(mults),random.choice(divs)]
		for i in range(0,len(qs)):
			qs[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)







def surdssimplify(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Simplify:"
		linebreak = 0.2
		from indices.surds import simplifysurd1,simplifysurd2,simplifysurdmult1,simplifysurdmult2, simplifysurddiv1,simplifysurdadd,simplifysurdsubtract,simplifysurddiv2,surdquadratic1, surdquadratic1squared,surdquadratic2,ratden1,ratden2,ratdenDOTS,ratden3,ratdenDOTS2
		q1 = [simplifysurd1,simplifysurd2]
		q2 = [simplifysurdmult1,simplifysurdmult2]
		q3 = [simplifysurddiv1,simplifysurddiv2]
		q4 = [simplifysurdadd]
		q5 = [simplifysurdsubtract]
		qs = [random.choice(q1),random.choice(q4),random.choice(q5),random.choice(q2),random.choice(q3)]
		for i in range(0,len(qs)):
			qs[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)

def surdsexpandsimplify(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Expand and simplify:"
		linebreak = 0.2
		from indices.surds import simplifysurd1,simplifysurd2,simplifysurdmult1,simplifysurdmult2, simplifysurddiv1,simplifysurdadd,simplifysurdsubtract,simplifysurddiv2,surdquadratic1, surdquadratic1squared,surdquadratic2,ratden1,ratden2,ratdenDOTS,ratden3,ratdenDOTS2
		qs = [surdquadratic1, surdquadratic1squared,surdquadratic2]
		for i in range(0,len(qs)):
			qs[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)

def surdsratden1(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Rationalise the denominator:"
		linebreak = 0.2
		from indices.surds import simplifysurd1,simplifysurd2,simplifysurdmult1,simplifysurdmult2, simplifysurddiv1,simplifysurdadd,simplifysurdsubtract,simplifysurddiv2,surdquadratic1, surdquadratic1squared,surdquadratic2,ratden1,ratden2,ratdenDOTS,ratden3,ratdenDOTS2
		qs = [ratden1,ratden2,ratden3]
		for i in range(0,len(qs)):
			qs[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)

def surdsratden2(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Rationalise the denominator:"
		linebreak = 0.2
		from indices.surds import simplifysurd1,simplifysurd2,simplifysurdmult1,simplifysurdmult2, simplifysurddiv1,simplifysurdadd,simplifysurdsubtract,simplifysurddiv2,surdquadratic1, surdquadratic1squared,surdquadratic2,ratden1,ratden2,ratdenDOTS,ratden3,ratdenDOTS2
		q1 = [ratden1,ratden2]
		dots = [ratdenDOTS,ratdenDOTS2]
		qs = [random.choice(q1),ratden3,random.choice(dots)]
		for i in range(0,len(qs)):
			qs[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)



def indicesnegfrac(n,explanationn):
#COLUMNS!
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Evaluate:"
		linebreak = 0.2
		from indices.fracneg import fracindices1,fracindices2,negindices,negfrac1,negfrac2,  fraction1pos,fraction1neg,fraction2pos,fraction2neg,zero
		q1 = [negindices,zero]
		if random.randrange(0,2)==1:
			q2 = [fracindices2]
			q3 = [negfrac1]
		else:
			q2 = [fracindices1]
			q3 = [negfrac2]
		if random.randrange(0,2)==1:
			q4 = [fraction1neg]
			q5 = [fraction2pos]
		else:
			q4 = [fraction1pos]
			q5 = [fraction2neg]
		qs = [random.choice(q1),random.choice(q2),random.choice(q3),random.choice(q4),random.choice(q5)]
		for i in range(0,len(qs)):
			qs[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["\\begin{columns}\\column{0.49\\textwidth}a) ","b) ","c) ","\\column{0.49\\textwidth}d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		question = question + "\\end{columns}"
		answer = answer + "\\end{columns}"
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)


def indiceswriteaspower(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Write:"
		linebreak = 0.2
		from indices.fracneg import writeaspower1,writeaspower2,writeaspower3,writeaspower4, writeaspower5,writeaspower6,writeaspower7,writeaspower8, writeaspowermult,writeaspowerdiv

		if random.randrange(0,2)==1:
			q1 = writeaspower1
			q2 = writeaspower4
		else:
			q1 = writeaspower2
			q2 = writeaspower3
		if random.randrange(0,2)==1:
			q3 = writeaspower5
			q4 = writeaspower8
		else:
			q3 = writeaspower6
			q4 = writeaspower7
		q5 = [writeaspowermult,writeaspowerdiv]
		qs = [q1,q2,q3,q4]
		random.shuffle(qs)
		for i in range(0,3):
			qs[i](1,0)
		random.choice(q5)(1,1)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)


def shapenamesstarter(n,explanationn):
#COLUMNS!
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Write down the names of these shapes:"
		linebreak = 0.2
		from shape.names import quadrilateralsstarter,polygonsstarter,trianglesstarter,threedstarter
		qs = [quadrilateralsstarter,polygonsstarter,trianglesstarter,threedstarter]
		random.shuffle(qs)
		for i in range(0,4):
			qs[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["\\begin{columns}\\column{0.49\\textwidth}a) ","b) ","\\column{0.49\\textwidth}c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		question = question + "\\end{columns}"
		answer = answer + "\\end{columns}"
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)




def timecalcs1(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = ""
		linebreak = 0.2
		from sdt.time import timeadd2451,timeadd2452,timesubtract2451,timesubtract2452,timeadd1251, timeadd1252,timesubtract1251,timesubtract1252,timediff,timediffdecimal
		combos = [[timeadd1251,timesubtract2452],[timeadd2451,timesubtract1252],[timeadd1252,timesubtract2451],[timeadd2452,timesubtract1251]]
		choice = random.randrange(0,4)
		combos[choice][0](1,1)
		combos[choice][1](1,1)
		timediff(1,1)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)



def timecalcs2(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = ""
		linebreak = 0.2
		from sdt.time import timeadd2451,timeadd2452,timesubtract2451,timesubtract2452,timeadd1251, timeadd1252,timesubtract1251,timesubtract1252,timediff,timediffdecimal
		combos = [[timeadd1251,timesubtract2452],[timeadd2451,timesubtract1252],[timeadd1252,timesubtract2451],[timeadd2452,timesubtract1251]]
		choice = random.randrange(0,4)
		combos[choice][0](1,1)
		combos[choice][1](1,1)
		diffs = [timediff,timediffdecimal]
		random.choice(diffs)(1,1)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)



def rearrangeeasy(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Make x the subject of:"
		linebreak = 0.2
		from algebra.manipulation import rearrangeonestepadd,rearrangeonestepsubtract1,rearrangeonestepsubtract2,rearrangeonestepmultiply, rearrangeonestepdivide1,rearrangeonestepdivide2,rearrangeonestepsquare,rearrangeonestepsquareroot
		from algebra.manipulation import rearrangetwostep1,rearrangetwostep2,rearrangetwostep3, rearrangetwostep4,rearrangetwostep5,rearrangetwostep6, rearrangetwostep7,rearrangetwostep8,rearrangetwostep9, rearrangetwostep10,rearrangetwostep11,rearrangetwostep12, rearrangetwostep13,rearrangetwostep14,rearrangetwostep15, rearrangetwostep16
		from algebra.manipulation import rearrangemulti
		subs = [rearrangeonestepsubtract1,rearrangeonestepsubtract2]
		divs = [rearrangeonestepdivide1,rearrangeonestepdivide2]
		squares = [rearrangeonestepsquare,rearrangeonestepsquareroot]
		ones = [rearrangeonestepadd,random.choice(subs),rearrangeonestepmultiply, random.choice(divs),random.choice(squares)]
		random.shuffle(ones)
		for i in range(0,3):
			ones[i](1,0)
		twos1 = [rearrangetwostep1,rearrangetwostep2]
		twos2 = [rearrangetwostep3,rearrangetwostep4]
		twos3 = [rearrangetwostep5,rearrangetwostep6]
		twos4 = [rearrangetwostep7,rearrangetwostep8]
		twos5 = [rearrangetwostep9,rearrangetwostep10]
		twos6 = [rearrangetwostep11,rearrangetwostep12]
		twos7 = [rearrangetwostep13,rearrangetwostep14]
		twos = [random.choice(twos1),random.choice(twos2),random.choice(twos3),random.choice(twos4), random.choice(twos5),random.choice(twos6),random.choice(twos7),rearrangetwostep15, rearrangetwostep16]
		random.shuffle(twos)
		for i in range(0,2):
			twos[i](1,0)

#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)




def rearrangemedium(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Make x the subject of:"
		linebreak = 0.2
		from algebra.manipulation import rearrangeonestepadd,rearrangeonestepsubtract1,rearrangeonestepsubtract2,rearrangeonestepmultiply, rearrangeonestepdivide1,rearrangeonestepdivide2,rearrangeonestepsquare,rearrangeonestepsquareroot
		from algebra.manipulation import rearrangetwostep1,rearrangetwostep2,rearrangetwostep3, rearrangetwostep4,rearrangetwostep5,rearrangetwostep6, rearrangetwostep7,rearrangetwostep8,rearrangetwostep9, rearrangetwostep10,rearrangetwostep11,rearrangetwostep12, rearrangetwostep13,rearrangetwostep14,rearrangetwostep15, rearrangetwostep16
		from algebra.manipulation import rearrangemulti
		subs = [rearrangeonestepsubtract1,rearrangeonestepsubtract2]
		divs = [rearrangeonestepdivide1,rearrangeonestepdivide2]
		squares = [rearrangeonestepsquare,rearrangeonestepsquareroot]
		ones = [rearrangeonestepadd,random.choice(subs),rearrangeonestepmultiply, random.choice(divs),random.choice(squares)]
		random.shuffle(ones)
		for i in range(0,1):
			ones[i](1,0)
		twos1 = [rearrangetwostep1,rearrangetwostep2]
		twos2 = [rearrangetwostep3,rearrangetwostep4]
		twos3 = [rearrangetwostep5,rearrangetwostep6]
		twos4 = [rearrangetwostep7,rearrangetwostep8]
		twos5 = [rearrangetwostep9,rearrangetwostep10]
		twos6 = [rearrangetwostep11,rearrangetwostep12]
		twos7 = [rearrangetwostep13,rearrangetwostep14]
		twos = [random.choice(twos1),random.choice(twos2),random.choice(twos3),random.choice(twos4), random.choice(twos5),random.choice(twos6),random.choice(twos7),rearrangetwostep15, rearrangetwostep16]
		random.shuffle(twos)
		for i in range(0,2):
			twos[i](1,0)
		rearrangemulti(1,0)

#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)




def metricconversionsstarter1(n,explanationn):	#UNTESTED
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Convert:"
		linebreak = 0.2
		from measures.metricconversions import mcdistance1,mcdistance2,mcmass1,mcmass2,mccapacity1,mccapacity2
		qs = [mcdistance1,mcdistance2,mcmass1,mcmass2,mccapacity1,mccapacity2]
		for i in range(0,6):
			qs[i](1,0)

#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)


def simplifyexpressions(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Simplify:"
		linebreak = 0.2

		from algebra.manipulation import collect1,collect1pos,collect2,collect2pos
		qs = [collect1pos,collect2pos,collect1,collect2]
		for i in range(0,4):
			qs[i](1,0)

#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)


def equationofalinestarter(n,explanationn):	#MODIFIED QUESTION LETTERS
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Find the equation of the line:"
		linebreak = 0.05
		from graphs.linear import equationofline2,equationofline3,equationofline4,equationoflineperp,equationoflinepara
		qs1 = [equationoflineperp,equationoflinepara]
		qs = [equationofline2,equationofline4,equationofline3,random.choice(qs1)]
		for i in range(0,4):
			qs[i](1,0)

#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		qprefixes = ["a) that passes through ","b) that passes ","c) that passes through ","d) that is ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + qprefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)





def ratiostarter(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = ""
		linebreak = 0.2

		from fdp.ratio import ratiosimplify,ratioshare1,ratioshare2,ratioreverse1,ratioreverse2,ratioreverse3
		revs = [ratioreverse1,ratioreverse2,ratioreverse3]
		qs = [ratiosimplify,ratioshare1,ratioshare2,random.choice(revs)]
		for i in range(0,4):
			qs[i](1,1)

#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)


def proportionfoundation(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = ""
		linebreak = 0.2
		from algebra.proportion import direct,inverse
		qs = [direct,inverse]
		for i in range(0,2):
			qs[i](1,1)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)


def proportionfoundationtable(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = ""
		linebreak = 0.2
		from algebra.proportion import directtable,inversetable
		qs = [directtable,inversetable]
		for i in range(0,2):
			qs[i](1,1)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)



def proportionhigher(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = ""
		linebreak = 0.2
		from algebra.proportion import direct,directsquare,directsquareroot,inverse,inversesquare,inversesquareroot
		ds = [direct,directsquare,directsquareroot]
		iis = [inverse,inversesquare,inversesquareroot]
		qs = [random.choice(ds),random.choice(iis)]
		for i in range(0,2):
			qs[i](1,1)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)




def proportionhighertable(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = ""
		linebreak = 0.2
		from algebra.proportion import directtable,directsquaretable,directsquareroottable,inversetable,inversesquaretable,inversesquareroottable
		ds = [directtable,directsquaretable,directsquareroottable]
		iis = [inversetable,inversesquaretable,inversesquareroottable]
		qs = [random.choice(ds),random.choice(iis)]
		for i in range(0,2):
			qs[i](1,1)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)


def recdec1(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = ""
		linebreak = 0.2
		from fdp.fdp import fractorec,recurringdec1,recurringdec2,recurringdec3
		qs = [fractorec,recurringdec1,recurringdec2,recurringdec3]
		for i in range(0,4):
			qs[i](1,1)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)


def errorintervalsrounding(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = ""
		linebreak = 0.2
		from fdp.rounding import errorintervals10,errorintervalsdp,errorintervalssf,errorintervalstruncdp,errorintervalstruncsf
		qs = [errorintervals10,errorintervalsdp,errorintervalssf]
		for i in range(0,3):
			qs[i](1,1)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)


def errorintervalstruncating(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = ""
		linebreak = 0.2
		from fdp.rounding import errorintervals10,errorintervalsdp,errorintervalssf,errorintervalstruncdp,errorintervalstruncsf
		qs = [errorintervalstruncdp,errorintervalstruncsf]
		for i in range(0,2):
			qs[i](1,1)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)




def nthtermhighermix(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = "Find the nth term of:"
		linebreak = 0.2
		from algebra.sequences import nthtermquad1,nthtermquad2,nthtermquad3,nthtermquad4,nthtermquad5, geoseqnthterm,geosurdseqnthterm,nthtermpos,nthtermneg
		quadseq = [nthtermquad1,nthtermquad2,nthtermquad3,nthtermquad4,nthtermquad5]
		lins = [nthtermpos,nthtermneg]
		geos = [geoseqnthterm,geosurdseqnthterm]
		qs = [random.choice(quadseq), random.choice(lins),random.choice(geos)]
		random.shuffle(qs)
		for i in range(0,3):
			qs[i](1,0)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)



def wordsfigures(n,explanationn):
	import random, linecache, os,time,shutil
	for x in range(0, n):
		with open("tempquestions", 'r') as file :
			originaltq = file.read()
		os.remove('tempquestions')
#edit from here
		explanation = ""
		linebreak = 0.2
		from fouroperators.figwords import figwords,wordfigs
		figwords(1,1)
		wordfigs(1,1)
#stop editing
		nl = "\\\\[" + str(linebreak) + "cm]"
		lines = sum(1 for line in open('tempquestions')) - 1
		if explanation=="":
			question = ""
		else:
			question = explanation + nl
		answer = ""
		prefixes = ["a) ","b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) "]
		with open("tempquestions", 'r') as file :
			newtq = file.read()
		for i in range(0,int(lines/2)):
			question = question + prefixes[i] + newtq.splitlines()[2*i+1]
			answer = answer + prefixes[i] + newtq.splitlines()[2*i+2]
			if i<int(lines/2)-1:
				question = question + nl
				answer = answer + nl
		os.remove('tempquestions')
		with open('tempquestions', 'w') as file:
			file.write(originaltq)
		with open('tempquestions', 'a') as file:
			file.write("\n")
			file.write(question)
			file.write("\n")
			file.write(answer)




def skillscheckreversefourops(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		choice = random.randrange(0,4)
		if choice==1:
			b = random.randrange(5,21)*10
			a = random.randrange(floor(0.3*b),floor(0.7*b))
			question = "? + " + str(a) + " = " + str(b)
			answer = str(b - a)
		elif choice==2:
			b = random.randrange(5,21)*10
			a = random.randrange(floor(0.3*b),floor(0.7*b))
			question = "? - " + str(b - a) + " = " + str(a)
			answer = str(b)
		elif choice==3:
			a = random.randrange(2,13) * 10**random.randrange(0,2)
			b = random.randrange(2,13)
			c = a * b
			question = "? $\\times$ " + str(b) + " = " + str(c)
			answer = str(a)
		else:
			a = random.randrange(2,16)
			b = random.randrange(2,13)
			c = a * b
			question = "? $\\div$ " + str(b) + " = " + str(a)
			answer = str(c)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def skillscheckdoublehalve(n,explanationn):
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		choice = random.randrange(0,2)
		a = random.randrange(20,100)
		b = a * 2
		if choice==0:
			question = "Double " + str(a)
			answer = str(b)
		else:
			question = "Halve " + str(b)
			answer = str(a)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)