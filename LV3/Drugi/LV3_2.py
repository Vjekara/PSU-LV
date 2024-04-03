import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mtcars = pd.read_csv('mtcars.csv')
print(mtcars)

mtcarsAvg = mtcars[mtcars['cyl'].isin([4,6,8])]


plt.figure(figsize = (8,6))
plt.bar(mtcarsAvg['cyl'], mtcars['mpg'])
plt.xlabel('Cylinders')
plt.ylabel('MPG')
plt.title('Cylinders vs MPG')
plt.show()