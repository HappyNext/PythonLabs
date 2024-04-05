import time

# Декоратор для вимірювання часу виконання функції
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання функції {func.__name__}: {end_time - start_time} сек")
        return result
    return wrapper

# Функція для читання кортежу
@measure_time
def read_tuple(data):
    for _ in range(len(data)):
        pass

# Функція для читання списку
@measure_time
def read_list(data):
    for _ in range(len(data)):
        pass

# Тестування для різних значень N
def test_speed(N):
    data_list = [i for i in range(N)]  # Створення списку
    data_tuple = tuple(data_list)       # Перетворення списку в кортеж

    print(f"При N = {N}:")
    read_tuple(data_tuple)  # Вимірюємо час для читання кортежу
    read_list(data_list)    # Вимірюємо час для читання списку

# Викликаємо тестування
test_speed(1000000)  # Приклад для N = 1 мільйон
