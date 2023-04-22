"""
The isalpha() method returns True if all characters in a string are alphabetic
 (both lowercase and uppercase) and returns False if at least one character is
 not an alphabet. The whitespace, numerics, and symbols are considered as 
 non-alphabetical characters.
 
*******************************************************************************
# str.isalpha()
           
Return Value: Returns True OR False.

*******************************************************************************
Created on sat Mar 25 11:43:00 2023

@author: Hamed Sargoli


Link to Example:
    https://github.com/hamedsargoli/Python/tree/main/Example%20Function/String
"""

#----------------------------------------------------------------
#Example 1
print("Ex 1:" , '\n')

#1.1
mystr = 'HelloWorld'
print(mystr.isalpha())      # returns True
#1.2
mystr = 'HelloWorld '
print(mystr.isalpha())      # returns False
#1.3
mystr = 'HelloWorld!'
print(mystr.isalpha())      # returns False
#1.4
mystr = 'Hello World'
print(mystr.isalpha())      # returns False
#1.5
print('12345'.isalpha())    # returns False
#1.6
print('X12'.isalpha())      # returns False
#1.7
print('#Hundred'.isalpha()) # returns False


print('--------------------')

#----------------------------------------------------------------
#Example 2
#the following German word 'außen'.
print("Ex 2:" , '\n')


mystr = 'außen'
print(mystr.isalpha())     # Returns True


print('--------------------')

#----------------------------------------------------------------
# Example 3 
#  Working of isalpha()
print("Ex 3:" , '\n')


name = "HamedSargoli"

if name.isalpha() == True:
   print("All characters are alphabets")
else:
   print("All characters are not alphabets.")
   
   
   
print('--------------------')

#----------------------------------------------------------------