import string,random
def generatepass(n):
  pasw=''.join(random.sample(string.ascii_letters,n)) 
  #does not repeate characters
  pasw=''.join(random.choice(string.ascii_letters) for i in range(n))
  print(pasw)
generatepass(55)


def generatepass(n):
  basket=string.ascii_letters+string.digits+string.punctuation
  pasw=''.join(random.choice(basket) for i in range(n))
  pasw=''.join(random.choice(string.printable) for i in range(n))
  print(pasw)
generatepass(5)