# Str.removesuffix(remove_str) 
"""
the string ends with the suffix and the suffix is not empty, the str.
removesuffix(suffix) function removes the suffix and returns the rest of the 
string. If the suffix string is not found then it returns the original string
*******************************************************************************
# Str.removesuffix(remove_str)
         
Parameters:
    remove_str : The suffix string for removing

Return Value:
    Returns a string.

*******************************************************************************
Created on May 12 09:27:00 2023

@author: Hamed Sargoli


Link to Example:
    https://github.com/hamedsargoli/Python/tree/main/Example%20Function/String
"""


print('-'*50)
#----------------------------------------------------------------
# Example 1 
print("Ex 1:" , '\n')


txt = "Hamed Sargoli"
print("Original string      : " , txt , '\n')

#1.1
remove = "Sargoli"
print(f"1.1 remove '{remove}' : " , txt.removesuffix(remove))

print('-'*25)

#1.2
remove = "sargoli"
print(f"1.2 remove '{remove}' : " , txt.removesuffix(remove))

print('-'*25)

#1.3
remove = "Sargol"
print(f"1.3 remove '{remove}'  : " , txt.removesuffix(remove))

print('-'*25)

#1.4
remove = "goli"
print(f"1.4 remove '{remove}'    : " , txt.removesuffix(remove))

print('-'*25)

#1.5
remove = ""
print(f"1.5 remove '{remove}'        : " , txt.removesuffix(remove))



print('-'*50)
#----------------------------------------------------------------
# Example 2 
# removeprefix() VS removesuffix()
print("Ex 2:" , '\n')


txt = "https://www.youtube.com/@hamedsargoli"
print("Orginal string   : " , txt , '\n')

remove_pre = "https://"
remove_suf = "/@hamedsargoli"
result = txt.removeprefix(remove_pre)
result = result.removesuffix(remove_suf)

print(f"remove '{remove_pre}' & '{remove_suf}' : " , result)