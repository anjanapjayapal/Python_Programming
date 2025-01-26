# TASK 23: Print the given pattern
'''
13579
3579
579
79
9
'''


# PROGRAM

num = "13579"  # Input string of digits

# Loop to print the pattern
for i in range(len(num)):
    print(num[i:])  # Print the substring starting from the current index
