class MainClass:
    def __init__(self, text):
        self.text = text
    def printinfo(self):
        print(f"Object MainClass: {self.text}")
class HeirClass(MainClass):
    def __init__(self, text, number):
        super().__init__(text)
        self.number = number
    def printinfo(self):
        print(f"Object HeirClass: {self.text}, {self.number}")

obj1 = MainClass("Hello!")
obj2 = HeirClass("Hello World!",43)
obj1.printinfo()
obj2.printinfo()