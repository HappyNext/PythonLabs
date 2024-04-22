import matplotlib.pyplot as plt
import numpy as np


def y(x):
    return x*2

x = np.linspace(0,10,20)
plt.plot(x,y(x),color='red')
plt.xlabel('X',size='14')
plt.ylabel('Y',size='14')
plt.title('Графік функції y(x) = 2x',size='14')
plt.grid(True)
plt.legend()
plt.show()