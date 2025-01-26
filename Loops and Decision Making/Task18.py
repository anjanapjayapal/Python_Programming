# TASK 18: Print the Fibonacci series for first 12 numbers.

# PROGRAM

num=12 # Number of Fibonacci terms
first=0
second=1

print("Fibonnaci series for first 12 numbers: ")
print(first,second,end=' ') # Print the first two numbers

for i in range(num-2):
    third=first+second # Compute next Fibonacci number
    first=second # Update first
    second=third # Update second

    print(third, end=' ')

    


# OUTPUT
'''
Fibonnaci series for first 12 numbers: 
0 1 1 2 3 5 8 13 21 34 55 89
'''
