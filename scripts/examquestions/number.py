#!/usr/bin/env python3
#number.py

def trains(n,explanationn):
#in ks4 pre higher number paper
	import random
	from math import floor
	from math import gcd
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
	from utilities.rounding import rounddp
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
		incmult = rounddp((100 + inc)/100,2)
		decmult = rounddp((100 - dec)/100,2)
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
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		amount = rounddp(random.randrange(10,30) + random.randrange(1,10)/10 + random.randrange(1,10) / 100,2)
		cost = rounddp(random.randrange(3,10) + random.randrange(1,10)/10 + random.randrange(1,10) / 100,2)
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
	from utilities.rounding import rounddp
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
		change = rounddp(note - (collar + tray),2)
		if change%1==0:
			change = int(change)
		elif change*10%1==0:
			change = str(change) + "0"
#write question
		tempquestions.write(explanation + "Jack bought a cat collar costing \\pounds" + str(collar) + " and a litter tray for \\pounds" + str(tray) + ". how much change will he get from \\pounds" + str(note) + "?")

		tempquestions.write("\n")
#write answer
		tempquestions.write("\\pounds" + str(change))



def sftable1(n,explanationn):
#in ks3 unit 2
	import random
	from utilities.rounding import roundnearest,rounddp
	from utilities.sf import sftonum,sftosf
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
		a = rounddp((random.randrange(1,10)*10**t + random.randrange(1,10**t))/10**t,2)
		num1 = sftosf(str(a),i)
		answera = sftonum(str(a),i)


		t = random.randrange(1,3)
		a = rounddp((random.randrange(1,10)*10**t + random.randrange(1,10**t))/10**t,2)
		b2 = a * 10**i
		num2 = sftosf(str(a),i)

		t = random.randrange(1,3)
		a = rounddp((random.randrange(1,10)*10**t + random.randrange(1,10**t))/10**t,2)
		b1 = a * 10**i2
		num3 = sftosf(str(a),i2)

		t = random.randrange(1,3)
		a = rounddp((random.randrange(1,10)*10**t + random.randrange(1,10**t))/10**t,2)
		num4 = sftosf(str(a),i)

		estimator = random.randrange(2,10)*10
		answerc = roundnearest(a,1) * estimator
		answerc = sftosf(str(answerc),i)
		intro = "The table below shows the number of crates of cat food produced each day in some countries."
		questiona = "(a) How many crates per day were produced in " + c1 + "? \\\\ Give your answer as an ordinary number."
		questionb = "(b) How many more crates per day were produced in " + c3 + " than " + c2 + "?"
		answerb = "\\num{" + str(int(rounddp(b1 - b2,0))) + "}"
		questionc = "(c) The production of one crate of cat food per day is equivalent to approximately " + str(estimator) + " tonnes of cat food per year. Estimate the number of tonnes of cat food produced in " + c4 + " each year. Give your answer in standard form."
		order = [0,1,2,3]
		random.shuffle(order)
		countries = (c1,c2,c3,c4)
		nums = (num1,num2,num3,num4)
		table = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{6cm} | } \\hline Country & Cat Food Produced (crates per day) \\\\ \\specialrule{1pt}{0pt}{0pt} " + countries[order[0]] + " & " + nums[order[0]] + " \\\\ \\hline " + countries[order[1]] + "  & " + nums[order[1]] + " \\\\ \\hline " + countries[order[2]] + " & " + nums[order[2]] + " \\\\ \\hline " + countries[order[3]] + "  & " + nums[order[3]] + " \\\\ \\hline \\end{tabular}~"
		nl = " \\\\[0.3cm] "
		question = intro + nl + "\\begin{center}" + table + "\\end{center}" +  questiona + nl + questionb + nl + questionc 
		answer = "(a) " + answera + "\\hspace{2cm}(b) " + answerb + "\\hspace{2cm}(c) " + answerc
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)






def countersrelativefrequency(n,explanationn):
#in nov 2012 higher non calc
	from math import floor
	from utilities.rounding import rounddp
	from math import gcd
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
		table = "\\centering\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{| p{2cm} | p{2cm} | p{2cm} | p{2cm} | p{2cm} |} \\hline Colour & Red & Green & Yellow & Blue  \\\\ \\hline Frequency & " + str(red) + " & " + str(green) + " & " + str(yellow) + " & " + str(blue) + "\\\\ \\hline \\end{tabular}"
		questiona = "\\raggedright \\textbf{Estimate} the number of counters of each colour."
		question = intro + nl + table + nl + questiona 
		red = "Red: " + str(int(rounddp((red/freq)*counters,0)))
		green = "Green: " + str(int(rounddp((green/freq)*counters,0)))
		yellow = "Yellow: " + str(int(rounddp((yellow/freq)*counters,0)))
		blue = "Blue: " + str(int(rounddp((blue/freq)*counters,0)))
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



def fmpeq1(n,explanationn):
#in old fia4
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		intro = "Choose a word from the box below to complete each of the following sentences."
		box = "\\centering\\ovalbox{\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ p{2.5cm}  p{3cm}  p{2cm}}  factor & square root & prime  \\\\ cube & multiple & square\\\\  \\end{tabular}}"
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
		question = intro + nl + box + nl + "\\raggedright(a) " + questions[0] + nl + "(b) " + questions[1] + nl + "(c) " + questions[2] + nl + "(d) " + questions[3]
		answer = "(a) " + answers[0] + nl + "(b) " + answers[1] + nl + "(c) " + answers[2] + nl + "(d) " + answers[3]
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def conversiongraph(n,explanationn):
#in ks4 higher unit 2
	import random
	from utilities.rounding import rounddp
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
		dollars = roundto * (rounddp(dollars/roundto,0)+ (-1)**random.randrange(1,3))
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
		graph = "\\includegraphics[scale=0.11]{examquestions/images/pounddollars}"
		questiona = "Jess can buy a cat from America for " + dollars + " plus " + str(perc) + "\\% for delivery." + nl + "She can buy the same cat in the UK for " + pounds + " plus " + poundfrac + " of this price for delivery." + nl + "Work out which is cheaper"
		question = "\\begin{minipage}{0.42\\textwidth}" + intro + nl + questiona + "\\end{minipage} \\hfill \\begin{minipage}{0.53\\textwidth}" + graph + " \\end{minipage}"
		ukdollar = rounddp(apounds*er,2)
		if ukdollar%1==0:
			ukdollar = int(ukdollar)
		elif ukdollar*10%1==0:
			ukdollar = str(ukdollar) + "0"
		americapound = rounddp(adollars/er,2)
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
	from utilities.rounding import rounddp,rounddpstring
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
			difference = "\\pounds" + str("{0:.2f}".format(abs(rounddp(amount * (1+compound/100)**(years),2) - rounddp(amount * (1+year1/100) * (1+year2/100),2))))
			compresult = "\\pounds" + str("{0:.2f}".format(amount * (1+compound/100)**(years)))
			simpresult = "\\pounds" + str("{0:.2f}".format(amount * (1+year1/100) * (1+year2/100)))
			table = "\\centering\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ p{4cm} | p{4cm} } Account A & Account B \\\\ \\hline " + "Interest: " + str(compound) + "\% per year compound interest." + " & " + "Interest: " + str(year1) + "\% for the first year and " + str(year2) + "\% for the second year." + " \\\\ \\end{tabular}"
		else:
			year1 = random.randrange(compound-2,compound)
			year2 = random.randrange(compound-1,compound+2)
			year3 = random.randrange(compound+1,compound+3)
			compresult = rounddp(amount * (1+compound/100)**(years),2)
			simpresult = rounddp(amount * (1+year1/100) * (1+year2/100) * (1+year3/100),2)
			difference = abs(simpresult-compresult)
			compresult = "\pounds" + rounddpstring(compresult,2)
			simpresult = "\pounds" + rounddpstring(simpresult,2)
			difference = "\pounds" + rounddpstring(difference,2)
			table = "\\centering\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ p{4cm} | p{4cm} } Account A & Account B \\\\ \\hline " + "Interest: " + str(compound) + "\% per year compound interest." + " & " + "Interest: " + str(year1) + "\% for the first year, " + str(year2) + "\% for the second year and " + str(year3) + "\% for the third year." + " \\\\ \\end{tabular}"
		intro = "Here are the interest rates for two accounts."
		questiona = "\\raggedright A cat has \pounds" + str(amount) + " to invest." + nl + "Calculate which account would give him most money if he invests his money for " + str(years) + " years." + nl + "Give the difference in interest to the nearest penny."
		question = intro + nl + table + nl + questiona
		answer = "Account A: " + compresult + nl + "Account B: " + simpresult + nl + "Difference: " + difference
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def compoundvssimple2(n,explanationn):
	import random
	from math import ceil, floor
	from utilities.rounding import rounddp,rounddpstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		amount = random.randrange(1,41)*500
		years = random.randrange(3,16)
		compperc = random.randrange(3,10)
		simpperc = (((rounddp(compperc/100,2)+1)**years) * 100 - 100)/years
		simpperc = random.randrange(floor(simpperc),ceil(simpperc)+1)
		compresult = rounddp(amount * (1 + rounddp(compperc/100,2))**years,2)
		simpresult = rounddp(amount * rounddp(simpperc/100,2) * years + amount,2)
		difference = rounddpstring(abs(compresult - simpresult),2)
		compresult = rounddpstring(compresult,2)
		simpresult = rounddpstring(simpresult,2)
		table = "\\centering\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ p{4cm} | p{4cm} } Account A & Account B \\\\ \\hline " + "Interest: " + str(compperc) + "\% per year compound interest." + " & " + "Interest: " + str(simpperc) + "\% per year simple interest."  + " \\\\ \\end{tabular}"
		intro = "Here are the interest rates for two accounts."
		questiona = "\\raggedright You have \pounds" + str(amount) + " to invest for " + str(years) + " years. Which account gives you the most interest and by how much?"
		question = intro + nl + table + nl + questiona
		answer = "Account A: \pounds" + compresult + nl + "Account B: \pounds" + simpresult + nl + "Difference: \pounds" + difference
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def compoundvssimplestarter1(n,explanationn):
	import random
	from math import ceil, floor
	from utilities.rounding import rounddp,rounddpstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		amount = random.randrange(1,41)*500
		years = random.randrange(3,16)
		compperc = random.randrange(3,10)
		simpperc = (((rounddp(compperc/100,2)+1)**years) * 100 - 100)/years
		simpperc = random.randrange(floor(simpperc),ceil(simpperc)+1)
		compresult = rounddp(amount * (1 + rounddp(compperc/100,2))**years,2)
		simpresult = rounddp(amount * rounddp(simpperc/100,2) * years + amount,2)
		difference = rounddpstring(abs(compresult - simpresult),2)
		compresult = rounddpstring(compresult,2)
		simpresult = rounddpstring(simpresult,2)
		table = "\\centering \\cfbox{myfg}{\\begin{varwidth}{0.5\\textwidth}\\underline{Bank A} \\\\ " + str(compperc) + "\% per year compound interest \\end{varwidth}}" + "\\hspace{0.2cm}" + "\\cfbox{myfg}{\\begin{varwidth}{0.5\\textwidth}\\underline{Bank B} \\\\ " + str(simpperc) + "\% per year simple interest \\end{varwidth}}"
		intro = "You have \\pounds" + str(amount) + " to invest in one of these bank accounts:"
		questiona = "\\raggedright Which gives you the most interest after " + str(years) + " years? How much more?"
		question = intro + nl + table + nl + questiona
		answer = "Bank A: \pounds" + compresult + nl + "Bank B: \pounds" + simpresult + nl + "Difference: \pounds" + difference
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def compoundvssimplestarter2(n,explanationn):
	import random
	from math import ceil, floor
	from utilities.rounding import rounddp,rounddpstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		amount = random.randrange(1,41)*500
		years = random.randrange(3,16)
		compperc = rounddp(random.randrange(30,70)/10,1)
		if compperc%1==0:
			compperc = int(compperc)
		simpperc = (((rounddp(compperc/100,2)+1)**years) * 100 - 100)/years
		simpperc = rounddp(random.randrange(floor(simpperc)*10, (ceil(simpperc)+1)*10)/10,1)
		if simpperc%1==0:
			simpperc = int(simpperc)
		compresult = rounddp(amount * (1 + rounddp(compperc/100,5))**years,2)
		simpresult = rounddp(amount * rounddp(simpperc/100,5) * years + amount,2)
		difference = rounddpstring(abs(compresult - simpresult),2)
		compresult = rounddpstring(compresult,2)
		simpresult = rounddpstring(simpresult,2)
		table = "\\centering \\cfbox{myfg}{\\begin{varwidth}{0.5\\textwidth}\\underline{Bank A} \\\\ " + str(compperc) + "\% per year compound interest \\end{varwidth}}" + "\\hspace{0.2cm}" + "\\cfbox{myfg}{\\begin{varwidth}{0.5\\textwidth}\\underline{Bank B} \\\\ " + str(simpperc) + "\% per year simple interest \\end{varwidth}}"
		intro = "You have \\pounds" + str(amount) + " to invest in one of these bank accounts:"
		questiona = "\\raggedright Which gives you the most interest after " + str(years) + " years? How much more?"
		question = intro + nl + table + nl + questiona
		answer = "Bank A: \pounds" + compresult + nl + "Bank B: \pounds" + simpresult + nl + "Difference: \pounds" + difference
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def sfdiff(n,explanationn):
#in ks4 higher unit 1
	import random
	from utilities.rounding import rounddp
	from utilities.sf import sftosf,sftonum
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		year1 = random.randrange(1980,2000)
		year2 = year1 + random.randrange(5,15)
		num2 = random.randrange(1,10)
		num1 = rounddp(random.randrange(1,10) + random.randrange(1,10)/10,1)
		ind2 = random.randrange(5,13)
		ind1 = ind2 + 1
		answer = int(num1*10**ind1 - num2*10**ind2)

		num1 = sftosf(str(num1),ind1)
		num2 = sftosf(str(num2),ind2)
		answer = sftosf(str(answer),0)


		intro = "The UK's Gross Domestic Product (GDP) in " + str(year1) + " was \\pounds" + num2 + " and in " + str(year2) + " it was \\pounds" + num1 + "."
		inst1 = "Work out the increase in GDP between " + str(year1) + " and " + str(year2) + "."
		inst2 = "Write your answer in standard form."
		question = intro + nl + inst1 + nl + inst2
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def sfdivprofit(n,explanationn):
#in ks4 higher unit 1
	import random
	from utilities.sf import sftosf,sftonum
	from utilities.rounding import rounddp
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		num2 = random.randrange(2,10)
		if num2==2 or num2==5 or num2==4:
			num1 = rounddp(random.randrange(0,10)/10 + random.randrange(1,10),1)
			num3 = rounddp(num1/num2,3)
		elif num2==6:
			num1 = rounddp(random.randrange(1,33) * 0.3,1)
			num3 = rounddp(num1/num2,3)
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
		ind3 = ind1 - ind2
		if num1%1==0:
			num1 = int(num1)
		profit = sftosf(str(num1),ind1)
		employees = sftosf(str(num2),ind2)
		answer = rounddp(num3*10**ind3,2)
		if answer%1==0:
			answer = int(answer)
		elif (answer*10)%1==0:
			answer = str(answer) + "0"
		answer = "\\pounds" + str(answer)
		nl = " \\\\[0.3cm] "
		intro = "Cat Hats Ltd. share their profit equally amongst their employees."
		intro2 = "One year, their profit was \\pounds" + profit + " and they had " + employees + " employees."
		questiona = "Work out how much each employee got that year."
		question = intro + nl + intro2 + nl + questiona
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def sfdouble(n,explanationn):
#in ks4 higher unit 1
	import random
	from utilities.rounding import rounddp
	from utilities.sf import sftosf
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		num1 = 2
		num2 = rounddp(random.randrange(5,10) + random.randrange(1,10)/10,1)
		num3 = rounddp(num1 * num2,1)
		ind2 = random.randrange(2,10)
		ind3 = ind2
		num2 = sftosf(str(num2),ind2)
		if num3>=10:
			num3 = rounddp(num3/10,2)
			ind3 = ind3 + 1
		intro = "Last year, Cat Hats Ltd. made a profit of \\pounds" + num2 + "."
		intro2 = "This year, their profit was double that of last year."
		questiona = "Work out their profit for this year."
		intro3 = "Write your answer in standard form."
		question = intro + nl + intro2 + nl + questiona + nl + intro3
		answer = "\\pounds" + sftosf(str(num3),ind3)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def carvaluedrop(n,explanationn):
#in ks4 higher unit 1
	import random
	from utilities.rounding import rounddp
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
		intro2 = "\\raggedright where $t$ is the age of the statue in complete years."
		questiona = "(a) Write down the value of V when t = 0."
		questionb = "(b) What is the value of V when t = " + str(t) + "?"
		questionc = "(c) After how many years will the statue's value drop below \\pounds" + str(v2) + "?"
		question = intro + nl + "\\centering" + formula + nl + intro2 + nl + questiona + nl + questionb + nl + questionc
		answera = "(a) \\pounds" + str(v)
		answerb = rounddp(v * decimal ** t,2)
		if answerb%1==0:
			answerb = int(answerb)
		elif (answerb*10)%1==0:
			answerb = str(answerb) + "0"
		answerb = "(b) \\pounds" + str(answerb)
		while v>v2:
			v = v*decimal
			years = years + 1
		answerc = "(c) " + str(years)
		answer = answera + nl + answerb + nl + answerc
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def expochangeformula1(n,explanationn):
#in ks4 higher unit 1
	import random
	from utilities.rounding import rounddp
	from math import floor,ceil
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0cm] "
		v = random.randrange(8,30)*1000
		answerrealb = random.randrange(3,16)
		decimal = rounddp((100-answerrealb)/100,2)
		v2 = int(v/2)
		t = random.randrange(2,5)
		years = 0
		intro = "The population, P, of a city after t years is given by the formula:"
		formula = "$P = " + str(v) + "\\times" + str(decimal) + "^{t}$"
		questiona = "\\raggedright a) What was the original population?"
		questionb = "b) By what percentage does it decrease each year?"
		questionc = "c) What is P after " + str(t) + " years?"
		questiond = "d) After how many years will the population first fall below " + str(v2) + "?"
		question = intro + nl + "\\centering" + formula + nl + questiona + nl + questionb + nl + questionc + nl + questiond
		answera = "a) " + str(v)
		answerb = rounddp(v * decimal ** t,2)
		if answerb%1==0:
			answerb = str(int(answerb))
		else:
			answerb = str(floor(answerb)) + " or " + str(ceil(answerb))
		answerb = "c) " + str(answerb)
		while v>v2:
			v = v*decimal
			years = years + 1
		answerc = "d) " + str(years)
		answer = answera + nl + "b) " + str(answerrealb) + "\%" + nl + answerb + nl + answerc
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def expochangeformula2(n,explanationn):
#in ks4 higher unit 1
	import random
	from utilities.rounding import rounddp
	from math import floor
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0cm] "
		v = random.randrange(8,30)*1000
		answerrealb = random.randrange(3,16)
		decimal = rounddp((100+answerrealb)/100,2)
		v2 = int(v/2) + v
		t = random.randrange(2,5)
		years = 0
		intro = "The value, \\pounds V, of an investment after t years is given by the formula:"
		formula = "$V = " + str(v) + "\\times" + str(decimal) + "^{t}$"
		questiona = "\\raggedright a) How much money was invested?"
		questionb = "b) What is the interest rate?"
		questionc = "c) What is the value of the investment after " + str(t) + " years?"
		questiond = "d) After how many years will V first be above \\pounds" + str(v2) + "?"
		question = intro + nl + "\\centering" + formula + nl + questiona + nl + questionb + nl + questionc + nl + questiond
		answera = "a) \\pounds" + str(v)
		answerb = rounddp(v * decimal ** t,2)
		if answerb%1==0:
			answerb = int(answerb)
		elif (answerb*10)%1==0:
			answerb = str(answerb) + "0"
		answerb = "c) \\pounds" + str(answerb)
		while v<v2:
			v = v*decimal
			years = years + 1
		answerc = "d) " + str(years)
		answer = answera + nl + "b) " + str(answerrealb) + "\%" + nl + answerb + nl + answerc
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
		answer = "(a) \\pounds" + str(int(price1 * ((100 + perc)/100))) + nl + "(b) " + answerb
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def bestbuy1(n,explanationn):
#in ks3 unit 2
	import random
	from utilities.rounding import rounddp
	from math import gcd
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
		difference = rounddp(abs(pricea2 - priceb2),2)
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




def bestbuy2(n,explanationn):
#in intermediate unit 2
	import random
	from utilities.rounding import rounddpstring
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		days = 40
		fractions = [2,3,4]
		fractionwords = ["half","a third of","a quarter of"]
		dec = random.randrange(0,3)
		fraction = fractionwords[dec]
		fractionvalue = 1/fractions[dec]
		mult = random.randrange(3,9)
		m1 = random.randrange(3,9)
		m2 = m1*mult
		p1 = random.randrange(4,10)
		p2 = p1*mult + random.randrange(1,4)*(-1)**random.randrange(1,3)
		if random.randrange(0,2)==0:
			temp = m1
			m1 = m2
			m2 = temp
			temp = p1
			p1 = p2
			p2 = temp
		days = m2*random.randrange(2,5)
		intro = "Jane's cats eat " + fraction + " a kilogram of cat food in total each day. \\\\ Cat food is sold in two different size bags."
		point1 = "\\item " + str(m1) + "kg for \\pounds" + str(p1)
		point2 = "\\item " + str(m2) + "kg for \\pounds" + str(p2)
		question = "Work out the cheapest cost for Jane to feed her cats for " + str(days) + " days.\\\\You must show how you decide."
		question = intro + "\\vspace{-0.0\\topsep}\\begin{itemize}\setlength{\itemsep}{0pt}" + point1 + point2 + "\\end{itemize}\\vspace{-0.5\\topsep}" + question
		if p1/m1<p2/m2:
			answer = ((days*fractionvalue)/m1)*p1
		else:
			answer = ((days*fractionvalue)/m2)*p2
		if answer%1==0:
			answer = str(int(answer))
		else:
			answer = rounddpstring(answer,2)
		answer = "\\pounds" + answer
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def percgate(n,explanationn):
#in ks3 unit 7
	import random
	from math import ceil,floor
	from utilities.rounding import rounddpstring,rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		wooden = random.randrange(5,31)*10
		if random.randrange(0,2)==1:
			plastic = ceil((wooden/1.2) + random.randrange(1,4))
			cheaper = "wooden"
		else:
			plastic = floor((wooden/1.2) - random.randrange(1,4))
			cheaper = "plastic"
		difference = rounddp(abs(wooden - (plastic*1.2)),2)
		if difference%1==0:
			difference = int(difference)
		else:
			difference = rounddpstring(difference,2)
		intro = "A cat wants to buy a cat flap.\\\\"
		point1 = "\\item A wooden cat flap costs \\pounds" + str(wooden) + " including VAT.\\\\"
		point2 = "\\item A plastic cat flap costs \\pounds" + str(plastic) + " excluding VAT.\\\\"
		point3 = "The rate of VAT is 20\%."
		questiona = "Which cat flap is cheaper and by how much?"
		question = intro + "\\vspace{-0.5\\topsep}\\begin{itemize}\setlength{\itemsep}{0pt}" + point1 + point2 + "\\end{itemize}\\vspace{-0.5\\topsep}" +  point3 + nl + questiona
		answer = cheaper + " by \\pounds" + str(difference)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def densityalloy(n,explanationn):
#in ks3 unit 7
	import random
	from math import ceil,floor
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		densities = [3,4,5,6,7,8,9,10,11,12,13,14,15]
		pd = random.choice(densities)
		densities.remove(pd)
		ad = random.choice(densities)
		pv = random.randrange(11,26)
		pm = pd * pv
		av = random.randrange(11,26)
		am = ad * av
		intro = str(pm) + " g of purrium is mixed with " + str(am) + " g of alumeownium to make an alloy."
		d1 = "The density of purrium is " + str(pd) + " g/cm$^{3}$"
		d2 = "The density of alumeownium is " + str(ad) + " g/cm$^{3}$"
		questiona = "(a) Work out the volume of purrium used in the alloy."
		questionb = "(b) What is the density of the alloy?"
		alloy = (pm + am) / (pv + av)
		if alloy%1==0:
			alloy = int(alloy)
		else:
			alloy = rounddp(alloy,3)
		question = intro + nl + d1 + "\\\\" + d2 + nl + questiona + nl + questionb
		answer = "(a) "+ str(pv) + " cm$^{3}$" + nl + "(b) " + str(alloy) + " g/cm$^{3}$"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def densityalloystarter(n,explanationn):
#in ks3 unit 7
	import random
	from math import ceil,floor
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		densities = [3,4,5,6,7,8,9,10,11,12,13,14,15]
		pd = random.choice(densities)
		densities.remove(pd)
		ad = random.choice(densities)
		pv = random.randrange(11,26)
		pm = pd * pv
		av = random.randrange(11,26)
		am = ad * av
		intro = str(pm) + "g of purrium is mixed with " + str(am) + "g of alumeownium to make an alloy."
		d1 = "The density of purrium is " + str(pd) + "g/cm$^{3}$"
		d2 = "The density of alumeownium is " + str(ad) + "g/cm$^{3}$"
		questionb = "What is the density of the alloy?"
		alloy = (pm + am) / (pv + av)
		if alloy%1==0:
			alloy = int(alloy)
		else:
			alloy = rounddp(alloy,3)
		question = intro + nl + d1 + "\\\\" + d2 + nl + questionb
		answer = str(alloy) + " g/cm$^{3}$"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)





def twospeedsstarter(n,explanationn):
#in ks3 unit 7
	import random
	from math import ceil,floor
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.2cm] "
		speeds = [50,55,60,65,70,75,80]
		s1 = random.choice(speeds)
		s2 = s1 + random.randrange(3,7)*5
		times = list(range(2,11))
		t1 = random.choice(times)
		t2 = random.choice(times)
		d1 = s1*t1
		d2 = s2*t2
		intro = "A cat drives for " + str(d1) + "km on normal roads and " + str(d2) + "km on motorways."
		l1 = "She drives at an average speed of " + str(s1) + "km/h on normal roads"
		l2 = "She drives at an average speed of " + str(s2) + "km/h on motorways"
		questionb = "What was her average speed for the whole journey?"
		speed = (d1 + d2) / (t1 + t2)
		if speed%1==0:
			speed = int(speed)
		else:
			speed = rounddp(speed,3)
		question = intro + nl + l1 + "\\\\[0.1cm]" + l2 + nl + questionb
		answer = str(speed) + " km/h"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def ratiosupermarket(n,explanationn):
#in ks3 unit 7
	import random
	from math import ceil,floor
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		base = random.randrange(2,6)*10
		scalers1 = [2,2,2,3,3,3,4,4,5,5,6]
		scalers2 = [3,5,7,4,5,7,5,7,6,7,7]
		scaler = random.randrange(0,len(scalers1))
		total1 = base * scalers1[scaler]
		total2 = base * scalers2[scaler]
		if random.randrange(0,2)==1:
			temp = total1
			total1 = total2
			total2 = temp
		totals = [5,5,5]
		for i in range(0,total2-15):
			choice = random.randrange(0,3)
			totals[choice] = totals[choice] + 1
		for i in range(0,3):
			totals[i] = totals[i]*10
		total1 = total1 * 10
		total2 = total2 * 10
		intro = "A supermarket gives \\pounds" + str(total1) + " every month to local charities. The amount given to each charity is in proportion to the number of votes given by customers."
		intro2 = "In October there were " + str(total2) + " votes altogether, given as follows:"
		point1 = "\\item Cat's charity - " + str(totals[0]) + " votes\\\\"
		point2 = "\\item Dogs' charity - " + str(totals[1]) + " votes\\\\"
		point3 = "\\item Children's charity - " + str(totals[2]) + " votes"
		questiona = "How much did each of these charities receive in October?"
		multiplier = total1/total2
		question = intro + nl + intro2 + "\\begin{itemize}" + point1 + point2 + point3 + "\\end{itemize}" + questiona
		for i in range(0,3):
			totals[i] = int(totals[i] * multiplier)
		answer = "Cats: \\pounds" + str(totals[0]) + "\\hspace{1cm} Dogs: \\pounds" + str(totals[1]) + "\\hspace{1cm} Children: \\pounds" + str(totals[2])
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def discount1(n,explanationn):
#in ks3 unit 7
	import random
	from math import ceil,floor
	from utilities.rounding import rounddp,rounddpstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		daily = random.randrange(5,13)
		intro = "River Cattery charge \\pounds" + str(daily) + " per day for each cat."
		discounted = daily - rounddp(random.randrange(1,6)/2,1)
		if discounted%1==0:
			discountword = str(int(discounted))
		else:
			discountword = rounddpstring(discounted,2)
		line2 = "The cost is reduced to \\pounds" + discountword + " if the owners take food for their cats."
		discount = random.randrange(1,6)*5
		line3 = "There is a " + str(discount) + "\\% discount off the bill for 2 or more cats."
		if random.randrange(0,10)==1:
			cats = 1
		else:
			cats = random.randrange(2,6)
		if cats==1:
			catword = " cat "
			discounter = 1
			dayword = "its"
		else:
			catword = str(cats) + " cats "
			discounter = 1 - discount/100
			dayword = "their"
		days = random.randrange(10,26)
		dec = random.randrange(0,2)
		if dec==1:
			dayword = " days and takes " + dayword + " food."
			cost = discounted
		else:
			dayword = " days but does not take " + dayword + " food."
			cost = daily
		line4 = "Rudy books her " + catword + "into the cattery for " + str(days) + dayword
		question = "How much does she pay altogether?"
		questiona = "(a) " + intro + nl + line2 + nl + line3 + nl + line4 + nl + question
		nums = (1,2,1,2,3,1,3,2,3,4,1,5,4,3,5,2,7,5,3,7,4,5,6,7,8,9)
		dens = (5,9,4,7,10,3,8,5,7,9,2,9,7,5,8,3,10,7,4,9,5,6,7,8,9,10)
		dec = random.randrange(0,len(nums))
		num = nums[dec]
		den = dens[dec]
		questionb = "(b) Rudy's " + str(cats) + " cats each eat $\\dfrac{" + str(num) + "}{" + str(den) + "}$ of a tin of cat food each day." + nl + "What is the least number of tins that Rudy needs to take for " + str(days) + " days?"
		answer = cost * discounter * cats * days
		if answer%1==0:
			answer = str(int(answer))
		else:
			answer = rounddpstring(answer,2)
		answerb = ceil((num/den) * cats * days)
		answer = "(a) \\pounds" + answer + nl + "(b) " + str(answerb)
#write question
		tempquestions.write(questiona + "\\\\[1cm]" + questionb)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def flatshare(n,explanationn):
#in ks3 unit 7
	import random
	from math import ceil,floor
	from utilities.rounding import rounddp,rounddpstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		intro = "Clawdia, Jennifurr and Tabbytha share a flat."
		perc = random.randrange(1,10)*5
		dens = [2,4,5,10]
		den = random.choice(dens)
		answer = random.randrange(3,31) * 100
		tab = int(answer - (answer * (perc/100) + answer * (1/den)))
		point1 = "\\item Clawdia pays " + str(perc) + "\\% of the rent"
		point2 = "\\item Jenifurr pays $\\dfrac{1}{" + str(den) + "}$ of the rent"
		point3 = "\\item Tabbytha pays \\pounds" + str(tab)
		questiona = "How much do they pay altogether for the rent?"
		question = intro + "\\begin{itemize}" + point1 + point2 + point3 + "\\end{itemize}" + questiona
		
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write("\\pounds" + str(answer))


def sdteq1(n,explanationn):
#in ks4 higher 4
	import random
	from fractions import Fraction
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.01cm] "
		nums = [1,1,1,2,3]
		dens = [2,3,4,3,4]
		dec = random.randrange(0,len(nums))
		motorwayt = random.randrange(2,6)
		motorways = random.randrange(50,76)
		motorwayd = motorwayt * motorways
		a = random.randrange(1,4)
		b = Fraction(nums[dec],dens[dec])
		hours = str(a + motorwayt) + "$\\dfrac{" + str(nums[dec]) + "}{" + str(dens[dec]) + "}$"
		ordinaryt = a + b
		mults = [5,10,12,15,18]
		ordinarys = dens[dec] * random.choice(mults)
		ordinaryd = ordinarys * ordinaryt
		miles = motorwayd + ordinaryd
		intro = "A cat drives " + str(miles) + " miles."
		line2 = "She drives " + str(ordinaryd) + " miles on ordinary roads and the rest on a motorway."
		line3 = "The journey takes " + str(hours) + " hours."
		line4 = "She drives at an average speed of " + str(ordinarys) + " mph on ordinary roads."
		line5 = "Work out her average speed on the motorway."
		question = intro + nl + line2 + nl + line3 + nl + line4 + nl + line5
		answer = str(motorways) + " mph"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def ratiopaint1(n,explanationn):
#in ks4 intermediate 6
	import random
	from fractions import Fraction
	from math import gcd
	from utilities.rounding import roundnearest,rounddpstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.1cm] "
		choices = [1,2,3,4,5]
		left = random.choice(choices)
		choices.remove(left)
		right = random.choice(choices)
		hcf = gcd(left,right)
		left = int(left/hcf)
		right = int(right/hcf)
		scaler = random.randrange(2,6)
		quant = (left+right)*scaler
		scaler2choices = [2,3,4,5]
		sc1 = random.choice(scaler2choices)
		scaler2choices.remove(sc1)
		sc2 = random.choice(scaler2choices)
		red = quant * sc1
		white = quant * sc2
		base = (red/(quant/(scaler*left))) + (white/(quant/(scaler*right)))
		price = roundnearest(base+5,10)
		profit = price - base
		if profit%1==0:
			profit = str(int(profit))
		else:
			profit = rounddpstring(profit,2)
		intro = "Picatso makes pink paint by mixing red and white paint in the ratio " + str(left) + " : " + str(right) + "."
		line2 = "Red paint costs \\pounds" + str(red) + " per " + str(quant) + " litres."
		line3 = "White paint costs \\pounds" + str(white) + " per " + str(quant) + " litres."
		line4 = "Picatso sells his " + str(quant) + "-litre tins for \\pounds" + str(price) + " each."
		line5 = "Calculate how much profit he makes for each tin he sells."
		question = intro + nl + line2 + nl + line3 + nl + line4 + nl + line5
		answer = "\\pounds" + profit


#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def ratiopaint2(n,explanationn):
#in ks4 intermediate 6
	import random
	from fractions import Fraction
	from math import gcd
	from utilities.rounding import roundnearest,rounddpstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.1cm] "
		choices = [1,2,3,4,5]
		left = random.choice(choices)
		choices.remove(left)
		right = random.choice(choices)
		hcf = gcd(left,right)
		left = int(left/hcf)
		right = int(right/hcf)
		scaler = random.randrange(2,6)
		quant = (left+right)*scaler
		scaler2choices = [2,3,4,5]
		sc1 = random.choice(scaler2choices)
		scaler2choices.remove(sc1)
		sc2 = random.choice(scaler2choices)
		quant1 = random.randrange(4,13)
		quant2 = random.randrange(4,13)
		red = quant1 * sc1
		white = quant2 * sc2
		base = (red/(quant1/(scaler*left))) + (white/(quant2/(scaler*right)))
		price = roundnearest(base+5,10)
		profit = price - base
		if profit%1==0:
			profit = str(int(profit))
		else:
			profit = rounddpstring(profit,2)
		intro = "Picatso makes pink paint by mixing red and white paint in the ratio " + str(left) + " : " + str(right) + "."
		line2 = "Red paint costs \\pounds" + str(red) + " per " + str(quant1) + " litres."
		line3 = "White paint costs \\pounds" + str(white) + " per " + str(quant2) + " litres."
		line4 = "Picatso sells his " + str(quant) + "-litre tins for \\pounds" + str(price) + " each."
		line5 = "Calculate how much profit he makes for each tin he sells."
		question = intro + nl + line2 + nl + line3 + nl + line4 + nl + line5
		answer = "\\pounds" + profit


#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def rateofpay(n,explanationn):
#in ks4 intermediate 6
	import random
	from utilities.rounding import rounddpstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.1cm] "
		h = (random.randrange(30,61) * 20)/100
		scalers = [1.2,1.25,1.5,1.75]
		overs = [random.randrange(1,3)*5,random.randrange(1,3)*4,random.randrange(1,6)*2,random.randrange(1,3)*4]
		dec = random.randrange(0,len(scalers))
		scaler = scalers[dec]
		over = overs[dec]
		normal = random.randrange(3,8)*10 - scaler*over
		if normal%1==0:
			normal = int(normal)
		pay = normal*h + over*scaler*h
		pay = str(int(pay))
		l1 = "Purrcy works for " + str(normal) + " hours from Monday to Friday at his normal rate of pay."
		l2 = "On Saturdays he gets an overtime rate of pay."
		l3 = "The overtime rate is " + str(scaler) + " times his normal rate."
		l4 = "He works for " + str(over) + " hours on a Saturday."
		l5 = "Altogether Purrcy earns \\pounds" + pay + " for his week's work."
		l6 = "What is his normal rate of pay per hour?"
		if h%1==0:
			h = str(int(h))
		else:
			h = rounddpstring(h,2)
		question = l1 + nl + l2 + nl + l3 + nl + l4 + nl + l5 + nl + l6
		answer = "\\pounds" + h
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def sftable2(n,explanationn):
#in ks3 unit 2
	import random
	from utilities.rounding import roundnearest,rounddp,rounddpstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		y1 = random.randrange(2000,2006)
		y2 = y1 + 5
		y3 = y2 + 5
		y1 = str(y1)
		y2 = str(y2)
		y3 = str(y3)

		p1 = random.randrange(200,800)
		p2 = p1 + random.randrange(20,80)
		p3 = p2 + random.randrange(20,80)
		p1 = rounddp(p1/100,2)
		p2 = rounddp(p2/100,2)
		p3 = rounddp(p3/100,2)
		i1 = random.randrange(5,9)

		s1 = random.randrange(5,10)*100 + random.randrange(1,100)
		s2 = random.randrange(100,400)
		s3 = s2 + random.randrange(90,200)
		s1 = rounddp(s1/100,2)
		s2 = rounddp(s2/100,2)
		s3 = rounddp(s3/100,2)
		i2 = random.randrange(8,12)
		i3 = i2 + 1

		a1 = "\\pounds\\num{" + str(int((s2*10**i3 - s1*10**i2)/1000000)) + "} million"


		pp1 = "\\num{" + rounddpstring((s1*10**i2) / (p1*10**i1),2) + "}"
		pp2 = "\\num{" + rounddpstring((s2*10**i3) / (p2*10**i1),2) + "}"
		pp3 = "\\num{" + rounddpstring((s3*10**i3) / (p3*10**i1),2) + "}"
		a2 = y1 + " - \\pounds" + pp1 + "\\\\" +  y2 + " - \\pounds" + pp2 + "\\\\" +  y3 + " - \\pounds" + pp3 + "\\\\"


		p1 = "$" + str(p1) + "\\times 10^"+ str(i1) + "$"
		p2 = "$" + str(p2) + "\\times 10^"+ str(i1) + "$"
		p3 = "$" + str(p3) + "\\times 10^"+ str(i1) + "$"
		s1 = "$" + str(s1) + "\\times 10^{"+ str(i2) + "}$"
		s2 = "$" + str(s2) + "\\times 10^{"+ str(i3) + "}$"
		s3 = "$" + str(s3) + "\\times 10^{"+ str(i3) + "}$"
		table = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{2cm} | p{2cm} | p{4cm} | } \\hline Year & Population & Total spent on cats (\\pounds) \\\\ \\specialrule{1pt}{0pt}{0pt} " + y1 + " & " + p1 + " & " + s1 + " \\\\ \\hline " + y2 + " & " + p2 + " & " + s2 + " \\\\ \\hline " + y3 + " & " + p3 + " & " + s3 +  "\\\\ \\hline \\end{tabular}~"

		nl = " \\\\[0.3cm] "
		intro = "The table shows data for the UK about its population and the total amount of money spent on cats in " + y1 + ", " + y2 + " and " + y3 + "."
		questiona = "(a) How much more was spent on cats in " + y2 + " than in " + y1 + "?" + nl + "Give your answer in millions of pounds."
		questionb = "(b) Calculate the amount spent on cats \\textbf{per person} in the UK for each year."
		question = intro + nl + "\\begin{center}" + table + "\\end{center}" +  questiona + nl + questionb
		answer = "(a) " + a1 + nl + "(b)\\\\" + a2
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def ratiopopulation(n,explanationn):
#in 2017 paper
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
		l1 = "The population of a village is in the following ratios."
		point1 = "\\item cats : humans = " + str(c1) + " : " + str(h1) + "\\\\"
		point2 = "\\item dogs : humans = " + str(d1) + " : " + str(h2) + "\\\\"
		questiona = "(a) Find the ratio cats : dogs.\\\\ Give your answer in its simplest form."
		questionb = "(b) There are " + str(humans) + " humans in the village.\\\\ Find the total population of the village."
		question = l1 + "\\vspace{-0.3\\topsep}\\begin{itemize}\setlength{\itemsep}{0pt}" + point1 + point2 + "\\end{itemize}\\vspace{-0.3\\topsep}" + questiona + nl + questionb
		hcf = gcd(c1*h2,d1*h1)
		answer = "(a) " + str(int((c1*h2)/hcf)) + " : " + str(int((d1*h1)/hcf)) + "\\hspace{1cm} (b) " + str(int(humans + (c1*humans/h1) + (d1*humans/h2)))
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def ricecakeproportion(n,explanationn):
#in higher unit 5
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.1cm] "
		rc = random.randrange(11,20)
		mult = random.randrange(11,20)/10
		grams = int(100 * mult)
		cal = random.randrange(250,500)
		answer = rounddp((cal*grams)/(rc*100),2)
		if answer%1==0:
			answer = int(answer)
		question = str(rc) + " cat biscuits weigh a total of " + str(grams) + "g. There are " + str(cal) + " calories in 100g of cat biscuits. How many calories are there in one cat biscuit?"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def chocsquareratio(n,explanationn):
#in higher unit 5
	import random
	from math import gcd
	from utilities.rounding import rounddp,rounddpstring,roundnearest
	from math import ceil
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.1cm] "
		total = random.randrange(2,13)
		ingred = [2,2,2]
		for i in range(0,total):
			dec = random.randrange(0,3)
			ingred[dec] = ingred[dec] + 1
		choc = ingred[0]
		pb = ingred[1]
		rice = ingred[2]
		mults = [4,5,6,8,9]	
		multiplier = random.choice(mults)
		choc2 = choc * multiplier
		pb2 = pb * multiplier
		rice2 = rice * multiplier
		chocfactors = []
		pbfactors = []
		ricefactors = []
		for i in range (2,ceil(choc2/2)):
			if choc2%i==0:
				chocfactors.append(i)
		for i in range (2,ceil(pb2/2)):
			if pb2%i==0:
				pbfactors.append(i)
		for i in range (2,ceil(rice2/2)):
			if rice2%i==0:
				ricefactors.append(i)
		chocweight = random.choice(chocfactors)
		pbweight = random.choice(pbfactors)
		riceweight = random.choice(ricefactors)
		choc = choc*50
		pb = pb*50
		rice = rice*50
		chocweight = chocweight * 50
		pbweight = pbweight*50
		riceweight = riceweight*50
		mix1 = choc + pb + rice
		hcf = gcd(gcd(choc,pb),rice)
		ratio = str(int(choc/hcf)) + " : " + str(int(pb/hcf)) + " : " + str(int(rice/hcf))
		mix2 = mix1 * multiplier / 1000
		if mix2%1==0:
			mix2 = int(mix2)
		chocprice = random.randrange(10,30)/10
		pbprice = random.randrange(10,30)/10
		riceprice = random.randrange(10,30)/10
		charge = random.randrange(4,10) * 10
		cost = ((choc*multiplier)/chocweight)*chocprice + ((pb*multiplier)/pbweight)*pbprice + ((rice*multiplier)/riceweight)*riceprice
		squares = roundnearest(ceil(cost/(charge/100))+5,10)
		profit = rounddp((charge*squares)/100 - (((choc*multiplier)/chocweight)*chocprice + ((pb*multiplier)/pbweight)*pbprice + ((rice*multiplier)/riceweight)*riceprice),2)
		if profit%1==0:
			profit = int(profit)
		else:
			profit = rounddpstring(profit,2)
		if chocprice%1==0:
			chocprice = int(chocprice)
		else:
			chocprice = rounddpstring(chocprice,2)
		if pbprice%1==0:
			pbprice = int(pbprice)
		else:
			pbprice = rounddpstring(pbprice,2)
		if riceprice%1==0:
			riceprice = int(riceprice)
		else:
			riceprice = rounddpstring(riceprice,2)
		line1 = "Lauren is going to make cat cakes to sell."
		line2 = "There are just three ingredients: tuna, catnip and filet mignon, mixed in the ratio " + ratio + " respectively."
		line3 = "(a) How much of each ingredient will she need to make " + str(mix1) + "g of the mixture?"
		line4 = " \\\\[1cm] "
		line5 = "(b) A tin of tuna weighs " + str(chocweight) + "g and costs \\pounds" + str(chocprice) + "."
		line6 = "A jar of catnip contains " + str(pbweight) + "g and costs \\pounds" + str(pbprice) + "."
		line7 = "A packet of filet mignon contains " + str(riceweight) + "g and costs \\pounds" + str(riceprice) + "."
		line8 = "Lauren makes " + str(mix2) + "kg of mixture, from which she can cut " + str(squares) + " cat cakes."
		line9 = "She charges " + str(charge) + "p for each cake and sells " + str(squares) + " cakes."
		line10 = "How much \\textbf{profit} does she make?" 
		question = line1 + nl + line2 + nl + line3 + line4 + line5 + nl + line6 + nl + line7 + nl + line8 + nl + line9 + nl + line10
		answer = "(a) tuna " + str(choc) + "g, catnip " + str(pb) + "g and filet mignon " + str(rice) + "g" + nl + "(b) \\pounds" + str(profit)
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def indicesmixedbase(n,explanationn):
#in higher unit 6
	import random
	from math import log
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Work out the value of k given "
		else:
			explanation = ""
		nl = " \\\\[0.1cm] "
		xs = [2,2,4,3]
		ys = [2,8,8,9]
		dec = random.randrange(0,len(xs))
		x = xs[dec]
		y = ys[dec]
		i1 = random.randrange(2,10) * (-1)**random.randrange(1,3)
		i2 = random.randrange(2,10) * (-1)**random.randrange(1,3)
		if x==3:
			i3 = i1 * log(x,3) + i2 * log(y,3)
			base = 3
		else:
			i3 = i1 * log(x,2) + i2 * log(y,2)
			base = 2
		if random.randrange(1,3)==2:
			temp = x
			x = y
			y = temp
			temp = i1
			i1 = i2
			i2 = temp
		if base==2:
			question = explanation + "\\mbox{$" + str(x) + "^{" + str(i1) + "} \\times " + str(y) + "^{" + str(i2) + "} = 2^{k}$}"
		else:
			question = explanation + "\\mbox{$" + str(x) + "^{" + str(i1) + "} \\times " + str(y) + "^{" + str(i2) + "} = 3^{k}$}"
		answer = str(int(i3))
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def differencesquareareas(n,explanationn):
#in higher unit 6
	import random
	from math import log
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "The lengths of the sides of two squares are integers, when measured in cm. "
		else:
			explanation = ""
		sides = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
		side1 = random.choice(sides)
		sides.remove(side1)
		side2 = random.choice(sides)
		diff = abs(side1**2 - side2**2)
		question = explanation + "The difference between the areas of two squares is " + str(diff) + "cm$^{2}$. Find the lengths of the sides of the two squares."
		answer = str(side1) + "cm and " + str(side2) + "cm"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def findrepeatpercentage(n,explanationn):
#in higher unit 7
	import random
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "The lengths of the sides of two squares are integers, when measured in cm. "
		else:
			explanation = ""
		months = ["December","January","February","March","April","May","June","July","August","September","October","November","December","January"]
		m1 = random.randrange(0,12)
		m2 = m1 + 1
		m3 = m2 + 1
		m1 = months[m1]
		m2 = months[m2]
		m3 = months[m3]
		amount = random.randrange(2,10)*200
		percs1 = [10,20,30,40]
		percs2 = [5,15,25,35,10,20,30,40]
		p1 = random.choice(percs1)
		p2 = random.choice(percs2)
		if random.randrange(0,2)==1:
			temp = p1
			p1 = p2
			p2 = temp
		l1 = "Lottie sells cats."
		l2 = "In " + m1 + " she sells " + str(amount) + " cats."
		if random.randrange(0,2)==0:
			l3 = "In " + m2 + " Lottie sold " + str(p1) + "\% more cats than in " + m1 + "."
			l4 = "In " + m3 + " Lottie sold " + str(p2) + "\% fewer cats than in " + m2 + "."
			answer = (100 + p1) * (100 - p2) * 0.01 - 100
		else:
			l3 = "In " + m2 + " Lottie sold " + str(p1) + "\% fewer cats than in " + m1 + "."
			l4 = "In " + m3 + " Lottie sold " + str(p2) + "\% more cats than in " + m2 + "."
			answer = (100 - p1) * (100 + p2) * 0.01 - 100
		l5 = "Calculate the percentage change in her sales from " + m1 + " to " + m3 + "."
		question = l1 + "\\\\" + l2 + "\\\\" + l3 + "\\\\" + l4 + "\\\\" + l5 
		if answer%1==0:
			answer = int(answer)
		else:
			answer = rounddp(answer,5)
		if answer<0:
			answer = str(abs(answer)) + "\% decrease"
		else:
			answer = str(answer) + "\% increase"
			
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def simpleinterestfindpercentage(n,explanationn):
#in higher unit 7
	import random
	from utilities.rounding import rounddp,rounddpstring
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		amount = random.randrange(15,80)*10
		perc = rounddp(random.randrange(3,20)/2,1)
		if perc%1==0:
			perc = int(perc)
		years = random.randrange(3,10)
		finalamount = amount + years*perc*amount/100
		if finalamount%1==0:
			finalamount = int(finalamount)
		else:
			finalamount = rounddpstring(finalamount,2)
		question = "Purrcy invests \\pounds " + str(amount) + " for " + str(years) + " years in a bank account paying simple interest. At the end of " + str(years) + " years, the amount in the bank account is \\pounds" + str(finalamount) + ". Calculate the annual rate of interest."
		answer = str(perc) + "\\%"
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def ratiovsfraction(n,explanationn):
#in higher nov p6
	import random
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.1cm] "
		n = random.randrange(3,13)
		l1 = "Two bags contain only red and yellow counters."
		l2 = "In Bag A, the ratio of red counters to yellow counters is 1 : " + str(n) + "."
		l3 = "In bag B, $\\dfrac{1}{" + str(n) + "}$ of the counters are red."
		l4 = "The number of counters in each bag is the same."
		l5 = "(a) Complete the table below to show how many counters of each colour could be in the bags."
		table = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{1.5cm} | p{2.5cm} | p{2.5cm} | } \\hline & Red Counters & Yellow Counters \\\\ \\specialrule{1pt}{0pt}{0pt} Bag A & & \\\\ \\hline Bag B & & \\\\ \\hline \\end{tabular}~"
		nums = (1,2,1,2,3,1,3,2,3,4,1,5,4,3,5,2,7,5,3,7,4,5,6,7,8,9)
		dens = (5,9,4,7,10,3,8,5,7,9,2,9,7,5,8,3,10,7,4,9,5,6,7,8,9,10)
		choice = random.randrange(0,len(nums))
		l = nums[choice]
		r = dens[choice]
		lcm = int((r * (r+1))/gcd(r,r+1))
		multa = int(lcm/r)
		multb = int(lcm/(r+1))
		diff = l*multa - l*multb
		answer = str(r*multa)
		l6 = "In another bag, Bag C, the ratio of red counters to yellow counters is " + str(l) + " : " + str(r) + ". If " + str(diff) + " of the red counters are removed from Bag C, the ratio of red counters to yellow counters is " + str(l) + " : " + str(r + 1) + "."
		l7 = "(b) How many yellow counters are in Bag C?"
		question = l1 + nl + l2 + nl + l3 + nl + l4 + nl + l5 + nl + "\\begin{center}" + table  + "~\\end{center}" + l6 + nl + l7
		lcm = int(((n+1) * (n))/gcd(n+1,n))
		multa = int(lcm/(n+1))
		multb = int(lcm/(n))		
		table = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{1.5cm} | p{2.5cm} | p{2.5cm} | } \\hline & Red Counters & Yellow Counters \\\\ \\specialrule{1pt}{0pt}{0pt} Bag A & " + str(multa) + " & " + str(multa*n) + " \\\\ \\hline Bag B & " + str(multb) + " & " + str(multb*(n-1)) + " \\\\ \\hline \\end{tabular}~"
		answer =  l1 + nl + l2 + nl + l3 + nl + l4 + nl + l5 + nl + "\\begin{center}" + table  + "~\\end{center}" + l6 + nl + l7 + nl + "(b) " + answer
#write question
		tempquestions.write(question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(str(answer))



def sftable3(n,explanationn):
#in fia1
	import random
	from utilities.rounding import roundnearest,rounddp
	from utilities.sf import sftonum,sftosf
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		countries = ["England","Scotland","Wales","Ireland","France","Spain","Russia","China","Germany","Belgium"]
		c1 = random.choice(countries)
		countries.remove(c1)
		c2 = random.choice(countries)
		countries.remove(c2)
		c3 = random.choice(countries)
		countries.remove(c3)
		c4 = random.choice(countries)
		countries.remove(c4)
		c5 = random.choice(countries)
		i = random.randrange(4,10)
		i1 = i + 1
		i5 = i - 1

		t = random.randrange(1,3)
		a = rounddp((random.randrange(1,10)*10**t + random.randrange(1,10**t))/10**t,2)
		num1 = sftosf(str(a),i1)

		t = random.randrange(1,3)
		a = rounddp((random.randrange(1,10)*10**t + random.randrange(1,10**t))/10**t,2)
		val2 = rounddp(a * 10**i,0)
		num2 = sftosf(str(a),i)

		t = random.randrange(1,3)
		b = a
		while b==a:
			b = rounddp((random.randrange(1,10)*10**t + random.randrange(1,10**t))/10**t,2)
		val3 = rounddp(b * 10**i,0)
		num3 = sftosf(str(b),i)

		t = random.randrange(1,3)
		c = a
		while c==b or c==a:
			c = rounddp((random.randrange(1,10)*10**t + random.randrange(1,10**t))/10**t,2)
		val4 = rounddp(c * 10**i,0)
		num4 = sftosf(str(c),i)

		t = random.randrange(1,3)
		a = rounddp((random.randrange(1,10)*10**t + random.randrange(1,10**t))/10**t,2)
		val5 = rounddp(a * 10**i5,0)
		num5 = sftosf(str(a),i5)

		intro = "The table below shows the number of tonnes of cat food produced in a particular year in four countries."
		questiona = "(a) Which country produced the most cat food?"
		answera = c1
		choices = list(range(0,4))
		choicenums = [num2,num3,num4,num5]
		choicecs = [c2,c3,c4,c5]
		choicevals = [val2,val3,val4,val5]
		choiceb = random.choice(choices)
		choices.remove(choiceb)
		questionb = "(b) Write " + choicenums[choiceb] + " as an ordinary number."
		answerb = str(int(choicevals[choiceb]))
		choicec = random.choice(choices)
		choices.remove(choicec)
		questionc = "(c) One tonne is equal to 1000 kilograms. Change " + choicenums[choicec] + " tonnes to kilograms. Give your answer in standard form."
		answerc = sftosf(str(choicevals[choicec]),3)
		choiced1 = choices[0]
		choiced2 = choices[1]
		if choicevals[choiced2]>choicevals[choiced1]:
			temp = choiced1
			choiced1 = choiced2
			choiced2 = temp
		questiond = "(d) How many more tonnes of cat food did " + choicecs[choiced1] + " produce than " + choicecs[choiced2] + "? Give your answer in standard form."
		answerd = sftosf(str(choicevals[choiced1] - choicevals[choiced2]),0)
		order = [0,1,2,3,4]
		random.shuffle(order)
		countries = (c1,c2,c3,c4,c5)
		nums = (num1,num2,num3,num4,num5)
		table = "\\renewcommand{\\arraystretch}{1.2}\\begin{tabular}{ | p{3cm} | p{6cm} | } \\hline Country & Cat Food Produced (tonnes) \\\\ \\specialrule{1pt}{0pt}{0pt} " + countries[order[0]] + " & " + nums[order[0]] + " \\\\ \\hline " + countries[order[1]] + "  & " + nums[order[1]] + " \\\\ \\hline " + countries[order[2]] + " & " + nums[order[2]] + " \\\\ \\hline " + countries[order[3]] + "  & " + nums[order[3]] + " \\\\ \\hline " + countries[order[4]] + "  & " + nums[order[4]] + " \\\\ \\hline \\end{tabular}~"
		nl = " \\\\[0.3cm] "
		question = intro + nl + "\\begin{center}" + table + "\\end{center}" +  questiona + nl + questionb + nl + questionc + nl + questiond
		answer = "(a) " + answera + "\\hspace{1cm}(b) " + answerb + "\\hspace{1cm}(c) " + answerc + "\\hspace{1cm}(d) " + answerd
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)




def hcflcmmassive(n,explanationn):
	import random
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		nl = " \\\\[0.3cm] "
		hcf = 2**random.randrange(1,4) * 3**random.randrange(1,3) * 5**random.randrange(0,3) * 7**random.randrange(0,2)
		num1 = hcf * 2**random.randrange(1,3) * 3**random.randrange(1,4) * 5**random.randrange(1,3) * 7**random.randrange(0,3) * 10**random.randrange(2,6)
		num2 = hcf * 2**random.randrange(0,3) * 3**random.randrange(1,4) * 5**random.randrange(1,3) * 7**random.randrange(0,3)
		question = str(hcf) + nl + str(num1) + nl + str(num2)
		hcf = gcd(num1, num2)
		#plan lcm of num1/10^?, product of primes num1 with 10s, hcf of both
		l4 = "(b) Write " + str(num1) + " as a product of prime factors"
		
		twos = 0
		threes = 0
		fives = 0
		sevens = 0
		while num1%(2**(twos+1))==0:
			twos += 1
		while num1%(3**(threes+1))==0:
			threes += 1
		while num1%(5**(fives+1))==0:
			fives += 1
		while num1%(7**(sevens+1))==0:
			sevens += 1
		if twos==0:
			twos = ""
		elif twos==1:
			twos = "2 \\times "
		else:
			twos = "2^{" + str(twos) + "} \\times "
		if threes==0:
			threes = ""
		elif threes==1:
			threes = "3 \\times "
		else:
			threes = "3^{" + str(threes) + "} \\times "
		if fives==0:
			fives = ""
		elif fives==1:
			fives = "5 \\times "
		else:
			fives = "5^{" + str(fives) + "} \\times "
		if sevens==0:
			sevens = ""
		elif sevens==1:
			sevens = "7 \\times "
		else:
			sevens = "7^{" + str(sevens) + "} \\times "
		num1index = twos + threes + fives + sevens
		num1index = num1index[:-7]
		num1index = "$" + num1index + "$"
		a2 = "(b) " + num1index


		l5 = "(c) Find the highest common factor of " + str(num1) + " and " + str(num2)
		a3 = "(C) " + str(gcd(num1,num2))
		tens = 0
		while num1%10==0:
			num1 = int(num1/10)
			tens += 1
		twos = 0
		threes = 0
		fives = 0
		sevens = 0
		while num1%(2**(twos+1))==0:
			twos += 1
		while num1%(3**(threes+1))==0:
			threes += 1
		while num1%(5**(fives+1))==0:
			fives += 1
		while num1%(7**(sevens+1))==0:
			sevens += 1
		if twos==0:
			twos = ""
		elif twos==1:
			twos = "2 \\times "
		else:
			twos = "2^{" + str(twos) + "} \\times "
		if threes==0:
			threes = ""
		elif threes==1:
			threes = "3 \\times "
		else:
			threes = "3^{" + str(threes) + "} \\times "
		if fives==0:
			fives = ""
		elif fives==1:
			fives = "5 \\times "
		else:
			fives = "5^{" + str(fives) + "} \\times "
		if sevens==0:
			sevens = ""
		elif sevens==1:
			sevens = "7 \\times "
		else:
			sevens = "7^{" + str(sevens) + "} \\times "
		num1index = twos + threes + fives + sevens
		num1index = num1index[:-7]
		num1index = "$" + num1index + "$"

		twos = 0
		threes = 0
		fives = 0
		sevens = 0
		while num2%(2**(twos+1))==0:
			twos += 1
		while num2%(3**(threes+1))==0:
			threes += 1
		while num2%(5**(fives+1))==0:
			fives += 1
		while num2%(7**(sevens+1))==0:
			sevens += 1
		if twos==0:
			twos = ""
		elif twos==1:
			twos = "2 \\times "
		else:
			twos = "2^{" + str(twos) + "} \\times "
		if threes==0:
			threes = ""
		elif threes==1:
			threes = "3 \\times "
		else:
			threes = "3^{" + str(threes) + "} \\times "
		if fives==0:
			fives = ""
		elif fives==1:
			fives = "5 \\times "
		else:
			fives = "5^{" + str(fives) + "} \\times "
		if sevens==0:
			sevens = ""
		elif sevens==1:
			sevens = "7 \\times "
		else:
			sevens = "7^{" + str(sevens) + "} \\times "
		num2index = twos + threes + fives + sevens
		num2index = num2index[:-7]
		num2index = "$" + num2index + "$"



		l1 = "You are given that:"
		l2 = str(num1) + " = " + num1index + "\\hspace{0.3cm} and \\hspace{0.3cm} " + str(num2) + " = " + num2index
		l3 = "(a) Find the lowest common multiple of " + str(num1) + " and " + str(num2)
		a1 = "(a) " + str(int((num1*num2)/gcd(num1,num2)))
		question = l1 + nl + l2 + nl + l3 + nl + l4 + nl + l5
		answer = a1 + nl + a2 + nl + a3


#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def hcflcmmassivebad(n,explanationn):
####DELETE THIS WHEN YOU FIX THE PROPER ONE
	import random
	from math import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = ""
		else:
			explanation = ""
		nl = " \\\\[0.3cm] "
		hcf = 1
		num2 = 1
		lcm = 1
		num1 = 1
		while hcf==num2 or lcm==int(num1):
			hcf = 2**random.randrange(1,4) * 3**random.randrange(1,3) * 5**random.randrange(0,3) * 7**random.randrange(0,2)
			num1 = hcf * 2**random.randrange(1,3) * 3**random.randrange(1,4) * 5**random.randrange(1,3) * 7**random.randrange(0,3) * 10**random.randrange(2,6)
			num2 = hcf * 2**random.randrange(0,3) * 3**random.randrange(1,4) * 5**random.randrange(1,3) * 7**random.randrange(0,3)
			question = str(hcf) + nl + str(num1) + nl + str(num2)
			hcf = gcd(num1, num2)
			l4 = "(b) Write " + str(num1) + " as a product of prime factors"
			
			twos = 0
			threes = 0
			fives = 0
			sevens = 0
			while num1%(2**(twos+1))==0:
				twos += 1
			while num1%(3**(threes+1))==0:
				threes += 1
			while num1%(5**(fives+1))==0:
				fives += 1
			while num1%(7**(sevens+1))==0:
				sevens += 1
			if twos==0:
				twos = ""
			elif twos==1:
				twos = "2 \\times "
			else:
				twos = "2^{" + str(twos) + "} \\times "
			if threes==0:
				threes = ""
			elif threes==1:
				threes = "3 \\times "
			else:
				threes = "3^{" + str(threes) + "} \\times "
			if fives==0:
				fives = ""
			elif fives==1:
				fives = "5 \\times "
			else:
				fives = "5^{" + str(fives) + "} \\times "
			if sevens==0:
				sevens = ""
			elif sevens==1:
				sevens = "7 \\times "
			else:
				sevens = "7^{" + str(sevens) + "} \\times "
			num1index = twos + threes + fives + sevens
			num1index = num1index[:-7]
			num1index = "$" + num1index + "$"
			a2 = "(b) " + num1index

			l5 = "(c) Find the highest common factor of " + str(num1) + " and " + str(num2)
			a3 = "(C) " + str(gcd(num1,num2))
			tens = 0
			while num1%10==0:
				num1 = int(num1/10)
				tens += 1
			twos = 0
			threes = 0
			fives = 0
			sevens = 0
			while num1%(2**(twos+1))==0:
				twos += 1
			while num1%(3**(threes+1))==0:
				threes += 1
			while num1%(5**(fives+1))==0:
				fives += 1
			while num1%(7**(sevens+1))==0:
				sevens += 1
			if twos==0:
				twos = ""
			elif twos==1:
				twos = "2 \\times "
			else:
				twos = "2^{" + str(twos) + "} \\times "
			if threes==0:
				threes = ""
			elif threes==1:
				threes = "3 \\times "
			else:
				threes = "3^{" + str(threes) + "} \\times "
			if fives==0:
				fives = ""
			elif fives==1:
				fives = "5 \\times "
			else:
				fives = "5^{" + str(fives) + "} \\times "
			if sevens==0:
				sevens = ""
			elif sevens==1:
				sevens = "7 \\times "
			else:
				sevens = "7^{" + str(sevens) + "} \\times "
			num1index = twos + threes + fives + sevens
			num1index = num1index[:-7]
			num1index = "$" + num1index + "$"

			twos = 0
			threes = 0
			fives = 0
			sevens = 0
			while num2%(2**(twos+1))==0:
				twos += 1
			while num2%(3**(threes+1))==0:
				threes += 1
			while num2%(5**(fives+1))==0:
				fives += 1
			while num2%(7**(sevens+1))==0:
				sevens += 1
			if twos==0:
				twos = ""
			elif twos==1:
				twos = "2 \\times "
			else:
				twos = "2^{" + str(twos) + "} \\times "
			if threes==0:
				threes = ""
			elif threes==1:
				threes = "3 \\times "
			else:
				threes = "3^{" + str(threes) + "} \\times "
			if fives==0:
				fives = ""
			elif fives==1:
				fives = "5 \\times "
			else:
				fives = "5^{" + str(fives) + "} \\times "
			if sevens==0:
				sevens = ""
			elif sevens==1:
				sevens = "7 \\times "
			else:
				sevens = "7^{" + str(sevens) + "} \\times "
			num2index = twos + threes + fives + sevens
			num2index = num2index[:-7]
			num2index = "$" + num2index + "$"



			l1 = "You are given that:"
			l2 = str(num1) + " = " + num1index + "\\hspace{0.3cm} and \\hspace{0.3cm} " + str(num2) + " = " + num2index
			l3 = "(a) Find the lowest common multiple of " + str(num1) + " and " + str(num2)
			lcm = int((num1*num2)/gcd(num1,num2))
			a1 = "(a) " + str(lcm)
			print(str(lcm) + " " + str(num1))
			question = l1 + nl + l2 + nl + l3 + nl + l4 + nl + l5
			answer = a1 + nl + a2 + nl + a3


#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
