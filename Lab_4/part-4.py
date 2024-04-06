# Відкриття файлу для читання
with open('part_4.txt', 'r') as file:
    # а) перший символ першого рядка
    first_char_first_line = file.readline()[0]
    print("а) Перший символ першого рядка:", first_char_first_line)

    # Переміщення курсора на початок файлу для подальшого читання
    file.seek(0)

    # б) п'ятий символ першого рядка
    fifth_char_first_line = file.readline()[4]
    print("б) П'ятий символ першого рядка:", fifth_char_first_line)

    # Переміщення курсора на початок файлу для подальшого читання
    file.seek(0)

    # в) перші 10 символів першого рядка
    first_10_chars_first_line = file.readline()[:10]
    print("в) Перші 10 символів першого рядка:", first_10_chars_first_line)

    # Переміщення курсора на початок файлу для подальшого читання
    file.seek(0)

    # г) перший символ другого рядка
    first_char_second_line = file.readlines()[1][0]
    print("г) Перший символ другого рядка:", first_char_second_line)

    # Переміщення курсора на початок файлу для подальшого читання
    file.seek(0)

    # д) k-й символ n-го рядка (наприклад, k=3, n=2)
    k = 3
    n = 2
    kth_char_nth_line = file.readlines()[n - 1][k - 1]
    print(f"д) {k}-й символ {n}-го рядка:", kth_char_nth_line)