# TASK 49:
'''Part 1: Write a Python program to check that a string contains only a certain set of characters 
(in this case a-z, A-Z and 0-9).'''


import re

def is_match(string):
    pattern=r"^[a-zA-Z0-9]+$"
    
    if re.match(pattern,string):
        print(f'{string} is Valid')
    else:
        print(f'{string} is Invalid')

print("Part 1 Answers")
is_match("Hello123")
is_match("Hello@123")



#Part 2: Write a Python program that matches a string that has an a followed by zero or one 'b

def is_match2(string):
    pattern2=r"^ab?$"
    
    if re.match(pattern2,string):
        print(f'{string} is Valid')
    else:
        print(f'{string} is Invalid')
 
print("\nPart 2 Answers\n")       
is_match2("ab")  
is_match2("a")
is_match2("abb")
        