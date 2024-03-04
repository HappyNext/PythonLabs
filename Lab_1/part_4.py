from math import *

print("Введіть значення х (1.11-1.15): ")
x = float(input())

y = acos(((x-log10(x)/(1+cos(3*x)))+1))

print("Значення y = ",y)