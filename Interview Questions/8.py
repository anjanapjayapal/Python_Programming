

class SubsetGenerator:
    def __init__(self, arr):
        self.arr = arr  # Store the input array

    def generate_subsets(self):
        result = [[]]  # Start with an empty subset
        
        for num in self.arr:
            new_subsets = [subset + [num] for subset in result]  # Add num to all existing subsets
            result.extend(new_subsets)  # Add new subsets to the result list
        
        return result  # Return all subsets

# Example usage
subset_obj = SubsetGenerator([4, 5, 6])
print(subset_obj.generate_subsets())

