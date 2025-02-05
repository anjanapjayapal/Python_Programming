
n=int(input("Enter the number of lines: "))

for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i,end=' ')
    print()


for j in range(1,n+1):
    print(" "*(n-j)+"* "*j,end=' ')
    print()
    
    

# OUTPUT
'''
Enter the number of lines: 5
* * * * *  
 * * * *
  * * *
   * *
    *
    *
   * *
  * * *
 * * * *
* * * * *
'''