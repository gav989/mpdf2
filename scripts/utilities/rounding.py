#rounding.py

def roundnearest(n,roundto):
	from math import log10, floor
	length = len(str(floor(n)))
	n = n * 10**(10-length)
	roundto = 10**(10-(length-(log10(roundto))))
	remainder = n%roundto
	if remainder < 0.5*roundto:
		rounded = n - remainder
	else:
		rounded = n + (roundto-remainder)
	rounded = rounded / 10**(10-length)
	if rounded%1==0:
		rounded = int(rounded)
	return rounded

def rounddp(n,dp): #rounds to decimal places but doesn't add zeros - for calculations, not answers
	from math import log10, floor
	roundto = 10**(dp*-1)
	length = len(str(floor(n)))
	n = n * 10**(10-length)
	roundto = 10**(10-(length-(log10(roundto))))
	remainder = n%roundto
	if remainder < 0.5*roundto:
		rounded = n - remainder
	else:
		rounded = n + (roundto-remainder)
	rounded = rounded / 10**(10-length)
	return rounded


def rounddpstring(n,dp): #returns string value with extra zeros
	from math import log10, floor
	roundto = 10**(dp*-1)
	length = len(str(floor(n)))
	n = n * 10**(10-length)
	roundto = 10**(10-(length-(log10(roundto))))
	remainder = n%roundto
	if remainder < 0.5*roundto:
		rounded = n - remainder
	else:
		rounded = n + (roundto-remainder)
	rounded = rounded / 10**(10-length)
	zeros = ""
	if rounded%1==0:
		rounded = int(rounded)
		zeros = "." + "0"*dp
	else:
		for i in range(1,dp):
			if (rounded*10**i)%1==0:
				zeros = "0"*(dp-i)
	rounded = str(rounded) + zeros
	return rounded

def roundsf(n,sf): #rounds to significant but doesn't add zeros - for calculations, not answers
	from math import log10,floor,ceil
	roundto = sf
	firstsig = ceil(log10(n))
	n = round(n * 10**(10-firstsig),1)
	roundto = 10**(10-roundto)
	remainder = n%roundto
	if remainder < 0.5*roundto:
		rounded = n - remainder
	else:
		rounded = n + (roundto-remainder)
	rounded = rounded / 10**(10-firstsig)
	return rounded


def roundsfstring(n,sf): #returns string value with extra zeros
	from math import log10,floor,ceil
	roundto = sf
	firstsig = ceil(log10(n))
	n = round(n * 10**(10-firstsig),1)
	roundto = 10**(10-roundto)
	remainder = n%roundto
	if remainder < 0.5*roundto:
		rounded = n - remainder
	else:
		rounded = n + (roundto-remainder)
	rounded = rounded / 10**(10-firstsig)
	if rounded%1==0:
		rounded = int(rounded)
	zeros = ""
	lastsig = 1
	test = rounded
	while test%1!=0:
		test = test * 10
		lastsig = lastsig - 1
	diff = abs(firstsig - lastsig)
	if (diff+1)<sf:
		if rounded%1==0:
			zeros = "." + "0" * (sf - diff - 1)
		else:
			zeros = "0" * (sf - diff - 1)
	rounded = str(rounded) + zeros
	return rounded
