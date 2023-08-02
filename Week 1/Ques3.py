import random
def lottery():
  lottery_num=[]
  for i in range(100):
    lottery_num.append(random.randrange(10000000,99999999))
  win = random.sample(lottery_num,3)
  print(win)
  print(lottery_num)
lottery()

