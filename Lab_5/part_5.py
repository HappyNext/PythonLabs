import numpy as np

array = np.random.randint(1,100,size=(4,6))
print(f'Заданий масив:\n {array}\nВідсортований масив:\n {np.sort(array)}\nМінімальне значення:\n {np.min(array)}\nСума усіх елементів:\n {np.sum(array)}\nСереднє значення:\n {np.mean(array)}')
