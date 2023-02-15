# islower() Function

"""
Created on Sun Feb  14 23:11:45 2023

@author: Hamed Sargoli
"""

print()
print('Example :\n')

#ex1:    
a = 'hi'
print( 'hi'.islower() , '\n')

#ex2:
a = 'HI'
print(f'2. Is {a !r} upper? :' , a.islower() , '\n')

#ex3:
a = 'HI 2.2'
print(f'3. Is {a !r} upper? :' , a.islower() , '\n')

#ex4:
a = '5 # HI'
print(f'4. Is {a !r} upper? :' , a.islower() , '\n')

#ex5: find the number of upper characters in the text(a)
a = "python IS a PROGRAMMING language."
#a = "python 3.03 $$$"
count=0
for i in a:
    if i.islower():
        count += 1
print(f'5. The {count} character is Lower.')
