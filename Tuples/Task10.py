# TASK 10: Write a Python program that takes a list of person tuples (name, age) and calculates and prints the average age of the group.

# PROGRAM

def avg_age(person_list):
    total_age=0
    for person in person_list:
        total_age+=person[1]
    return total_age/len(person_list)if person_list else 0

# User input for list of tuples
person_list = []
n = int(input("Enter the number of people: "))

for i in range(n):
    name = input(f"Enter name of person {i+1}: ")
    age = int(input(f"Enter age of {name}: "))
    person_list.append((name, age))  # Append tuple (name, age)

# Calculate and print average age
avg_age = avg_age(person_list)
print(f"\nThe average age of the group is: {avg_age:.2f}")


# OUTPUT
'''
Enter the number of people: 3
Enter name of person 1: anjana
Enter age of anjana: 21
Enter name of person 2: ardhra
Enter age of ardhra: 22
Enter name of person 3: sijo
Enter age of sijo: 25

The average age of the group is: 22.67
'''
    
