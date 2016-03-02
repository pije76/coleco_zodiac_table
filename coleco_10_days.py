#!/usr/bin/python
# Calculate Coleco Zodiac "daily preview/advice date codes"
# since last midnight and during the next ten days
# (needs Python 3 and PySwissEph)
# 2016-03-01

import datetime
import swisseph as s

planets = (s.SUN, s.MERCURY, s.VENUS, s.MARS, s.JUPITER, s.SATURN, s.URANUS, s.NEPTUNE, s.MOON)
r = (
('A','a'),
('D','b'),
('E','c'),
('J','d'),
('L','e'),
('P','f')
)

sn = 9*[0]
old=''

n = datetime.datetime.utcnow()

date1 = "%4u-%02u-%02u" % (n.year, n.month, n.day)
startdate = datetime.datetime.strptime(date1, '%Y-%m-%d')
enddate = startdate + datetime.timedelta(days=10)
step = datetime.timedelta(hours=1)

while startdate <= enddate:
	out = ''
	y,m,d = startdate.year, startdate.month, startdate.day
	hh,mm = startdate.hour, startdate.minute
	j = s.julday(y, m, d, hh)
	for n, b in enumerate(planets):
		ra = (s.calc_ut(j, b))[0]
		sn[n] = int(ra//30.)
	p = sn[3]*1728+sn[8]*144+sn[6]*12+sn[5]
	q = sn[4]*1728+sn[7]*144+sn[2]*12+sn[0]
	p = "{0:x}".format(p)
	q = "{0:x}".format(q)
	if len(p) < 4:
		p = (4-len(p)) * '0' + p
	if len(q) < 4:
		q = (4-len(q)) * '0' + q
	for xx,yy in r:
		p = p.replace(yy,xx)
		q = q.replace(yy,xx)
	dmer = sn[1] - sn[0]
	if dmer == 1 or dmer == -11:
		mer = '+'
	elif dmer == -1 or dmer == 11:
		mer = '-'
	else:
		mer = ' '
	out = "%s %s %s" % (p, q, mer)
	if out != old:
		print("%2u/%2u/%4u %02u:%02u \t%s" % (m, d, y, hh, mm, out))
		old = out
	startdate += step


