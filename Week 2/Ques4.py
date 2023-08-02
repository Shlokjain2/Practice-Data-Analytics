import numpy as np
def auth():
  ar = np.array(["U1", "P1", "U2", "P2", "U3", "P3", "U4", "P4", "U5", "P5"])
  newarr = ar.reshape(5, 2)
  print(newarr)
  flag = 0
  user = input("Enter the username")
  passw = input("Enter the password")
  for (i, j) in newarr:
    if (i == user and j == passw):
      flag = -1
      break
  if flag == -1:
    print("success")
  else:
    print("failure")


auth()
