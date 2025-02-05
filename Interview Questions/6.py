
# Swapping without using temporary variable
a,b=int(input("First number: ")),int(input("Second number: "))

print(f'Before swapping: a:{a}\t b:{b}')

a,b = b,a   # Swapping using tuple unpacking

print(f'After swapping: a:{a}\t b:{b}')





# Swapping arithmetic operations

a=a+b
b=a-b
a=a-b
print(f'After swapping using arithmetic operations: a:{a}\t b:{b}')


a= a*b
b= a //b
a= a //b
print(f'After swapping using arithmetic operations: a:{a}\t b:{b}')

