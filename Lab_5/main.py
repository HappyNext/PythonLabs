import numpy as np

array1 = np.array([1,2,3,4,5,6])
array2 = np.array([7,8,9,10,11,12])

print('Додавання масивів: ',array1+array2,'\nВіднімання масивів: ',array1-array2,'\nМноження масивів: ',array1*array2,'\nДілення масивів: ',array1/array2)
array = np.concatenate((array1,array2))
print(f'Новий масив: {array}\nМінімальний елемент: {np.min(array)}\nМаксимальний елемент: {np.max(array)}\nСума елементів: {np.sum(array)}\nДобуток елементів: {np.prod(array)}')