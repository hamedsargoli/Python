# islower() Function

"""
Created on Sun Feb  14 23:11:45 2023

@author: Hamed Sargoli
"""


#ex1:   
print('\n' , 'ex1:')    

result = 'Hi'.islower()

print( result , '\n')


#ex2:
a = 'hi'
print(f'ex2. Is {a !r} lower? :' , a.islower() , '\n')

#ex3:
a = 'HI 2.2'
print(f'ex3. Is {a !r} lower? :' , a.islower() , '\n')

#ex4:
a = '5 # hi'
print(f'ex4. Is {a !r} lower? :' , a.islower() , '\n')

#ex5: How to use islower() in a program?
print('ex5:')
s = 'this is good'
if s.islower() == True:
  print('Does not contain uppercase letter.')
else:
  print('Contains uppercase letter.')

#ex6: How to use islower() in a program?  
print('ex6:')
s = 'this is Good'
if s.islower():
  print('Does not contain uppercase letter.')
else:
  print('Contains uppercase letter.')

