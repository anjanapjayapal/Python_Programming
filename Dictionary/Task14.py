# TASK 14: Convert two lists into a dictionary in Python without using a built-in method.

# PROGRAM

# Function to convert two lists into a dictionary
def lists_to_dict(keys, values):
    dictionary = {}  # Initialize an empty dictionary
    min_length = min(len(keys), len(values))  # Ensure we don't exceed the shorter list length
    
    for i in range(min_length):
        dictionary[keys[i]] = values[i]  # Assign key-value pairs manually

    return dictionary

# User input for lists
keys = input("Enter keys separated by space: ").split()
values = input("Enter values separated by space: ").split()

# Convert lists to dictionary
result = lists_to_dict(keys, values)
print("\nConverted Dictionary:", result)


# OUTPUT
'''
Enter keys separated by space: pen book pencil
Enter values separated by space: 10 45 5

Converted Dictionary: {'pen': '10', 'book': '45', 'pencil': '5'}
'''
