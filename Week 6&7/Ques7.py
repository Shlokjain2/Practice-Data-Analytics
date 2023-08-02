import pandas as pd
import matplotlib.pyplot as plt
dt = pd.read_csv('heart_failure_clinical_records_dataset.csv')
print(dt)
#b
print(dt.head(1))
#c
print(dt.tail(1))
#d
print(pd.options.display.max_rows)
#e
print(dt['serum_creatinine'].dtypes)
#f
nul = dt.columns[dt.isnull().any()].tolist()
print(nul)
#g
for i in nul:
  dt[i].fillna(dt[i].mean(),inplace=True)
#h
print(dt.shape[0])
#i
print(dt['platelets'].median())
#j
print(dt[dt['creatinine_phosphokinase']>4000])
#k
mean=dt['creatinine_phosphokinase'].min()
std=dt['creatinine_phosphokinase'].std()
sd=[]
for i in dt.index:
  x=dt.loc[i,'creatinine_phosphokinase']
  sd.append(((x-mean)/std))
  print(i," standard score ",(x-mean)/std)
plt.scatter(dt['creatinine_phosphokinase'],sd)
plt.show()
#l
dt.drop_duplicates(inplace=True)
print(dt.tail(1))
#m
print(dt['age'].corr(dt['ejection_fraction']))
