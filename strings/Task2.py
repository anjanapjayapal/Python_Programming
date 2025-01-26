#TASK 2: Write a Program to given string is a palindrome (reads the same forwards and backwards).


# PROGRAM

str1=input("Enter a string: ") # User Input

# Reversing the string
reverse=str1[::-1]

if str1==reverse:
    print("palindrome string")
else:
    print("Not a palindrome string")





# OUTPUT
'''
Enter a string: madam
palindrome string
'''
    
