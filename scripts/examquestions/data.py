#!/usr/bin/env python3
#data.py

def averagespuzzle(n,explanationn):
#in ks4 higher unit 2
	import random
	from math import ceil
	from utilities.rounding import roundnearest
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		smallest = random.randrange(1,7)
		rang = random.randrange(8,15)
		largest = smallest + rang
		mode = random.randrange(smallest + 1,largest)
		total = smallest + largest + mode + mode
		total5 = roundnearest(total + 5,5)
		other = int(total5 - total) + 1
		if random.randrange(0,2)==1:
			while other<=smallest:
				other = other + 5
		else:
			other = other + 20
			while other >= largest:
				other = other - 5

		
		mean = int((smallest + other + mode + mode + largest)/5)
		l1 = "Five whole numbers have the following properties:"
		l2 = "\\item the range is " + str(rang)
		if random.randrange(1,3)==2:
			l3 = "\\item the largest number is " + str(largest)
		else:
			l3 = "\\item the smallest number is " + str(smallest)
		l4 = "\\item the mode is " + str(mode)
		l5 = "\\item the mean is " + str(mean)
		l6 = "What are the five numbers?"
		nums = sorted([smallest,mode,mode,other,largest])
		answer = str(nums[0]) + " , " + str(nums[1]) + " , " + str(nums[2]) + " , " + str(nums[3]) + " , " + str(nums[4]) 
		question = l1 + "\\begin{itemize}" + l2 + l3 + l4 + l5 + "\\end{itemize}" + l6
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def timetable1(n,explanationn):
#in ks4 higher unit 2
	import random
	from utilities.time import timestring,timeadd
	from math import ceil
	from utilities.rounding import roundnearest
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		places = ["a","b","c","d","e","f","g","h","i","j","k"]
		random.shuffle(places)
		gaps = [random.randrange(5,31),random.randrange(5,31),random.randrange(5,31),random.randrange(5,31),random.randrange(5,31)]
		col1 = [0]
		col2 = [0]
		col3 = [0]
		col4 = [0]
		col5 = [0]
		cols = [col1,col2,col3,col4,col5]
		h1 = random.randrange(6,10)
		m1 = random.randrange(0,12)*5
		cols[0][0] = timestring(h1,m1)
		for i in range(1,5):
			hdiff = random.randrange(0,3)
			mdiff = random.randrange(0,12)*5
			tdiff = timestring(hdiff,mdiff)
			cols[i][0] = timeadd(cols[i-1][0],tdiff)
		for i in range(0,5):
			for j in range(1,6):
				cols[i].append(timeadd(cols[i][j-1],timestring(0,gaps[j-1])))
		table = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{| p{1cm} || p{1cm} | p{1cm} | p{1cm} | p{1cm} | p{1cm} | } \\hline " + places[0] + " & " + col1[0] + " & " + col2[0] + " & " + col3[0] + " & " + col4[0] + " & " + col5[0] + "\\\\" +places[1] + " & " + col1[1] + " & " + col2[1] + " & " + col3[1] + " & " + col4[1] + " & " + col5[1] + "\\\\" + places[2] + " & " + col1[2] + " & " + col2[2] + " & " + col3[2] + " & " + col4[2] + " & " + col5[2] + "\\\\" + places[3] + " & " + col1[3] + " & " + col2[3] + " & " + col3[3] + " & " + col4[3] + " & " + col5[3] + "\\\\" + places[4] + " & " + col1[4] + " & " + col2[4] + " & " + col3[4] + " & " + col4[4] + " & " + col5[4] + "\\\\ \\hline \\end{tabular}"
		question = table
		answer = "hi"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
