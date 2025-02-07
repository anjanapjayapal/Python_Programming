
numbers=[10,20,10,40,50,60,70]  # target=50 output= 3, 4 (Indices of the numbers whose sum gives the target)

target=50

def check(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] != numbers[j]:
                if numbers[i]+numbers[j] == target:
                    return i,j

print(check(numbers))
            