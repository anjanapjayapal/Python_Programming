# Fibonacci series using lambda function

n=int(input("Enter a number: "))

from functools import reduce

fibo= lambda n: reduce(lambda x,_: x + [x[-1]+x[-2]],range(n-2),[0,1]) [:n]

print(fibo(n))


# OUTPUT
'''
Enter a number: 4
[0, 1, 1, 2]

'''