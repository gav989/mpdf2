#sf.py
#NUMBERS MUST BE PASSED AS STRINGS

def sftonum(num,power):
	from math import floor,log10,ceil
	if num=="0":
		result = "0"
	else:
		while num.find(".")!=-1 and num[-1:]=="0":
			num = num[:-1]
		if num[-1:]==".":
			num = num[:-1]
		while num[0]=="0" and num[1]!=".":
			num = num[1:]
		if power==0:
			result = "\\num{" + num + "}"
		elif power>0:
			if num.find(".")==-1:
				result = "\\num{" + num + "0"*power + "}"
			else:
				pointpos = num.find(".")
				prepoint = num[:pointpos]
				postpoint = num[-(len(num)-pointpos-1):]
				if power==len(postpoint):
					result = "\\num{" + prepoint + postpoint + "}"
				elif power>len(postpoint):
					power = power - len(postpoint)
					result = "\\num{" + prepoint + postpoint + "0"*power + "}"
				else:
					prepoint = prepoint + postpoint[:power]
					postpoint = postpoint[-(len(postpoint)-power):]
					result = "\\num{" + prepoint + "." + postpoint + "}"
		else:
			power = abs(power)
			if num.find(".")==-1:
				if power==len(num):
					result = "\\num{0." + num + "}"
				elif power>len(num):
					result = "\\num{0." + "0"*(power-len(num)) + num + "}"
				else:
					prepoint = num[:(len(num)-power)]
					postpoint = num[-power:]
					result = "\\num{" + prepoint + "." + postpoint + "}"
			else:
				pointpos = num.find(".")
				prepoint = num[:pointpos]
				postpoint = num[-(len(num)-pointpos-1):]
				if power==len(prepoint):

					result = "\\num{0." + prepoint + postpoint + "}"
				elif power>len(prepoint):
					power = power-len(prepoint)
					result = "\\num{0." + "0"*power + prepoint + postpoint + "}"
				else:
					postpoint = prepoint[-power:] + postpoint
					prepoint = prepoint[:len(prepoint)-power]
					result = "\\num{" + prepoint + "." + postpoint + "}"
	return result


def sftosf(num,power):
	if num=="0":
		result = "0"
	else:
		while num.find(".")!=-1 and num[-1:]=="0":
			num = num[:-1]
		if num[-1:]==".":
			num = num[:-1]
		while num[0]=="0" and num[1]!=".":
			num = num[1:]
		if len(num)==1:
			num = num
		elif num.find(".")==-1:
			power = power + len(num) - 1
			num = num[:1] + "." + num[-(len(num)-1):]
			while num[-1:]=="0":
				num = num[:-1]
		elif num.find(".")>1:
			while num[-1:]=="0":
				num = num[:-1]
			pointpos = num.find(".")
			prepoint = num[:pointpos]
			postpoint = num[-(len(num)-pointpos-1):]
			power = power + len(prepoint) - 1
			postpoint = prepoint[-(len(prepoint)-1):] + postpoint
			prepoint = prepoint[:1]
			num = prepoint + "." + postpoint
		elif num.find(".")==1 and num[0]=="0":
			while num[-1:]=="0":
				num = num[:-1]
			zerosafterpoint = 0
			while num[2+zerosafterpoint]=="0":
				zerosafterpoint = zerosafterpoint + 1
			power = power - zerosafterpoint - 1
			num = num[(2+zerosafterpoint):]
			num = num[0] + "." + num[1:]
		else:
			while num[-1:]=="0":
				num = num[:-1]
		if num[-1:]==".":
			num = num[:-1]
		power = str(power)
		result = num + " $\\times$ 10$^{" + power + "}$"
	return result
