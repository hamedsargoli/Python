# strip() Function
"""
The strip() method returns a copy of the string by removing both the leading 
and the trailing characters. By default, it removes leading whitespaces if no
argument passed.
*******************************************************************************
# str.strip(characters)
         
Parameters:
    characters    : (Optional) a string to be removed from the starting and 
                    ending of a string. By default, it removes all leading 
                    and trailing whitespaces if no argument is specified.

Return Value:
    Returns a string.

*******************************************************************************
Created on  May 12 10:29:00 2023

@author: Hamed Sargoli


Link to Example:
    https://github.com/hamedsargoli/Python/tree/main/Example%20Function/String
"""

print('-'*50)
#----------------------------------------------------------------
# Example 1 
# The following examples demonstrates the strip() method.
print("Ex 1:" , '\n')

mystr = '     Hello World     *'
print('1.1\noriginal string :' , mystr)
print('striped string  :' , mystr.strip())

print('-'*25)

mystr = '''
          Python is 
a programming language'''
print('1.2\noriginal string :' , mystr)
print('striped string  :' , mystr.strip())

print('-'*25)

mystr = '----Hello World----'
print('1.3\noriginal string :' , mystr)
print('striped string  :' , mystr.strip('-'))

print('-'*25)

mystr = '#$2Hello World#$2'
print('1.4\noriginal string :' , mystr)
print('striped string  :' , mystr.strip('$2#'))

print('-'*25)

mystr = '#$-2Hello World#$2'
print('1.5\noriginal string :' , mystr)
print('striped string  :' , mystr.strip('$2#'))

print('-'*25)

mystr = "www.youtube.com/@hamedsargoli/"             
print('1.6\noriginal string :' , mystr)
print('striped string  :' , mystr.strip('/w.'))

print('-'*25)

mystr = 'ābcā'
print('1.7\noriginal string :' , mystr)
print('striped string  :' , mystr.strip('ā'))        # remove Unicode char


print('-'*50)
#----------------------------------------------------------------
# Example 2 
# strip VS removeprefix VS removesuffix
print("Ex 2:" , '\n')

txt = ",,,,,rrttgg.....banana....rrr"
print('original string :' , txt)
print('strip           :' , txt.strip(",.grt"))
print('removeprefix    :' , txt.removeprefix(",.grt"))
print('removesuffix    :' , txt.removesuffix(",.grt"))
