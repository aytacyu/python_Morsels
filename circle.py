"""
***The circle should have a radius, a diameter, and an area. It should also have a nice string representation.
***Additionally the radius should default to 1 if no radius is specified when you create your circle.
***Make sure when the radius of your class changes that the diameter and area both change as well
***Make sure you can set the diameter attribute in your Circle class and the radius will update
and also that you cannot set the area (setting area should raise an AttributeError)
***Make sure your radius cannot be set to a negative number
"""
from math import pi
class Circle():
    def __init__(self,radius=1):
        self.radius = radius
    def __repr__(self):
        return f'Circle({self.radius})'
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self,radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius
    @property
    def diameter(self):
        return self.radius*2
    @diameter.setter
    def diameter(self,diameter):
        self.radius = diameter /2
    @property
    def area(self):
        return pi*self.radius**2
    def print_circle(self):
        print(c)
        print(c.radius)
        print(c.diameter)
        print("{:0.2f}".format(c.area))
c = Circle()
c.print_circle()
c.radius=3
c.print_circle()
c.diameter=8
c.print_circle()
c.radius = 3
c.print_circle()
c.radius = -3
c.print_circle()
