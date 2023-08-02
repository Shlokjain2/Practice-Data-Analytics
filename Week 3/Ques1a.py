import matplotlib.pyplot as plt
n=int(input("number"))
x=[]
y=[]
for i in range(n):
  x.append(float(input()))
  y.append(float(input()))
plt.plot(x,y,'r+--',markersize=10.5,linewidth=2.5)
plt.title("multiple points")
plt.xlabel("x-cor")
plt.ylabel("y-cor")
minx=min(x)
maxx=max(x)
miny=min(y)
maxy=max(y)
plt.axis([minx-4,maxx+4,miny-4,maxy+4])
plt.grid()
fig=plt.figure()
plt.show()
fig.savefig("r1.jpg")


Question: differnece between plt.scatter and plt.plot

Answer: Both `plt.scatter()` and `plt.plot()` are functions in the Matplotlib library of Python that can be used to create scatter plots. However, they have different use cases and produce different types of plots.

`plt.scatter(x, y, s=None, c=None, marker=None, cmap=None, alpha=None, linewidths=None, edgecolors=None)`: 
- This function is used to create a scatter plot of x and y data points. 
- The `x` and `y` arguments are arrays or lists of the x and y coordinates of the points, respectively.
- The `s` argument is the size of the markers used for each point, and can be a scalar or an array the same length as `x` and `y`. 
- The `c` argument is the color of the markers, which can be a single color or an array of colors the same length as `x` and `y`. 
- The `marker` argument specifies the shape of the marker used for each point. 
- The `cmap` argument is used to specify the colormap to use for coloring the markers. 
- The `alpha` argument sets the opacity of the markers. 
- The `linewidths` argument sets the width of the marker edges. 
- The `edgecolors` argument sets the color of the marker edges.

Example usage:
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]
colors = ['r', 'g', 'b', 'c', 'm']
sizes = [20, 50, 100, 200, 500]

plt.scatter(x, y, s=sizes, c=colors, marker='o')
plt.show()

`plt.plot(x, y, fmt=None, data=None, **kwargs)`: 
- This function is used to create a line plot of x and y data points. 
- The `x` and `y` arguments are arrays or lists of the x and y coordinates of the points, respectively.
- The `fmt` argument is a shorthand string that specifies the style of the plot, including the color, marker, and line style. 
- The `data` argument specifies the data source for the plot, which can be a dictionary, Pandas DataFrame, or other iterable data structure. 
- The `**kwargs` argument is used to pass additional keyword arguments that control various aspects of the plot, such as the line width and style.

Example usage:
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]

plt.plot(x, y, 'ro--', linewidth=2.0)
plt.show()

In summary, `plt.scatter()` is used to create scatter plots with markers that can have different sizes, colors, shapes, and opacities, while `plt.plot()` is used to create line plots that can have different line styles and colors.
