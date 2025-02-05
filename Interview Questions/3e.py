
n=int(input("Enter the number of lines: "))


for i in range(n):
    for j in range(i,-1,-1):
        print(chr(69-j), end=' ')
    print()
    
    
    
# OUTPUT
'''
Enter the number of lines: 5
E 
D E
C D E
B C D E
A B C D E
'''
