# TASK 26:
'''Write a Python program that uses a list comprehension to create a new list that
contains only the uppercase letters in an existing list of strings.'''


# PROGRAM

string=input("Enter the string: ")

upper_string=[item.upper() for item in string if item != ' ']

print(upper_string)



# OUTPUT
'''
Enter the string: hello world
['H', 'E', 'L', 'L', 'O', 'W', 'O', 'R', 'L', 'D']
'''
