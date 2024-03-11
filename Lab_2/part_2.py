def y(x):
    if (x < 0):
        return x
    elif (x <=0 and x < 1):
        return 0
    else:
        return 2*x

x = int(input("Введіть значення х: "))
print(f"Функція y(x) = {y(x)}")