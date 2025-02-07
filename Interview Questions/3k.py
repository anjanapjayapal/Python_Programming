
n= int(input("Enter the number of lines: "))

num=10; step=2

for i in range(1,n+1):
    print(' '.join(str(num-step*j)for j in range(i)))




# OUTPUT
'''
Enter the number of lines: 5
10
10 8
10 8 6
10 8 6 4
10 8 6 4 2
'''