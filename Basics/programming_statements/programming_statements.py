# 1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd 
#The syntax of mimicking ternary operator in Python is:
#[when_true] if [condition] else [when_false]
num=int(input("Enter a number: ")) 
number= 'Even' if num%2==0 else 'Odd'  # Ternary operator
print(f"{num} is {number}")

# 2. Using input function take two number and then swap the number 
num1,num2=int(input("Enter the first number: ")),int(input("Enter the second number: "))
print(f"The user input numbers: {num1} and {num2}")
num1,num2=num2,num1 # Swapping the numbers
print(f"The numbers after swapping: {num1} and {num2}")

# 3. Write a Program to Convert Kilometers to Miles 
kilometers = float(input("Enter value in kilometers: ")) # Taking kilometers input from the user
conv_fac = 0.621371 # conversion factor
miles = kilometers * conv_fac # calculate miles
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))


# 4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year.
P=200 # Principal amount
R=5   # Rate of interest
T=5   # Time Period
simple_interest=(P*R*T)/100   
print(f"Simple Interest on Rs. 200 for 5 years at 5% per year is {simple_interest}")
