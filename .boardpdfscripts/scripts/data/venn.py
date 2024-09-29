#ven.py

def vennneither(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		justcats = random.randrange(10,50)
		justdogs = random.randrange(10,50)
		catsdogs = random.randrange(10,50)
		cats = justcats + catsdogs
		dogs = justdogs + catsdogs
		neither = random.randrange(10,100)
		total = justcats + justdogs + catsdogs + neither
		intro = "In a school there are " + str(total) + " students."
		fact1 = str(cats) + " students like cats.\\\\"
		fact2 = str(dogs) + " students like dogs.\\\\"
		fact3 = str(catsdogs) + " students like both cats and dogs."
		question = "Work out how many students like neither cats nor dogs."
		question = intro + nl + fact1 + fact2 + fact3 + nl + question
		answer = str(neither)
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def vennboth(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		nl = " \\\\[0.3cm] "
		justcats = random.randrange(10,50)
		justdogs = random.randrange(10,50)
		catsdogs = random.randrange(10,50)
		cats = justcats + catsdogs
		dogs = justdogs + catsdogs
		neither = random.randrange(10,100)
		total = justcats + justdogs + catsdogs + neither
		intro = "In a school there are " + str(total) + " students."
		fact1 = str(cats) + " students like cats.\\\\"
		fact2 = str(dogs) + " students like dogs.\\\\"
		fact3 = str(neither) + " students like neither cats nor dogs."
		question = "Work out how many students like both cats and dogs."
		question = intro + nl + fact1 + fact2 + fact3 + nl + question 
		answer = str(catsdogs)
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



