# TASK 7:
'''Create a Python program that takes two lists and returns a new list containing elements that are common in both input lists.'''

# PROGRAM

# User input for first list
list1 = []
n1 = int(input("Enter the number of elements for the first list: "))
for i in range(n1):
    num = int(input(f"Enter element {i+1}: "))
    list1.append(num)

# User input for second list
list2 = []
n2 = int(input("Enter the number of elements for the second list: "))
for i in range(n2):
    num = int(input(f"Enter element {i+1}: "))
    list2.append(num)

# Function to find common elements
def common_elements(lst1, lst2):
    common = []  # List to store common elements
    for i in lst1:
        if i in lst2 and i not in common:  # Check for common elements and avoid duplicates
            common.append(i)
    return common

result = common_elements(list1, list2)
print(f"First list: {list1}\nSecond list: {list2}\nCommon elements: {result}")

# OUTPUT
'''
Enter the number of elements for the first list: 2
Enter element 1: 3
Enter element 2: 2
Enter the number of elements for the second list: 3
Enter element 1: 1
Enter element 2: 3
Enter element 3: 3
First list: [3, 2]
Second list: [1, 3, 3]
Common elements: [3]'''
