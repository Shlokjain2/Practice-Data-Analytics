def word(s1,s2):
  
  r=s1[0]
  r=r+s2[0]
  l1=len(s1)
  mi=int(l1/2)
  r=r+s1[mi]
  l2=len(s2)
  mi=int(l2/2)
  r=r+s2[mi]
  r=r+s1[l1-1]
  r=r+s2[l2-1]
  return r

def main():
  s1=input("enter string 1 ")
  s2=input("enter string 2 ") 
  print("new string ",word(s1,s2))

main()