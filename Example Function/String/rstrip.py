# rstrip() Function
"""
The rstrip() method returns a copy of the string by removing the trailing
characters specified as argument. If the characters argument is not provided, 
all trailing whitespaces are removed from the string.
*******************************************************************************
# str.rstrip(characters)
         
Parameters:
    characters    : (optional) A char or string to be removed from the end of 
                    the string.

Return Value:
    Returns a string.

*******************************************************************************
Created on  May 18 21:10:00 2023

@author: Hamed Sargoli


Link to Example:
    https://github.com/hamedsargoli/Python/tree/main/Example%20Function/String
"""

print('-'*50)
#----------------------------------------------------------------
# Example 1 
# The following examples demonstrates the rstrip() method.
print("Examples:" , '\n')


#1.1
mystr = '     Hello World     '
print(f'1.1\noriginal string : "{mystr}"')
out= mystr.rstrip()
print(f'rstrip string   : "{out}"')

print('-'*25)


#1.2
mystr = '''
          Python is 
a programming language      '''
print(f'1.2\noriginal string : "{mystr}"')
out= mystr.rstrip()
print(f'rstrip string   : "{out}"')

print('-'*25)


#1.3
mystr = '----Hello World----'
print('1.3\noriginal string :' , mystr)
print('rstrip string   :' , mystr.rstrip('-'))

print('-'*25)


#1.4
mystr = "www.youtube.com/@hamedsargoli/"             
print('1.4\noriginal string :' , mystr)
print('rstrip string   :' , mystr.rstrip('/w.'))

print('-'*25)


#1.5
mystr = 'ābcā'
print('1.5\noriginal string :' , mystr)
print('rstrip string   :' , mystr.rstrip('ā'))        # remove Unicode char