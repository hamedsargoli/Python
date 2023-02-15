# isupper() Function

"""
Created on Sun Feb  5 23:11:45 2023

@author: Hamed Sargoli

"""

print()
print('Example :\n')

#ex1:    
a = 'hi'
print( 'hi'.isupper() , '\n')

#ex2:
a = 'HI'
print(f'2. Is {a !r} upper? :' , a.isupper() , '\n')

#ex3:
a = 'HI 2.2'
print(f'3. Is {a !r} upper? :' , a.isupper() , '\n')

#ex4:
a = '5 # HI'
print(f'4. Is {a !r} upper? :' , a.isupper() , '\n')

#ex5: find the number of upper characters in the text(a)
a = "python IS a PROGRAMMING language"
count=0
for i in a:
    if i.isupper():
        count += 1
print(f'5. The {count} character is Upper.')
