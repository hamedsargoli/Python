# isdecimal() Function
"""
Created on Fri Feb 28 20:31:21 2023

@author: Hamed Sargoli


*** is decimal only (0-9) ***

Link to Example:
    https://github.com/hamedsargoli/Python/tree/main/Example%20Function/String
"""


#----------------------------------------------------------------
#Example 1
print('\nExample 1:')

var1="123"
var2="\u0030"   # unicode for 0
print(f'  "{var1}" is decimal : '       , var1.isdecimal())
print(f'  "{var2}"   is decimal : '     , var2.isdecimal())

#----------------------------------------------------------------
#Example 2
print('\nExample 2:')

var1 = "22.5"
var2 = "-225"
var3 = '\u2730'

#isnumeric() -> True
var4 = '\u00BD'      # string with fraction value   "½"
var5 = '\u00B23455'  # string with superscript      "²3455"
var6 = "\u2162"      # string with Roman Numeral    "Ⅲ"

print(f'  "{var1}"  is decimal : '      , var1.isdecimal())
print(f'  "{var2}"  is decimal : '      , var2.isdecimal())
print(f'  "{var3}"    is decimal : '    , var3.isdecimal())
print(f'  "{var4}"     is decimal : '   , var4.isdecimal())
print(f'  "{var5}" is decimal : '       , var5.isdecimal())
print(f'  "{var6}"    is decimal : '    , var6.isdecimal())
