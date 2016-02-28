# Coleco Zodiac table calculator
***Python script to create code tables for the [Coleco Zodiac](http://www.handheldmuseum.com/Coleco/Zodiac.htm) (which can be emulated by MAME 0.171 or later)***

Note that the codes computed by this script may differ slightly from those in the Coleco Zodiac manual (on pages 17 to 30, and 41 to 48, respectively).

## Output files

[Coleco_zodiac_table.txt](https://raw.githubusercontent.com/mdoege/coleco_zodiac_table/master/coleco_zodiac_table.txt) contains birth date output of the program from 1900 to 2100.

[Coleco_zodiac_advice_table.txt](https://raw.githubusercontent.com/mdoege/coleco_zodiac_table/master/coleco_zodiac_advice_table.txt) has date codes for daily preview and advice modes between 1979 and 2030.

## Prerequisites

Python3 and [PySwissEph](https://github.com/astrorigin/pyswisseph)

Coleco_table_create.py computes birth date codes.

Coleco_table_advice_preview_create.py computes date codes for daily preview and advice modes.

## Technical background

Table elements are a compact hexadecimal representation of the signs the astrological planets are in at that date.

So, first for each planet the current sign is computed for that date at noon, giving a value from 0 (Aries) to 11 (Pisces).

Then, for the left and right numbers, four planet positions each are combined as duodecimal digits (base 12) like this:

z = 12³ * n1 + 12² * n2 + 12 * n3 + n4

Left number (malefic planets):
n1 = Mars, n2 = Pluto, n3 = Uranus, n4 = Saturn

Right number (benefic planets):
n1 = Jupiter, n2 = Neptune, n3 = Venus, n4 = Sun

These numbers are then each converted to hexadecimal (base 16), with space padding for the left number and zero padding for the right.

Letters are replaced, because instead of the standard hexadecimal ABCDEF this table uses ADEJLP to represent 10 to 15.

Finally, if Mercury is one sign ahead (+) or behind the Sun (-), a plus or minus sign is added.

Strings are only printed if they change on that day from the previous day.

The only differences for daily preview/advice mode is that the Moon's sign is used where Pluto's sign it put in birth date codes. Also, the left number is zero-padded.
