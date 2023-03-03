# replace(oldvalue, newvalue) 
# replace(oldvalue, newvalue, count)
"""
Created on Fri Mar 3 8:31:21 2023

@author: Hamed Sargoli


Link to Example:
    https://github.com/hamedsargoli/Python/tree/main/Example%20Function/String
"""


#----------------------------------------------------------------
#Example 1
print('\nExample 1:\n')

txt = "I like bananas , bananas are very good"
print(txt , '\n')
R_txt = txt.replace("bananas", " apples")
print(R_txt)
RW_txt = txt.replace("Bananas", "apples")   #just copy txt to RW_txt
print(RW_txt)

print('--------------------')
#----------------------------------------------------------------
#Example 2
print('\nExample 2:\n')

txt = "'one' 'one' was a race horse, two two was 'one' too."
print(txt , '\n')
R2_txt = txt.replace("one", "123", 2)    #2 'one' chenaged
print(R2_txt)
R0_txt = txt.replace("one", "123", 0)    #copy original string
print(R0_txt)


