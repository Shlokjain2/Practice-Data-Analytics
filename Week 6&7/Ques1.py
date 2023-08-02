import pandas as pd
dic = {'Coordinate':['C1','C2','C3','C4','C5'], 'Count':[300,210,230,260,270], 'Mismatch':[5,13,14,3,2]}
pd.DataFrame(dic).to_csv('myfile.csv', header=True, index=False)
dataset = pd.read_csv('myfile.csv')
print(dataset)
mean=dataset['Count'].min()
std=dataset['Count'].std()
print('mean = ',mean)
print('stddev = ',std)
for i in dataset.index:
  x=dataset.loc[i,'Count']
  print('Coordinate',dataset.loc[i,'Coordinate'])
  print("standard score ",((x-mean)/std))  