#import string,random
def word(str):
  
  c=0
  v=0
  for i in str:
    c=c+1
    if i in ('a','e','i','o','u'):  
        v = v + 1;
    
  print("no. of vowel",v)
  print("length",c)
  
def main():
  str=input("enter string ")
  word(str)

main()