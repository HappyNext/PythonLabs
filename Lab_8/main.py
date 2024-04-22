import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def square(self):
        return math.pi*(self.radius**2)
    def lenght(self):
        return math.pi*(self.radius/2)

    def printinfo(self):
        print(f"Коло радіусом: {self.radius}, площею: {self.square()} та довжиною: {self.lenght()}")

circle1 = Circle(10)
circle1.printinfo()
