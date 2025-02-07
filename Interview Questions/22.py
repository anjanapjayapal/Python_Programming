# Second largest number in a list

def second_largest(arr):
    if len(arr) < 2:
        return None  # Not enough elements to find second largest
    
    largest = second = float('-inf')  # Initialize with very small values

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second if second != float('-inf') else None  # If no second largest, return None

# Example usage
array = [10, 20, 4, 45, 99, 99, 6]
print(f'Second largest number: {second_largest(array)}')




        