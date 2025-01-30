# TASK 36: Abstract class 'Animal' with abstract method 'sound()'. Create subclasses 'Lion' and 'Tiger'.

from abc import ABC,abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def sound(self,sound):
        pass
    
class Lion(Animal):
    def __init__(self,animal):
        self.animal=animal
        
    def sound(self,sound):
        return f"{self.animal} makes {sound} sound"
    
class Tiger(Animal):
    def __init__(self,animal):
        self.animal=animal
        
    def sound(self,sound):
        return f"{self.animal} makes {sound} sound"
    
animal1=Lion("Lion")
print(animal1.sound("Roar"))

animal2=Tiger("Tiger")
print(animal2.sound("Growl"))