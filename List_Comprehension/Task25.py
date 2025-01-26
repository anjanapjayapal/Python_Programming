# TASK 25:
'''
Write a Python program that uses a "for" loop to iterate over a string and prints
out each character along with its count.'''


# PROGRAM

string=input("Enter the string: ")

# Using list comprehension with for loop
char_count = [(char, string.count(char)) for char in string]

# Print each character and its count
for char, count in char_count:
    print(f"Character: {char}, Count: {count}")



# OUTPUT
'''
Enter a string: hello
Character: h, Count: 1
Character: e, Count: 1
Character: l, Count: 2
Character: l, Count: 2
Character: o, Count: 1
'''
