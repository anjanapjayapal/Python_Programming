# TASK 34: Create a class 'MathUtils' that provides various mathematical utility functions. Also implement a static method 'Calculatesum' which should accept an array of elements and return their sum

class MathUtils():
    
    @staticmethod
    def calculatesum():
        arr=list(map(int,input("Enter numbers with spaces: ").split()))
        return sum(arr)
    
    def difference(self):
        a,b=map(int,input("Enter two numbers with spaces: ").split())
        return a-b
    
    def division(self):
        a,b=map(int,input("Enter two numbers with spaces: ").split())
        return a/b
    
    def multiplication(self):
        a,b=map(int,input("Enter two numbers with spaces: ").split())
        return a*b

# Calling static method directly using the class    
print(f'Sum of array of elements: {MathUtils.calculatesum()}\n')

obj=MathUtils() # Creating an instance of MathUtils

print(f'Difference of numbers: {obj.difference()}\n')  
print(f'Multiplication of numbers: {obj.multiplication()}\n') 
print(f'Division of numbers: {obj.division()}\n')   


