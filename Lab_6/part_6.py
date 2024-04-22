import matplotlib.pyplot as plt


categories = ['1й квартал', '2й квартал', '3й квартал', '4й квартал']
values1 = [112, 231, 178, 129]
values2 = [187, 195, 118, 149]
values3 = [167, 129, 70, 90]


bar_width = 0.2
index = range(len(categories))
opacity = 0.8


plt.figure(figsize=(10, 6))

plt.barh(index, values1, bar_width, alpha=opacity, color='b', label='MS Excel')
plt.barh([i + bar_width for i in index], values2, bar_width, alpha=opacity, color='g', label='MS Word')
plt.barh([i + 2 * bar_width for i in index], values3, bar_width, alpha=opacity, color='r', label='MS Power Point')


plt.xlabel('Значения')

plt.ylabel('Категории')

plt.title('Обьемы продаж книг в разрезе кварталов')

plt.legend()


plt.yticks([i + bar_width for i in index], categories)


plt.gca().invert_yaxis()


plt.savefig('grouped_horizontal_bar_chart.png')


plt.show()