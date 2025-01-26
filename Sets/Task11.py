# TASK 11:
'''Create a Python program that takes two sets and returns a new set containing elements that are common in both input sets.'''

# PROGRAM

# User input 
n1=int(input("Enter the number of elements in set 1: "))
set1=set(int(input(f"Enter element {i+1}: "))for i in range(n1))

n2=int(input("Enter the number of elements in set 2: "))
set2=set(int(input(f"Enter element {i+1}: "))for i in range(n2))

# Function to find the common elements
def common(set1,set2):
    return set1.intersection(set2)

# Call function and print result
result=common(set1,set2)
print(f"Set1: {set1}\nSet2:{set2}\nThe common elements in both sets: {result}")


# OUTPUT
'''
Enter the number of elements in set 1: 3
Enter element 1: 6
Enter element 2: 7
Enter element 3: 3
Enter the number of elements in set 2: 3
Enter element 1: 2
Enter element 2: 7
Enter element 3: 9
Set1: {3, 6, 7}
Set2:{9, 2, 7}
The common elements in both sets: {7}
'''
