class Point3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def printinfo(self):
        if (hasattr(self,'z')):
            print(f"Point3D ({self.x}, {self.y}, {self.z})")
        else:
            print(f"Point3D ({self.x}, {self.y})")

    def del_z(self):
        del self.z

point = Point3D(3,5,6)
point.printinfo()
point.x = 10
point.printinfo()
point.del_z()
point.printinfo()

