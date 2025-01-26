# TASK 22:  Write a Program to Check Whether a Number is Prime or Not.

#PROGRAM

num = int(input("Enter a number: "))

if num < 2:
    print(f"{num} is not a prime number")
else:
    for i in range(2, int(num ** 0.5) + 1):  # Loop from 2 to sqrt(num)
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")

# OUTPUT
'''
Enter a number: 5
5 is a prime number

Enter a number: 1
1 is not a prime number
'''

        

        
