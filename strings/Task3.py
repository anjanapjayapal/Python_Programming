# TASK 3: Write a program to remove duplicate values in the given string.


# PROGRAM

str1=input("Enter a string: ")

# Initialize an empty list to store unique characters
new=[]

for i in str1:
    if not i in new:
        new.append(i)

# Convert the list back to a string
result = ''.join(new) 
        
print(f"String after removing duplicates: {result}")




# OUTPUT
'''
Enter a string: anjana
String after removing duplicates: anj
        
 '''       
