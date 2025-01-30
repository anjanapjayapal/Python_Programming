# TASK 33: Implement a abstract class 'Shape' and abstract method 'CalculateArea'. Create concrete classes 'Circle' and 'Rectangle'.

from abc import ABC ,abstractmethod

class Shape(ABC):                   # Abstract class
    @abstractmethod
    def calculateArea(self):        # Abstract method
        pass

class Circle(Shape):                # Concrete class 
    def __init__(self,radius):
        self.radius=radius
        
    def calculateArea(self):        
        return 3.14 * self.radius**2
    
class Rectangle(Shape):             # Concrete class
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def calculateArea(self):
        return self.length * self.breadth
    
circle=Circle(3)
print(f"Area of circle: {circle.calculateArea()}")

rectangle=Rectangle(4,3)
print(f"Area of rectangle: {rectangle.calculateArea()}")

    
    
