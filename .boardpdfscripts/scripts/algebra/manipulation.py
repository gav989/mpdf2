#manipulation.py

def collect1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		type = random.randrange(1,4)
		co1 = random.randrange(1,10)
		co2 = random.randrange(1,10)
		num1 = random.randrange(1,10)
		signs = [" + "," - "]
		sign1 = random.choice(signs)
		sign2 = random.choice(signs)
		if type==1:
			if random.randrange(0,2)==1:
				signa = sign1
				if sign2==" - ":
					coa = co1-co2
				else:
					coa = co1+co2
				numa = num1
				if co1==1:
					co1 = ""
				if co2==1:
					co2 = ""
				question = str(co1) + letter1 + sign1 + str(num1) + sign2 + str(co2) + letter1
			else:
				signa = sign2
				if sign1==" - ":
					coa = co1-co2
				else:
					coa = co1+co2
				numa = num1
				if co1==1:
					co1 = ""
				if co2==1:
					co2 = ""
				question = str(co1) + letter1 + sign1 + str(co2) + letter1 + sign2 + str(num1) 
		elif type==2:
			num2 = random.randrange(1,10)
			coa = co1
			if sign1==sign2:
				numa = num1 + num2
				signa = sign1 
			elif sign1==" + " and sign2==" - ":
				numa = num1 - num2
				if numa<0:
					signa = " - "
					numa = abs(numa)
				else:
					signa = " + "
			else:
				numa = num2 - num1
				if numa<0:
					signa = " - "
					numa = abs(numa)
				else:
					signa = " + "
			if co1==1:
				co1 = ""
			question = str(co1) + letter1 + sign1 + str(num1) + sign2 + str(num2)
		else:
			num2 = random.randrange(1,10)
			sign3 = random.choice(signs)
			dec = random.randrange(0,3)
			if dec==1:
				if sign1==" + ":
					coa = co1 + co2
				else:
					coa = co1 - co2
				if sign2==sign3:
					numa = num1 + num2
					signa = sign2 
				elif sign2==" + " and sign3==" - ":
					numa = num1 - num2
					if numa<0:
						signa = " - "
						numa = abs(numa)
					else:
						signa = " + "
				else:
					numa = num2 - num1
					if numa<0:
						signa = " - "
						numa = abs(numa)
					else:
						signa = " + "
				if co1==1:
					co1 = ""
				if co2==1:
					co2 = ""
				question = str(co1) + letter1 + sign1 + str(co2) + letter1 + sign2 + str(num1) + sign3 + str(num2)
			elif dec==2:
				if sign2==" + ":
					coa = co1 + co2
				else:
					coa = co1 - co2
				if sign1==sign3:
					numa = num1 + num2
					signa = sign1 
				elif sign1==" + " and sign3==" - ":
					numa = num1 - num2
					if numa<0:
						signa = " - "
						numa = abs(numa)
					else:
						signa = " + "
				else:
					numa = num2 - num1
					if numa<0:
						signa = " - "
						numa = abs(numa)
					else:
						signa = " + "
				if co1==1:
					co1 = ""
				if co2==1:
					co2 = ""
				question = str(co1) + letter1 + sign1 + str(num1) + sign2 + str(co2) + letter1 + sign3 + str(num2)
			else:
				if sign3==" + ":
					coa = co1 + co2
				else:
					coa = co1 - co2
				if sign1==sign2:
					numa = num1 + num2
					signa = sign1 
				elif sign1==" + " and sign2==" - ":
					numa = num1 - num2
					if numa<0:
						signa = " - "
						numa = abs(numa)
					else:
						signa = " + "
				else:
					numa = num2 - num1
					if numa<0:
						signa = " - "
						numa = abs(numa)
					else:
						signa = " + "
				if co1==1:
					co1 = ""
				if co2==1:
					co2 = ""
				question = str(co1) + letter1 + sign1 + str(num1) + sign2 + str(num2) + sign3 + str(co2) + letter1
		if coa==1:
			coa = ""
		elif coa==-1:
			coa = "-"
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		if coa==0:
			if signa==" - ":
				numa = 0 - numa
			tempquestions.write(str(numa))
		elif numa==0:
			tempquestions.write(str(coa) + letter1)
		else:
			tempquestions.write(str(coa) + letter1 + signa + str(numa))
			

def collect2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		letters.remove(letter1)
		letter2 = random.choice(letters)
		type = random.randrange(1,3)
		if type==1:
			co1 = random.randrange(1,10)
			co2 = random.randrange(1,10)
			co3 = random.randrange(1,10)
			if random.randrange(0,2)==1:
				sign1 = " - "
			else:
				sign1 = " + "
			if random.randrange(0,2)==1:
				sign2 = " - "
			else:
				sign2 = " + "
			order = random.randrange(1,4)
			if order==1:
				if sign1==" - ":
					co2 = 0 - co2
				if sign2==" - ":
					co3 = 0 - co3
				coa1 = co1
				coa2 = co2 + co3
				co2 = str(abs(co2))
				co3 = str(abs(co3))
				if co1==1:
					co1 = ""
				else:
					co1 = str(co1)
				if co2=="1":
					co2 = ""
				if co3=="1":
					co3 = ""
				question = co1 + letter1 + sign1 + co2 + letter2 + sign2 + co3 + letter2
			elif order==2:
				if sign1==" - ":
					co2 = 0 - co2
				if sign2==" - ":
					co3 = 0 - co3
				coa1 = co1 + co3
				coa2 = co2
				co2 = str(abs(co2))
				co3 = str(abs(co3))
				if co1==1:
					co1 = ""
				else:
					co1 = str(co1)
				if co2=="1":
					co2 = ""
				if co3=="1":
					co3 = ""
				question = co1 + letter1 + sign1 + co2 + letter2 + sign2 + co3 + letter1
			else:
				if sign1==" - ":
					co2 = 0 - co2
				if sign2==" - ":
					co3 = 0 - co3
				coa1 = co1 + co2
				coa2 = co3
				co2 = str(abs(co2))
				co3 = str(abs(co3))
				if co1==1:
					co1 = ""
				else:
					co1 = str(co1)
				if co2=="1":
					co2 = ""
				if co3=="1":
					co3 = ""
				question = co1 + letter1 + sign1 + co2 + letter1 + sign2 + co3 + letter2
		else:
			co1 = random.randrange(1,10)
			co2 = random.randrange(1,10)
			co3 = random.randrange(1,10)
			co4 = random.randrange(1,10)
			if random.randrange(0,2)==1:
				sign1 = " - "
			else:
				sign1 = " + "
			if random.randrange(0,2)==1:
				sign2 = " - "
			else:
				sign2 = " + "
			if random.randrange(0,2)==1:
				sign3 = " - "
			else:
				sign3 = " + "
			order = random.randrange(1,4)
			if order==1:
				if sign1==" - ":
					co2 = 0 - co2
				if sign2==" - ":
					co3 = 0 - co3
				if sign3==" - ":
					co4 = 0 - co4
				coa1 = co1 + co2
				coa2 = co3 + co4
				co2 = str(abs(co2))
				co3 = str(abs(co3))
				co4 = str(abs(co4))
				if co1==1:
					co1 = ""
				else:
					co1 = str(co1)
				if co2=="1":
					co2 = ""
				if co3=="1":
					co3 = ""
				if co4=="1":
					co4 = ""
				question = co1 + letter1 + sign1 + co2 + letter1 + sign2 + co3 + letter2 + sign3 + co4 + letter2
			elif order==2:
				if sign1==" - ":
					co2 = 0 - co2
				if sign2==" - ":
					co3 = 0 - co3
				if sign3==" - ":
					co4 = 0 - co4
				coa1 = co1 + co3
				coa2 = co2 + co4
				co2 = str(abs(co2))
				co3 = str(abs(co3))
				co4 = str(abs(co4))
				if co1==1:
					co1 = ""
				else:
					co1 = str(co1)
				if co2=="1":
					co2 = ""
				if co3=="1":
					co3 = ""
				if co4=="1":
					co4 = ""
				question = co1 + letter1 + sign1 + co2 + letter2 + sign2 + co3 + letter1 + sign3 + co4 + letter2
			else:
				if sign1==" - ":
					co2 = 0 - co2
				if sign2==" - ":
					co3 = 0 - co3
				if sign3==" - ":
					co4 = 0 - co4
				coa1 = co1 + co4
				coa2 = co2 + co3
				co2 = str(abs(co2))
				co3 = str(abs(co3))
				co4 = str(abs(co4))
				if co1==1:
					co1 = ""
				else:
					co1 = str(co1)
				if co2=="1":
					co2 = ""
				if co3=="1":
					co3 = ""
				if co4=="1":
					co4 = ""
				question = co1 + letter1 + sign1 + co2 + letter2 + sign2 + co3 + letter2 + sign3 + co4 + letter1
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		if coa1==0 and coa2==0:
			tempquestions.write(str(0))
		elif coa1==0:
			tempquestions.write(str(coa2) + letter2)
		elif coa2==0:
			if coa1==1:
				coa1 = ""
			if coa1==-1:
				coa1 = "-"
			tempquestions.write(str(coa1) + letter1)
		else:
			if coa1==1:
				coa1 = ""
			if coa1==-1:
				coa1 = "-"
			if coa2<0:
				signa = " - "
				coa2 = abs(coa2)
			else:
				signa = " + "
			if coa2==1:
				coa2 = ""
			tempquestions.write(str(coa1) + letter1 + signa + str(coa2) + letter2)



def collect1pos(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		type = random.randrange(1,4)
		co1 = random.randrange(1,10)
		co2 = random.randrange(1,10)
		num1 = random.randrange(1,10)
		signs = [" + "," + "]
		sign1 = random.choice(signs)
		sign2 = random.choice(signs)
		if type==1:
			if random.randrange(0,2)==1:
				signa = sign1
				if sign2==" - ":
					coa = co1-co2
				else:
					coa = co1+co2
				numa = num1
				if co1==1:
					co1 = ""
				if co2==1:
					co2 = ""
				question = str(co1) + letter1 + sign1 + str(num1) + sign2 + str(co2) + letter1
			else:
				signa = sign2
				if sign1==" - ":
					coa = co1-co2
				else:
					coa = co1+co2
				numa = num1
				if co1==1:
					co1 = ""
				if co2==1:
					co2 = ""
				question = str(co1) + letter1 + sign1 + str(co2) + letter1 + sign2 + str(num1) 
		elif type==2:
			num2 = random.randrange(1,10)
			coa = co1
			if sign1==sign2:
				numa = num1 + num2
				signa = sign1 
			elif sign1==" + " and sign2==" - ":
				numa = num1 - num2
				if numa<0:
					signa = " - "
					numa = abs(numa)
				else:
					signa = " + "
			else:
				numa = num2 - num1
				if numa<0:
					signa = " - "
					numa = abs(numa)
				else:
					signa = " + "
			if co1==1:
				co1 = ""
			question = str(co1) + letter1 + sign1 + str(num1) + sign2 + str(num2)
		else:
			num2 = random.randrange(1,10)
			sign3 = random.choice(signs)
			dec = random.randrange(0,3)
			if dec==1:
				if sign1==" + ":
					coa = co1 + co2
				else:
					coa = co1 - co2
				if sign2==sign3:
					numa = num1 + num2
					signa = sign2 
				elif sign2==" + " and sign3==" - ":
					numa = num1 - num2
					if numa<0:
						signa = " - "
						numa = abs(numa)
					else:
						signa = " + "
				else:
					numa = num2 - num1
					if numa<0:
						signa = " - "
						numa = abs(numa)
					else:
						signa = " + "
				if co1==1:
					co1 = ""
				if co2==1:
					co2 = ""
				question = str(co1) + letter1 + sign1 + str(co2) + letter1 + sign2 + str(num1) + sign3 + str(num2)
			elif dec==2:
				if sign2==" + ":
					coa = co1 + co2
				else:
					coa = co1 - co2
				if sign1==sign3:
					numa = num1 + num2
					signa = sign1 
				elif sign1==" + " and sign3==" - ":
					numa = num1 - num2
					if numa<0:
						signa = " - "
						numa = abs(numa)
					else:
						signa = " + "
				else:
					numa = num2 - num1
					if numa<0:
						signa = " - "
						numa = abs(numa)
					else:
						signa = " + "
				if co1==1:
					co1 = ""
				if co2==1:
					co2 = ""
				question = str(co1) + letter1 + sign1 + str(num1) + sign2 + str(co2) + letter1 + sign3 + str(num2)
			else:
				if sign3==" + ":
					coa = co1 + co2
				else:
					coa = co1 - co2
				if sign1==sign2:
					numa = num1 + num2
					signa = sign1 
				elif sign1==" + " and sign2==" - ":
					numa = num1 - num2
					if numa<0:
						signa = " - "
						numa = abs(numa)
					else:
						signa = " + "
				else:
					numa = num2 - num1
					if numa<0:
						signa = " - "
						numa = abs(numa)
					else:
						signa = " + "
				if co1==1:
					co1 = ""
				if co2==1:
					co2 = ""
				question = str(co1) + letter1 + sign1 + str(num1) + sign2 + str(num2) + sign3 + str(co2) + letter1
		if coa==1:
			coa = ""
		elif coa==-1:
			coa = "-"
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		if coa==0:
			if signa==" - ":
				numa = 0 - numa
			tempquestions.write(str(numa))
		elif numa==0:
			tempquestions.write(str(coa) + letter1)
		else:
			tempquestions.write(str(coa) + letter1 + signa + str(numa))
			

def collect2pos(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		letters.remove(letter1)
		letter2 = random.choice(letters)
		type = random.randrange(1,3)
		sign1 = " + "
		sign2 = " + "
		sign3 = " + "
		if type==1:
			co1 = random.randrange(1,10)
			co2 = random.randrange(1,10)
			co3 = random.randrange(1,10)
			order = random.randrange(1,4)
			if order==1:
				if sign1==" - ":
					co2 = 0 - co2
				if sign2==" - ":
					co3 = 0 - co3
				coa1 = co1
				coa2 = co2 + co3
				co2 = str(abs(co2))
				co3 = str(abs(co3))
				if co1==1:
					co1 = ""
				else:
					co1 = str(co1)
				if co2=="1":
					co2 = ""
				if co3=="1":
					co3 = ""
				question = co1 + letter1 + sign1 + co2 + letter2 + sign2 + co3 + letter2
			elif order==2:
				if sign1==" - ":
					co2 = 0 - co2
				if sign2==" - ":
					co3 = 0 - co3
				coa1 = co1 + co3
				coa2 = co2
				co2 = str(abs(co2))
				co3 = str(abs(co3))
				if co1==1:
					co1 = ""
				else:
					co1 = str(co1)
				if co2=="1":
					co2 = ""
				if co3=="1":
					co3 = ""
				question = co1 + letter1 + sign1 + co2 + letter2 + sign2 + co3 + letter1
			else:
				if sign1==" - ":
					co2 = 0 - co2
				if sign2==" - ":
					co3 = 0 - co3
				coa1 = co1 + co2
				coa2 = co3
				co2 = str(abs(co2))
				co3 = str(abs(co3))
				if co1==1:
					co1 = ""
				else:
					co1 = str(co1)
				if co2=="1":
					co2 = ""
				if co3=="1":
					co3 = ""
				question = co1 + letter1 + sign1 + co2 + letter1 + sign2 + co3 + letter2
		else:
			co1 = random.randrange(1,10)
			co2 = random.randrange(1,10)
			co3 = random.randrange(1,10)
			co4 = random.randrange(1,10)
			order = random.randrange(1,4)
			if order==1:
				if sign1==" - ":
					co2 = 0 - co2
				if sign2==" - ":
					co3 = 0 - co3
				if sign3==" - ":
					co4 = 0 - co4
				coa1 = co1 + co2
				coa2 = co3 + co4
				co2 = str(abs(co2))
				co3 = str(abs(co3))
				co4 = str(abs(co4))
				if co1==1:
					co1 = ""
				else:
					co1 = str(co1)
				if co2=="1":
					co2 = ""
				if co3=="1":
					co3 = ""
				if co4=="1":
					co4 = ""
				question = co1 + letter1 + sign1 + co2 + letter1 + sign2 + co3 + letter2 + sign3 + co4 + letter2
			elif order==2:
				if sign1==" - ":
					co2 = 0 - co2
				if sign2==" - ":
					co3 = 0 - co3
				if sign3==" - ":
					co4 = 0 - co4
				coa1 = co1 + co3
				coa2 = co2 + co4
				co2 = str(abs(co2))
				co3 = str(abs(co3))
				co4 = str(abs(co4))
				if co1==1:
					co1 = ""
				else:
					co1 = str(co1)
				if co2=="1":
					co2 = ""
				if co3=="1":
					co3 = ""
				if co4=="1":
					co4 = ""
				question = co1 + letter1 + sign1 + co2 + letter2 + sign2 + co3 + letter1 + sign3 + co4 + letter2
			else:
				if sign1==" - ":
					co2 = 0 - co2
				if sign2==" - ":
					co3 = 0 - co3
				if sign3==" - ":
					co4 = 0 - co4
				coa1 = co1 + co4
				coa2 = co2 + co3
				co2 = str(abs(co2))
				co3 = str(abs(co3))
				co4 = str(abs(co4))
				if co1==1:
					co1 = ""
				else:
					co1 = str(co1)
				if co2=="1":
					co2 = ""
				if co3=="1":
					co3 = ""
				if co4=="1":
					co4 = ""
				question = co1 + letter1 + sign1 + co2 + letter2 + sign2 + co3 + letter2 + sign3 + co4 + letter1
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		if coa1==0 and coa2==0:
			tempquestions.write(str(0))
		elif coa1==0:
			tempquestions.write(str(coa2) + letter2)
		elif coa2==0:
			if coa1==1:
				coa1 = ""
			if coa1==-1:
				coa1 = "-"
			tempquestions.write(str(coa1) + letter1)
		else:
			if coa1==1:
				coa1 = ""
			if coa1==-1:
				coa1 = "-"
			if coa2<0:
				signa = " - "
				coa2 = abs(coa2)
			else:
				signa = " + "
			if coa2==1:
				coa2 = ""
			tempquestions.write(str(coa1) + letter1 + signa + str(coa2) + letter2)



def multiplyterms1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		question = letter1 + " $\\times$ " + letter1
		answer = letter1 + "$^{2}$"
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def multiplyterms2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		letters.remove(letter1)
		letter2 = random.choice(letters)
		question = letter1 + " $\\times$ " + letter2
		if letter1>letter2:
			temp = letter1
			letter1 = letter2
			letter2 = temp
		answer = letter1 + letter2
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def multiplyterms3(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		num1 = random.randrange(2,10)
		a = str(num1) + letter1
		b = letter1
		if random.randrange(0,2)==1:
			temp = a
			a = b
			b = temp
		question = a + " $\\times$ " + b
		answer = str(num1) + letter1 + "$^{2}$"
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def multiplyterms4(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		letters.remove(letter1)
		letter2 = random.choice(letters)
		num1 = random.randrange(2,10)
		a = str(num1) + letter1
		b = letter2
		if random.randrange(0,2)==1:
			temp = a
			a = b
			b = temp
		question = a + " $\\times$ " + b
		if letter1>letter2:
			temp = letter1
			letter1 = letter2
			letter2 = temp
		answer = str(num1) + letter1 + letter2
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def multiplyterms5(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		num1 = random.randrange(2,10)
		num2 = random.randrange(2,10)
		numa = num1 * num2
		a = str(num1) + letter1
		b = str(num2) + letter1
		question = a + " $\\times$ " + b
		answer = str(numa) + letter1 + "$^{2}$"
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def multiplyterms6(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		letters.remove(letter1)
		letter2 = random.choice(letters)
		num1 = random.randrange(2,10)
		num2 = random.randrange(2,10)
		numa = num1 * num2
		a = str(num1) + letter1
		b = str(num2) + letter2
		question = a + " $\\times$ " + b
		if letter1>letter2:
			temp = letter1
			letter1 = letter2
			letter2 = temp
		answer = str(numa) + letter1 + letter2
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def multiplyterms7(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		letters.remove(letter1)
		letter2 = random.choice(letters)
		num1 = random.randrange(2,10)
		if letter1>letter2:
			temp = letter1
			letter1 = letter2
			letter2 = temp
		if random.randrange(0,2)==1:
			a = str(num1) + letter1
			b = letter1 + letter2
			answer = str(num1) + letter1 + "$^{2}$" + letter2
		else:
			a = str(num1) + letter2
			b = letter1 + letter2
			answer = str(num1) + letter1 + letter2 + "$^{2}$"
		if random.randrange(0,2)==1:
			temp = a
			a = b
			b = temp
		question = a + " $\\times$ " + b
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def multiplyterms8(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Simplify "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		letters.remove(letter1)
		letter2 = random.choice(letters)
		num1 = random.randrange(2,10)
		num2 = random.randrange(2,10)
		numa = num1 * num2
		if letter1>letter2:
			temp = letter1
			letter1 = letter2
			letter2 = temp
		if random.randrange(0,2)==1:
			a = str(num1) + letter1
			b = str(num2) + letter1 + letter2
			answer = str(numa) + letter1 + "$^{2}$" + letter2
		else:
			a = str(num1) + letter2
			b = str(num2) + letter1 + letter2
			answer = str(numa) + letter1 + letter2 + "$^{2}$"
		if random.randrange(0,2)==1:
			temp = a
			a = b
			b = temp
		question = a + " $\\times$ " + b
#write question
		tempquestions.write(explanation + question)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def singlebracketexpansion1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Expand "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		num1 = random.randrange(2,10)
		num2 = random.randrange(1,10)
		swap = random.randrange(0,2)
		coa = num1
		numa = num1 * num2
		if random.randrange(0,2)==1:
			sign = " + "
		else:
			sign = " - "
#write question
		if swap==1:
			tempquestions.write(explanation + str(num1) + "(" + str(num2) + sign + letter1 + ")")
		else:
			tempquestions.write(explanation + str(num1) + "(" + letter1 + sign + str(num2) + ")")
		tempquestions.write("\n")
#write answer
		if swap==1:
			tempquestions.write(str(numa) + sign + str(coa) + letter1)
		else:
			tempquestions.write(str(coa) + letter1 + sign + str(numa))
		

def singlebracketexpansion2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Expand "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		num1 = random.randrange(2,10)
		num2 = random.randrange(1,10)
		co1 = random.randrange(2,10)
		swap = random.randrange(0,2)
		coa = num1*co1
		numa = num1 * num2
		if random.randrange(0,2)==1:
			sign = " + "
		else:
			sign = " - "
#write question
		if swap==1:
			tempquestions.write(explanation + str(num1) + "(" + str(num2) + sign + str(co1) + letter1 + ")")
		else:
			tempquestions.write(explanation + str(num1) + "(" + str(co1) + letter1 + sign + str(num2) + ")")
		tempquestions.write("\n")
#write answer
		if swap==1:
			tempquestions.write(str(numa) + sign + str(coa) + letter1)
		else:
			tempquestions.write(str(coa) + letter1 + sign + str(numa))


def singlebracketexpansion3(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Expand "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		num2 = random.randrange(1,10)
		swap = random.randrange(0,2)
		if random.randrange(0,2)==1:
			sign = " + "
		else:
			sign = " - "
#write question
		if swap==1:
			tempquestions.write(explanation + letter1 + "(" + str(num2) + sign + letter1 + ")")
		else:
			tempquestions.write(explanation + letter1 + "(" + letter1 + sign + str(num2) + ")")
		tempquestions.write("\n")
#write answer
		if swap==1:
			tempquestions.write(str(num2) + letter1 + sign + letter1 + "$^2$")
		else:
			tempquestions.write(letter1 + "$^2$"+ sign + str(num2) + letter1)



def singlebracketexpansion4(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Expand "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		num2 = random.randrange(1,10)
		co2 = random.randrange(2,10)
		swap = random.randrange(0,2)
		if random.randrange(0,2)==1:
			sign = " + "
		else:
			sign = " - "
#write question
		if swap==1:
			tempquestions.write(explanation + letter1 + "(" + str(num2) + sign + str(co2) + letter1 + ")")
		else:
			tempquestions.write(explanation + letter1 + "(" + str(co2) + letter1 + sign + str(num2) + ")")
		tempquestions.write("\n")
#write answer
		if swap==1:
			tempquestions.write(str(num2) + letter1 + sign + str(co2) + letter1 + "$^2$")
		else:
			tempquestions.write(str(co2) + letter1 + "$^2$"+ sign + str(num2) + letter1)


def singlebracketexpansion5(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Expand "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		num2 = random.randrange(1,10)
		co1 = random.randrange(2,10)
		co2 = random.randrange(2,10)
		numa = co1 * num2
		coa = co1 * co2
		swap = random.randrange(0,2)
		if random.randrange(0,2)==1:
			sign = " + "
		else:
			sign = " - "
#write question
		if swap==1:
			tempquestions.write(explanation + str(co1) + letter1 + "(" + str(num2) + sign + str(co2) + letter1 + ")")
		else:
			tempquestions.write(explanation + str(co1) + letter1 + "(" + str(co2) + letter1 + sign + str(num2) + ")")
		tempquestions.write("\n")
#write answer
		if swap==1:
			tempquestions.write(str(numa) + letter1 + sign + str(coa) + letter1 + "$^2$")
		else:
			tempquestions.write(str(coa) + letter1 + "$^2$"+ sign + str(numa) + letter1)


def singlebracketexpansion6(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		num1 = random.randrange(2,10)
		num2 = random.randrange(1,10) * (-1)**random.randrange(1,3)
		num3 = random.randrange(2,10)
		num4 = random.randrange(1,10) * (-1)**random.randrange(1,3)
		if num2>0:
			sign1 = " + "
		else:
			sign1 = " - "
		if num4>0:
			sign2 = " + "
		else:
			sign2 = " - "
		coa = num1 + num3
		numa = num1*num2 + num3*num4
		if numa>0:
			signa = " + "
		else:
			signa = " - "
		if numa==0:
			answer = str(coa) + letter1
		else:
			answer = str(coa) + letter1 + signa + str(abs(numa))
#write question
		tempquestions.write(explanation + str(num1) + "(" + letter1 + sign1 + str(abs(num2)) + ") + " + str(num3) + "(" + letter1 + sign2 + str(abs(num4)) + ")")
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def singlebracketexpansion7(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		num2 = random.randrange(1,10) * (-1)**random.randrange(1,3)
		num3 = random.randrange(2,7)
		num1 = num3 + random.randrange(1,6)
		num4 = random.randrange(1,10) * (-1)**random.randrange(1,3)
		if num2>0:
			sign1 = " + "
		else:
			sign1 = " - "
		if num4>0:
			sign2 = " + "
		else:
			sign2 = " - "
		coa = num1 - num3
		numa = num1*num2 - num3*num4
		if numa>0:
			signa = " + "
		else:
			signa = " - "	
		if coa==1:
			coa = ""
		if numa==0:
			answer = str(coa) + letter1
		else:
			answer = str(coa) + letter1 + signa + str(abs(numa))
#write question
		tempquestions.write(explanation + str(num1) + "(" + letter1 + sign1 + str(abs(num2)) + ") - " + str(num3) + "(" + letter1 + sign2 + str(abs(num4)) + ")")
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)

def singlebracketexpansion7showthat(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Show that "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		num2 = random.randrange(1,10) * (-1)**random.randrange(1,3)
		num3 = random.randrange(2,7)
		num1 = num3 + random.randrange(1,6)
		num4 = random.randrange(1,10) * (-1)**random.randrange(1,3)
		if num2>0:
			sign1 = " + "
		else:
			sign1 = " - "
		if num4>0:
			sign2 = " + "
		else:
			sign2 = " - "
		coa = num1 - num3
		numa = num1*num2 - num3*num4
		if numa>0:
			signa = " + "
		else:
			signa = " - "	
		if coa==1:
			coa = ""
		if numa==0:
			answer = str(coa) + letter1
		else:
			answer = str(coa) + letter1 + signa + str(abs(numa))
#write question
		tempquestions.write(explanation + str(num1) + "(" + letter1 + sign1 + str(abs(num2)) + ") - " + str(num3) + "(" + letter1 + sign2 + str(abs(num4)) + ") = " + answer)
		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)


def singlebracketexpansion8(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Expand and simplify "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		letters.remove(letter1)
		letter2 = random.choice(letters)
		num1 = random.randrange(2,10)
		num2 = random.randrange(2,10)
		if random.randrange(1,3)==2:
			sign = " - "
		else:
			sign = " + "
		if letter1>letter2:
			letters = letter2 + letter1
		else:
			letters = letter1 + letter2
		if random.randrange(1,3)==2:
			brackets = str(num1) + letter1 + "(" + letter1 + sign + str(num2) + letter2 + ")"
			expanded = str(num1) + letter1 + "$^{2}$" + sign + str(num1*num2) + letters
		else:
			brackets = str(num1) + letter1 + "(" + str(num2) + letter2 + sign + letter1 + ")"
			expanded = str(num1*num2) + letters + sign + str(num1) + letter1 + "$^{2}$"
#write question
		tempquestions.write(explanation + brackets)
		tempquestions.write("\n")
#write answer
		tempquestions.write(expanded)


def singlebracketfactorise1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise fully "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		num1 = random.randrange(2,10)
		num2 = random.randrange(1,10)
		swap = random.randrange(0,2)
		coa = num1
		numa = num1 * num2
		if random.randrange(0,2)==1:
			sign = " + "
		else:
			sign = " - "
#write question
		if swap==1:
			tempquestions.write(explanation + str(numa) + sign + str(coa) + letter1)
		else:
			tempquestions.write(explanation + str(coa) + letter1 + sign + str(numa))
		tempquestions.write("\n")
#write answer
		if swap==1:
			tempquestions.write(str(num1) + "(" + str(num2) + sign + letter1 + ")")
		else:
			tempquestions.write(str(num1) + "(" + letter1 + sign + str(num2) + ")")

def singlebracketfactorise2(n,explanationn):
	import random
	from fractions import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise fully "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		num1 = random.randrange(2,10)
		num2 = random.randrange(1,10)
		co1 = random.randrange(2,10)
		swap = random.randrange(0,2)
		coa = num1*co1
		numa = num1 * num2
		if random.randrange(0,2)==1:
			sign = " + "
		else:
			sign = " - "
		hcf = gcd(num2,co1)
		num2 = int(num2 / hcf)
		co1 = int(co1 / hcf)
		num1 = int(num1 * hcf)
		if co1==1:
			co1 = ""
#write question
		if swap==1:
			tempquestions.write(explanation + str(numa) + sign + str(coa) + letter1)
		else:
			tempquestions.write(explanation + str(coa) + letter1 + sign + str(numa))
		tempquestions.write("\n")
#write answer
		if swap==1:
			tempquestions.write(str(num1) + "(" + str(num2) + sign + str(co1) + letter1 + ")")
		else:
			tempquestions.write(str(num1) + "(" + str(co1) + letter1 + sign + str(num2) + ")")


def singlebracketfactorise3(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise fully "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		num2 = random.randrange(1,10)
		swap = random.randrange(0,2)
		if random.randrange(0,2)==1:
			sign = " + "
		else:
			sign = " - "
#write question
		if swap==1:
			tempquestions.write(explanation + str(num2) + letter1 + sign + letter1 + "$^2$")
		else:
			tempquestions.write(explanation + letter1 + "$^2$"+ sign + str(num2) + letter1)
		tempquestions.write("\n")
#write answer
		if swap==1:
			tempquestions.write(letter1 + "(" + str(num2) + sign + letter1 + ")")
		else:
			tempquestions.write(letter1 + "(" + letter1 + sign + str(num2) + ")")


def singlebracketfactorise4(n,explanationn):
	import random
	from fractions import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise fully "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		nums = (2,2,2,2,3,3,3,3,4,4,4,5,5,5,5,6,7,7,8,1,1,1,1,1,1,1,1)
		dens = (3,5,7,9,4,5,7,8,5,7,9,6,7,8,9,7,8,9,9,2,3,4,5,6,7,8,9)
		choice = random.randrange(0,27)
		num2 = nums[choice]
		co2 = dens[choice]
		swap = random.randrange(0,2)
		if swap==1:
			temp = num2
			num2 = co2
			co2 = temp
		swap = random.randrange(0,2)
		if random.randrange(0,2)==1:
			sign = " + "
		else:
			sign = " - "
		if co2==1:
			co2 = ""
		numq = num2
		if numq==1:
			numq = ""
#write question
		if swap==1:
			tempquestions.write(explanation + str(numq) + letter1 + sign + str(co2) + letter1 + "$^2$")
		else:
			tempquestions.write(explanation + str(co2) + letter1 + "$^2$"+ sign + str(numq) + letter1)
		tempquestions.write("\n")
#write answer
		if swap==1:
			tempquestions.write(letter1 + "(" + str(num2) + sign + str(co2) + letter1 + ")")
		else:
			tempquestions.write(letter1 + "(" + str(co2) + letter1 + sign + str(num2) + ")")

def singlebracketfactorise5(n,explanationn):
	import random
	from fractions import gcd
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise fully "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		num2 = random.randrange(1,10)
		co1 = random.randrange(2,10)
		co2 = random.randrange(2,10)
		numa = co1 * num2
		coa = co1 * co2
		swap = random.randrange(0,2)
		if random.randrange(0,2)==1:
			sign = " + "
		else:
			sign = " - "
		hcf = gcd(num2,co2)
		num2 = int(num2 / hcf)
		co2 = int(co2 / hcf)
		co1 = int(co1 * hcf)
		if co2==1:
			co2 = ""
#write question
		if swap==1:
			tempquestions.write(explanation + str(numa) + letter1 + sign + str(coa) + letter1 + "$^2$")
		else:
			tempquestions.write(explanation + str(coa) + letter1 + "$^2$"+ sign + str(numa) + letter1)
		tempquestions.write("\n")
#write answer
		if swap==1:
			tempquestions.write(str(co1) + letter1 + "(" + str(num2) + sign + str(co2) + letter1 + ")")
		else:
			tempquestions.write(str(co1) + letter1 + "(" + str(co2) + letter1 + sign + str(num2) + ")")


def singlebracketfactorise8(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Factorise fully "
		else:
			explanation = ""
		letters = ["a","b","c","x","y"]
		letter1 = random.choice(letters)
		letters.remove(letter1)
		letter2 = random.choice(letters)
		num1 = random.randrange(2,10)
		num2 = random.randrange(2,10)
		if random.randrange(1,3)==2:
			sign = " - "
		else:
			sign = " + "
		if letter1>letter2:
			letters = letter2 + letter1
		else:
			letters = letter1 + letter2
		if random.randrange(1,3)==2:
			brackets = str(num1) + letter1 + "(" + letter1 + sign + str(num2) + letter2 + ")"
			expanded = str(num1) + letter1 + "$^{2}$" + sign + str(num1*num2) + letters
		else:
			brackets = str(num1) + letter1 + "(" + str(num2) + letter2 + sign + letter1 + ")"
			expanded = str(num1*num2) + letters + sign + str(num1) + letter1 + "$^{2}$"
#write question
		tempquestions.write(explanation + expanded)
		tempquestions.write("\n")
#write answer
		tempquestions.write(brackets)



def rearrange1(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Make x the subject of the formula "
		else:
			explanation = ""
		letters = ["a","b","c","d","e","f","g","h","j","k","m","n","p","q","r","t","y"]
		a = random.choice(letters)
		letters.remove(a)
		b = random.choice(letters)
		letters.remove(b)
		c = random.choice(letters)
		letters.remove(c)
		d = random.choice(letters)
		letters.remove(d)
		e = random.choice(letters)
		letters.remove(e)
		f = random.choice(letters)
		letters.remove(f)
		g = random.choice(letters)
		letters.remove(g)
		h = random.choice(letters)
		numbers = ("2","3","5","7")
		n = random.choice(numbers)
		x = "x"
		if random.randrange(0,2)==1:
			sign1 = " - "
			sign2 = " + "
		else:
			sign1 = " + "
			sign2 = " - "
		type1q = (a + " = " + b + x + sign1 + c,a + " = " + n + x + sign1 + c,n + " = " + b + x + sign1 + c)
		type1a = (x + " = \\dfrac{" + a + sign2 + c + "}{" + b + "}",x + " = \\dfrac{" + a + sign2 + c + "}{" + n + "}",x + " = \\dfrac{" + n + sign2 + c + "}{" + b + "}")
		questions = (type1q,type1q)
		answers = (type1a,type1a)
		qlookup = random.randrange(0,len(questions))
		tlookup = random.randrange(0,len(questions[qlookup]))
		question = questions[qlookup][tlookup]
		answer = answers[qlookup][tlookup]
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + answer + "$")



def rearrange2(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Make x the subject of the formula "
		else:
			explanation = ""
		letters = ["a","b","c","d","e","f","g","h","j","k","m","n","p","q","r","t","y"]
		a = random.choice(letters)
		letters.remove(a)
		b = random.choice(letters)
		letters.remove(b)
		c = random.choice(letters)
		letters.remove(c)
		d = random.choice(letters)
		letters.remove(d)
		e = random.choice(letters)
		letters.remove(e)
		f = random.choice(letters)
		letters.remove(f)
		g = random.choice(letters)
		letters.remove(g)
		h = random.choice(letters)
		numbers = ("2","3","4","5","6","7","8")
		n = random.choice(numbers)
		x = "x"
		question = a + " = " + str(n) + x + "^{2}"
		answer = x + " = \\sqrt{\\dfrac{" + a + "}{" + str(n) + "}}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + answer + "$")



def rearrange3(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation = "Make x the subject of the formula "
		else:
			explanation = ""
		letters = ["a","b","c","d","e","f","g","h","j","k","m","n","p","q","r","t","y"]
		a = random.choice(letters)
		letters.remove(a)
		b = random.choice(letters)
		letters.remove(b)
		c = random.choice(letters)
		letters.remove(c)
		d = random.choice(letters)
		letters.remove(d)
		e = random.choice(letters)
		letters.remove(e)
		f = random.choice(letters)
		letters.remove(f)
		g = random.choice(letters)
		letters.remove(g)
		h = random.choice(letters)
		numbers = ("2","3","4","5","6","7","8")
		n = random.choice(numbers)
		x = "x"
		dec = random.randrange(0,2)
		if dec==0:
			question = a + " = " + x + "^{2} + " + n + c
			answer = x + " = \\sqrt{" + a + " - " + n + c + "}"
		else:
			question = a + " = " + x + "^{2} - " + n + c
			answer = x + " = \\sqrt{" + a + " + " + n + c + "}"
#write question
		tempquestions.write(explanation + "$" + question + "$")
		tempquestions.write("\n")
#write answer
		tempquestions.write("$" + answer + "$")
