# Str.removeprefix(remove_str) 
"""
Created on Fri Mar 4 22:56:21 2023

@author: Hamed Sargoli


Link to Example:
    https://github.com/hamedsargoli/Python/tree/main/Example%20Function/String
"""

#----------------------------------------------------------------
#Example 1
print('\nExample 1:\n')

txt = "Hamed Sargoli"
print('"' , txt , '"\n')

remove = "hamed"
print(f"remove '{remove}' : " , txt.removeprefix(remove))

print('--------------------')

remove = "Hamed"
print(f"remove '{remove}' : " , txt.removeprefix(remove))

print('--------------------')

remove = "med"
print(f"remove '{remove}' : " , txt.removeprefix(remove))

print('--------------------')

remove = "Ham"
print(f"remove '{remove}' : " , txt.removeprefix(remove))

print('--------------------')


#----------------------------------------------------------------
#Example 2
print('\nExample 2:\n')

txt = "https://www.youtube.com/@hamedsargoli"
print('"' , txt , '"\n')

remove = "https://"
print(f"remove '{remove}' : " , txt.removeprefix(remove))
