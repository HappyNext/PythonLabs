class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed -= 10

    def get_speed(self):
        return self.speed

car1 = Car("BMW", "M5","2023")
for i in range (6):
    car1.accelerate()
    print(car1.speed)
for i in range (5):
    car1.brake()
    print(car1.speed)


