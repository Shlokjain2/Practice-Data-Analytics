import Mymodule
def auth():
  user=input("Enter the username")
  passw=input("Enter the password")
  if(Mymodule.Authenticate(user,passw)==True):
    print("Success")
  else:
    print("Failure")

def Area():
  length=int(input("Enter the Length of Rectangle"))
  breadth=int(input("Enter the Breadth of Rectangle"))
  print("Area = ",Mymodule.Rect_Area(length,breadth))
def main():
  auth()
  Area()
  Mymodule.Multi(int(input("Enter a number")))
main()