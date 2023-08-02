# Python3 implementation of the approach
import random,numpy
def fuzzy() :
  n=int(input("Enter number of Data Points"))
  c=int(input("Enter number of clusters"))
  ar = numpy.zeros((n,c))
  for i in range(n):
    s=0.0
    for j in range(c-1):
      ar[i][j] = random.uniform(0, 1-s)  
      s=s+ar[i][j]
    ar[i][c-1]=1-s
  print(ar, end = " ");
 
fuzzy()