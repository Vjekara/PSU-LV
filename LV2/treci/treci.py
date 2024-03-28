import numpy as np
import matplotlib.pyplot as plt
img = plt.imread("tiger.png")
img = img[:,:,0].copy()
print(img.shape)
print(img.dtype)

broj = 150
brightness = img + broj #inkrementirao sam za x, ovo se dodaje svim pikselima
brightness = np.clip(brightness, 0, 255) # granice vrijednosti moraju ostat u rasponu od 0 do 255

plt.figure() #prikaz slike
plt.imshow(brightness, cmap="gray")
plt.title("brightness")

plt.figure()
plt.imshow(img, cmap="gray")
plt.title("original")

rotirana = np.rot90(img, k= 1) #k = 1  znaci jedna rotacija za 90 stupnjeva suprotno smjera kazaljke na satu
plt.figure()
plt.imshow(rotirana, cmap="gray")
plt.title("rotirano za 90")

mirror = img[:, ::-1] #zrcalim sliku
plt.figure()
plt.imshow(mirror, cmap="gray")
plt.title("zrcaljena slika")

length = img.shape[0]
height = img.shape[1]

smanjena = img.reshape(img.shape[0] // 10, 10, img.shape[1] // 10, 10).mean(axis=(1,3)) #pomocu // dobijamo cjelobrojni ostatak djeljenja za redove i stupce slike
# te axis=1,3 su dimnezije jer smo ih stvorili s reshape funkcijom, 10 je faktor
plt.figure()
plt.imshow(smanjena, cmap="gray")
plt.title("smanjena slika")

plt.show()