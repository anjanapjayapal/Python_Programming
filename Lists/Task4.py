# TASK 4: Write a Python program that takes a list of numbers as input and calculates and prints the sum and average of those numbers.


# PROGRAM

# Initialize a list to store the user input numbers
numlist=[]

# Take input from user
numbers=int(input("How many numbers do you want to enter: "))
for i in range(numbers):
    num=int(input(f"Enter number {i+1}: "))
    numlist.append(num)
    
def sumandavg(numlist):
    sums=0
    avg=0
    for number in numlist:
        sums+=number
    avg=round(sums/len(numlist),2)
    return sums,avg

sums,avg=sumandavg(numlist) # Function call
print(f"Sum of numbers: {sums}\nAverage of numbers: {avg}")



# OUTPUT
'''
How many numbers do you want to enter: 3
Enter number 1: 8
Enter number 2: 2
Enter number 3: 3
Sum of numbers: 13
Average of numbers: 4.33
'''

    
