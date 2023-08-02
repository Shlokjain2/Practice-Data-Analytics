import string,random
def generatepass(n):
  pasw=''.join(random.sample(string.ascii_letters,n)) 
  #does not repeate characters
  pasw=''.join(random.choice(string.ascii_letters,n)) for i in range(n))
  print(pasw)
generatepass(55)


