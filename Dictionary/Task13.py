# TASK 13:
'''Write a Python function that takes a dictionary of items and their prices as input
and finds and prints the keys (items) with the highest prices.'''

# PROGRAM

# Function to find items with the highest price
def highest_priced_items(items_dict):
    if not items_dict:  # Check if dictionary is empty
        return []
    max_price = max(items_dict.values())  # Find the highest price
    return [item for item, price in items_dict.items() if price == max_price]  # Find all items with max price

# User input for dictionary
n = int(input("Enter the number of items: "))
items_dict = {}

for _ in range(n):
    item = input("Enter item name: ")
    price = float(input(f"Enter price of {item}: "))
    items_dict[item] = price  # Add item-price pair to dictionary

# Find and print highest-priced items
result = highest_priced_items(items_dict)
print(f"\nItem(s) with the highest price: {', '.join(result)}")


# OUTPUT
'''
Enter the number of items: 3
Enter item name: pen
Enter price of pen: 10
Enter item name: book
Enter price of book: 45
Enter item name: pencil
Enter price of pencil: 5
Item(s) with the highest price: book
'''
