# TASK 47: Write a function in Python to count words in a text file those are ending with alphabet "e".

count=0
with open("story.txt",'r') as file:
    lines=file.readlines()
    print("Total number of lines in the file: ",len(lines))
    for i in lines:
        if i.strip().endswith('e'):
            count+=1
print("Number of lines ends with e: ",count)