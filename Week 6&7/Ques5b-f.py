import pandas as pd
import sklearn as sk
from sklearn.datasets import load_iris
iris_obj=load_iris()
print('data set')
print(iris_obj.data)
print("features ",iris_obj.feature_names)
print('class level ',iris_obj.target)
print('class level name ',iris_obj.target_names)

iris=pd.DataFrame(iris_obj.data,columns=iris_obj.feature_names\
                  ,index=pd.Index(i for i in range(iris_obj.data.shape[0])))\
                  .join(pd.DataFrame(iris_obj.target,columns=pd.Index(['species']),
                                     index=pd.Index(i for i in range(iris_obj.target.shape[0]))))

print(iris)
iris.species.replace({0:'setosa',1:'versicolor',2:'virginica'},inplace=True)
print(iris)
iris_grps=iris.groupby("species")
for name,data in iris_grps:
  print(data)
  print('sepal length mean: ',data['sepal length (cm)'].mean()," for ",name)
  print('sepal width mean: ',data['sepal width (cm)'].mean()," for ",name)

print('sepal length max: ',iris['sepal length (cm)'].max())
print('sepal width max: ',iris['sepal width (cm)'].max())
print('petal length max: ',iris['petal length (cm)'].max())
print('petal width max: ',iris['petal width (cm)'].max())
print('sepal length std: ',iris['sepal length (cm)'].std())
print('sepal width std: ',iris['sepal width (cm)'].std())
print('petal length std: ',iris['petal length (cm)'].std())
print('petal width std: ',iris['petal width (cm)'].std())
