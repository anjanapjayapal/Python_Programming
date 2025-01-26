# TASK 17: Write a program to print sum of digits.


# PROGRAM

# Function to find the sum of digits
def findsum(digits):
    sum=0
    for num in digits:
        sum+=num
    return sum

# User Input
n=int(input("Number of elements: "))
print("Enter the numbers: ")
digits=[int(input()) for i in range(n)]

# Function call and results
result=findsum(digits)
print(f"The sum of digits: {result}")



# OUTPUT
'''
Number of elements: 4
Enter the numbers: 
3
6
7
8
The sum of digits: 24
'''
