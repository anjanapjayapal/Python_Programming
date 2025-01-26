# TASK 8: Write a Python function that takes a list and an element as input and counts how many times that element appears in the list.

# PROGRAM

# Function to count occurrences of an element in a list
def count_occurrences(lst, element):
    count = 0  # Initialize count to zero
    for i in lst:
        if i == element:  # Check if the element matches
            count += 1
    return count

# User input for list
lst = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    lst.append(num)

# User input for element to count
element = int(input("Enter the element to count: "))

# Call function and print result
result = count_occurrences(lst, element)
print(f"The element {element} appears {result} times in the list.")


# OUTPUT
'''
Enter the number of elements in the list: 5
Enter element 1: 1
Enter element 2: 4
Enter element 3: 2
Enter element 4: 4
Enter element 5: 4
Enter the element to count: 4
The element 4 appears 3 times in the list.
'''

    
    
               
