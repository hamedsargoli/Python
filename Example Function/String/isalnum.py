# isalnum() 
"""
Created on Fri Mar 23 10:31:21 2023

@author: Hamed Sargoli

(a-z) and (0-9).

Link to Example:
    https://github.com/hamedsargoli/Python/tree/main/Example%20Function/String
"""

#----------------------------------------------------------------
#Example 1
print('\nExample 1:\n')

txt = "Company123"
print('"' , txt , '"')
print("Are all characters of string alphanumeric? " , txt.isalnum())


print('--------------------')

#----------------------------------------------------------------
#Example 2
print('\nExample 2:\n')

txt = "Company company123"
print('"' , txt , '"')
print("Are all characters of string alphanumeric? " , txt.isalnum())


print('--------------------')


#----------------------------------------------------------------
#Example 3
print('\nExample 3:\n')

txt = "Comp@any123"
print('"' , txt , '"')
print("Are all characters of string alphanumeric? " , txt.isalnum())


print('--------------------')
