
n=int(input("Enter the number of lines: "))

for i in range(1,n+1):
    print(i,end=' ')
    for j in range(2,i+1):
        print(i*j,end=' ')
    print()



# OUTPUT
'''
Enter the number of lines: 5

1 
2 4
3 6 9
4 8 12 16
5 10 15 20 25

'''