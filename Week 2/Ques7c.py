#import string,random
def word(str):
  a=0
  d=0
  s=0
  for i in range(len(str)):
    if(str[i].isalpha()):
        a = a + 1
    elif(str[i].isdigit()):
        d = d + 1
    else:
        s = s + 1

  print("Number of Alphabets ", a)
  print("Number of Digits in this String ", d)
  print("Number of Special ", s)

def main():
  str=input("enter string ")
  word(str)

main()