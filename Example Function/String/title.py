"""
The title() method returns a string where each word starts with an uppercase
 character, and the remaining characters are lowercase. If the word contains a
 number or a symbol, the first letter after that will be converted to upper case.
*******************************************************************************
# str.title()
          
Return Value: Returns a string.

*******************************************************************************
Created on sat May 29 18:53:00 2023

@author: Hamed Sargoli


Link to Example:
    https://github.com/hamedsargoli/Python/tree/main/Example%20Function/String
"""

#----------------------------------------------------------------
# Example 1 
# The following example demonstrates use of the title() method.
print("Ex 1:" , '\n')

#1.1
mystr = 'hello world'
print("1.1\nmystr is:  "  , mystr)
print("Title  --> "     , mystr.title() , "\n")

#1.2
mystr = 'yOUtube is a free sCHOOl.'
print("1.2\nmystr is:  "  , mystr)
print("Title  --> "     , mystr.title() , "\n")

#1.3
mystr = '12!3456$%'
print("1.3\nmystr is:  "  , mystr)
print("Title  --> "     , mystr.title() , "\n")

#1.4
mystr = '#1 room side'
print("1.4\nmystr is:  "  , mystr)
print("Title  --> "     , mystr.title() , "\n")


print('--------------------')
#----------------------------------------------------------------
# Example 2 
print("Ex 2:" , '\n')

mystr = 'Hello worLD'
if mystr.istitle():
    print("mystr is the title string!") 
else:
    print(mystr.title())
        

print('--------------------')
#----------------------------------------------------------------
