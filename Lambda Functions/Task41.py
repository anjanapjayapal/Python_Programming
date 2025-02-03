# TASK 41: Write a Python program to sort a list of dictionaries using Lambda.


dict=[
    {'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': 2, 'color':
     'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]


# Sorting the list based on the 'model' key
sorted_dict=sorted(dict,key=lambda x : x['model'])
print(sorted_dict)
