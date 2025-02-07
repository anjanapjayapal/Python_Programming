# Find the first non-repeating element of an array

array=[1,7,4,8,1,7]


def check(array):
    for i in range(len(array)):
        is_repeating = False
        for j in range(len(array)):
            if i != j and array[i] == array[j]:
                is_repeating = True
                break
        if not is_repeating:
            return array[i]
    return None  # If all elements are repeating

print(f'First non-repeating element: {check(array)}')

            
    
    