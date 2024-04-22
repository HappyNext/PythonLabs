import matplotlib.pyplot as plt
import numpy as np
import math

def y1(x):
    return np.power(x, 3) * np.cos(np.power(x, 2))

def y2(x):
    return np.power(x, 3) * np.cos(15*x)

x = np.linspace(-2,3,20)
f1 = y1(x)
f2 = y2(x)

plt.plot(x,f1,color='red')
plt.plot(x,f2,color='green')
plt.annotate('Це початок координат', xy=(0, 0), xytext=(0, -6),
             arrowprops=dict(facecolor='black'))
plt.grid(True)
plt.xlabel('X',color='blue',fontsize='14')
plt.ylabel('Y',color='blue',fontsize='14')
plt.tight_layout()
plt.legend()
plt.show()

plt.subplot(2, 1, 1)
plt.plot(x,f1,color='red')
plt.title('Графік №1',fontsize=14)
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(x,f2,color='green')
plt.title('Графік №2',fontsize=14)
plt.grid()

plt.tight_layout()
plt.show()
