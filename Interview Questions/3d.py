
n=int(input("Enter the number of lines: "))

num=1
for i in range(1,n+1,2):
    for j in range(i):
        print(num,end=' ')
        num+=1
    print()
    

# OUTPUT
'''
Enter the number of lines: 5
1 
2 3 4
5 6 7 8 9
'''