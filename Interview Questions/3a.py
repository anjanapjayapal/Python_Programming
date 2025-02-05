
n=int(input("Number of lines: "))

for i in range(n):
    value=' '.join(str(11 **i))
    print(" "*(n-i-1)+value )
    




# OUTPUT
'''
Enter the number of lines: 5

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

'''