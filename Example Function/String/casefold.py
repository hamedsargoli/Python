"""
The casefold() method returns a string where all the characters are in lower
 case. It is similar to the lower() method, but the casefold() method converts
 more characters into lower case.
*******************************************************************************
# str.casefold()
         
Return Value: Returns a string converted to lowercase.

*******************************************************************************
Created on sat April 22 14:45:00 2023

@author: Hamed Sargoli


Link to Example:
    https://github.com/hamedsargoli/Python/tree/main/Example%20Function/String
"""

#----------------------------------------------------------------
# Example 1 
print("Ex 1:" , '\n')

#1.1
mystr = 'HELLO WORLD'
print("mystr is:    "    , mystr)
print("casefold --> "    , mystr.casefold() , "\n")
#1.2
mystr = 'Hello World'
print("mystr is:    "    , mystr)
print("casefold --> "    , mystr.casefold() , "\n")
#1.3    
mystr = 'H3ll0 W0rld'
print("mystr is:    "    , mystr)
print("casefold --> "    , mystr.casefold() , "\n")
#1.4
mystr = '#Hello*World#'
print("mystr is:    "    , mystr)
print("casefold --> "    , mystr.casefold() , "\n")
#1.5
mystr = 'hello world'
print("mystr is:    "    , mystr)
print("casefold --> "    , mystr.casefold() , "\n")


print('--------------------')
#----------------------------------------------------------------
# Example 2 
# The difference between the lower() and casefold()
print("Ex 2:" , '\n')

mystr = 'außen'
print(mystr.casefold())
print(mystr.lower())


print('--------------------')
#----------------------------------------------------------------