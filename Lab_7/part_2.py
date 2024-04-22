class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average_marks(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

student1 = Student("Іван",  {
    'Математика': 5,
    'Фізика': 4,
    'Історія': 5
})

# Виведення ПІБ студента
print(student1.name)

# Виведення оцінок студента
print(student1.marks)

# Виведення середньої оцінки
print(student1.average_marks())