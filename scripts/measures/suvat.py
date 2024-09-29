#!/usr/bin/env python3
#suvat.py

def suvat1pos(n,explanationn):
	import random
	from math import sqrt
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		dec = random.randrange(0,3)
		if dec==1:
			u = random.randrange(0,101)
			a = random.randrange(1,21)
			t = random.randrange(2,101)
			v = u + a*t
			question = "Find the final velocity when initial velocity is " + str(u) + "ms$^{-1}$, acceleration is " + str(a) + "ms$^{-2}$ and time is " + str(t) + " seconds."
			answer = str(v) + "ms$^{-1}$"
		elif dec==2:
			u = random.randrange(0,101)
			t = random.randrange(5,101)
			a = random.randrange(1,21)
			s = u*t + .5*a*t**2
			if s%1==0:
				s = int(s)
			else:
				s = rounddp(s,2)
			question = "Find the displacement when initial velocity is " + str(u) + "ms$^{-1}$, acceleration is " + str(a) + "ms$^{-2}$ and time is " + str(t) + " seconds."
			answer = str(s) + "m"
		else:
			u = random.randrange(0,101)
			a = random.randrange(1,21)
			s = random.randrange(100,10000)
			v = sqrt(u**2 + 2*a*s)
			if v%1==0:
				v = int(v)
			else:
				v = rounddp(v,2)
			question = "Find the final velocity when initial velocity is " + str(u) + "ms$^{-1}$, acceleration is " + str(a) + "ms$^{-2}$ and displacement is " + str(s) + "m."
			answer = str(v) + "ms$^{-1}$"
			
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def suvat1(n,explanationn):
	import random
	from math import sqrt,ceil
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		dec = random.randrange(0,3)
		if dec==1:
			u = random.randrange(0,101)
			a = random.randrange(1,21) * (-1)**random.randrange(1,3)
			t = random.randrange(2,101)
			v = u + a*t
			question = "Find the final velocity when initial velocity is " + str(u) + "ms$^{-1}$, acceleration is " + str(a) + "ms$^{-2}$ and time is " + str(t) + " seconds."
			answer = str(v) + "ms$^{-1}$"
		elif dec==2:
			u = random.randrange(0,101)
			t = random.randrange(5,101)
			a = random.randrange(1,21) * (-1)**random.randrange(1,3)
			s = u*t + .5*a*t**2
			if s%1==0:
				s = int(s)
			else:
				s = rounddp(s,2)
			question = "Find the displacement when initial velocity is " + str(u) + "ms$^{-1}$, acceleration is " + str(a) + "ms$^{-2}$ and time is " + str(t) + " seconds."
			answer = str(s) + "m"
		else:
			dec2 = random.randrange(0,4)
			if dec2==1:
				u = random.randrange(0,101)
				a = random.randrange(1,21)
				s = random.randrange(100,10000)
			elif dec2==2:
				u = random.randrange(0,101)
				a = random.randrange(1,21) * (-1)
				s = random.randrange(100,10000) * (-1)
			elif dec2==3:
				a = random.randrange(1,21) * (-1)
				s = random.randrange(100,10000)
				umin = ceil(sqrt(abs(2*a*s)))
				u = random.randrange(umin,umin + 50)
			else:
				a = random.randrange(1,21)
				s = random.randrange(100,10000) * -1
				umin = ceil(sqrt(abs(2*a*s)))
				u = random.randrange(umin,umin + 50)
			v = sqrt(u**2 + 2*a*s)
			if v%1==0:
				v = int(v)
			else:
				v = rounddp(v,2)
			question = "Find the final velocity when initial velocity is " + str(u) + "ms$^{-1}$, acceleration is " + str(a) + "ms$^{-2}$ and displacement is " + str(s) + "m."
			answer = str(v) + "ms$^{-1}$"
			
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)



def suvat2pos(n,explanationn):
	import random
	from math import sqrt
	from utilities.rounding import rounddp
	for x in range(0, n):
		tempquestions = open("tempquestions","a")
		tempquestions.write("\n")
#create question
		dec = random.randrange(0,3)
		if dec==1:
			dec2=random.randrange(0,4)
			if dec2==1:
				u = random.randrange(0,101)
				a = random.randrange(1,21)
				t = random.randrange(2,101)
				v = u + a*t
				question = "Find the final velocity when initial velocity is " + str(u) + "ms$^{-1}$, acceleration is " + str(a) + "ms$^{-2}$ and time is " + str(t) + " seconds."
				answer = str(v) + "ms$^{-1}$"
			elif dec2==2:
				a = random.randrange(1,21)
				t = random.randrange(2,101)
				v = random.randrange(a*t+1,a*t+51)
				u = v - a*t
				question = "Find the initial velocity when final velocity is " + str(v) + "ms$^{-1}$, acceleration is " + str(a) + "ms$^{-2}$ and time is " + str(t) + " seconds."
				answer = str(u) + "ms$^{-1}$"
			elif dec2==3:
				u = random.randrange(0,101)
				v = u + random.randrange(1,51)
				t = random.randrange(2,101)
				a = rounddp((v-u)/t,2)
				if a%1==0:
					a = int(a)
				question = "Find the acceleration when initial velocity is " + str(u) + "ms$^{-1}$, final velocity is " + str(v) + "ms$^{-1}$ and time is " + str(t) + " seconds."
				answer = str(a) + "ms$^{-2}$"
			else:
				u = random.randrange(0,101)
				v = u + random.randrange(1,51)
				a = random.randrange(1,21)
				t = rounddp((v-u)/a,2)
				if a%1==0:
					a = int(a)
				question = "Find the time when initial velocity is " + str(u) + "ms$^{-1}$, final velocity is " + str(v) + "ms$^{-1}$ and acceleration is " + str(a) + " ms$^{-2}$."
				answer = str(t) + " seconds"
		elif dec==2:
			dec2 = random.randrange(0,4)
			if dec2==1:
				u = random.randrange(0,101)
				t = random.randrange(5,101)
				a = random.randrange(1,21)
				s = u*t + .5*a*t**2
				if s%1==0:
					s = int(s)
				else:
					s = rounddp(s,2)
				question = "Find the displacement when initial velocity is " + str(u) + "ms$^{-1}$, acceleration is " + str(a) + "ms$^{-2}$ and time is " + str(t) + " seconds."
				answer = str(s) + "m"
			elif dec2==2:
				t = random.randrange(5,101)
				a = random.randrange(1,21)
				smin = int(0.5 * a * t**2 + 1)
				s = random.randrange(smin, smin+51)
				u = rounddp((s - 0.5 * a * t**2)/t,2)
				if u%1==0:
					u = int(u)	
				question = "Find the initial velocity when displacement is " + str(s) + "m, acceleration is " + str(a) + "ms$^{-2}$ and time is " + str(t) + " seconds."
				answer = str(u) + "ms$^{-1}$"
			elif dec2==3:
				u = random.randrange(0,101)
				t = random.randrange(5,101)
				smin = u*t + 1
				s = random.randrange(smin,smin + 50)
				a = rounddp((s - u*t)/(0.5*t**2),2)
				if a%1==0:
					a = int(a)
				question = "Find the acceleration when displacement is " + str(s) + "m, initial velocity is " + str(u) + "ms$^{-1}$ and time is " + str(t) + " seconds."
				answer = str(a) + "ms$^{-2}$"
			else:
				u = random.randrange(0,101)
				a = random.randrange(1,21)
				s = random.randrange(100,1000)
				t1 = rounddp(((-1)*u + sqrt(2*a*s + u))/a,2)
				t2 = rounddp(((-1)*u - sqrt(2*a*s + u))/a,2)
				if t1%1==0:
					t1 = int(t1)
				if t2%1==0:
					t2 = int(t2)
				if t1>t2:
					t = t1
				else:
					t = t2
				question = "Find the time when displacement is " + str(s) + "m, initial velocity is " + str(u) + "ms$^{-1}$ and acceleration is " + str(a) + " ms$^{-2}$."
				answer = str(t) + " seconds"
		else:
			dec2=random.randrange(0,4)
			if dec2==1:
				u = random.randrange(0,101)
				a = random.randrange(1,21)
				s = random.randrange(100,10000)
				v = sqrt(u**2 + 2*a*s)
				if v%1==0:
					v = int(v)
				else:
					v = rounddp(v,2)
				question = "Find the final velocity when initial velocity is " + str(u) + "ms$^{-1}$, acceleration is " + str(a) + "ms$^{-2}$ and displacement is " + str(s) + "m."
				answer = str(v) + "ms$^{-1}$"
			elif dec2==1:
				a = random.randrange(1,21)
				s = random.randrange(100,10000)
				vmin = 2*a*s + 1
				v = random.randrange(vim,vmin+51)
				u = rounddp(sqrt(v**2 - 2 * a * s),2)
				if u%1==0:
					u = int(u)
				question = "Find the initial velocity when final velocity is " + str(v) + "ms$^{-1}$, acceleration is " + str(a) + "ms$^{-2}$ and displacement is " + str(s) + "m."
				answer = str(v) + "ms$^{-1}$"
			elif dec2==3:
				u = random.randrange(0,101)
				v = u + random.randrange(1,51)
				s = random.randrange(100,10000)
				a = rounddp((v**2 - u**2)/(2*s),2)
				if a%1==0:
					a = int(a)
				question = "Find the acceleration when initial velocity is " + str(u) + "ms$^{-1}$, final velocity is " + str(v) + "ms$^{-1}$ and displacement is " + str(s) + "m."
				answer = str(a) + "ms$^{-2}$"
			else:
				u = random.randrange(0,101)
				v = u + random.randrange(1,51)
				a = random.randrange(1,21)
				s = rounddp((v**2 - u**2)/(2*a),2)
				if s%1==0:
					s = int(s)
				question = "Find the displacement when initial velocity is " + str(u) + "ms$^{-1}$, final velocity is " + str(v) + "ms$^{-1}$ and acceleration is " + str(a) + "ms$^{-2}$."
				answer = str(s) + "m"
#write question
		tempquestions.write(question)

		tempquestions.write("\n")
#write answer
		tempquestions.write(answer)
