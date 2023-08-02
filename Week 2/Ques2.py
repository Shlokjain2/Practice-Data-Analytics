import string,random
def generatepass():
  basket=string.ascii_letters + string.digits + string.punctuation
  basket2=''.join(random.choice(string.ascii_uppercase) for i in range(2))
  basket2+=random.choice(string.digits)
  basket2+=random.choice(string.punctuation)
  for i in range(6):
    basket2 +=(random.choice(basket))
  passwordlist= list(basket2)
  random.shuffle(passwordlist)
  basket=''.join(passwordlist)
  print(basket)
  if '@' not in passwordlist:
    passwordlist[2]='@'
  basket=''.join(passwordlist)
  print(basket)
generatepass()
