import numpy as np

array = np.random.randint(-15,16,size=(5,3))
print(f'Заданий масив:\n {array}')

newarray = np.where(array > 0,1,-1)
print(f'Новий масив:\n {newarray}')
