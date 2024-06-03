import matplotlib.pyplot as plt

labels = ['Полісся', 'Грант', 'Міріса', 'AT Trading', 'Trade F']
sizes = [10, 45, 19, 11, 15]
colors = ['#ff9999', 'green', '#66b3ff', '#99ff99', '#ffcc99']
explode = (0, 0.1, 0, 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')

plt.title('Розподіл ринку серед компаній')

plt.savefig('pie_chart.png')

plt.show()
