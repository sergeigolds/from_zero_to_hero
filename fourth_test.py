class Line:

    def __init__(self, cord1, cord2):
        self.cord1 = coordinate1
        self.cord2 = coordinate2

    def distance(self):
        x1, y1 = coordinate1
        x2, y2 = coordinate2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def slope(self):
        x1, y1 = coordinate1
        x2, y2 = coordinate2
        return (y2 - y1) / (x2 - x1)


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

li.distance()
li.slope()


class Cylinder:
    from math import pi

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.pi * self.height * (self.radius ** 2)

    def surface_area(self):
        top = self.pi * (self.radius ** 2)
        return (2 * top) + (2 * self.pi * self.radius * self.height)


c = Cylinder(2, 3)

c.volume()
c.surface_area()
