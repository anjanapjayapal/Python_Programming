
n=int(input("Enter the number of lines: "))

for i in range(n,0,-1):
    for j in range(i):
        print(i,end=' ')
        i-=1
    print()


# OUTPUT
'''
Enter the number of lines: 5
5 4 3 2 1 
4 3 2 1
3 2 1
2 1
1
'''
