
string='i.like.this.program.very.much'

words=[]
word=''

for char in string:
    if char.isalpha():
        word+=char
    else:
        if word:
            words.append(word)
            word=''
        words.append(char)
if word:
    words.append(word) 
 
new=''   
for i in range(len(words)-1,-1,-1):
    new+=words[i]
    
print(new)


# OUTPUT
'''
much.very.program.this.like.i
'''
        
        

