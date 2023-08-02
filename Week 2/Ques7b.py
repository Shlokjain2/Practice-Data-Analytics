#import string,random
def word():
  mylist = []
  num = int(input("Enter a number"))
  for i in range(num):
    mylist.append(input())
  for j in range(num):
    str = mylist[j]
    c = 0
    v = 0
    for i in str:
      c = c + 1
      if i in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        v = v + 1

    print("no. of vowel", v)
    print("length", c)


word()