# TASK 16: Write a program to check palindrome number.

# PROGRAM

num=int(input("Enter a number: "))

# Function to check palindrome using loops
def is_palindrome(num):
    original=num
    reverse=0

    while num>0:
        digit=num%10 # Extract last digit
        reverse=reverse*10+digit # Build the reversed number
        num//=10 # Remove the last digit

    return original==reverse # Compare with original number

result=is_palindrome(num)
print(f"{num} is palindrome: {result}")


# OUTPUT
'''
Enter a number: 545
545 is palindrome: True

Enter a number: 98765
98765 is palindrome: False
'''


