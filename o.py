from abc import ABC, abstractmethod
import math




class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius**2
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return self.side_length**2
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width
def main():
    #create an array of random sample shapes for fun.
    shapes = [Circle(5), Square(4), Rectangle(3, 6)]

    #loop through the list of shapes and print areas
    for shape in shapes:
        print(f"Area of {type(shape).__name__}: {shape.get_area()}")
if __name__ == "__main__":
    main()

#this code shows OCP since if we want to add a new type of shape we have to create its 
#own shape class without interfering with anything that already exists.