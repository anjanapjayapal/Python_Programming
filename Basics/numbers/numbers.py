# 1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
length=92
breadth=48.8
area=length * breadth
print(f"Area: {area}") # Area: 4489.599999999999


# 2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. 
# Find out using python, how many dollars is the shopkeeper going to give you back?
no_packets=9
cost=1.49
paid=20
balance=20-(no_packets*cost)
print(f"Balance: {balance}") # Balance: 6.59


# 3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. 
# If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. 
# Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
length=5.5
area=length**2
price=500
total=area*price
print(f"Amount: {total}") # Amount: 15125.0


# 4. Print binary representation of number 17
number=7
print(f"Binary of {number}: {format(number,'b')}") # Binary of 7: 111
