import numpy as np

array = np.random.randint(0,10,size=(10,3))

x = array[:,0]
y = array[:,1]
z = array[:,2]

r = np.sqrt(x**2 + y**2 + z**2)
theta = np.arccos(z / r)
phi = np.arctan2(y,x)

print("Декартові координати:")
print(array)
print("\nПолярні координати:")
print("Радіус (r):", r)
print("Кут theta:", theta)
print("Кут phi:", phi)