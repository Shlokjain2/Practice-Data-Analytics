def Authenticate(a, b):
  usr = ["User1", "User2", "User3", "User4", "User5"]
  pwd = ["Pass1", "Pass2", "Pass3", "Pass4", "Pass5"]
  flag = 0
  for (i,j) in zip(usr,pwd):
    if (i == a and j==b):
      flag = -1
      break
  if flag == -1:
    return True
  else:
    return False
def Rect_Area(l,b):
  return l*b;
def Multi(x):
  for i in range(1,11):
    print(x,"X",i,"=",(x*i))