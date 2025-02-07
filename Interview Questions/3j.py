
n=int(input("Enter the number of lines: "))

for i in range(1,n+1):
    for j in range(i):
        print(" "*(n-i) + "* "," "*(j-i)+"*" ,end=' ')
        print()
    
