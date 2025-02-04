# TASK 43: Write a Python program to create Fibonacci series up to n using Lambda.

n=int(input("Enter a number: "))

from functools import reduce

# Lambda function to generate Fibonacci series
fibonacci = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n-2), [0, 1])[:n]

print(fibonacci(n))

        
               
        