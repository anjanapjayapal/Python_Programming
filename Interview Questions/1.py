
string="""He said, "That's what he said"""

words=[]
word=''

for char in string:
    if char.isalpha():
        word+=char
    else:
        if word:
            words.append(word)
            word=''
if word:
    words.append(word)   # Add the last word if any
    
for i in words:
    print(i)



# OUTPUT
'''
He
said
That
s
what
he
said

'''


