# TASK 37: Abstract class 'Shape' with abstract methods 'calculatearea()' and çalculateperimeter(). Create subclasses 'Circle' and 'Traingle'.

from abc import ABC,abstractmethod
import math

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return f"Area of circle: {3.14 * self.radius**2}"
    
    def perimeter(self):
        return f"Perimeter of circle: {2 * 3.14 * self.radius}\n"
    
class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
    def area(self):
        s=(self.a + self.b + self.c)/2
        area=math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return f"Area of Triangle: {area}"
    
    def perimeter(self):
        return f"Perimeter of Triangle: {self.a + self.b + self.c}"
    
obj1=Circle(3)
print(obj1.area())
print(obj1.perimeter())

obj2=Triangle(3,4,5)
print(obj2.area())
print(obj2.perimeter())





    

        