import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9,10,11,12]
m=["January", "February", "March", "April", "May", "June","July", "August","September","October","November","December"]
plt.xticks(x,m,rotation='vertical')
plt.title("graph")
plt.xlabel("x-cor")
plt.ylabel("y-cor(in k)")
y=[]
for i in range(12):
  y.append(float(input()))
plt.bar(x,y)
plt.show()