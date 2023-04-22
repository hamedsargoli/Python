"""
*******************************************************************************
The rsplit() 
*******************************************************************************
# str.rsplit(separator, maxsplit)

separator: (optional) The delimiter string. 
           The default separator is any whitespace character such as
           space, \t, \n, etc.
maxsplit:  (optional) Defines the maximum number of splits that can be done.
           Thus, the list can contain at most maxsplit + 1 elements. 
           The default maxsplit is -1 that means unlimited splits.
           
Return Value: Returns a list object with string elements.

*******************************************************************************
Created on sat April 21 10:53:00 2023

@author: Hamed Sargoli


Link to Example:
    https://github.com/hamedsargoli/Python/tree/main/Example%20Function/String
"""

#----------------------------------------------------------------
# Example 1 
print("Ex 1:" , '\n')


langs = 'C,Python,R,Java,SQL,Hadoop'
print("langs  ->" , langs)
print("split  ->" , langs.split(',' , 2))
print("rsplit ->" , langs.rsplit(',', 2))


print('--------------------')
