"""
*******************************************************************************
The splitlines() method splits the string at line boundaries and returns
 a list of lines in the string
------------------------------------------------------------------------------- 
str.splitlines(keepends)

keepends: (optional)  if its value as true, line breaks need are also included
          in the output. Default is False.
           
Return Value: A list object with all the lines.


Various line boundaries this method recognizes are given below:

\n − Line Feed

\r − Carriage Return

\r\n − Carriage Return + Line Feed

\v or \x0b − Line Tabulation

\f or \x0c − Form Feed

\x1c − File Separator

\x1d − Group Separator

\x1e − Record Separator

\x85 − Next Line (C1 Control Code)

\u2028 − Line Separator

\u2029 − Paragraph Separator

*******************************************************************************
Created on sat April 6 07:08:00 2023

@author: Hamed Sargoli


Link to Example:
    https://github.com/hamedsargoli/Python/tree/main/Example%20Function/String
"""

#----------------------------------------------------------------
# Example 1 
# keepends defaults to False => boundary lines aren't displaying
print("Ex 1:" , '\n')


mystr = 'Python\nis a\nprogramming language.\n'

print("mystr is:"  , mystr)
print(mystr.splitlines())


print('--------------------')
#----------------------------------------------------------------
# Example 2 
# keepends is True
# Note: In the above example, triple ''' is used to define a multi-line string.
print("Ex 2:" , '\n')
 

mystr = '''Python
is a
programming language.\n'''

print("mystr is:"  , mystr)
print(mystr.splitlines(True))



print('--------------------')
#----------------------------------------------------------------
# Example 3 
print("Ex 3:" , '\n')
 

langs = 'C++\rPython3\rJava\rSQL\rHadoop' # \r as line boundary
print(langs.splitlines())

langs = 'C++\vPython3\vJava\vSQL\vHadoop' # \v as line boundary
print(langs.splitlines())

langs = 'C++\x1dPython3\x1dJava\x1dSQL\x1dHadoop' # \x1d as line boundary
print(langs.splitlines())



print('--------------------')
#----------------------------------------------------------------
# Example 4 
# false(0)  &&  True(positive and negative integer)
print("Ex 4:" , '\n')
 

langs = 'C++\rPython3\rJava\rSQL\rHadoop' # \r as line boundary
print(langs.splitlines(0))
print(langs.splitlines(1))
print(langs.splitlines(125))
print(langs.splitlines(-21))



print('--------------------')
#----------------------------------------------------------------
# Example 5 
# Empty String
print("Ex 5:" , '\n')
 
mystr = ''
out_str = mystr.splitlines()
print(out_str)



print('--------------------')
#----------------------------------------------------------------
# Example 6 
# No boundary Line
print("Ex 6:" , '\n')
 
mystr = 'Hello World' 
out_str = mystr.splitlines()
print(out_str)



print('--------------------')
#----------------------------------------------------------------