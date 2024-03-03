from abc import ABC, abstractmethod



class BaseShape(ABC):
    @abstractmethod
    def get_area(self):
        pass
    @abstractmethod
    def set_height(self, height):
        pass
    @abstractmethod
    def set_width(self, width):
        pass
      
class Circle(BaseShape):
  def __init__(self, radius):
      self.radius = radius
  def get_area(self):
      return 3.14 * self.radius * self.radius
  def set_height(self, height):
      self.radius = height / 2
  def set_width(self, width):
      self.radius = width / 2
    
class Rectangle(BaseShape):
  def __init__(self, width, height):
      self.width = width
      self.height = height
  def get_area(self):
      return self.width * self.height
  def set_height(self, height):
      self.height = height
  def set_width(self, width):
      self.width = width
    
class Triangle(BaseShape):
  def __init__(self, base, height):
      self.base = base
      self.height = height
  def set_height(self, height):
    self.height = height
  def set_width(self, width):
    self.base = width
  def get_area(self):
      return 0.5 * self.base * self.height
    
class Polygon(BaseShape):
  def __init__(self, num_sides, side_length):
      self.num_sides = num_sides
      self.side_length = side_length
  def get_area(self):
      return self.num_sides * self.side_length
  def set_height(self, height):
      self.side_length = height
  def set_width(self, width):
      self.num_sides = width

def main():
  #some sample stuff to show you how it would work and what not.
  circle = Circle(5)
  rectangle = Rectangle(3, 6)
  triangle = Triangle(4, 3)
  polygon = Polygon(6, 4)
  shapes = [circle, rectangle, triangle, polygon]
  for shape in shapes:
      print(f"Area of {type(shape).__name__}: {shape.get_area()}")
  circle.set_height(8)
  circle.set_width(8)
  rectangle.set_height(5)
  rectangle.set_width(7)
  for shape in shapes:
      print(f"Area of {type(shape).__name__}: {shape.get_area()}")
if __name__ == "__main__":
  main()
#this shows LSP since all of the shapes' subclasses can be utilized over the BaseShape 
#main-class. This is done by allowing the subclass to abstractly inherit the get and set
#methods and define them within there own specifications, even if the function doesn't  
#make sense necessarily. We can battle the complications by inheriting the get_area
#function through each subclass and if we misuse the height and width functions for 
#other purposes, we can utilize the same abstract functions like how I have sort of 
#proposed in the WAP with base being width or how I have th polygon set up to use 
#the width as number of sides.