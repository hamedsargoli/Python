# center() Function
"""
The center() method returns a new centered string of the specified length, 
which is padded with the specified character. The deafult character is space.
*******************************************************************************
# str.center(width, fillchar)
         
Parameters:
    width    : The total length of the string.
    fillchar :(Optional) A character to be used for padding.

Return Value:
    Returns a string.

*******************************************************************************
Created on May 5 10:00:00 2023

@author: Hamed Sargoli


Link to Example:
    https://github.com/hamedsargoli/Python/tree/main/Example%20Function/String
"""

print('-'*50)
#----------------------------------------------------------------
# Example 1 
# The following example demonstrates the center() method.
print("Ex 1:" , '\n')

char='Hi'
print('char       -> ' , char)
print('center_4W_ -> ' , char.center(4 , '-'))
print('center_5W  -> ' , char.center(5 , '*'))
print('center_6W  -> ' , char.center(6 , '>'))


print('-'*50)
#----------------------------------------------------------------
# Example 2 
# The default fill character is a space, as shown below.
print("Ex 2:" , '\n')

char = 'Hi'
centered_3 = char.center(3)
centered_6 = char.center(6)
print(f"Centered String (3):{centered_3}")
print(f"Centered String (6):{centered_6}" ,)


print('-'*50)
#----------------------------------------------------------------
# Example 3 
# center() throws error
print("Ex 3:" , '\n')

#3.1
char = 'Hello'
#print(char.center(10, '$$'))
#3.2
greet = 'Hi'
#print(greet.center())


print('-'*50)
#----------------------------------------------------------------
# Example 4 
print("Ex 4:" , '\n')

mystr = 'Python is a programming language'    #32 length
print(mystr.center(20, '-'))

mystr = 'Hello World'
print(mystr.center(2,'*'))