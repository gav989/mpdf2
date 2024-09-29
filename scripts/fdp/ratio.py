#!/usr/bin/env python3
#ratio.py

def ratiosimplify(n,explanationn):
	from math import gcd
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		choices = [1,2,3,4,5,6,7,8,9,10,11,12]
		left = random.choice(choices)
		choices.remove(left)
		right = random.choice(choices)
		scaler = random.randrange(2,11)*10**random.randrange(0,2)
		scaler = random.randrange(2,11)*10**random.randrange(0,2)
		left = left * scaler
		right = right * scaler
		question = str(left) + " : " + str(right)
		hcf = gcd(left,right)
		left = int(left/hcf)
		right = int(right/hcf)
		answer = str(left) + " : " + str(right)
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def ratioshare1(n,explanationn):
	from math import gcd
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Share "
		else:
			explanation = ""
		choices = [1,2,3,4,5,6,7,8,9,10,11,12]
		left = random.choice(choices)
		choices.remove(left)
		right = random.choice(choices)
		hcf = gcd(left,right)
		left = int(left/hcf)
		right = int(right/hcf)
		scaler = random.randrange(2,13)
		quantity = (left + right) * scaler
		question = "\\pounds" + str(quantity) + " in ratio \\mbox{" + str(left) + " : "+ str(right) + "}"
		left = left * scaler
		right = right * scaler
		answer = "\\pounds" + str(left) + " : \\pounds" + str(right)
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def ratioshare2(n,explanationn):
	from math import gcd
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Share "
		else:
			explanation = ""
		choices = [1,2,3,4,5,6,7,8,9,10,11,12]
		left = random.choice(choices)
		choices.remove(left)
		right = random.choice(choices)
		choices.remove(right)
		middle = random.choice(choices)
		hcf = gcd(left,right)
		hcf = gcd(hcf,middle)
		left = int(left/hcf)
		right = int(right/hcf)
		middle = int(middle/hcf)
		scaler = random.randrange(2,13)
		quantity = (left + right + middle) * scaler
		question = "\\pounds" + str(quantity) + " in ratio \\mbox{" + str(left) + " : " + str(middle) + " : " + str(right) + "}"
		left = left * scaler
		right = right * scaler
		middle = middle * scaler
		answer = "\\mbox{\\pounds" + str(left) + " : \\pounds" + str(middle) + " : \\pounds" + str(right) + "}"
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def ratioreverse1(n,explanationn):
	from math import gcd
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Bob and Tom share some biscuits in the ratio \\mbox{"
		else:
			explanation = ""
		choices = [1,2,3,4,5,6,7,8,9,10,11,12]
		left = random.choice(choices)
		choices.remove(left)
		right = random.choice(choices)
		hcf = gcd(left,right)
		left = int(left/hcf)
		right = int(right/hcf)
		scaler = random.randrange(2,13)
		quantity = (left + right) * scaler
		ratio = str(left) + " : "+ str(right)
		left = left * scaler
		right = right * scaler
		if random.randrange(0,2)==1:
			question = ratio + "}. Bob receives " + str(left) + " biscuits. How many biscuits does Tom receive?"
			answer = str(right)
		else:
			question = ratio + "}. Tom recieves " + str(right) + " biscuits. How many biscuits does Bob recieve?"
			answer = str(left)
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def ratioreverse2(n,explanationn):
	from math import gcd
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Bob and Tom share some biscuits in the ratio \\mbox{"
		else:
			explanation = ""
		choices = [1,2,3,4,5,6,7,8,9,10,11,12]
		left = random.choice(choices)
		choices.remove(left)
		right = random.choice(choices)
		hcf = gcd(left,right)
		left = int(left/hcf)
		right = int(right/hcf)
		scaler = random.randrange(2,13)
		quantity = (left + right) * scaler
		ratio = str(left) + " : "+ str(right)
		left = left * scaler
		right = right * scaler
		if random.randrange(0,2)==1:
			question = ratio + "}. Bob receives " + str(left) + " biscuits. How many biscuits did they share?"
		else:
			question = ratio + "}. Tom recieves " + str(right) + " biscuits. How many biscuits did they share?"
		answer = str(left + right)
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def ratioreverse3(n,explanationn):
	from math import gcd
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Bob and Tom share some biscuits in the ratio \\mbox{"
		else:
			explanation = ""
		choices = [1,2,3,4,5,6,7,8,9,10,11,12]
		left = random.choice(choices)
		choices.remove(left)
		right = random.choice(choices)
		hcf = gcd(left,right)
		left = int(left/hcf)
		right = int(right/hcf)
		scaler = random.randrange(2,13)
		quantity = (left + right) * scaler
		ratio = str(left) + " : "+ str(right)
		left = left * scaler
		right = right * scaler
		if left>right:
			diff = left-right
			question = ratio + "}. Bob gets " + str(diff) + " more biscuits than Tom. How many does each cat receive?"
		else:
			diff = right-left
			question = ratio + "}. Tom gets " + str(diff) + " more biscuits than Bob. How many does each cat receive?"
		answer = str(left) + " and " + str(right)
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def ratiofraction1(n,explanationn):
	from math import gcd
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "The ratio of black cats to white cats is \\mbox{"
		else:
			explanation = ""
		choices = [1,2,3,4,5,6,7,8,9,10,11,12]
		left = random.choice(choices)
		choices.remove(left)
		right = random.choice(choices)
		hcf = gcd(left,right)
		left = int(left/hcf)
		right = int(right/hcf)
		if random.randrange(0,2)==1:
			question = str(left) + " : " + str(right) + "}, what fraction of the cats are white?"
			answer = "$\\dfrac{" + str(right) + "}{" + str(left + right) + "}$"
		else:
			question = str(left) + " : " + str(right) + "}, what fraction of the cats are black?"
			answer = "$\\dfrac{" + str(left) + "}{" + str(left + right) + "}$"
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def ratiofraction2(n,explanationn):
	from math import gcd
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		choices = [1,2,3,4,5,6,7,8,9,10,11,12]
		left = random.choice(choices)
		choices.remove(left)
		right = random.choice(choices)
		hcf = gcd(left,right)
		left = int(left/hcf)
		right = int(right/hcf)
		ratio = str(left) + " : " + str(right)
		if random.randrange(0,2)==1:
			fraction = "$\\dfrac{" + str(left) + "}{" + str(left + right) + "}$"
			question = fraction + " of the cats in a bag are white, the rest are black. Write down the ratio of white to black cats."
		else:
			fraction = "$\\dfrac{" + str(right) + "}{" + str(left + right) + "}$"
			question = fraction + " of the cats in a bag are black, the rest are white. Write down the ratio of white to black cats."
		answer = ratio
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def ratiochange1(n,explanationn):
	from math import gcd,floor
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		nl = "\\\\[0.1cm]"
		nums = (1,2,1,2,3,1,3,2,3,4,1,5,4,3,5,2,7,5,3,7,4,5,6,7,8,9)
		dens = (5,9,4,7,10,3,8,5,7,9,2,9,7,5,8,3,10,7,4,9,5,6,7,8,9,10)
		choice = random.randrange(0,len(nums))
		l = nums[choice]
		r = dens[choice]
		if random.randrange(0,2)==1:
			l,r = r,l
		multer = random.randrange(5,13)
		bigl = l * multer
		bigr = r * multer
		bigl = bigl - random.randrange(1,floor(bigl/2))
		while gcd(bigl,bigr)==1:
			bigl -= 1
		diff = l*multer - bigl
		hcf = gcd(bigl,bigr)
		newl = int(bigl/hcf)
		newr = int(bigr/hcf)
		answer = str(bigr)
		
#		lcm = int((r * (r+1))/gcd(r,r+1))
#		multa = int(lcm/r)
#		multb = int(lcm/(r+1))
#		diff = l*multa - l*multb
#		answer = str(r*multa)
		l1 = "In a bag the ratio of red counters to yellow counters is " + str(l) + " : " + str(r) + ". If " + str(diff) + " of the red counters are removed from the bag, the ratio of red counters to yellow counters is \\mbox{" + str(newl) + " : " + str(newr) + "}."
		l2 = "How many yellow counters are in the bag?"
#		lcm = int(((n+1) * (n))/gcd(n+1,n))
		question = l1 + nl + l2
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def ratiopopulationlite(n,explanationn):
	import random
	from utilities.rounding import rounddpstring
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.1cm] "
		humans = [2,3,4,5,6,7,8,9]
		h1 = random.choice(humans)
		humans.remove(h1)
		h2 = random.choice(humans)
		cats = [2,3,4,5,6,7,8,9]
		cats.remove(h1)
		c1 = random.choice(cats)
		while gcd(h1,c1)!=1:
			cats.remove(c1)
			c1 = random.choice(cats)
		dogs = [2,3,4,5,6,7,8,9]
		dogs.remove(h2)
		d1 = random.choice(dogs)
		while gcd(h2,d1)!=1:
			dogs.remove(d1)
			d1 = random.choice(dogs)
		humans = h1 * h2 * random.randrange(2,7)
		point1 = "\\mbox{cats : humans = " + str(c1) + " : " + str(h1) + "}"
		point2 = "\\mbox{dogs : humans = " + str(d1) + " : " + str(h2) + "}"
		question = "The ratio of " + point1 + ". The ratio of " + point2 + ". Find the ratio of \\mbox{cats : dogs}."
		hcf = gcd(c1*h2,d1*h1)
		answer = str(int((c1*h2)/hcf)) + " : " + str(int((d1*h1)/hcf))
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
