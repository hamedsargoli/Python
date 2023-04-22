"""
The lower() method returns the copy of the original string wherein all the
 characters are converted to lowercase. If no uppercase characters present,
 it returns the original string. Symbols and numbers remain unaffected by
 this function.
*******************************************************************************
# str.lower()
         
Return Value: Returns a string converted to lowercase.



*******************************************************************************
Created on sat April 22 08:33:00 2023

@author: Hamed Sargoli


Link to Example:
    https://github.com/hamedsargoli/Python/tree/main/Example%20Function/String
"""

#----------------------------------------------------------------
# Example 1 
print("Ex 1:" , '\n')

#1.1
mystr = 'HELLO WORLD'
print("mystr is: "    , mystr)
print("Lower --> "    , mystr.lower() , "\n")
#1.2
mystr = 'Hello World'
print("mystr is: "    , mystr)
print("Lower --> "    , mystr.lower() , "\n")
#1.3    
mystr = 'H3ll0 W0rld'
print("mystr is: "    , mystr)
print("Lower --> "    , mystr.lower() , "\n")
#1.4
mystr = '#Hello*World#'
print("mystr is: "    , mystr)
print("Lower --> "    , mystr.lower() , "\n")
#1.5
mystr = 'hello world'
print("mystr is: "    , mystr)
print("Lower --> "    , mystr.lower() , "\n")


print('--------------------')
#----------------------------------------------------------------
# Example 2 
# The lower() method does not convert all the Unicode chars.
# the German lowercase letter 'ß' is equivalent to 'ss'.
print("Ex 2:" , '\n')

mystr = 'Außen'
print("mystr is: "    , mystr)
print("Lower --> "    , mystr.lower() , "\n")


print('--------------------')
#----------------------------------------------------------------
# Example 3 
# How lower() is used in a program?
print("Ex 3:" , '\n')

# first string
firstString = "MY NAME IS HAMED SARGOLI."

# second string
secondString = "My NaMe is Hamed Sargoli."

lower1 = firstString.lower()
lower2 = secondString.lower()

if(lower1 == lower2):
    print("The strings are same.")
else:
    print("The strings are not same.")


print('--------------------')
#----------------------------------------------------------------