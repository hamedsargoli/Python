# Str.isascii() 
"""
Created on Fri Mar 5 23:10:21 2023

@author: Hamed Sargoli


(0000 ~ 007F) -> True

Link Unicode table : 
    https://www.tamasoft.co.jp/en/general-info/unicode.html

Link to Example:
    https://github.com/hamedsargoli/Python/tree/main/Example%20Function/String
"""

#----------------------------------------------------------------
#Example

mystr = "\u00e2"                        # Unicode of â
print(f"1- '{mystr}':"  , mystr.isascii())
print('--------------------')

mystr = '\u00f8'                        # Unicode of ø
print(f"2- '{mystr}':" , mystr.isascii())
print('--------------------')

mystr = 'õ'  
print(f"3- '{mystr}':" , mystr.isascii())
print('--------------------')

mystr = 'Å' 
print(f"4- '{mystr}':" , mystr.isascii())
print('--------------------')

mystr = 'ß'                             # German letter
print(f"5- '{mystr}':" , mystr.isascii())
print('--------------------')

mystr = '\u0000'                        # Unicode of Null
print("6- null string:" , mystr.isascii())
print('--------------------')

mystr = '\u0041'                        # Unicode of A
print(f"7- '{mystr}':" , mystr.isascii())
print('--------------------')

mystr = '\u0061'                        # Unicode of a
print(f"8- '{mystr}':" , mystr.isascii())
print('--------------------')

mystr = '\u007f'                        # Unicode of DEL
print(f"9- '{mystr}':" , mystr.isascii())
print('--------------------')

mystr = '#'
print(f"10- '{mystr}':" , mystr.isascii())
print('--------------------')

mystr = '$'
print(f"11- '{mystr}':" , mystr.isascii())
print('--------------------')

mystr = ''
print("12- empty string:" , mystr.isascii())
print('--------------------')

mystr = '\n'
print("13- \ n:" , mystr.isascii())
print('--------------------')

mystr = 'ABC'
print(f"14- '{mystr}':" , mystr.isascii())
print('--------------------')

mystr = '012345'
print(f"15- '{mystr}':" , mystr.isascii())
print('--------------------')

mystr = 'Room 26'
print(f"16- '{mystr}':" , mystr.isascii())
print('--------------------')
