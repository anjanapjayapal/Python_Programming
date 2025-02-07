

string=input("Enter the string: ")


upper=0; lower=0

for i in string:
    if i.isalpha():
        if i.isupper():
            upper+=1
        else:
            lower+=1
print(f'Uppercase count: {upper}\nLowercase count: {lower}')
        
        

# OUTPUT
'''
Enter the string: Anjana Jayapal 21
Uppercase count: 2
Lowercase count: 11
'''