from math import pi

class Shape:
  """
  Base class representing a generic shape.
  """
  def area(self):
    """
    Raises a NotImplementedError as derived classes must implement this method.
    """
    raise NotImplementedError("Area calculation not implemented for base Shape class")

class Rectangle(Shape):
  """
  Derived class representing a rectangle with specific area calculation.
  """
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def area(self):
    """
    Overrides the base area method to calculate the area of a rectangle.
    """
    return self.length * self.width

class Circle(Shape):
  """
  Derived class representing a circle with specific area calculation.
  """
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    """
    Overrides the base area method to calculate the area of a circle.
    """
    return pi * self.radius**2


from polymorphism_demo import Shape, Rectangle, Circle
import math

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()