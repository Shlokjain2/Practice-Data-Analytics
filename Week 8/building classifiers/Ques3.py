import pandas as pd
import matplotlib.pyplot as plt
import sklearn 
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score , precision_score , recall_score
from sklearn.tree import export_text
from sklearn.naive_bayes import CategoricalNB

df=pd.read_csv('/content/train.csv')
#a
print(df.columns)
print(df.iloc[:,-1].name)
#c
df.dropna(inplace=True)
#b
numdf=df.select_dtypes(include=['int', 'float']);
#numdf=pd.concat([numdf, df['satisfaction']], axis=1)
#d
x=numdf.iloc[:,:-1]
y=df['satisfaction']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20)
dmod=DecisionTreeClassifier()
dmod.fit(x_train,y_train)
dpre=dmod.predict(x_test)
print(dpre)
#e
print('Accuracy:',accuracy_score(dpre,y_test))
#f
print('Precision:',precision_score(dpre,y_test,pos_label='satisfied'))
print('Sensitivity:',recall_score(dpre,y_test,pos_label='satisfied'))
#g
clf=tree.DecisionTreeClassifier(max_depth=2)
clf=clf.fit(x,y)
fig=plt.figure()
tree.plot_tree(clf)
r=export_text(clf)
print(r)
#h
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['Class_code'] = le.fit_transform(df['Class'])
print(df)
#i
nb=CategoricalNB()
nb.fit(x_train, y_train)
nbpre=nb.predict(x_test)

#j
print('Decision Tree Accuracy:',accuracy_score(y_test,dpre))
print('Naive Bayes Accuracy:',accuracy_score(y_test,nbpre))