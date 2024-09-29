#!/usr/bin/env python3
#figwords.py
def figwords(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Write "
			explanation2 = " in words"
		else:
			explanation1 = ""
			explanation2 = ""
		length = random.randrange(4,8)
		if length==7:
			a = random.randrange(1,10)
		else:
			a = ""
		if length==6:
			b = random.randrange(1,10)
		elif length>5:
			b = random.randrange(0,10)
		else:
			b = ""
		if length==5:
			c = random.randrange(1,10)
		elif length>4:
			c = random.randrange(0,10)
		else:
			c = ""
		if length==4:
			d = random.randrange(1,10)
		else:
			d = random.randrange(0,10)
		e = random.randrange(0,10)
		f = random.randrange(0,10)
		g = random.randrange(0,10)
		figures = "\\num{" + str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g)  + "}"
		units = {0:"",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
		teens = {0:"ten",1:"eleven",2:"twelve",3:"thirteen",4:"fourteen",5:"fifteen",6:"sixteen",7:"seventeen",8:"eighteen",9:"nineteen"}
		tens = {2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}
		if a!="":
			a = units[a] + " million "
		if b!="" and b!=0:
			b = units[b] + " hundred "
			if c!="":
				b = b + "and "
		else:
			b = ""
		if c==1:
			cd = teens[d]
		elif c==0 or c=="":
			cd = units[d]
		elif d==0:
			cd = tens[c]
		else:
			cd = tens[c] + "-" + units[d]
		if e!=0:
			e = units[e] + " hundred "
		else:
			e = ""
		if f==1:
			fg = teens[g]
		elif f==0:
			fg = units[g]
		elif g==0:
			fg = tens[f]
		else:
			fg = tens[f] + "-" + units[g]
		words = a + b + cd + " thousand " + e + "and " + fg
			
#write question
		tempquestions.write(explanation1 + figures + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(words)



def wordfigs(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Write "
			explanation2 = " in figures"
		else:
			explanation1 = ""
			explanation2 = ""
		length = random.randrange(4,8)
		if length==7:
			a = random.randrange(1,10)
		else:
			a = ""
		if length==6:
			b = random.randrange(1,10)
		elif length>5:
			b = random.randrange(0,10)
		else:
			b = ""
		if length==5:
			c = random.randrange(1,10)
		elif length>4:
			c = random.randrange(0,10)
		else:
			c = ""
		if length==4:
			d = random.randrange(1,10)
		else:
			d = random.randrange(0,10)
		e = random.randrange(0,10)
		f = random.randrange(0,10)
		g = random.randrange(0,10)
		figures = "\\num{" + str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g)  + "}"
		units = {0:"",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
		teens = {0:"ten",1:"eleven",2:"twelve",3:"thirteen",4:"fourteen",5:"fifteen",6:"sixteen",7:"seventeen",8:"eighteen",9:"nineteen"}
		tens = {2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}
		if a!="":
			a = units[a] + " million "
		if b!="" and b!=0:
			b = units[b] + " hundred "
			if c!="":
				b = b + "and "
		else:
			b = ""
		if c==1:
			cd = teens[d]
		elif c==0 or c=="":
			cd = units[d]
		elif d==0:
			cd = tens[c]
		else:
			cd = tens[c] + "-" + units[d]
		if e!=0:
			e = units[e] + " hundred "
		else:
			e = ""
		if f==1:
			fg = teens[g]
		elif f==0:
			fg = units[g]
		elif g==0:
			fg = tens[f]
		else:
			fg = tens[f] + "-" + units[g]
		words = a + b + cd + " thousand " + e + "and " + fg
			
#write question
		tempquestions.write(explanation1 + words + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(figures)



def figwordsnomill(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Write "
			explanation2 = " in words"
		else:
			explanation1 = ""
			explanation2 = ""
		length = random.randrange(4,7)
		if length==7:
			a = random.randrange(1,10)
		else:
			a = ""
		if length==6:
			b = random.randrange(1,10)
		elif length>5:
			b = random.randrange(0,10)
		else:
			b = ""
		if length==5:
			c = random.randrange(1,10)
		elif length>4:
			c = random.randrange(0,10)
		else:
			c = ""
		if length==4:
			d = random.randrange(1,10)
		else:
			d = random.randrange(0,10)
		e = random.randrange(0,10)
		f = random.randrange(0,10)
		g = random.randrange(0,10)
		figures = "\\num{" + str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g)  + "}"
		units = {0:"",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
		teens = {0:"ten",1:"eleven",2:"twelve",3:"thirteen",4:"fourteen",5:"fifteen",6:"sixteen",7:"seventeen",8:"eighteen",9:"nineteen"}
		tens = {2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}
		if a!="":
			a = units[a] + " million "
		if b!="" and b!=0:
			b = units[b] + " hundred "
			if c!="":
				b = b + "and "
		else:
			b = ""
		if c==1:
			cd = teens[d]
		elif c==0 or c=="":
			cd = units[d]
		elif d==0:
			cd = tens[c]
		else:
			cd = tens[c] + "-" + units[d]
		if e!=0:
			e = units[e] + " hundred "
		else:
			e = ""
		if f==1:
			fg = teens[g]
		elif f==0:
			fg = units[g]
		elif g==0:
			fg = tens[f]
		else:
			fg = tens[f] + "-" + units[g]
		words = a + b + cd + " thousand " + e + "and " + fg
			
#write question
		tempquestions.write(explanation1 + figures + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(words)



def wordfigsnomill(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Write "
			explanation2 = " in figures"
		else:
			explanation1 = ""
			explanation2 = ""
		length = random.randrange(4,7)
		if length==7:
			a = random.randrange(1,10)
		else:
			a = ""
		if length==6:
			b = random.randrange(1,10)
		elif length>5:
			b = random.randrange(0,10)
		else:
			b = ""
		if length==5:
			c = random.randrange(1,10)
		elif length>4:
			c = random.randrange(0,10)
		else:
			c = ""
		if length==4:
			d = random.randrange(1,10)
		else:
			d = random.randrange(0,10)
		e = random.randrange(0,10)
		f = random.randrange(0,10)
		g = random.randrange(0,10)
		figures = "\\num{" + str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g)  + "}"
		units = {0:"",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
		teens = {0:"ten",1:"eleven",2:"twelve",3:"thirteen",4:"fourteen",5:"fifteen",6:"sixteen",7:"seventeen",8:"eighteen",9:"nineteen"}
		tens = {2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}
		if a!="":
			a = units[a] + " million "
		if b!="" and b!=0:
			b = units[b] + " hundred "
			if c!="":
				b = b + "and "
		else:
			b = ""
		if c==1:
			cd = teens[d]
		elif c==0 or c=="":
			cd = units[d]
		elif d==0:
			cd = tens[c]
		else:
			cd = tens[c] + "-" + units[d]
		if e!=0:
			e = units[e] + " hundred "
		else:
			e = ""
		if f==1:
			fg = teens[g]
		elif f==0:
			fg = units[g]
		elif g==0:
			fg = tens[f]
		else:
			fg = tens[f] + "-" + units[g]
		words = a + b + cd + " thousand " + e + "and " + fg
			
#write question
		tempquestions.write(explanation1 + words + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(figures)

def figwordsthousands(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Write "
			explanation2 = " in words"
		else:
			explanation1 = ""
			explanation2 = ""
		d = random.randrange(1,10)
		e = random.randrange(0,10)
		f = random.randrange(0,10)
		g = random.randrange(0,10)
		figures = "\\num{" + str(d) + str(e) + str(f) + str(g)  + "}"
		units = {0:"",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
		teens = {0:"ten",1:"eleven",2:"twelve",3:"thirteen",4:"fourteen",5:"fifteen",6:"sixteen",7:"seventeen",8:"eighteen",9:"nineteen"}
		tens = {2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}
		cd = units[d]
		if e!=0:
			e = units[e] + " hundred "
		else:
			e = ""
		if f==1:
			fg = teens[g]
		elif f==0:
			fg = units[g]
		elif g==0:
			fg = tens[f]
		else:
			fg = tens[f] + "-" + units[g]
		words = cd + " thousand " + e + "and " + fg
#write question
		tempquestions.write(explanation1 + figures + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(words)



def wordfigsthousands(n,explanationn):
	import random
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		if explanationn==1:
			explanation1 = "Write "
			explanation2 = " in figures"
		else:
			explanation1 = ""
			explanation2 = ""
		d = random.randrange(1,10)
		e = random.randrange(0,10)
		f = random.randrange(0,10)
		g = random.randrange(0,10)
		figures = "\\num{" + str(d) + str(e) + str(f) + str(g)  + "}"
		units = {0:"",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
		teens = {0:"ten",1:"eleven",2:"twelve",3:"thirteen",4:"fourteen",5:"fifteen",6:"sixteen",7:"seventeen",8:"eighteen",9:"nineteen"}
		tens = {2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}
		cd = units[d]
		if e!=0:
			e = units[e] + " hundred "
		else:
			e = ""
		if f==1:
			fg = teens[g]
		elif f==0:
			fg = units[g]
		elif g==0:
			fg = tens[f]
		else:
			fg = tens[f] + "-" + units[g]
		words = cd + " thousand " + e + "and " + fg	
#write question
		tempquestions.write(explanation1 + words + explanation2)
		tempquestions.write("\n")
#write answer
		tempquestions.write(figures)
