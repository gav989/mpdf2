#!/usr/bin/env python3
#number.py

def trains(n,explanationn):
#in ks4 pre higher number paper
	import random
	from math import floor
	from fractions import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		explanation = ""
		hcfchoice = (2,3,4,5,6,7,8,9,10,11,12)
		hcf = random.choice(hcfchoice)
		choices = [2,3,4,5,6,7,8,9,10,11,12,14,15,16,18,20]
		length = len(choices)
		for i in range(0,length-1):
			item = choices[length-1-i]
			if item>floor(40/hcf)+1:
				choices.remove(item)
		a = random.choice(choices)
		length = len(choices)
		for i in range(0,length):
			item = choices[length-1-i]
			if item%a==0 or a%item==0:
				choices.remove(item)
		b = random.choice(choices)
		interval1 = a*hcf
		interval2 = b*hcf
		hcf = gcd(interval1,interval2)
		lcm = int(interval1 * interval2 / hcf)
		hour = random.randrange(8,20)
		mins = random.randrange(0,6)*10
		if hour<10:
			h = "0" + str(hour)
		else:
			h = str(hour)
		if mins==0:
			m = "00"
		else:
			m = str(mins)
		starttime = h + ":" + m
		temphours = floor(lcm/60)
		lcm = lcm - 60*temphours
		hour = hour + temphours
		mins = mins + lcm
		if mins>59:
			mins = mins - 60
			hour = hour + 1
		if hour<10:
			h = "0" + str(hour)
		else:
			h = str(hour)
		if mins==0:
			m = "00"
		elif mins<10:
			mins = "0" + str(mins)
		else:
			m = str(mins)
		endtime = h + ":" + m
#write question
		tempquestions.write(explanation + "At a train station, northbound trains stop every " + str(interval1)  + " minutes and southbound trains stop every " + str(interval2) + " minutes.\\\\[0.3cm] Two trains stopped together at " + starttime + ".\\\\[0.3cm] Work out the next time when two trains will stop together at this station.")

		tempquestions.write("\n")
#write answer
		tempquestions.write(endtime)



def populationcross(n,explanationn):
#in ks4 higher unit 2
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		explanation = ""
		pop1 = random.randrange(60,81)*100
		pop2 = random.randrange(30,51)*100
		inc = random.randrange(2,10)
		dec = random.randrange(2,10)
		startyear = random.randrange(2005,2017)
		incmult = round((100 + inc)/100,2)
		decmult = round((100 - dec)/100,2)
		years = 0
		question = "In a location there are cats and dogs.\\\\[0.3cm] At the start of " + str(startyear) + ":\\\\[0.3cm] The population of cats was " + str(pop1) + " and was \\textbf{decreasing} by " + str(dec) + "\\% each year\\\\ The population of dogs was " + str(pop2) + " and was \\textbf{increasing} by " + str(inc) + " \\% each year.\\\\[0.3cm] At the start of which year will the population of dogs first be greater than that of the cats?"
		while pop1>pop2:
			pop1 = pop1 * decmult
			pop2 = pop2 * incmult
			years = years + 1
		answer = startyear + years
		
#write question
		tempquestions.write(explanation + question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))


def changefromtransaction(n,explanationn):
#in ks3 unit 2
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		amount = round(random.randrange(10,30) + random.randrange(1,10)/10 + random.randrange(1,10) / 100,2)
		cost = round(random.randrange(3,10) + random.randrange(1,10)/10 + random.randrange(1,10) / 100,2)
		result = amount - cost
		result = "{0:.2f}".format(result)
#write question
		tempquestions.write(explanation + "A boy has \\pounds" + str(amount) + ". He spends \\pounds" + str(cost) + ". How much money does he have left?")

		tempquestions.write("\n")
#write answer
		tempquestions.write("\\pounds" + str(result))



def changefromtransaction2(n,explanationn):
#in ks3 unit 6
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		note = random.randrange(1,3)*5
		price = random.randrange(20,60)
		if (note*100)/price>9:
			top = 10
		else:
			top = floor((note*100)/price)
		quantity = random.randrange(4,top)
		numbers = ("four","five","six","seven","eight","nine")
		change = ((note*100) - (quantity*price))/100
		quantity = numbers[quantity - 4]
		#write question
		tempquestions.write(explanation + "A girl buys " + quantity + " cans of cat food costing " + str(price) + "p each. How much change does she get from \\pounds" + str(note) + "?")

		tempquestions.write("\n")
#write answer
		tempquestions.write("\\pounds" + str(change))



def changefromtransaction3(n,explanationn):
#in ks3 unit 2
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		collar = (random.randrange(1,5)*100 + random.randrange(1,10)*10 + random.randrange(1,10))/100
		tray = (random.randrange(1,5)*100 + random.randrange(1,10)*10 + random.randrange(1,10))/100
		note = random.randrange(1,3)*10
		change = round(note - (collar + tray),2)
		if change%1==0:
			change = int(change)
		elif change*10%1==0:
			change = str(change) + "0"
#write question
		tempquestions.write(explanation + "Jack bought a cat collar costing \\pounds" + str(collar) + " and a litter tray for \\pounds" + str(tray) + ". how much change will he get from \\pounds" + str(note) + "?")

		tempquestions.write("\n")
#write answer
		tempquestions.write("\\pounds" + str(change))



def sftable(n,explanationn):
#in ks3 unit 2
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		countries = ["England","Scotland","Wales","Ireland","Northern Ireland","France","Spain","Russia","China"]
		c1 = random.choice(countries)
		countries.remove(c1)
		c2 = random.choice(countries)
		countries.remove(c2)
		c3 = random.choice(countries)
		countries.remove(c3)
		c4 = random.choice(countries)
		countries.remove(c4)
		i = random.randrange(3,8)
		i2 = i + 1
		t = random.randrange(1,3)
		a = random.randrange(1,10)*10**t + random.randrange(1,10**t)
		answera = "\\num{" + str(a) + ("0" * (abs(i)-t)) + "}"
		a = a/10**t
		num1 = "$" + str(a) + "\\times 10^"+ str(i) + "$"
		t = random.randrange(1,3)
		a = random.randrange(1,10)*10**t + random.randrange(1,10**t)
		a = a/10**t
		b2 = a * 10**i
		num2 = "$" + str(a) + "\\times 10^"+ str(i) + "$"
		t = random.randrange(1,3)
		a = random.randrange(1,10)*10**t + random.randrange(1,10**t)
		a = a/10**t
		b1 = a * 10**i2
		num3 = "$" + str(a) + "\\times 10^"+ str(i2) + "$"
		t = random.randrange(1,3)
		a = random.randrange(1,10)*10**t + random.randrange(1,10**t)
		a = a/10**t
		num4 = "$" + str(a) + "\\times 10^"+ str(i) + "$"
		estimator = random.randrange(2,10)*10
		answerc = round(a,0) * estimator
		while answerc>=10:
			answerc = answerc/10
			i = i + 1
		if answerc%1==0:
			answerc = int(answerc)
		answerc = str(answerc) + " $\\times 10^{" + str(i) + "}$" 
		intro = "The table below shows the number of crates of cat food produced each day in some countries."
		questiona = "(a) How many crates per day were produced in " + c1 + "? \\\\ Give your answer as an ordinary number."
		questionb = "(b) How many more crates per day were produced in " + c3 + " than " + c2 + "?"
		answerb = "\\num{" + str(int(round(b1 - b2,0))) + "}"
		questionc = "(c) The production of one crate of cat food per day is equivalent to approximately " + str(estimator) + " tonnes of cat food per year. Estimate the number of tonnes of cat food produced in " + c4 + " each year. Give your answer in standard form."
		order = [0,1,2,3]
		random.shuffle(order)
		countries = (c1,c2,c3,c4)
		nums = (num1,num2,num3,num4)
		table = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{7cm} | } \\hline Country & Cat Food Produced (crates per day) \\\\ \\specialrule{1pt}{0pt}{0pt} " + countries[order[0]] + " & " + nums[order[0]] + " \\\\ \\hline " + countries[order[1]] + "  & " + nums[order[1]] + " \\\\ \\hline " + countries[order[2]] + " & " + nums[order[2]] + " \\\\ \\hline " + countries[order[3]] + "  & " + nums[order[3]] + " \\\\ \\hline \\end{tabular}\\hfill"


		nl = " \\\\[0.3cm] "
		question = intro + nl + table + nl + questiona + nl + questionb + nl + questionc 
		answer = "(a) " + answera + "\\\\(b) " + answerb + "\\\\(c) " + answerc
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def hcflcmreverse(n,explanationn):
#in nov 2012 higher non calc
	from math import floor
	from fractions import gcd
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		hcfchoice = (2,3,4,5,6,7,8,9,10,11,12,14,15,16,18,20,22,24,25)
		hcf = random.choice(hcfchoice)
		choices = [2,3,5]
		a = random.choice(choices)
		choices.remove(a)
		b = random.choice(choices)
		a = a*hcf
		b = b*hcf
		hcf = gcd(a,b)
		lcm = int(a * b / hcf)
		nl = " \\\\[0.3cm] "
		question = "The highest common factor of two numbers is " + str(hcf) + "." + nl + "The lowest common multiple of these two numbers is " + str(lcm) + "." + nl + "Both numbers are greater than " + str(hcf) + "\\\\[0.5cm]" + "What are the two numbers?"
		answer = str(a) + " and " + str(b)
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def countersrelativefrequency(n,explanationn):
#in nov 2012 higher non calc
	from math import floor
	from fractions import gcd
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		counters = 4 * random.randrange(3,11)
		freq = 100 * 2**random.randrange(0,4)
		halfdiff = int(0.01*freq)
		half1 = int(freq/4 + random.randrange(1,halfdiff + 1))
		half2 = int(freq/4 - random.randrange(1,halfdiff + 1))
		quarts1 = int(freq/8 + random.randrange(1,halfdiff + 1)*-1**(random.randrange(1,3)))
		quarts2 = freq - (quarts1 + half1 + half2)
		freqs = [half1,half2,quarts1,quarts2]
		random.shuffle(freqs)
		red = freqs[0]
		green = freqs[1]
		yellow = freqs[2]
		blue = freqs[3]
		intro = "A bag contains red, green, yellow and blue counters only." + nl + "There are " + str(counters) + " altogether in the bag." + nl + "John takes a counter at random from the bag, records the colour and replaces it." + nl + "He does this " + str(freq) + " times." + nl + "Her results are shown in the table."
		table = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{| p{2cm} | p{2cm} | p{2cm} | p{2cm} | p{2cm} |} \\hline Colour & Red & Green & Yellow & Blue  \\\\ \\hline Frequency & " + str(red) + " & " + str(green) + " & " + str(yellow) + " & " + str(blue) + "\\\\ \\hline \\end{tabular}\\hfill"
		questiona = "\\textbf{Estimate} the number of counters of each colour."


		question = intro + nl + table + nl + questiona 
		red = "Red: " + str(int(round((red/freq)*counters,0)))
		green = "Green: " + str(int(round((green/freq)*counters,0)))
		yellow = "Yellow: " + str(int(round((yellow/freq)*counters,0)))
		blue = "Blue: " + str(int(round((blue/freq)*counters,0)))
		answer = red + nl + green + nl + yellow + nl + blue
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def negativestemperature(n,explanationn):
#in old fia4
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		midday = random.randrange(2,11)
		midnight = random.randrange(-9,0)
		fall = midday - midnight
		degc = "$\\SI{}{\\degreeCelsius}$"
		intro = "On Monday the temperature at midday was " + str(midday) + degc + "." + nl + "At midnight the temperature had fallen to " + str(midnight) + degc + "."
		questiona = "(a) How many degrees had the temperature fallen?"
		rise = random.randrange(2,fall)
		questionb = "(b) By midday on Tuesday the temperature had risen by " +  str(rise) + " degrees from the temperature at midnight." + nl + "What was the temperature at midday on Tuesday?"
		question = intro + nl + questiona + nl + questionb
		answer = "(a) " + str(fall) + nl + "(b) " + str(midnight + rise) + degc
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def fmpeq(n,explanationn):
#in old fia4
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		intro = "Choose a word from the box below to complete each of the following sentences."
		box = "\\hfill\\ovalbox{\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ p{2.5cm}  p{3cm}  p{2cm}}  factor & square root & prime  \\\\ cube & multiple & square\\\\  \\end{tabular}}\\hfill"
		done = 0
		questions = []
		answers = []
		choices = ["factor","square root","prime","cube","multiple","square"]
		while done<4:
			choice = random.choice(choices)
			choices.remove(choice)
			if choice=="factor":
				num1 = random.randrange(2,13)
				num2 = num1 * random.randrange(2,13)
				question = str(num1) + " is a $\\rule[-1.5mm]{2cm}{0.3mm}$  of " + str(num2)
			elif choice=="multiple":
				num2 = random.randrange(2,13)
				num1 = num2 * random.randrange(2,13)
				question = str(num1) + " is a $\\rule[-1.5mm]{2cm}{0.3mm}$  of " + str(num2)
			if choice=="square root":
				num1 = random.randrange(2,13)
				num2 = num1**2
				question = str(num1) + " is the $\\rule[-1.5mm]{2cm}{0.3mm}$  of " + str(num2)
			if choice=="square":
				nums = [2,3,4,5,6,7,9,10,11,12]
				num1 = random.choice(nums)**2
				question = str(num1) + " is a $\\rule[-1.5mm]{2cm}{0.3mm}$  number "
			if choice=="cube":
				nums = [2,3,5]
				num1 = random.choice(nums)**3
				question = str(num1) + " is a $\\rule[-1.5mm]{2cm}{0.3mm}$  number "
			if choice=="prime":
				nums = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
				num1 = random.choice(nums)
				question = str(num1) + " is a $\\rule[-1.5mm]{2cm}{0.3mm}$  number "
			questions.append(question)
			answers.append(choice)
			done = done+1
		question = intro + nl + box + nl + "(a) " + questions[0] + nl + "(b) " + questions[1] + nl + "(c) " + questions[2] + nl + "(d) " + questions[3]
		answer = "(a) " + answers[0] + nl + "(b) " + answers[1] + nl + "(c) " + answers[2] + nl + "(d) " + answers[3]
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def conversiongraph(n,explanationn):
#in ks4 higher unit 2
	import random
	from math import ceil, sqrt
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		er = 1.46
		maxx = 41
		roundtos = [3,4,5]
		poundchoices = []
		for i in range(10,maxx):
			if i%2==0 or i%5==0:
				poundchoices.append(i)
		pounds = random.choice(poundchoices)
		apounds = pounds
		dollars = pounds * er
		roundto = random.choice(roundtos)
		dollars = roundto * (round(dollars/roundto,0)+ (-1)**random.randrange(1,3))
		adollars = dollars
		poundfactors = []
		for i in range(2,ceil(pounds/2)):
			if pounds%i==0:
				poundfactors.append(i)
		poundfactor = random.choice(poundfactors)
		poundfrac = "$\\dfrac{1}{" + str(int((pounds-poundfactor)/poundfactor)) + "}$"
		dollarfactors = []
		for i in range(2,ceil(dollars/2)):
			if dollars%i==0:
				dollarfactors.append(i)
		newdollar = dollars - 1
		while ((dollars/newdollar)*100 - 100)%5!=0:
			newdollar = newdollar-1
		perc = int(100*(dollars-newdollar)/newdollar)
		dollars = newdollar
		dollars = "\\$" + str(int(dollars))
		pounds = "\\pounds" + str(pounds - poundfactor)
		intro = "This conversion graph can be used to change between prices in pounds (\\pounds) and dollars (\\$)."
		graph = "\\includegraphics[scale=0.135]{examquestions/images/pounddollars}"
		questiona = "Jess can buy a cat from America for " + dollars + " plus " + str(perc) + "\\% for delivery." + nl + "She can buy the same cat in the UK for " + pounds + " plus " + poundfrac + " of this price for delivery." + nl + "Work out which is cheaper"
		question = "\\begin{columns} \\begin{column}{.35\\textwidth} " + intro + nl + questiona + " \\end{column} \\begin{column}{.55\\textwidth}\\raggedleft " + graph + " \\end{column} \\end{columns}."
		ukdollar = round(apounds*er,2)
		if ukdollar%1==0:
			ukdollar = int(ukdollar)
		elif ukdollar*10%1==0:
			ukdollar = str(ukdollar) + "0"
		americapound = round(adollars/er,2)
		if americapound%1==0:
			americapound = int(americapound)
		elif americapound*10%1==0:
			americapound = str(americapound) + "0"
			
		answer = "UK - \\pounds" + str(apounds) + " = \\$" + str(ukdollar) + "\\hspace{1cm}  America - \\pounds" + str(americapound) + " = \\$" + str(int(adollars))
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def compoundvssimple(n,explanationn):
#in new higher unit 1
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		amount = random.randrange(1,51)*500
		years = random.randrange(2,4)
		compound = random.randrange(3,10)
		if years==2:
			year1 = random.randrange(compound-2,compound)
			year2 = random.randrange(compound+1,compound+3)
			difference = "\\pounds" + str("{0:.2f}".format(abs(round(amount * (1+compound/100)**(years),2) - round(amount * (1+year1/100) * (1+year2/100),2))))
			compresult = "\\pounds" + str("{0:.2f}".format(amount * (1+compound/100)**(years)))
			simpresult = "\\pounds" + str("{0:.2f}".format(amount * (1+year1/100) * (1+year2/100)))
			table = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ p{4cm} | p{4cm} } Account A & Account B \\\\ \\hline " + "Interest: " + str(compound) + "\% per year compound interest." + " & " + "Interest: " + str(year1) + "\% for the first year and " + str(year2) + "\% for the second year." + " \\\\ \\end{tabular}\\hfill"
		else:
			year1 = random.randrange(compound-2,compound)
			year2 = random.randrange(compound-1,compound+2)
			year3 = random.randrange(compound+1,compound+3)
			difference = "\pounds" + str("{0:.2f}".format(abs(round(amount * (1+compound/100)**(years),2) - round(amount * (1+year1/100) * (1+year2/100) * (1+year3/100),2))))
			compresult = "\pounds" + str("{0:.2f}".format(amount * (1+compound/100)**(years)))
			simpresult = "\pounds" + str("{0:.2f}".format(amount * (1+year1/100) * (1+year2/100) * (1+year3/100)))
			table = "\\hfill\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ p{4cm} | p{4cm} } Account A & Account B \\\\ \\hline " + "Interest: " + str(compound) + "\% per year compound interest." + " & " + "Interest: " + str(year1) + "\% for the first year, " + str(year2) + "\% for the second year and " + str(year3) + "\% for the third year." + " \\\\ \\end{tabular}\\hfill"
		intro = "Here are the interest rates for two accounts."
		questiona = "A cat has \pounds" + str(amount) + " to invest." + nl + "Calculate which account would give him most money if he invests his money for " + str(years) + " years." + nl + "Give the difference in interest to the nearest penny."
		question = intro + nl + table + nl + questiona
		answer = "Account A: " + compresult + nl + "Account B: " + simpresult + nl + "Difference: " + difference
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def sfdiff(n,explanationn):
#in ks4 higher unit 1
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		year1 = random.randrange(1980,2000)
		year2 = year1 + random.randrange(5,15)
		num2 = random.randrange(1,10)
		num1 = round(random.randrange(1,10) + random.randrange(1,10)/10,1)
		ind2 = random.randrange(5,13)
		ind1 = ind2 + 1
		answer = num1*10**ind1 - num2*10**ind2
		ind3 = 0
		while answer>=10:
			answer = answer/10
			ind3 = ind3 + 1
		if answer%1==0:
			answer = int(answer)
		answer = "$" + str(answer) + "\\times 10^{" + str(ind3) + "}$" 
		num1 = "$" + str(num1) + "\\times 10^{" + str(ind1) + "}$"
		num2 = "$" + str(num2) + "\\times 10^{" + str(ind2) + "}$"
		intro = "The UK's Gross Domestic Product (GDP) in " + str(year1) + " was \\pounds" + num2 + " and in " + str(year2) + " it was \\pounds" + num1 + "."
		inst1 = "Work out the increase in GDP between " + str(year1) + " and " + str(year2) + "."
		inst2 = "Write your answer in standard form."
		question = intro + nl + inst1 + nl + inst2 + nl
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def sfdivprofit(n,explanationn):
#in ks4 higher unit 1
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		num2 = random.randrange(2,10)
		if num2==2 or num2==5 or num2==4:
			num1 = round(random.randrange(0,10)/10 + random.randrange(1,10),1)
			num3 = round(num1/num2,3)
		elif num2==6:
			num1 = round(random.randrange(1,33) * 0.3,1)
			num3 = round(num1/num2,3)
		else:
			num3 = random.randrange(2,10)
			num1 = num2 * num3
		ind1 = random.randrange(2,10)
		inds = [2,3,4,5,6,7,8,9]
		inds.remove(ind1)
		ind2 = random.choice(inds)
		if ind1<ind2:
			temp = ind1
			ind1 = ind2
			ind2 = temp
		if num1>=10:
			num1 = round(num1/10,3)
			alter = 1
		else:
			alter = 0
		ind3 = ind1 - ind2
		if alter==1:
			ind1 = ind1 + 1
		if num1%1==0:
			num1 = int(num1)
		if num3<1:
			num3 = round(num3*10,3)
			ind3 = ind3 - 1
		if num3%1==0:
			num3 = int(num3)
		profit = "$" + str(num1) + " \\times 10^{" + str(ind1) + "}$"
		employees = "$" + str(num2) + " \\times 10^{" + str(ind2) + "}$"
		answer = round(num3*10**ind3,2)
		if answer%1==0:
			answer = int(answer)
		elif (answer*10)%1==0:
			answer = str(answer) + "0"
		answer = "\\pounds" + str(answer)
		nl = " \\\\[0.3cm] "
		intro = "Cat Hats Ltd. share their profit equally amongst their employees."
		intro2 = "One year, their profit was \\pounds" + profit + " and they had " + employees + " employees."
		questiona = "Work out how much each employee got that year."
		question = intro + nl + intro2 + nl + questiona + nl
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def sfdouble(n,explanationn):
#in ks4 higher unit 1
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		num1 = 2
		num2 = round(random.randrange(5,10) + random.randrange(1,10)/10,1)
		num3 = round(num1 * num2,1)
		ind2 = random.randrange(2,10)
		ind3 = ind2
		if num3>=10:
			num3 = round(num3/10,2)
			ind3 = ind3 + 1
		intro = "Last year, Cat Hats Ltd. made a profit of \\pounds$" + str(num2) + "\\times 10^{" + str(ind2) + "}$."
		intro2 = "This year, their profit was double that of last year."
		questiona = "Work out their profit for this year."
		intro3 = "Write your answer in standard form."
		question = intro + nl + intro2 + nl + questiona + nl + intro3 + nl
		answer = "\\pounds$" + str(num3) + "\\times 10^{" + str(ind3) + "}$"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def carvaluedrop(n,explanationn):
#in ks4 higher unit 1
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		v = random.randrange(8,30)*1000
		decimal = random.randrange(90,98)/100
		v2 = int(v/2)
		t = random.randrange(2,5)
		years = 0
		intro = "The value of a cat statue \\pounds V is given by "
		formula = "$V = " + str(v) + "\\times" + str(decimal) + "^{t}$"
		intro2 = "where $t$ is the age of the statue in complete years."
		questiona = "(a) Write down the value of V when t = 0."
		questionb = "(b) What is the value of V when t = " + str(t) + "?"
		questionc = "(c) After how many years will the statue's value drop below \\pounds" + str(v2) + "?"
		question = intro + nl + formula + nl + intro2 + nl + questiona + nl + questionb + nl + questionc
		answera = "\\pounds" + str(v)
		answerb = round(v * decimal ** t,2)
		if answerb%1==0:
			answerb = int(answerb)
		elif (answerb*10)%1==0:
			answerb = str(answerb) + "0"
		answerb = "\\pounds" + str(answerb)
		while v>v2:
			v = v*decimal
			years = years + 1
		answerc = str(years)
		answer = answera + nl + answerb + nl + answerc
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def houseincdec(n,explanationn):
#in ks4 higher unit 1
	import random
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		perc = random.randrange(2,10)
		year1 = random.randrange(1999,2016)
		year2 = year1 + 1
		prices = list(range(11,25))
		price1 = random.choice(prices)
		prices.remove(price1)
		price2 = random.choice(prices) * 10000
		price1 = price1 * 10000
		answerb = "\\pounds" + str(price2)
		price2 = int(price2 * ((100 + perc)/100))
		intro = "In Catville, luxury scratching post prices rose by " + str(perc) + "\% from " + str(year1) + " to " + str(year2) + "."
		questiona = "(a) On 1 January " + str(year1) + " a scratching post was priced at \\pounds" + str(price1) + ". \\\\ Calculate its price on 1 January " + str(year2) + "."
		questionb = "(b) On 1 January " + str(year2) + " another scratching post was priced at \\pounds" + str(price2) + ". \\\\ Calculate its price on 1 January " + str(year1) + "."
		question = intro + nl + questiona + nl + questionb
		answer = "(a) \\pounds" + str(int(price1 * ((100 + perc)/100))) + nl + answerb
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def bestbuy1(n,explanationn):
#in ks3 unit 2
	import random
	from fractions import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		quants = [3,4,5,6,7,8,9,10,11,12]
		nums = (3,3,3,3,3,3,4,4,4,4,5,5,5,5,5,5,6,6,7,7,7,7,7,8,8,9,9,10,11)
		dens = (4,5,7,8,10,11,5,7,9,11,6,7,8,9,11,12,7,11,8,9,10,11,12,9,11,10,11,11,12)
		choice = random.randrange(0,29)
		quanta = nums[choice]
		quantb = dens[choice]
		pricea = random.randrange(4,20) * 5
		priceb = pricea
		pricea = pricea * quanta/100
		priceb = (priceb * quantb + 10 * (-1)**random.randrange(1,3))/100
		total = int(quanta * quantb / gcd(quanta,quantb))
		pricea2 = pricea * quantb
		priceb2 = priceb * quanta
		if pricea%1==0:
			pricea = int(pricea)
		elif pricea*10%1==0:
			pricea = str(pricea) + "0"
		if priceb%1==0:
			priceb = int(priceb)
		elif priceb*10%1==0:
			priceb = str(priceb) + "0"
		annie = "Annie buys " + str(total) + " cat treats. \\\\ The treats are sold in packs of " + str(quanta) + ". Each pack costs \pounds" + str(pricea) + "."
		bill = "Bill also buys " + str(total) + " cat treats. \\\\ The treats are sold in packs of " + str(quantb) + ". Each pack costs \pounds" + str(priceb) + "."
		if pricea2>priceb2:
			answer1 = "Annie"
		else:
			answer1 = "Bill"
		difference = round(abs(pricea2 - priceb2),2)
		if difference%1==0:
			difference = int(difference)
		elif difference*10%1==0:
			difference = str(difference) + "0"
		question = "Who pays more for the cat treats? How much more?"
		question = annie + nl + bill + nl + question
		answer = answer1 + " by \pounds" + str(difference)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
