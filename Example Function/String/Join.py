"""
*******************************************************************************
sep.join(iterable) 
    iterable: (Required) An iterable object such as 
              list, tuple, string, set, dict.

    Return Value: Returns a string.
*******************************************************************************

Created on sat Mar 25 6:10:21 2023

@author: Hamed Sargoli


Link to Example:
    https://github.com/hamedsargoli/Python/tree/main/Example%20Function/String

"""

#----------------------------------------------------------------
# Example 1 
print("Ex 1:" , '\n')

sep = ','
names = ['Steve', 'Bill', 'Ravi', 'Jonathan'] # list
print(" list   --> " , sep.join(names))

mystr = 'Hello' # string
print(" string --> " , sep.join(mystr))

nums = ('1', '2', '3', '4') # tuple
print(" tuple  --> " , sep.join(nums))

langs = {'Python' , 'C#' , 'Java' , 'C++' , 'C#' , 'Java'} # set
print(" set    --> " , sep.join(langs))

print('--------------------')



#----------------------------------------------------------------
# Example 2 
# The seperator string can be of any length or char.
print("Ex 2:" , '\n')

sep = 'õ' # Unicode seperator
names = ['Steve', 'Bill', 'Ravi', 'Jonathan'] # list
print("" , names);
print(" sep = 'õ'    --> " , sep.join(names) , '\n')

sep = '_&_'
mystr = 'Hello' # string
print("" , mystr);
print(" sep = '_&_'  --> " , sep.join(mystr) , '\n')

sep = '****'
nums = ('1', '2', '3', '4') # tuple
print("" , nums);
print(" sep = '****' --> " , sep.join(nums) , '\n')


print('--------------------')

#----------------------------------------------------------------
# Example 3 
# Error
print("Ex 3:" , '\n')

nums = (1, 2, 3, 4, 5)
#print(sep.join(nums))


print('--------------------')

#----------------------------------------------------------------
# Example 4 
# In dictionary joins the keys only
# If keys are not strings, then it will raise a TypeError.
print("Ex 4:" , '\n')

emp = {'Steve': 1, 'Bill': 2, 'Ravi': 3 } #dictionary
print("" , '>-'.join(emp) , '\n')

emp = {1:'Steve', 2:'Bill', 3:'Ravi' } # raise an error
#print("" , '>-'.join(emp) , '\n')






