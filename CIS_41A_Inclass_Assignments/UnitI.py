from math import pi

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def getArea(self):
        return ((self.radius**2)*pi)

class Cylinder(Circle):
    def __init__(self,radius,height):
        Circle.__init__(self,radius)
        self.height = height
    def getVolume(self):
        return (Circle.getArea(self)*self.height)

circ = Circle(4)
print("Circle area is:",format(circ.getArea(),"^-03.2f"))
cill = Cylinder(2,5)
print('Cylinder volume is:',format(cill.getVolume(),"^-03.2f"))