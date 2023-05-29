#istitle
"""
The istitle() method checks whether each word's first character is upper case
 and the rest are in lower case or not. It returns True if a string is 
 titlecased; otherwise, it returns False. The symbols and numbers are ignored.
 
*******************************************************************************
# str.istitle()
           
Return Value: Returns True OR False.

*******************************************************************************
Created on sat May  12:19:00 2023

@author: Hamed Sargoli


Link to Example:
    https://github.com/hamedsargoli/Python/tree/main/Example%20Function/String
"""

#----------------------------------------------------------------
#Example 1
#The following example demonstrates the istitle() method.
print("Ex 1:" , '\n')

#1.1
mystr = 'Hello World'
print('1.1->' , mystr.istitle())      # returns True

#1.2
mystr = 'Hello WORLD'
print('1.2->' , mystr.istitle())      # returns False

#1.3
mystr = 'hello world'
print('1.3->' , mystr.istitle())      # returns False

#1.4
mystr = 'HelloWorld'
print('1.4->' , mystr.istitle())      # returns False

#1.5
mystr = 'Python Is Good.'
print('1.5->' , mystr.istitle())      # returns True

#1.6
mystr = 'This Is @ Symbol.'
print('1.6->' , mystr.istitle())      # returns True

#1.7
mystr = '#1 Harbor Side'
print('1.7->' , mystr.istitle())      # returns True

#1.8
mystr = '1 Central Park'
print('1.8->' , mystr.istitle())      # returns True

#1.9
mystr = "This Is %'!?"
print('1.9->' , mystr.istitle())      # returns True


print('--------------------')

#----------------------------------------------------------------
#Example 2 
#An empty string, numeric string, or a string with only symbols are not 
# considered titlecased.
print("Ex 2:" , '\n')

#2.1
mystr = ''
print('2.1->' , mystr.istitle())      # returns False

#2.2
mystr = '100'
print('2.2->' , mystr.istitle())      # returns False

#2.3
mystr = '#'
print('2.3->' , mystr.istitle())      # returns False
   
print('--------------------')

#----------------------------------------------------------------