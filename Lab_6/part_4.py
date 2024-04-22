import matplotlib.pyplot as plt

# Функція для обчислення частоти голосних літер у тексті
def count_vowels(text):
    vowels = 'aeiouAEIOU'
    vowel_counts = {vowel: 0 for vowel in vowels}
    total_vowels = 0

    for char in text:
        if char in vowels:
            vowel_counts[char] += 1
            total_vowels += 1

    return vowel_counts, total_vowels

# Зчитуємо текст з файлу
with open('text.txt', 'r') as file:
    text = file.read().lower()  # Перетворюємо текст у нижній регістр

# Обчислюємо частоту голосних літер
vowel_counts, total_vowels = count_vowels(text)

# Створюємо стовпчикову гістограму
vowels = list(vowel_counts.keys())
counts = list(vowel_counts.values())

plt.bar(vowels, counts)
plt.xlabel('Голосні літери')
plt.ylabel('Частота появи')
plt.title('Гістограма частоти появи голосних літер у тексті')
plt.grid(True)

# Зберігаємо графік у файл PNG
plt.savefig('histogram.png')

# Показуємо графік
plt.show()
