# TASK 9:
'''Write a Python function that takes a tuple and an element as input and counts how many times that element appears in the tuple.'''

# PROGRAM

# Function to count occurrences of an element in a tuple
def occurence(tpl,item):
    count=0
    for i in tpl:
        if i==item:
            count+=1
    return count
 
# User input for tuple and element to count
n=int(input("Enter the number of elements in the tuple: "))
tpl=tuple(int(input(f"Enter element {i+1}: "))for i in range(n))

item=int(input("Enter the item to be count: "))

# Call function and print result
result=occurence(tpl,item)
print(f"The element {item} appears {result} times in the tuple.")
      

# OUTPUT
'''
Enter the number of elements in the tuple: 4
Enter element 1: 2
Enter element 2: 4
Enter element 3: 6
Enter element 4: 2
Enter the item to be count: 2
The element 2 appears 2 times in the tuple.
'''
