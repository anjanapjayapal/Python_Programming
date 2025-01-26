# TASK 5:
'''Write a Python function that takes a list and returns a new list with the elements reversed.
Do this without using the built-in reverse method.'''


# PROGRAM

# User input
lists=[]
numbers = int(input("How many numbers do you want to enter: "))

for i in range(numbers):
    num = int(input(f"Enter number {i+1}: "))
    lists.append(num)

# Function to reverse the list
def reversing(lists):
    reverse=[]
    for i in range(len(lists)-1,-1,-1):
        reverse.append(lists[i])
    return reverse

result=reversing(lists)
print(f"Original list: {lists}\nReversed list: {result}")



# OUTPUT
'''
How many numbers do you want to enter: 4
Enter number 1: 6
Enter number 2: 7
Enter number 3: 3
Enter number 4: 2
Original list: [6, 7, 3, 2]
Reversed list: [2, 3, 7, 6]
'''
