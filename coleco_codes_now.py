#!/usr/bin/python
# Print current Coleco Zodiac date codes
# (needs Python 3 and PySwissEph)
# 2016-02-29

import datetime
import swisseph as s

planets = (s.SUN, s.MERCURY, s.VENUS, s.MARS, s.JUPITER, s.SATURN, s.URANUS, s.NEPTUNE, s.PLUTO, s.MOON)
r = (
('A','a'),
('D','b'),
('E','c'),
('J','d'),
('L','e'),
('P','f')
)

sn = 10*[0]
n = datetime.datetime.utcnow()
j = s.julday(n.year, n.month, n.day, n.hour + n.minute / 60.)

for n, b in enumerate(planets):
	ra = (s.calc_ut(j, b))[0]
	sn[n] = int(ra//30.)
#####################################################################

p = sn[3]*1728+sn[8]*144+sn[6]*12+sn[5]
q = sn[4]*1728+sn[7]*144+sn[2]*12+sn[0]
p = "{0:x}".format(p)
q = "{0:x}".format(q)
if len(p) < 4:
	p = (4-len(p)) * ' ' + p
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
print("Birth date code\t\t\t%s" % (out))
#####################################################################


p = sn[3]*1728+sn[9]*144+sn[6]*12+sn[5]
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
print("Daily preview/advice date code\t%s" % (out))
#####################################################################


