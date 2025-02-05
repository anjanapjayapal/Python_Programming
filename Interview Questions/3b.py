
n=int(input("Enter the number of lines: "))


for i in range(1,n+1):
    print(f"{i}"*i,end='')
    for j in range(i+1,n+1):
        print(j,end='')
    print()
    


# OUTPUT
'''
Enter the number of lines: 5

12345
22345
33345
44445
55555

'''

    