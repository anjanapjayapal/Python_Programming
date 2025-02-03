# TASK 45:
'''Write a Python program to calculate the sum of the positive and negative numbers of a given list
of numbers using the lambda function.'''

lst=[4,7,-9,3,-8,-4]

# Calculate the sum of positive numbers
positive_sum=sum(filter(lambda x: x>=0,lst))

# Calculate the sum of negative numbers
negative_sum=sum(filter(lambda x: x<0,lst))

print(f"Positive sum: {positive_sum}\nNegative sum: {negative_sum}")