
words=['apple','orange','jackfruit','kiwi']

dic={}
for word in words:
    if word not in dic:
        dic[word]=len(word)
        
longest = max(dic, key=dic.get)
shortest = min(dic, key=dic.get)


print(f'Longest word: {longest}\nShortest word: {shortest}')