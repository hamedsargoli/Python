# isnumeric() Function
"""
Created on Tue Feb 21 22:16:14 2023

@author: Hamed Sargoli

Link Unicode table : https://www.tamasoft.co.jp/en/general-info/unicode.html
"""


#----------------------------------------------------------------
#Example 1
print('\nEx1:')
var1="123"
var2="12.3"
var3="-123"
print(var1.isnumeric())
print(var2.isnumeric())
print(var3.isnumeric())


#----------------------------------------------------------------
#Example 2
print('\nEx2:')
str = "Welcome to 2023"
result=str.isnumeric()
print(f" Are all the characters of the '{str}' numeric?", result)


#----------------------------------------------------------------
#Example 3
print('\nEx3:')

unicode = "\u0030"             # unicode for 0
superscript_string = '²3455'   # string with superscript 
fraction_string = '½123'       # string with fraction value 

result_1=unicode.isnumeric()
result_2=superscript_string.isnumeric()
result_3=fraction_string.isnumeric()

print(" Are all the characters of the '\u0030' numeric?", result_1)
print(f" Are all the characters of the '{superscript_string}' numeric?", result_2)
print(f" Are all the characters of the '{fraction_string}' numeric?", result_3)


#----------------------------------------------------------------
#Example 4
print('\nEx4:')
char_number = ''
var = '***Tell number = +98 912 1111111 #***'
for i in var:
    if i.isnumeric():
        char_number += i
print(' var is = ' , var)
print(' number in var = ' , char_number)

