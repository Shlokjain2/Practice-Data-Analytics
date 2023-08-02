import matplotlib.pyplot as plt
n=int(input('enter population'))
year_list =[2019,2020,2021]
per_list=[20,60,80]
aff_list=[]
for i in per_list:
  aff_list.append((i/100)*n)
print(aff_list)
plt.pie(per_list, labels = year_list,autopct='%.2f')
plt.legend(title = "Covid-19 cases:")
plt.show()