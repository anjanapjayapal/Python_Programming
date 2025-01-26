# TASK 19: Print the patterns

#1. 
'''
* 
** 
*** 
**** 
***** 
***** 
**** 
*** 
** 
*
'''

n=5 # Number of rows for the upper half

# Upper half of the pattern
for i in range(1,n+1):
    print("*"*i,end=' ')
    print()

# Lower half of the pattern
for j in range(n,0,-1):
    print("*"*j,end=' ')
    print()
    

#2.
'''
1 
2 3 
4 5 6 
7 8 9 10
'''

n=4
first=1 
for i in range(1,n+1):
    for j in range(i):
        print(first,end=' ')
        first+=1
    print()


#3.
'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''

n=5
for i in range(1,n+1):
    print(' '*(n-i)+"* "*i)



#4.
'''
6
56
456
3456
23456
123456
'''

n=6
for i in range(n,0,-1):
    for j in range(i,n+1):
        print(j,end='')
    print()











