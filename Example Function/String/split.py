"""
*******************************************************************************
# str.split(separator, maxsplit)

separator: (optional) The delimiter string. 
           The default separator is any whitespace character such as
           space, \t, \n, etc.
maxsplit:  (optional) Defines the maximum number of splits that can be done.
           Thus, the list can contain at most maxsplit + 1 elements. 
           The default maxsplit is -1 that means unlimited splits.
           
Return Value: Returns a list object with string elements.

*******************************************************************************
Created on sat Mar 25 11:43:00 2023

@author: Hamed Sargoli


Link to Example:
    https://github.com/hamedsargoli/Python/tree/main/Example%20Function/String
"""

#----------------------------------------------------------------
# Example 1 
# The following example demonstrates the simple use of the split() method.
print("Ex 1:" , '\n')


mystr = 'Hello World'
print("mystr is:       "  , mystr)
print("default  --> "     , mystr.split() , "\n")

mystr = 'Hello      World'
print("mystr is:     "    , mystr)
print("space    --> "     , mystr.split(), "\n")
    
mystr = 'Hello\tWorld'
print("mystr is:      "   , mystr)    
print("\ t      --> "     , mystr.split(), "\n")

mystr = 'Hello\nWorld'
print("mystr is:      "   , mystr) 
print("\ n      --> "     , mystr.split(), "\n")

mystr = 'Hello\u2028World'
print("mystr is:      "   , mystr)
print("\ u2028  --> "     , mystr.split(), "\n")

mystr = 'my name is:\n\t\t\t\t\t\t\tHamed Sargoli'
print("mystr is:      "   , mystr)
print("default  --> "     , mystr.split() , "\n")


print('--------------------')
#----------------------------------------------------------------
# Example 2 
# The following examples specifies the separator.
print("Ex 2:" , '\n')


langs = 'C, Python, R, Java, SQL, Hadoop'
print("var is:      " , langs)
print("sep=','  --> " , langs.split(','))
print("sep=', ' --> " , langs.split(', ') , "\n")

fruits = 'apples$banana$mango$fig$pear'
print("var is:      " , fruits)
print("sep='$'  --> " , fruits.split('$') , "\n")

number = str(263.32598)
print("var is:      " , number)
print("sep='.'  --> " , number.split('.'))

print('--------------------')
#----------------------------------------------------------------
# Example 3 
# If the specified seperator does not exist, 
# then it returns a list with the whole string as an element.
print("Ex 3:" , '\n')


langs = 'C,Python,R,Java,SQL,Hadoop'
print("var is:     " , langs)
print("sep='@' --> " , langs.split('@') , "\n")


print('--------------------')
#----------------------------------------------------------------
# Example 4 
# Error 
# The split() method will raise the ValueError if 
# a separator is an empty string ''.
print("Ex 4:" , '\n')


langs = 'C,Python,R,Java,SQL,Hadoop'
print("var is:     " , langs)
#print("sep='' --> " , langs.split('') , "\n")



print('--------------------')
#----------------------------------------------------------------
# Example 5 
# The following example limits the split by specifying the maxsplit parameter.
print("Ex 5:" , '\n')


langs = 'C,Python,R,Java,SQL,Hadoop'
print("var is:          " , langs , "\n")
print("max split=1 -->  " , langs.split(',' , 1) , "\n")

print("max split=3 -->  " , langs.split(',' , 3) , "\n")

print("max split=9 -->  " , langs.split(',' , 9) , "\n")

print("max split=-1 --> " , langs.split(',' , -1) , "\n")   #default

