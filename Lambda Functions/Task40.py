# TASK 40: Anonymous function
'''Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]'''


# Original List
lst=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Sorting the list based on the second element of each tuple
sorted_lst=sorted(lst,key=lambda x : x[1])  # sorted(iterable,key)
print(sorted_lst)

average=(sum(map(lambda x: x[1] ,sorted_lst))) / len(sorted_lst)
print("Average of marks: ",average)