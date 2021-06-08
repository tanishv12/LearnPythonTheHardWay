#WhatWasThat?
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
Ill do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)




#This is all of the escape sequences Python supports. You may not use many of these, but memorize their
#format and what they do anyway. Try them out in some strings to see if you can make them work.
#Escape What it does.
#\\ Backslash (\)
#\' Single-quote (’)
#\" Double-quote (”)
#\a ASCII bell (BEL)
#\b ASCII backspace (BS)
#\f ASCII formfeed (FF)
#\n ASCII linefeed (LF)
#\N{name} Character named name in the Unicode database (Unicode only)
#\r Carriage Return (CR)
#\t Horizontal Tab (TAB)
#\uxxxx Character with 16-bit hex value xxxx
#\Uxxxxxxxx Character with 32-bit hex value xxxxxxxx
#\v ASCII vertical tab (VT)
#\ooo Character with octal value ooo
#\xhh Character with hex value hh