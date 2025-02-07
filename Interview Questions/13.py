

with open("story.txt",'r') as file:
    content=file.read()
    words=content.split()
 
 
dictionary={}   
for word in words:
    if word in dictionary:
        dictionary[word]+=1
    else:
        dictionary[word]=1


print(dictionary)
        
    
    