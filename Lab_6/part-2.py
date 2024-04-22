import matplotlib.pyplot as plt
import numpy as np


def y1(x):
    return abs(x)

def y2(x):
    return pow(x,3)

def y3(x):
    return np.sqrt(x)

x = np.linspace(-6,6,10)

plt.plot(x,y1(x),'r-',label='abs(x)')
plt.plot(x,y2(x),'g--',label='x^3')
plt.plot(x,y3(x),'b',label='sqrt(x)')
plt.grid(True)
plt.xlabel('X',color='red',fontsize='14')
plt.ylabel('Y',color='red',fontsize='14')
plt.title('Графіки математичних функцій', fontsize=16, color='blue', fontweight='bold')

# Сохранение изображения в формате PNG
plt.savefig('графіки_функцій.png')

# Сохранение изображения в формате PDF
plt.savefig('графіки_функцій.pdf')

plt.tight_layout()  # автоматическая коррекция расположения графиков
plt.legend(loc='lower right')
plt.show()