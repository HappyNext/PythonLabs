def quick_sort(lst):
    """Швидке сортування"""
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def search_element(lst, value):
    """Пошук елементу за значенням"""
    return value in lst

def search_first_p_min(lst, p):
    """Пошук перших p мінімальних елементів"""
    return sorted(lst)[:p]

def arithmetic_mean(lst):
    """Пошук середнього арифметичного"""
    return sum(lst) / len(lst)

def remove_duplicates(lst):
    """Повернення списку без повторень"""
    return list(set(lst))

def process_lists(input_file, output_file):
    """Обробка списків з файлу та запис результатів у файл"""
    with open(input_file, 'r') as f:
        lists = [list(map(int, line.strip().split())) for line in f]

    with open(output_file, 'a') as f:
        for lst in lists:
            sorted_lst = quick_sort(lst)
            f.write(f"Sorted list: {sorted_lst}\n")
            value = 10
            f.write(f"Element {value} exists: {search_element(lst, value)}\n")
            p = 5
            f.write(f"First {p} min elements: {search_first_p_min(lst, p)}\n")
            avg = arithmetic_mean(lst)
            f.write(f"Arithmetic mean: {avg}\n")
            no_duplicates_lst = remove_duplicates(lst)
            f.write(f"List without duplicates: {no_duplicates_lst}\n")
            f.write("\n")

# Виклик функції для обробки списків з файлу 'input.txt' та запису результатів у файл 'output.txt'
process_lists('input.txt', 'output.txt')