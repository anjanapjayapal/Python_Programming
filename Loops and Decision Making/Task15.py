# TASK 15: Write a program to check Armstrong number.

# PROGRAM

# Function to check if a number is an Armstrong number
def is_armstrong(num):
    num_str = str(num)  # Convert number to string to get individual digits
    n = len(num_str)  # Get the number of digits
    armstrong_sum = sum(int(digit) ** n for digit in num_str)  # Calculate sum of digits raised to the power of n
    
    return num == armstrong_sum  # Return True if Armstrong number, else False

# Take user input
num = int(input("Enter a number: "))

# Check and display result
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")



# OUTPUT
'''
Enter a number: 153
153 is an Armstrong number.

Enter a number: 56
56 is not an Armstrong number.
'''
