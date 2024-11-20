#!/usr/bin/env python3
#recurringdecimals.py
import random
from math import floor,gcd
from utilities.rounding import rounddp

def recdec1(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation1 = "Convert "
			explanation2 = " to a fraction"
		else:
			explanation1 = ""
			explanation2 = ""
		recdec = random.randrange(1,9)
		pos = random.randrange(1,3)
		if pos==2:
			extras = [0,1,2,3,4,5,6,7,8,9]
			extras.remove(recdec)
			extra = random.choice(extras)
			num = 9*extra + recdec
			den = 90
		else:
			extra = ""
			num = recdec
			den = 9
		if random.randrange(0,2)==1:
			inte = 0
		else:
			inte = random.randrange(1,10)
		number = str(inte) + "." + str(extra) + "\\.{" + str(recdec) + "}"
		hcf = gcd(num,den)
		num = int(num/hcf)
		den = int(den/hcf)
		if inte==0:
			inte = ""
		frac = "$" + str(inte) + "\\dfrac{" + str(num) + "}{" + str(den) + "}$"
		question = explanation1 + number + explanation2
		answer = frac
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)



def recdec2(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation1 = "Convert "
			explanation2 = " to a fraction"
		else:
			explanation1 = ""
			explanation2 = ""
		recdec1 = random.randrange(0,10)
		recs = [0,1,2,3,4,5,6,7,8,9]
		recs.remove(recdec1)
		recdec2 = random.choice(recs)
		recdec = recdec1*10 + recdec2
		if random.randrange(0,2)==1:
			inte = 0
		else:
			inte = random.randrange(1,10)
		pos = random.randrange(1,3)
		if pos==2:
			extras = [0,1,2,3,4,5,6,7,8,9]
			extras.remove(recdec2)
			extra = random.choice(extras)
			num = 99*extra + 10*recdec1 + recdec2
			den = 990
		else:
			extra = ""
			num = recdec
			den = 99
		number = str(inte) + "." + str(extra) + "\\.{" + str(recdec1) + "}\\.{" + str(recdec2) + "}"
		hcf = gcd(num,den)
		num = int(num/hcf)
		den = int(den/hcf)
		if inte==0:
			inte = ""
		frac = "$" + str(inte) + "\\dfrac{" + str(num) + "}{" + str(den) + "}$"
		question = explanation1 + number + explanation2
		answer = frac
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)




def recdec3(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation1 = "Convert "
			explanation2 = " to a fraction"
		else:
			explanation1 = ""
			explanation2 = ""
		recdec1 = random.randrange(0,10)
		recs = [0,1,2,3,4,5,6,7,8,9]
		recdec2 = random.randrange(0,10)
		if recdec1==recdec2:
			recs.remove(recdec2)
		recdec3 = random.choice(recs)
		recdec = recdec1*100 + recdec2*10 + recdec3
		if random.randrange(0,2)==1:
			inte = 0
		else:
			inte = random.randrange(1,10)
		pos = 1 #CHANGE IF NEEDED
		if pos==2:
			extras = [0,1,2,3,4,5,6,7,8,9]
			if recdec1==recdec3:
				extras.remove(recdec2)
			extras.remove(recdec3)
			extra = random.choice(extras)
			num = 999*extra + 100*recdec1 + 10*recdec2 + recdec3
			den = 9990
		else:
			extra = ""
			num = recdec
			den = 999
		number = str(inte) + "." + str(extra) + "\\.{" + str(recdec1) + "}" + str(recdec2) + "\\.{" + str(recdec3) + "}"
		hcf = gcd(num,den)
		num = int(num/hcf)
		den = int(den/hcf)
		if inte==0:
			inte = ""
		frac = "$" + str(inte) + "\\dfrac{" + str(num) + "}{" + str(den) + "}$"
		question = explanation1 + number + explanation2
		answer = frac
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)




def recdec3hard(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation1 = "Convert "
			explanation2 = " to a fraction"
		else:
			explanation1 = ""
			explanation2 = ""
		recdec1 = random.randrange(0,10)
		recs = [0,1,2,3,4,5,6,7,8,9]
		recdec2 = random.randrange(0,10)
		if recdec1==recdec2:
			recs.remove(recdec2)
		recdec3 = random.choice(recs)
		recdec = recdec1*100 + recdec2*10 + recdec3
		if random.randrange(0,2)==1:
			inte = 0
		else:
			inte = random.randrange(1,10)
		pos = 2 #CHANGE IF NEEDED - CHANGED!
		if pos==2:
			extras = [0,1,2,3,4,5,6,7,8,9]
			if recdec1==recdec3:
				extras.remove(recdec2)
			extras.remove(recdec3)
			extra = random.choice(extras)
			num = 999*extra + 100*recdec1 + 10*recdec2 + recdec3
			den = 9990
		else:
			extra = ""
			num = recdec
			den = 999
		number = str(inte) + "." + str(extra) + "\\.{" + str(recdec1) + "}" + str(recdec2) + "\\.{" + str(recdec3) + "}"
		hcf = gcd(num,den)
		num = int(num/hcf)
		den = int(den/hcf)
		if inte==0:
			inte = ""
		frac = "$" + str(inte) + "\\dfrac{" + str(num) + "}{" + str(den) + "}$"
		question = explanation1 + number + explanation2
		answer = frac
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)


def fractorecdec(n,explanationn):
	returnlist = []
	for x in range(0, n):
##################################
		if explanationn==1:
			explanation1 = "Convert "
			explanation2 = " to a recurring decimal"
		else:
			explanation1 = ""
			explanation2 = ""
		dens = [3,6,7,9,11]
		den = random.choice(dens)
		if den==6:
			nums = [1,5]
			num = random.choice(nums)
		elif den==9:
			nums = [1,2,4,5,7,8]
			num = random.choice(nums)
		else:
			num = random.randrange(1,den)
		question = "$\\dfrac{" + str(num) + "}{" + str(den) + "}$"
		aden = 9
		if den==6:
			if num==1:
				answer = "0.1\\.{6}"
			else:
				answer = "0.8\\.{3}"
		elif num==1 and den==11:
			answer = "0.\\.{0}\\.{9}"
		else:
			while aden%den!=0:
				aden = aden * 10 + 9
			scaler = int(aden/den)
			answer = num * scaler
			answerl = list(str(answer))
			answer1 = answerl[0]
			if len(answerl)==1:
				answer = "0.\\.{" + str(answer1) + "}"
			else:
				answer = "0.\\.{" + str(answer1) + "}"
				for i in range(1,len(answerl)-1):
					answer = answer + answerl[i]
				answer = answer + "\\.{" + str(answerl[len(answerl)-1]) + "}"
		question = explanation1 + question + explanation2
##################################
		returnlist.append(question)
		returnlist.append(answer)
	return(returnlist)

