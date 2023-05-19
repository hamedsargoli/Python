# lstrip() Function
"""
The lstrip() method returns a copy of the string by removing leading characters
specified as an argument. By default, it removes leading whitespaces if no 
argument passed.
*******************************************************************************
# str.lstrip(characters)
         
Parameters:
    characters    : (optional) A char or string to be removed from the starting
                    of the string.

Return Value:
    Returns a string.

*******************************************************************************
Created on  May 18 21:28:00 2023

@author: Hamed Sargoli


Link to Example:
    https://github.com/hamedsargoli/Python/tree/main/Example%20Function/String
"""

print('-'*50)
#----------------------------------------------------------------
# Example 1 
# The following examples demonstrates the lstrip() method.
print("Examples:" , '\n')


#1.1
mystr = '     Hello World     '
print(f'1.1\noriginal string : "{mystr}"')
out= mystr.lstrip()
print(f'lstrip string   : "{out}"')

print('-'*25)


#1.2
mystr = '''
          Python is 
a programming language      '''
print(f'1.2\noriginal string : "{mystr}"')
out= mystr.lstrip()
print(f'lstrip string   : "{out}"')

print('-'*25)


#1.3
mystr = '----Hello World----'
print('1.3\noriginal string :' , mystr)
print('lstrip string   :' , mystr.lstrip('-'))

print('-'*25)


#1.4
mystr = "www.youtube.com/@hamedsargoli/"             
print('1.4\noriginal string :' , mystr)
print('lstrip string   :' , mystr.lstrip('/w.'))

print('-'*25)


#1.5
mystr = 'ābcā'
print('1.5\noriginal string :' , mystr)
print('lstrip string   :' , mystr.lstrip('ā'))        # remove Unicode char