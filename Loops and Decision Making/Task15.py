# TASK 15: Write a program to check Armstrong number.

# PROGRAM

# Function to check Armstrong number without converting to string
def is_armstrong(num):
    temp = num
    n = len(str(num))  # Find the number of digits (using str only for length)
    armstrong_sum = 0

    while temp > 0:
        digit = temp % 10  # Extract last digit
        armstrong_sum += digit ** n  # Add digit^n to sum
        temp //= 10  # Remove last digit

    return num == armstrong_sum  # Compare with original number

# User input
num = int(input("Enter a number: "))

# Check Armstrong condition
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
