class Triangle:
    def __init__(self, a, b, c):
        # Перевірка чи можливо утворити трикутник зі сторонами a, b, і c
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Три сторони a, b, і c не можуть утворити трикутник")
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        # Обчислення напівпериметру
        s = self.perimeter() / 2
        # Формула Герона для обчислення площі
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

try:
    triangle = Triangle(3, 4, 5)
    print("Периметр трикутника:", triangle.perimeter())
    print("Площа трикутника:", triangle.square())
except ValueError as e:
    print(e)
