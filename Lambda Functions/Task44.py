# TASK 44: 
'''Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers 
  using Lambda.'''


lst = [13, 19, 35, 139, 26, 57, 95]

# Filtering elements divisible by 13 or 19
new=list(filter(lambda x: x%13==0 or x%19==0, lst))

print("Elements divisible by 13 or 19: ",new)