# TASK 28:
'''Write a Python program to remove duplicates from a list while preserving the
order of elements.'''


# PROGRAM

# Input list with duplicates
input_list = [1, 2, 3, 4, 2, 5, 6, 1, 7, 5]

# Using list comprehension to remove duplicates while preserving order
unique_list = []
[unique_list.append(item) for item in input_list if item not in unique_list]

# Print the list after removing duplicates
print("List after removing duplicates:", unique_list)



# OUTPUT
'''
List after removing duplicates: [1, 2, 3, 4, 5, 6, 7]
'''
