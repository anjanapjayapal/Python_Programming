# Print the character and their count


string='hai hello how are you'

dict={}
for i in string:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
        
        
print(dict)


# OUTPUT
'''
{'h': 3, 'a': 2, 'i': 1, ' ': 4, 'e': 2, 'l': 2, 'o': 3, 'w': 1, 'r': 1, 'y': 1, 'u': 1}
'''