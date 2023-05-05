# isdigit() Function
"""
The isdigit() method returns True if all characters in a string are digits or
 Unicode char of a digit. If not, it returns False.
*******************************************************************************
# str.isdigit()
         
Return Value: Returns True Or False.

*******************************************************************************
Created on April 27 06:30:21 2023

@author: Hamed Sargoli


Link to Example:
    https://github.com/hamedsargoli/Python/tree/main/Example%20Function/String
"""


#----------------------------------------------------------------
# Example 1 
print("Ex 1:" , '\n')

#1.1
mystr = '12345'
print("mystr is:     "  , mystr)
print("isdigit   --> "  , mystr.isdigit() , "\n")   
#1.2
mystr = '\u0039'
print("mystr is:     "  , mystr)
print("isdigit   --> "  , mystr.isdigit() , "\n")   # Unicode char for 9
#1.3
mystr = '۶' 
print("mystr is:     "  , mystr)
print("isdigit   --> "  , mystr.isdigit() , "\n")   # persian digit 6
#1.4
mystr = '10.5'
print("mystr is:     "  , mystr)
print("isdigit   --> "  , mystr.isdigit() , "\n")   #.
#1.5
mystr = 'python'
print("mystr is:     "  , mystr)
print("isdigit   --> "  , mystr.isdigit() , "\n")   #string
#1.6
mystr = '$100'
print("mystr is:     "  , mystr)
print("isdigit   --> "  , mystr.isdigit() , "\n")   #$
#1.7
mystr = '105 '
print("mystr is:     "  , mystr)
print("isdigit   --> "  , mystr.isdigit() , "\n")   #space
#1.8
mystr = '\u0038\u0061'  
print("mystr is:     "  , mystr)
print("isdigit   --> "  , mystr.isdigit() , "\n")   # Unicode char 8a


print('--------------------')
#----------------------------------------------------------------
# Example 2 
# isdigit vs isdecimal vs isnumeric
print("Ex 2:" , '\n')


import itertools
line = '-' * 52
print(line)
print("| number | isdigit | isdecimal | isnumeric | char  |")
print(line)
for number in itertools.chain(range(1000), range(4969, 4978), range(8304, 11000)):
    char = chr(number)
    if (char.isdigit() or char.isdecimal() or char.isnumeric()):
        print('|{0:^8}|{1:^9}|{2:^11}|{3:^11}|{4:^7}|'.format
              (
            number,
            '+' if char.isdigit() else '-',
            '+' if char.isdecimal() else '-',
            '+' if char.isnumeric() else '-',
            char
              )
             )  


print(line)
#----------------------------------------------------------------
