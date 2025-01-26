# TASK 21: How to find the factorial of number 5.

num=5

def numfactorial(num):
    fact =1
    if num == 0 or num == 1:
        return 1
    for i in range(1,num+1):
        fact *= i
    return fact


print(f"Factorial of 5 is: {numfactorial(num)}")



# OUTPUT
'''
Factorial of 5 is: 120
'''
