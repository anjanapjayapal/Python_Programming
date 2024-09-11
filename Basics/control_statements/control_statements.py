# 1. Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.
num=int(input("Enter the number: ")) 
if num%2==0:     
  print("Even")
else:
  print("Odd")

# 2. Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.
age=int(input("Enter your age: "))
if age>=18:
  print("You are eligible to vote")
else:
  print("You are not eligible to vote")

# 3.  Write a Python program that determines if a given year is a leap year or not.
year=int(input("Enter a year: "))
if(year%4==0 and year%100!=0) or (year%400==0):
  print(f"{year} is a leap year")
else:
  print(f"{year} is not a leap year")

# 4.   Create a Python program that checks if a user-given number is positive, negative, or zero.
number=int(input("Enter a number: "))
if number>0:
  print(f"{number} is a positive number")
else:
  print(f"{number} is a negative number")

# 5. Write a Python program that determines the largest of three numbers entered by the user.
# Taking three numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Determine the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Print the largest number
print(f'The largest number is: {largest}')

                  
                            
