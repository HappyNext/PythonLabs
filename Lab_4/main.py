import numpy as np

def y(x):
    return 2*x-1

x = np.arange(-3,3.1,0.5)
print(x)
f = open('part_1.txt','w')
np.savetxt(f,y(x),delimiter=' ')
f.close()