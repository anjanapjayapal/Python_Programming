# TASK 30:
'''Create a Python function that takes a string as input and counts the number of
vowels and consonants in the string.'''

# Function to count vowels and consonants
def count_vowels_and_consonants(input_string):
    vowels = "AEIOUaeiou"
    vowels_count = 0
    consonants_count = 0

    # Iterate through each character in the string
    for char in input_string:
        if char.isalpha():  # Check if the character is an alphabet
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1

    return vowels_count, consonants_count

# Take user input
input_string = input("Enter a string: ")

# Call the function and display the result
vowels_count, consonants_count = count_vowels_and_consonants(input_string)
print(f"Vowels: {vowels_count}")
print(f"Consonants: {consonants_count}")

# OUTPUT
'''
Enter a string: hello girl
Vowels: 3
Consonants: 6
'''
