import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

dt = pd.read_csv('water_potability.csv')
#a
print(dt)
#b
print(dt.columns)
print(dt.iloc[:, -1].name)
#c
print(dt.shape[0])
#d
print(dt.dtypes)
#e
plt.plot(dt['Hardness'])
plt.show()
#f
print(dt['Sulfate'].mean())
#g
nul = dt.columns[dt.isnull().any()].tolist()
for i in nul:
  dt[i].fillna(dt[i].mean(), inplace=True)
#h
print(dt.loc[(dt['ph'] < 4) & (dt['Chloramines'] == 5)])
#i
dt['ph'].mask(dt['ph'] < 4, other=dt['ph'].mean(), inplace=True)
#j
dt['Potability'].replace({1: 'Drinkable', 0: 'Non-drinkable'}, inplace=True)
#k
data = dt
x = data.iloc[:, :-1]
y = data['Potability']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15)
#0.15 as 15% of test set is required
#l
smod = SVC()
kmod = KNeighborsClassifier(n_neighbors=5)
smod.fit(x_train, y_train)
kmod.fit(x_train, y_train)
#m
spre = smod.predict(x_test)
kpre = kmod.predict(x_test)
print(accuracy_score(spre, y_test))
print(accuracy_score(kpre, y_test))
print(classification_report(spre, y_test, zero_division=0))
print(classification_report(kpre, y_test, zero_division=0))
