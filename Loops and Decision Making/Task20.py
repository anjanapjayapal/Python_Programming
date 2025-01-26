#TASK 20: Write a Program to print the multiplication table.

n=int(input("Enter a number: ")) # User Input

print(f"Multiplication Table of {n}:")
for i in range(1,11):
    print(f"{i}*{n} = {i*n}")




# OUTPUT
'''
Enter a number: 7
Multiplication Table of 7:
1*7 = 7
2*7 = 14
3*7 = 21
4*7 = 28
5*7 = 35
6*7 = 42
7*7 = 49
8*7 = 56
9*7 = 63
10*7 = 70


'''
