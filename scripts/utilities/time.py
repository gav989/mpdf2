#time.py

def timestring(h3,m3):
#used for train timetables question, 24h, no colon
	from math import floor
	h3 = h3 + floor(m3/60)
	m3 = m3%60
	if h3>23:
		h3 = h3-24
	if h3==0:
		h3 = "00"
	elif h3<10:
		h3 = "0" + str(h3)
	else:
		h3 = str(h3)
	if m3==0:
		m3 = "00"
	elif m3<10:
		m3 = "0" + str(m3)
	else:
		m3 = str(m3)
	result = h3 + m3
	return result


def timeadd(t1,t2):
#used for train timetables question, 24h, no colon
	from math import floor
	h1 = int(t1[:2])
	m1 = int(t1[-2:])
	h2 = int(t2[:2])
	m2 = int(t2[-2:])
	h3 = h1 + h2
	m3 = m1 + m2
	h3 = h3 + floor(m3/60)
	m3 = m3%60
	if h3>23:
		h3 = h3-24
	if h3==0:
		h3 = "00"
	elif h3<10:
		h3 = "0" + str(h3)
	else:
		h3 = str(h3)
	if m3==0:
		m3 = "00"
	elif m3<10:
		m3 = "0" + str(m3)
	else:
		m3 = str(m3)
	result = h3 + m3
	return result

def timesub(t1,t2):
#UNTESTED
#used for train timetables question, 24h, no colon
	from math import floor
	h1 = int(t1[:2])
	m1 = int(t1[-2:])
	h2 = int(t2[:2])
	m2 = int(t2[-2:])
	h3 = h1 - h2
	m3 = m1 - m2
	while m3<0:
		m3 = m3+60
		h3 = h3-1
	while h3<0:
		h3 = h3+24
	h3 = h3 + floor(m3/60)
	m3 = m3%60
	if h3>23:
		h3 = h3-24
	if h3==0:
		h3 = "00"
	elif h3<10:
		h3 = "0" + str(h3)
	else:
		h3 = str(h3)
	if m3==0:
		m3 = "00"
	elif m3<10:
		m3 = "0" + str(m3)
	else:
		m3 = str(m3)
	result = h3 + m3
	return result


