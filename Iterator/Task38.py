# TASK 38: Write a program to create an iterator to print English alphabets from A to Z.

alphabets=[chr(letter) for letter in range(ord('A'), ord('Z') + 1)]

iterator=iter(alphabets)

for element in iterator:
    print(element,end=' ')
