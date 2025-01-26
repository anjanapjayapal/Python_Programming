# TASK 12:
'''Create a Python program that takes a string as input and checks if all the characters in the string are unique
(i.e., no character repeats). Return True if all characters are unique, and False otherwise.'''

# PROGRAM

# User Input
string=input("Enter the string: ")

# Function to check whether the characters are unique or not
def isunique(string):
    if len(set(string))==len(string):
        return True
    else:
        return False

# Function call and result
result=isunique(string)
print(f"String characters are unique: {result}")



# OUTPUT
'''
Enter the string: abcdef
String characters are unique: True

Enter the string: anjana
String characters are unique: False
'''
