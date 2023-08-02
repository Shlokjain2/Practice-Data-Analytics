import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sk
from sklearn.cluster import KMeans
mydata={'Country':['USA','Canada','France','UK','Germany','Australia'],
        'Latitude':[44.97,62.40,46.75,54.01,51.15,-25.45],
        'Longitude':[-103.77,-96.80,2.40,-2.53,10.40,133.11],
        'language':['English','English','French','English','German','English']}
df=pd.DataFrame(mydata)
df.to_csv('country.csv')

plt.scatter(df['Latitude'],df['Longitude'])
plt.xlim(-180,180)
plt.show()

x=df.iloc[:,1:3]
print(x)
kmeans=KMeans(3)
kmeans.fit(x)
clu=kmeans.fit_predict(x)

a=x[clu == 0]
b=x[clu == 1]
c=x[clu == 2]
u= pd.unique(clu)
plt.scatter(a['Latitude'] , a['Longitude'] , color = 'red')
plt.scatter(b['Latitude'] , b['Longitude'] , color = 'black')
plt.scatter(c['Latitude'] , c['Longitude'] , color = 'green')

plt.show()
