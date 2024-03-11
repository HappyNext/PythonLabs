str = "Олег, ІКМ-121, Прикладна математика"

data = str.split(",")

print(data[1])

data[0] = "Семененко"

print(data)

print("Кіл-сть слів у рядку: ",len(str.split()))