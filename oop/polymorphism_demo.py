import math

class Shape:
    def area(self):
        """Raises NotImplementedError to indicate derived classes need to override."""
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculates rectangle area: length × width."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculates circle area: π × radius²."""
        return math.pi * (self.radius ** 2)
``"

And here's the `(link unavailable)` script for testing:

python
from polymorphism_demo import Rectangle, Circle

def main():
    rectangle = Rectangle(4, 5)
    circle = Circle(3)

    print(f"Rectangle area: {rectangle.area()}")
    print(f"Circle area: {circle.area():.2f}")

if _name_ == "_main_":
    main()
