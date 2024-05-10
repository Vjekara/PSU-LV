import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from sklearn.metrics import accuracy_score 



# MNIST podatkovni skup
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# TODO: prikazi nekoliko slika iz train skupa

# pick a sample to plot
sample = 1
image = x_train[sample]

# plot the sample
fig = plt.figure
plt.imshow(image, cmap='gray')
plt.show()

sample2 = 4
image2 = x_train[sample2]


# plot the sample
fig2 = plt.figure
plt.imshow(image2, cmap='gray')
plt.show()

sample3 = 3
image3 = x_train[sample3]

# plot the sample
fig = plt.figure
plt.imshow(image3, cmap='gray')
plt.show()


# Skaliranje vrijednosti piksela na raspon [0,1]
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

# Slike 28x28 piksela se predstavljaju vektorom od 784 elementa
x_train_s = x_train_s.reshape(60000, 784)
x_test_s = x_test_s.reshape(10000, 784)

# Kodiraj labele (0, 1, ... 9) one hot encoding-om
y_train_s = keras.utils.to_categorical(y_train, 10)
y_test_s = keras.utils.to_categorical(y_test, 10)


# TODO: kreiraj mrezu pomocu keras.Sequential(); prikazi njenu strukturu pomocu .summary()

mreza = keras.Sequential()
mreza.add(Dense(units=100, activation='relu'))
mreza.add(Dense(units=50, activation='relu'))
mreza.add(Dense(units=10, activation='softmax'))





# TODO: definiraj karakteristike procesa ucenja pomocu .compile()

mreza.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])


# TODO: provedi treniranje mreze pomocu .fit()

mreza.fit(x_train_s, y_train_s, epochs= 1, batch_size=25)
mreza.summary()
# TODO: Izracunajte tocnost mreze na skupu podataka za ucenje i skupu podataka za testiranje
y_pred=mreza.predict(x_test_s)
trainL, trainA=mreza.evaluate(x_test_s,y_test_s)
testL, testA=mreza.evaluate(x_train_s,y_train_s)
print('Tocnost na skupu podataka za ucenje:', trainA)
print('Tocnost na skupu podataka za testiranje:', testA)

# TODO: Prikazite matricu zabune na skupu podataka za testiranje

y_pred = mreza.predict(x_test_s)
y_pred_classes = np.argmax(y_pred, axis=1)
conf_matrix = confusion_matrix(y_test, y_pred_classes)
print('Matrica zabune:')
print(conf_matrix)

# TODO: Prikazi nekoliko primjera iz testnog skupa podataka koje je izgrađena mreza pogresno klasificirala
misclassified_idx = np.where(y_pred_classes != y_test)[0]
plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.imshow(x_test[misclassified_idx[i]], cmap="gray")
    plt.title(f"Predicted: {y_pred_classes[misclassified_idx[i]]}, True: {y_test[misclassified_idx[i]]}")
    plt.axis("off")
plt.show()

