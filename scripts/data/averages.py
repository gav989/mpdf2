#averages.py


def median(n,explanationn):
#in ks3 unit 2
	import random
	from math import floor,ceil
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate the median of "
		else:
			explanation = ""
		randtop = random.randrange(20,100)
		length = random.randrange(4,10)
		choices = list(range(1,randtop))
		a = random.choice(choices)
		numbers = [a,a]
		for i in range(2,length):
			b = random.choice(choices)
			numbers.append(b)
			choices.remove(b)
		random.shuffle(numbers)
		question = str(numbers[0])
		for i in range(1,length):
			question = question + ", " + str(numbers[i])
		numbers.sort()
		median = (length+1)/2 - 1
		if median%1==0:
			median = numbers[int(median)]
		else:
			median = (numbers[int(floor(median))] + numbers[int(ceil(median))])/2		
		if median%1==0:
			median = int(median)
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(median))


def mode(n,explanationn):
#in ks3 unit 2
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate the mode of "
		else:
			explanation = ""
		randtop = random.randrange(20,100)
		length = random.randrange(4,10)
		choices = list(range(1,randtop))
		a = random.choice(choices)
		numbers = [a,a]
		for i in range(2,length):
			b = random.choice(choices)
			numbers.append(b)
			choices.remove(b)
		random.shuffle(numbers)
		question = str(numbers[0])
		for i in range(1,length):
			question = question + ", " + str(numbers[i])
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(a))


def rang(n,explanationn):
#in ks3 unit 2
	import random
	from math import floor,ceil
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate the range of "
		else:
			explanation = ""
		randtop = random.randrange(20,100)
		length = random.randrange(4,10)
		choices = list(range(1,randtop))
		a = random.choice(choices)
		numbers = [a,a]
		for i in range(2,length):
			b = random.choice(choices)
			numbers.append(b)
			choices.remove(b)
		random.shuffle(numbers)
		question = str(numbers[0])
		for i in range(1,length):
			question = question + ", " + str(numbers[i])
		numbers.sort()
		rang = numbers[length-1] - numbers[0]
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(rang))


def mmmr(n,explanationn):
#in ks3 unit 2
	import random
	from math import floor,ceil
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Calculate the mean, median, mode and range of "
		else:
			explanation = ""
		randtop = random.randrange(20,100)
		length = random.randrange(4,10)
		choices = list(range(1,randtop))
		a = random.choice(choices)
		numbers = [a,a]
		for i in range(2,length):
			b = random.choice(choices)
			numbers.append(b)
			choices.remove(b)
		random.shuffle(numbers)
		question = str(numbers[0])
		for i in range(1,length):
			question = question + ", " + str(numbers[i])
		numbers.sort()
		median = (length+1)/2 - 1
		if median%1==0:
			median = numbers[int(median)]
		else:
			median = (numbers[int(floor(median))] + numbers[int(ceil(median))])/2		
		if median%1==0:
			median = int(median)
		rang = numbers[length-1] - numbers[0]
		total = 0
		for i in range(0,length):
			total = total + numbers[i]
		mean = total / length
		if mean%1==0:
			mean = int(mean)
		else:
			mean = rounddp(mean,2)
		answer = "Mean = " + str(mean) + ", Median = " + str(median) + ", Mode = " + str(a) + ", Range = " + str(rang)
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))
