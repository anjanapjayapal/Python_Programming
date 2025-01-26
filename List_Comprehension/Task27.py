# TASK 27:
'''To write a program in python find the second smallest and third largest number
in a list.'''


# PROGRAM

# Input list
numbers = [12, 34, 1, 56, 77, 23, 90, 3, 9, 25]

# Sort the list
numbers.sort()

# Second smallest and third largest using list comprehension
second_smallest = [numbers[i] for i in range(len(numbers)) if i == 1][0]
third_largest = [numbers[i] for i in range(len(numbers)) if i == len(numbers) - 3][0]

print(f"Second smallest number: {second_smallest}")
print(f"Third largest number: {third_largest}")


# OUTPUT
'''
Second smallest number: 3
Third largest number: 56 '''
