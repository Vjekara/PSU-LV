import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, precision_score, recall_score, accuracy_score, classification_report
from sklearn.tree import DecisionTreeClassifier, plot_tree





# ucitaj podatke za ucenje
df = pd.read_csv('occupancy_processed.csv')

feature_names = ['S3_Temp', 'S5_CO2']
target_name = 'Room_Occupancy_Count'
class_names = ['Slobodna', 'Zauzeta']

X = df[feature_names].to_numpy()
y = df[target_name].to_numpy()

x_train, x_test, y_train, y_test = train_test_split(X,y, stratify=y)
scaler = StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.fit_transform(x_test)

dt = DecisionTreeClassifier()
dt.fit(x_train ,y_train)
# Predikcija modela
y_pred = dt.predict(x_test)


precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
# Izracunaj tocnost
accuracy = accuracy_score(y_test, y_pred)
print(classification_report(y_test, y_pred))

plt.figure(figsize=(12, 8))
plot_tree(dt, filled=True)
plt.show()


cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Class 0',
'Class 1'])
disp.plot(cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.show()


