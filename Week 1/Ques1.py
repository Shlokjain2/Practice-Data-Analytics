#print("bye")
def prime(n):
 
  for j in range(1,n+1):
    c=0;
    for i in range(1,j+1):
      if j%i == 0:
        c=c+1
    if c==2:
      print (j)

def Armstrong(n):
  for i in range(100,n):
    x=i
    s=0
    while x>0:
      d=x%10
      s=s+ d**3
      x=x//10
    if s==i:
      print(i)

def pattern(n):
  for i in range(1,n+1):
    for j in range(0,i):
      print("*",end=" ")
    print()
  for i in range(n-1,0,-1):
    for j in range(0,i):
      print("*",end=" ")  
    print()

def main():
  print('Enter the Range for armstrong')
  num1=int(input());
  print('Enter the Range for prime')
  num3=int(input());
  print('Enter the Number')
  num2=int(input());
  print("armstrong")
  Armstrong(num1)
  print("prime")
  prime(num3)
  print("pattern")
  pattern(num2)

main()

