point_input = input("Введіть точку (x, y): ")

# Разделение строки на координаты
coordinates = point_input.split(',')

# Преобразование строковых значений в числа
x = float(coordinates[0])
y = float(coordinates[1])

if (x == 0 and y == 0):
    print("Точка на початку координат")
elif (x > 0 and y > 0):
    print("Точка знаходиться у першій чверті")
elif (x < 0 and y > 0):
    print("Точка знаходиться у другій чверті")
elif (x < 0 and y < 0):
    print("Точка знаходиться у третій чверті")
else:
    print("Точка знаходиться у четвертій чверті")