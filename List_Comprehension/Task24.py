# TASK 24:
'''Write a Python program that uses list comprehension to create a new list
containing the squares of the numbers from 1 to 10.'''


# PROGRAM 


squares=[item*item for item in range(1,11)]

print(f"Square of numbers from 1 to 10:\n{squares}")


# OUTPUT
'''
Square of numbers from 1 to 10:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''
