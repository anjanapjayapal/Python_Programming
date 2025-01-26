# TASK 29: Create a simple calculator operations using function.

# PROGRAM

# Functions to add, subtract, multiply, and divide two numbers
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."


# Take input from the user
choice = input("Enter choice\n1 (add)\n2 (subtract)\n3 (multiply)\n4 (divide): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform the operation based on the user's choice
if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid input!")


# OUTPUT
'''
Enter choice
1 (add)
2 (subtract)
3 (multiply)
4 (divide): 4
Enter first number: 8
Enter second number: 2
8.0 / 2.0 = 4.0
'''
