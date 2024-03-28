import matplotlib.pyplot as plt
import numpy as np

x =np.array([1,2,3,3,1])
y =np.array([1,2,2,1,1])

plt.xlabel('x os')
plt.ylabel('y os')
plt.axis((0,4,0,4))
plt.plot(x, y, 'b', linewidth=3, marker=".", markersize=15, markerfacecolor='0.5', color='yellow')

plt.title('Primjer')

plt.show()