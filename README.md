# Coleco Zodiac table calculator
***Python script to create birthday tables for the [Coleco Zodiac](http://www.handheldmuseum.com/Coleco/Zodiac.htm) (which can be emulated by MAME 0.171 or later)***

Note that the codes computed by this script may differ slightly from those in the Coleco Zodiac manual (on pages 17 to 30).

Also note the daily preview/advice codes seem to work differently and that this table is not for them!

## Output

Coleco_zodiac_table.txt contains output of the program from 1900 to 2100.

## Prerequisites

Python3 and [PySwissEph](https://github.com/astrorigin/pyswisseph)

## Technical Background

Table elements are a compact hexadecimal representation of the signs the astrological planets are in at that date.

So, first the current sign is computed for that date at noon, giving a value from 0 (Aries) to 11 (Pisces).

Then, for the left and right numbers, four planets each are combined in duodecimal (base 12) like this:

z = 12³ * n1 + 12² * n2 + 12 * n3 + n4

Left number (malefics):
n1 = Mars, n2 = Pluto, n3 = Uranus, n4 = Saturn

Right number (benefics):
n1 = Jupiter, n2 = Neptune, n3 = Venus, n4 = Sun

These numbers are then each converted to hexadecimal (base 16), with space padding for the left number and zero padding for the right.

Letters are replaced, because instead of the standard hexadecimal ABCDEF this table uses ADEJLP to represent 10 to 15.

Finally, if Mercury is one sign ahead (+) or behind the Sun (-), a plus or minus sign is added.

Strings are only printed if they change on that day from the previous day.
