#!/usr/bin/env python3
#trees.py


def treesind2col(n,explanationn):
	import random
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.1cm] "
		if explanationn==1:
			explanation = "Write "
		else:
			explanation = ""
		choices1 = [2,2,2,3,5,7,3,3,3,4,5,7,4,4,5,7,5,5,6,7,1,1,1,1,1,1,2,3,4,5,6,7]
		choices2 = [3,5,7,2,2,2,4,5,7,3,3,3,5,7,4,4,6,7,5,5,2,3,4,5,6,7,1,1,1,1,1,1]
		dec = random.randrange(0,len(choices1))
		black = choices1[dec]
		white = choices2[dec]
		total = black + white
		line1 = "There are " + str(black) + " black cats and " + str(white) + " white cats in a bag. I take a cat out of the bag at random, put it back in, then take out another cat at random."
		if random.randrange(0,2)==1:
			questiona = "black"
			hcf = gcd(black**2,total**2)
			answera = "$\\dfrac{" + str(int(black**2/hcf)) + "}{" + str(int(total**2/hcf)) + "}$"
		else:
			questiona = "white"
			hcf = gcd(white**2,total**2)
			answera = "$\\dfrac{" + str(int(white**2/hcf)) + "}{" + str(int(total**2/hcf)) + "}$"
		line2 = "(a) Find the probability that I get two " + questiona + " cats."
		line3 = "(b) Find the probablity that I get one of each colour."
		hcf = gcd(2*white*black,total**2)
		answerb = "$\\dfrac{" + str(int((2*white*black)/hcf)) + "}{" + str(int(total**2/hcf)) + "}$"
		question = line1 + nl + line2 + nl + line3
		answer = "(a) " + answera + "\\hspace{2cm}(b) " + answerb
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def treesind2col2(n,explanationn):
	import random
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.1cm] "
		if explanationn==1:
			explanation = "Write "
		else:
			explanation = ""
		choices1 = [2,2,2,3,5,7,3,3,3,4,5,7,4,5,1,1,1,1,1,1,2,3,4,5,6,7]
		choices2 = [3,5,7,2,2,2,4,5,7,3,3,3,5,4,2,3,4,5,6,7,1,1,1,1,1,1]
		dec = random.randrange(0,len(choices1))
		black = choices1[dec]
		white = choices2[dec]
		total = black + white
		line1 = "There are " + str(black) + " black cats and " + str(white) + " white cats in a bag. I take a cat out of the bag at random three times, replacing it each time."
		if random.randrange(0,2)==1:
			questiona = "black"
			hcf = gcd(black**3,total**3)
			answera = "$\\dfrac{" + str(int(black**3/hcf)) + "}{" + str(int(total**3/hcf)) + "}$"
		else:
			questiona = "white"
			hcf = gcd(white**3,total**3)
			answera = "$\\dfrac{" + str(int(white**3/hcf)) + "}{" + str(int(total**3/hcf)) + "}$"
		line2 = "(a) Find the probability that I get three " + questiona + " cats."
		dec = random.randrange(0,3)
		if dec==1:
			if random.randrange(0,2)==1:
				line3 = "(b) Find the probablity that I get at least one black cat."
				temp = total**3-white**3
				hcf = gcd(temp,total**3)
				answerb = "$\\dfrac{" + str(int((temp)/hcf)) + "}{" + str(int(total**3/hcf)) + "}$"
			else:
				line3 = "(b) Find the probablity that I get at least one white cat."
				temp = total**3-black**3
				hcf = gcd(temp,total**3)
				answerb = "$\\dfrac{" + str(int((temp)/hcf)) + "}{" + str(int(total**3/hcf)) + "}$"
		elif dec==2:
			if random.randrange(0,2)==1:
				line3 = "(b) Find the probablity that I get at least two black cats."
				temp = black**3 + 3*black*black*white
				hcf = gcd(temp,total**3)
				answerb = "$\\dfrac{" + str(int((temp)/hcf)) + "}{" + str(int(total**3/hcf)) + "}$"
			else:
				line3 = "(b) Find the probablity that I get at least two white cats."
				temp = white**3 + 3*black*white*white
				hcf = gcd(temp,total**3)
				answerb = "$\\dfrac{" + str(int((temp)/hcf)) + "}{" + str(int(total**3/hcf)) + "}$"
		else:
			if random.randrange(0,2)==1:
				if random.randrange(0,2)==1:
					line3 = "(b) find the probablity that I get exactly two black cats."
				else:
					line3 = "(b) find the probablity that I get exactly one white cat."
				temp = 3*black*black*white
				hcf = gcd(temp,total**3)
				answerb = "$\\dfrac{" + str(int((temp)/hcf)) + "}{" + str(int(total**3/hcf)) + "}$"
			else:
				if random.randrange(0,2)==1:
					line3 = "(b) find the probablity that I get exactly two white cats."
				else:
					line3 = "(b) find the probablity that I get exactly one black cat."
				temp = 3*black*white*white
				hcf = gcd(temp,total**3)
				answerb = "$\\dfrac{" + str(int((temp)/hcf)) + "}{" + str(int(total**3/hcf)) + "}$"
		question = line1 + nl + line2 + nl + line3
		answer = "(a) " + answera + "\\hspace{2cm}(b) " + answerb
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def treesind3col(n,explanationn):
	import random
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.1cm] "
		if explanationn==1:
			explanation = "Write "
		else:
			explanation = ""
		choices1 = [2,2,2,3,5,7,3,3,3,4,5,7,4,4,5,7,5,5,6,7,1,1,1,1,1,1,2,3,4,5,6,7]
		choices2 = [3,5,7,2,2,2,4,5,7,3,3,3,5,7,4,4,6,7,5,5,2,3,4,5,6,7,1,1,1,1,1,1]
		dec = random.randrange(0,len(choices1))
		black = choices1[dec]
		white = choices2[dec]
		grey = random.randrange(1,8)
		total = black + white + grey
		line1 = "There are " + str(black) + " black cats, " + str(grey) + " grey cats and " + str(white) + " white cats in a bag. I take a cat out of the bag at random, put it back in, then take out another cat."
		dec = random.randrange(0,3)
		if dec==1:
			questiona = "black"
			hcf = gcd(black**2,total**2)
			answera = "$\\dfrac{" + str(int(black**2/hcf)) + "}{" + str(int(total**2/hcf)) + "}$"
		elif dec==2:
			questiona = "white"
			hcf = gcd(white**2,total**2)
			answera = "$\\dfrac{" + str(int(white**2/hcf)) + "}{" + str(int(total**2/hcf)) + "}$"
		else:
			questiona = "grey"
			hcf = gcd(grey**2,total**2)
			answera = "$\\dfrac{" + str(int(grey**2/hcf)) + "}{" + str(int(total**2/hcf)) + "}$"
		dec = random.randrange(0,3)
		if dec==1:
			questionb = "black"
			temp = grey*white + grey*grey + white*white + white*grey
			hcf = gcd(temp,total**2)
			answerb = "$\\dfrac{" + str(int(temp/hcf)) + "}{" + str(int(total**2/hcf)) + "}$"
		elif dec==2:
			questionb = "grey"
			temp = black*white + black*black + white*white + white*black
			hcf = gcd(temp,total**2)
			answerb = "$\\dfrac{" + str(int(temp/hcf)) + "}{" + str(int(total**2/hcf)) + "}$"
		else:
			questionb = "white"
			temp = black*grey + black*black + grey*grey + grey*black
			hcf = gcd(temp,total**2)
			answerb = "$\\dfrac{" + str(int(temp/hcf)) + "}{" + str(int(total**2/hcf)) + "}$"
		line2 = "(a) Find the probability that I get two " + questiona + " cats."
		line3 = "(b) Find the probablity that I get no " + str(questionb) + " cats."
		question = line1 + nl + line2 + nl + line3
		answer = "(a) " + answera + "\\hspace{2cm}(b) " + answerb
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def treesdep2col(n,explanationn):
	import random
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.1cm] "
		if explanationn==1:
			explanation = "Write "
		else:
			explanation = ""
		choices1 = [2,2,2,3,5,7,3,3,3,4,5,7,4,4,5,7,5,5,6,7,1,1,1,1,1,1,2,3,4,5,6,7]
		choices2 = [3,5,7,2,2,2,4,5,7,3,3,3,5,7,4,4,6,7,5,5,2,3,4,5,6,7,1,1,1,1,1,1]
		dec = random.randrange(0,len(choices1))
		black = choices1[dec]
		white = choices2[dec]
		total = black + white
		line1 = "There are " + str(black) + " black cats and " + str(white) + " white cats in a bag. I take a cat out of the bag at random, leave it out, then take out another cat at random."
		if random.randrange(0,2)==1:
			questiona = "black"
			hcf = gcd(black*(black-1),total*(total-1))
			answera = "$\\dfrac{" + str(int(black*(black-1)/hcf)) + "}{" + str(int(total*(total-1)/hcf)) + "}$"
		else:
			questiona = "white"
			hcf = gcd(white*(white-1),total*(total-1))
			answera = "$\\dfrac{" + str(int(white*(white-1)/hcf)) + "}{" + str(int(total*(total-1)/hcf)) + "}$"
		line2 = "(a) Find the probability that I get two " + questiona + " cats."
		line3 = "(b) Find the probablity that I get one of each colour."
		hcf = gcd(2*white*black,total*(total-1))
		answerb = "$\\dfrac{" + str(int((2*white*black)/hcf)) + "}{" + str(int(total*(total-1)/hcf)) + "}$"
		question = line1 + nl + line2 + nl + line3
		answer = "(a) " + answera + "\\hspace{2cm}(b) " + answerb
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def treesdep2col2(n,explanationn):
	import random
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.1cm] "
		if explanationn==1:
			explanation = "Write "
		else:
			explanation = ""
		choices1 = [2,2,2,3,5,7,3,3,3,4,5,7,4,5]
		choices2 = [3,5,7,2,2,2,4,5,7,3,3,3,5,4]
		dec = random.randrange(0,len(choices1))
		black = choices1[dec]
		white = choices2[dec]
		total = black + white
		totalcube = total*(total-1)*(total-2)
		blackcube = black*(black-1)*(black-2)
		whitecube = white*(white-1)*(white-2)
		line1 = "There are " + str(black) + " black cats and " + str(white) + " white cats in a bag. I take a cat out of the bag at random three times without replacing it."
		if random.randrange(0,2)==1:
			questiona = "black"
			hcf = gcd(blackcube,totalcube)
			if blackcube==0:
				answera = "0"
			else:
				answera = "$\\dfrac{" + str(int(blackcube/hcf)) + "}{" + str(int(totalcube/hcf)) + "}$"
		else:
			questiona = "white"
			hcf = gcd(whitecube,totalcube)
			if whitecube==0:
				answera = "0"
			else:
				answera = "$\\dfrac{" + str(int(whitecube/hcf)) + "}{" + str(int(totalcube/hcf)) + "}$"
		line2 = "(a) Find the probability that I get three " + questiona + " cats."
		dec = random.randrange(0,3)
		if dec==1:
			if random.randrange(0,2)==1:
				line3 = "(b) Find the probablity that I get at least one black cat."
				temp = totalcube-whitecube
				hcf = gcd(temp,totalcube)
				answerb = "$\\dfrac{" + str(int((temp)/hcf)) + "}{" + str(int(totalcube/hcf)) + "}$"
			else:
				line3 = "(b) Find the probablity that I get at least one white cat."
				temp = totalcube-blackcube
				hcf = gcd(temp,total**3)
				answerb = "$\\dfrac{" + str(int((temp)/hcf)) + "}{" + str(int(totalcube/hcf)) + "}$"
		elif dec==2:
			if random.randrange(0,2)==1:
				line3 = "(b) Find the probablity that I get at least two black cats."
				temp = blackcube + 3*black*(black-1)*white
				hcf = gcd(temp,total**3)
				answerb = "$\\dfrac{" + str(int((temp)/hcf)) + "}{" + str(int(totalcube/hcf)) + "}$"
			else:
				line3 = "(b) Find the probablity that I get at least two white cats."
				temp = whitecube + 3*black*white*(white-1)
				hcf = gcd(temp,totalcube)
				answerb = "$\\dfrac{" + str(int((temp)/hcf)) + "}{" + str(int(totalcube/hcf)) + "}$"
		else:
			if random.randrange(0,2)==1:
				if random.randrange(0,2)==1:
					line3 = "(b) find the probablity that I get exactly two black cats."
				else:
					line3 = "(b) find the probablity that I get exactly one white cat."
				temp = 3*black*(black-1)*white
				hcf = gcd(temp,totalcube)
				answerb = "$\\dfrac{" + str(int((temp)/hcf)) + "}{" + str(int(totalcube/hcf)) + "}$"
			else:
				if random.randrange(0,2)==1:
					line3 = "(b) find the probablity that I get exactly two white cats."
				else:
					line3 = "(b) find the probablity that I get exactly one black cat."
				temp = 3*black*white*(white-1)
				hcf = gcd(temp,totalcube)
				answerb = "$\\dfrac{" + str(int((temp)/hcf)) + "}{" + str(int(totalcube/hcf)) + "}$"
		question = line1 + nl + line2 + nl + line3
		answer = "(a) " + answera + "\\hspace{2cm}(b) " + answerb
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def treesdep3col(n,explanationn):
	import random
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.1cm] "
		if explanationn==1:
			explanation = "Write "
		else:
			explanation = ""
		choices1 = [2,2,2,3,5,7,3,3,3,4,5,7,4,4,5,7,5,5,6,7,1,1,1,1,1,1,2,3,4,5,6,7]
		choices2 = [3,5,7,2,2,2,4,5,7,3,3,3,5,7,4,4,6,7,5,5,2,3,4,5,6,7,1,1,1,1,1,1]
		dec = random.randrange(0,len(choices1))
		black = choices1[dec]
		white = choices2[dec]
		grey = random.randrange(1,8)
		total = black + white + grey
		totalsquare = total*(total-1)
		blacksquare = black*(black-1)
		whitesquare = white*(white-1)
		greysquare = grey*(grey-1)
		line1 = "There are " + str(black) + " black cats, " + str(grey) + " grey cats and " + str(white) + " white cats in a bag. I take a cat out of the bag at random, leave it out, then take out another cat."
		dec = random.randrange(0,3)
		if dec==1:
			questiona = "black"
			hcf = gcd(blacksquare,totalsquare)
			answera = "$\\dfrac{" + str(int(blacksquare/hcf)) + "}{" + str(int(totalsquare/hcf)) + "}$"
		elif dec==2:
			questiona = "white"
			hcf = gcd(whitesquare,totalsquare)
			answera = "$\\dfrac{" + str(int(whitesquare/hcf)) + "}{" + str(int(totalsquare/hcf)) + "}$"
		else:
			questiona = "grey"
			hcf = gcd(greysquare,totalsquare)
			answera = "$\\dfrac{" + str(int(greysquare/hcf)) + "}{" + str(int(totalsquare/hcf)) + "}$"
		dec = random.randrange(0,3)
		if dec==1:
			questionb = "black"
			temp = grey*white + greysquare + whitesquare + white*grey
			hcf = gcd(temp,totalsquare)
			answerb = "$\\dfrac{" + str(int(temp/hcf)) + "}{" + str(int(totalsquare/hcf)) + "}$"
		elif dec==2:
			questionb = "grey"
			temp = black*white + blacksquare + whitesquare + white*black
			hcf = gcd(temp,totalsquare)
			answerb = "$\\dfrac{" + str(int(temp/hcf)) + "}{" + str(int(totalsquare/hcf)) + "}$"
		else:
			questionb = "white"
			temp = black*grey + blacksquare + greysquare + grey*black
			hcf = gcd(temp,total**2)
			answerb = "$\\dfrac{" + str(int(temp/hcf)) + "}{" + str(int(totalsquare/hcf)) + "}$"
		line2 = "(a) Find the probability that I get two " + questiona + " cats."
		line3 = "(b) Find the probablity that I get no " + str(questionb) + " cats."
		question = line1 + nl + line2 + nl + line3
		answer = "(a) " + answera + "\\hspace{2cm}(b) " + answerb
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
