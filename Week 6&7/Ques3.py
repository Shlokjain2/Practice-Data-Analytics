import shutil

n=input("Enter paragraph")
f=open('r1.txt','w')
f.write(n)
f.close()

f=open('r1.txt','r')
print("paragraph:")
a=f.read()
print(a)

shutil.copyfile('r1.txt','r2.txt')
f=open('r2.txt','r')
print("copy paragraph:")
a=f.read()
print(a)
