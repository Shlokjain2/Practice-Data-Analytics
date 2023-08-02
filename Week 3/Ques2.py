import matplotlib.pyplot as plt
n=int(input("number"))
x=[]
for i in range(n):
  x.append(float(input()))
y1=[t**1 for t in x]
y2=[t**2 for t in x]
y3=[t**3 for t in x]
y4=[t**4 for t in x]
y5=[t**5 for t in x]
y6=[t**6 for t in x]

plt.subplot(2,3,1)
plt.plot(x,y1,'m*--',label="x1")
plt.xlabel("x-cor")
plt.ylabel("y-cor")
plt.legend()
plt.subplot(2,3,2)
plt.plot(x,y2,'m*--',label="x2")
plt.xlabel("x-cor")
plt.ylabel("y-cor")
plt.legend()
plt.subplot(2,3,3)
plt.plot(x,y3,'m*--',label="x3")
plt.xlabel("x-cor")
plt.ylabel("y-cor")
plt.legend()
plt.subplot(2,3,4)
plt.plot(x,y4,'m*--',label="x4")
plt.xlabel("x-cor")
plt.ylabel("y-cor")
plt.legend()
plt.subplot(2,3,5)
plt.plot(x,y5,'m*--',label="x5")
plt.xlabel("x-cor")
plt.ylabel("y-cor")
plt.legend()
plt.subplot(2,3,6)
plt.plot(x,y6,'m*--',label="x6")
plt.xlabel("x-cor")
plt.ylabel("y-cor")
plt.legend()
plt.tight_layout()
plt.show()