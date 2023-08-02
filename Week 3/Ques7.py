import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9,10,11,12]
l=["faceCreamSalesData","faceWashSalesData","toothPasteSalesData", "bathingsoapSalesData","shampooSalesData","moisturizerSalesData"]
m=["January", "February", "March", "April", "May", "June","July", "August","September","October","November","December"]
plt.xticks(x,m,rotation='vertical')
plt.title("graph")
plt.xlabel("x-cor")
plt.ylabel("y-cor(in k)")

y=[]
j=0
print("enter sales for ",l[j])
for i in range(12):
  y.append(float(input()))
plt.plot(x,y,'r+:',markersize=1.5,linewidth=0.5,label=l[j])
plt.legend(loc=2)

y=[]
j=j+1
print("enter sales for ",l[j])
for i in range(12):
  y.append(float(input()))
plt.plot(x,y,'c+:',markersize=1.5,linewidth=0.5,label=l[j])
plt.legend(loc=2)

y=[]
j=j+1
print("enter sales for ",l[j])
for i in range(12):
  y.append(float(input()))
plt.plot(x,y,'k*--',markersize=1.5,linewidth=0.5,label=l[j])
plt.legend(loc=2)

y=[]
j=j+1
print("enter sales for ",l[j])
for i in range(12):
  y.append(float(input()))
plt.plot(x,y,'g*--',markersize=1.5,linewidth=0.5,label=l[j])
plt.legend(loc=2)

y=[]
j=j+1
print("enter sales for ",l[j])
for i in range(12):
  y.append(float(input()))
plt.plot(x,y,'yo-.',markersize=1.5,linewidth=0.5,label=l[j])
plt.legend(loc=2)

y=[]
j=j+1
print("enter sales for ",l[j])
for i in range(12):
  y.append(float(input()))
plt.plot(x,y,'mo-.',markersize=1.5,linewidth=0.5,label=l[j])
plt.legend(loc=2)

plt.show()