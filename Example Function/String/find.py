# find(str) Function
# find(str, beg=0, end=len(string))

"""
Created on Sun Feb  16 20:33:45 2023

@author: Hamed Sargoli
"""


#ex1:   
message = 'Python is a fun programming language'
print('\nEx1:')
# check the index of 'fun'
print(' index = ' , message.find('fun'))

#Ex2:
# check the index of 'Fun'
print('Ex2:\n' , 'index = ' , message.find('Fun') ,'\n')

#Ex3:
quote = 'Let it be, let it be, let it be'
# first occurance of 'let it'(case sensitive)
result = quote.find('let it')
print('Ex3:\n' , "Substring index 'let it':", result)

#Ex4:
# find returns -1 if substring not found
result = quote.find('small')
print('Ex4:\n' , "Substring index 'small ':", result)

#Ex5:
print('Ex5:')
# How to use find()
if (quote.find('be,') != -1):
    print(" Contains substring 'be,'")
else:
    print(" Doesn't contain substring")

#Ex6:
print('Ex6:')
index = quote.find('be,')
print(quote[index:index+3])


print()



#Ex7:
print('Ex7:')
quote = 'Do small things with great love'
# Substring is searched in 'hings with great love'
print(' index = ' , quote.find('small things' , 10))

#Ex8:
print('Ex8:')
# Substring is searched in ' small things with great love' 
print(' index = ' , quote.find('small things', 2))

#Ex9:
print('Ex9:')
# Substring is searched in 'hings with great lov'
print(' index = ' , quote.find('o small ', 10, -1))

#Ex10:
print('Ex10:')
# Substring is searched in 'll things with'
print(' index = ' , quote.find('things ', 6, 20))


print()


#Ex11: Find the number of str_find variable
print('Ex11:')

flag = True
index = 0
count = 0
str_find = 'e'

while flag:
    index = quote.find(str_find , index)
    if index >= 0:
        count += 1
        index += 1  
    else:
        flag = False
print(' counter = ' , count)
