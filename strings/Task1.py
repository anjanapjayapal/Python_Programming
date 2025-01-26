#TASK 1: Write a program that counts the number of vowels and consonants in a string.


# PROGRAM 

# Define a set of vowels
vowels_set='AEIOUaeiou'

str1=input("Enter a string: ")

# Initialize counters for vowels and consonants
vowels=0; consonants=0

for char in str1:
    if char.isalpha():# Check if the character is a letter
        if char in vowels_set:
            vowels+=1
        else:
            consonants+=1

# Print the results    
print(f"vowels: {vowels}\nconsonants:{consonants}")




# OUTPUT
'''
Enter a string: anjanajayapal
vowels: 6
consonants:7
'''









