import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn as sk
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

np.random.seed(42)
#np.random.seed(42) sets the seed value for the NumPy random number generator to 42.When you generate random numbers using NumPy, the numbers are not truly random but rather pseudorandom. This means that the numbers appear to be random, but they are generated using a deterministic algorithm.By setting the seed value to a specific number, you can ensure that the same sequence of random numbers is generated every time you run the code. This is useful for debugging and testing purposes, as it allows you to reproduce the same results consistently.In the code I provided earlier, setting the seed value to 42 ensures that the same sequence of random values is generated every time the code is run, which makes it easier to debug and compare the results

mapping_values= np.random.normal(loc=45,scale=1.2,size=2000000)
df=pd.DataFrame({'Position':range(0,2000000),'Mapping Values': mapping_values})
print(mapping_values)
print(df.head(1000))

plt.plot(df['Position'],df['Mapping Values'])
plt.xlabel('Position')
plt.ylabel('Mapping Values')
plt.show()

p=np.random.randint(2000000)
l=np.random.randint(1000,5000)
#print(p)
#all positions from p to p+l
mask=(df['Position']>=p) & (df['Position']<=p+l)
new_mapping_values=np.random.normal(loc=4000,scale=0.5,size=mask.sum())
#using mask() to replace the values
df['Mapping Values'].mask(mask,other=new_mapping_values,inplace=True)
#instead of mask() we can also use loc from p : to p+l
#df.loc[p:p+l,'Mapping Values']=np.random.normal(4000,0.5,l+1)
print(df.head(1000))

pos=np.random.choice(df.loc[mask,'Position'],size=3,replace=False)
df['Mapping Values'].mask(df['Position'].isin(pos),inplace=True)
print(df.head(1000))

print(df.loc[df['Mapping Values']>4000])# ,'Position'])

#to find nan values
#mask=df['Mapping Values'].isna()
#print(df.loc[mask,'Position'])

df['Mapping Values'].mask(df.isna(),other=999,inplace=True)

mask=df['Mapping Values']<12
print('count=',mask.sum())

df['Class Level']=np.where(df['Mapping Values']>3000,'Abnormal','Normal')

df['Mapping Values'].mask(df['Mapping Values']==999,inplace=True)


#dtc cannot take null value
df.dropna(inplace=True)
pd.DataFrame(df).to_csv('myfile.csv', header=True, index=False)
data = pd.read_csv('myfile.csv')

x=data.iloc[:,:-1]
y=data['Class Level']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20)

smod=SVC()
kmod=KNeighborsClassifier(n_neighbors=5)
dmod=DecisionTreeClassifier()
dmod.fit(x_train,y_train)
smod.fit(x_train,y_train)
kmod.fit(x_train,y_train)
spre=smod.predict(x_test)
kpre=kmod.predict(x_test)
dpre=dmod.predict(x_test)
print(accuracy_score(spre,y_test))
print(accuracy_score(kpre,y_test))
print(accuracy_score(dpre,y_test))
print(sk.metrics.confusion_matrix(spre,y_test))
print(sk.metrics.confusion_matrix(kpre,y_test))
print(sk.metrics.confusion_matrix(dpre,y_test))
