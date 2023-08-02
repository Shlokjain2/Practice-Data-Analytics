import random 
n=int(input("Enter n"))
f=open('ab','w')
for i in range(1,n):
  z=random.randint(60,90)
  f.write(str(z)+',')
z=random.randint(60,90)
f.write(str(z))
f.close()

f=open('ab','r')
a=f.read().split(',')
print("file content")
for i in range(len(a)):
  print(a[i])
print("maximum: ",max(a))
print("minimum: ",min(a))
f.close()