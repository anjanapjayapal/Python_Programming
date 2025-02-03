# TASK 48: Write a function in Python to count and display the total number of words in a text file.

count=0
with open("story.txt",'r') as file:
    content=file.read()
    words=content.split()
    
print(content)   
print("Count of words in the file: ",len(words))
