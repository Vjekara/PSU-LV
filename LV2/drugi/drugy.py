import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = np.loadtxt(open(r"C:\Users\student\Desktop\LV2\drugi\mtcars.csv", "rb"), usecols=(1,4,6,2),
                  delimiter=",", skiprows=1) # stavio sam cols 1,4,6,2 jer nam ostali nisu potrebni
#indeks pocinje od nula

mpg =data[:, 0] #prvi stupac(indeks je nula)
hp = data[:, 1] #cetvrti stupac(indeks je jedan jer koristim columns 1 4 6 2)
wt=data[:, 2] #sesti stupac(indeks je 2 jer koristim columns 1 4 6 2)
cyl=data[:,3]

plt.scatter(mpg, hp, s=wt*15) #pomnozio sam brojem 15 da se tocke bolje vide jer wt vrijednosti nisu bas velike
plt.xlabel("mpg")
plt.ylabel("hp")
plt.title("ovisnost potrosnje automobila o konjskim snagama")
plt.show()

min_mpg=mpg.min()
max_mpg=mpg.max()
avg_mpg=mpg.mean()

print(min_mpg)
print(max_mpg)
print(avg_mpg)
print("\n")

cilindri6 = np.where(cyl == 6)[0]
mpg6= mpg[cilindri6]

min_mpg6=np.min(mpg6)
max_mpg6=np.max(mpg6)
avg_mpg6=np.mean(mpg6)

print(min_mpg6)
print(max_mpg6)
print(avg_mpg6)