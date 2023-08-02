import matplotlib.pyplot as plt
def myplot(x):
  y3=[2*t+4 for t in x]
  y4=[4*(t**2)+5*t+4 for t in x]
  plt.plot(x,y3,'k+--',markersize=10.5,linewidth=2.5,label="2x+4")
  plt.plot(x,y4,'c>--',markersize=10.5,linewidth=2.5,label="4x^2+5x+4")
  plt.title("graph")
  plt.xlabel("x-cor")
  plt.ylabel("y-cor")
  plt.legend()
  plt.show()

def main():
  n=int(input("enter num"))
  x=[]
  for i in range(n):
    x.append(float(input()))
  myplot(x)
main()
