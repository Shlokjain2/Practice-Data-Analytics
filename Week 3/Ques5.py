import matplotlib.pyplot as plt
x=[4,5,5,7,6,8,8,9,4,4,4,4,5,5,7,7,8,8,8]
plt.title("Plotting Histogram")
plt.ylabel("Frequency")
plt.xlim(min(x)-4,max(x)+4)
plt.hist(x,edgecolor="black",bins=5)
fig=plt.figure()
plt.show()
fig.savefig("hist.jpg")

