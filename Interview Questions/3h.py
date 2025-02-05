
n=int(input("Enter the number of lines: "))

for i in range(1,n+1):
    print("* "*i,end=' ')
    print()
    
print()
for j in range(n,0,-1):
    print("* "*j,end=' ')
    print()

    
    
# OUTPUT
'''
Enter the number of lines: 5
*  
* *
* * *
* * * *
* * * * *

* * * * *
* * * *
* * *
* *
*
'''