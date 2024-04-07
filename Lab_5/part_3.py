import numpy as np
import csv

array = np.random.randint(1,100,20)
print(f'Заданий масив: {array}')
newarray = array.reshape(5,4)
print(f'Двовимірний масив:\n {newarray}')
newarray = newarray + 10
print(f'Двовимірний масив + 10:\n {newarray}')

with open('result.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Записуємо шапку
    writer.writerow(['Column1', 'Column2', 'Column3', 'Column4', 'Column5'])

    # Записуємо дані
    for row in newarray:
        writer.writerow(row)