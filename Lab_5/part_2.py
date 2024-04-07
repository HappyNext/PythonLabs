import numpy as np

# Заданий масив
original_array = np.random.randint(1, 100, 15)  # Згенеруємо випадковий масив з чисел від 1 до 100
print("Заданий масив:", original_array)

# Зменшуємо кожен елемент на середнє значення
mean_value = np.mean(original_array)
modified_array = original_array - mean_value
print("Змінений масив:", modified_array)

# Відсортуємо масив за зростанням
sorted_array = np.sort(modified_array)
print("Відсортований масив за зростанням:", sorted_array)

# Записуємо результати операцій у файл
with open("result.txt", "w") as file:
    file.write("Заданий масив:\n")
    file.write(np.array2string(original_array) + "\n\n")
    file.write("Змінений масив (зменшений на середнє значення):\n")
    file.write(np.array2string(modified_array) + "\n\n")
    file.write("Відсортований масив за зростанням:\n")
    file.write(np.array2string(sorted_array))