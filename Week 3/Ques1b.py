import matplotlib.pyplot as plt

n = int(input("number"))
x = []
y1 = []
y2 = []
for i in range(n):
  x.append(float(input()))
y1 = [t**2 for t in x]
y2 = [t**3 for t in x]
plt.plot(x, y1, 'r+--', markersize=10.5, linewidth=2.5, label="y=x^2")
plt.plot(x, y2, 'ko--', markersize=5, linewidth=2, label="y=x^3")
plt.title("graph")
plt.xlabel("x-cor")
plt.ylabel("y-cor")
plt.legend()
minx = min(x)
maxx = max(x)
miny = min(y1)
maxy = max(y2)
plt.axis([minx - 4, maxx + 4, miny - 4, maxy + 4])
plt.grid()
fig = plt.figure()
plt.show()
fig.savefig("r1.jpg")
