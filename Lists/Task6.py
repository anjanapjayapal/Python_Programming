# TASK 6:
'''Create a Python function that takes a list as input and removes duplicate
elements, preserving the order of the elements. Return the new list.'''

# PROGRAM

# User input
lists = []
numbers = int(input("How many numbers do you want to enter: "))

for i in range(numbers):
    num = int(input(f"Enter number {i+1}: "))
    lists.append(num)

# Function to remove duplicates while maintaining order
def uniquelist(lists):
    new=[]
    for i in lists:
        if i not in new:
            new.append(i)
    return new

result=uniquelist(lists)
print(f"Original list: {lists}\nList after removing duplicates: {result}")


# OUTPUT
'''
How many numbers do you want to enter: 4
Enter number 1: 30
Enter number 2: 10
Enter number 3: 20
Enter number 4: 30
Original list: [30, 10, 20, 30]
List after removing duplicates: [30, 10, 20]
'''
