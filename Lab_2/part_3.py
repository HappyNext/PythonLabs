def calc(x,y,type):
    if type == '+':
        return x+y
    elif type == '-':
        return x-y
    elif type == '*':
        return x*y
    elif type == '/':
        try:
            return x/y
        except ZeroDivisionError:
            print("Ділення на нуль!")

x = input("Введіть х: ")
y = input("Введіть y: ")
try:
    x = int(x)
    y = int(y)
except ValueError:
    print("Введено не число!")
type = input("Введіть операцію (+,-,*,/): ")
print(calc(x,y,type))