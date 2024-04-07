def count_positive_halves(*args):
    # Разделяем последовательность на две половины
    n = len(args)
    half1 = args[:n // 2]
    half2 = args[n // 2:]

    # Если длина последовательности нечетная, корректируем длины половин
    if n % 2 != 0:
        half1 = half1[:-(n // 2)]
        half2 = half2[n // 2:]

    # Подсчитываем количество положительных элементов в каждой половине
    count_half1 = sum(1 for num in half1 if num > 0)
    count_half2 = sum(1 for num in half2 if num > 0)

    # Определяем, в какой половине больше положительных элементов
    if count_half1 > count_half2:
        return "Больше положительных элементов в первой половине"
    elif count_half1 < count_half2:
        return "Больше положительных элементов во второй половине"
    else:
        return "Количество положительных элементов в обеих половинах одинаково"


# Пример использования функции
sequence = [1, -2, -3, -4, -5, 6, 7, -8]
result = count_positive_halves(*sequence)
print(result)