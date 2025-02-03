# TASK 46: Write a function in python to count the number of lines from a text file "story.txt" 
# which is not starting with an alphabet "T".

count=0
with open("story.txt",'r') as file:
    lines=file.readlines()
    print("Total number of lines in the file: ",len(lines))
    for i in lines:
        if not i.startswith('T'):
            count+=1
print("Number of lines not starting with T: ",count)
                
        
    

