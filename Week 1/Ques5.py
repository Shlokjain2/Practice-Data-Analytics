import random
Test_list=[]
for i in range(5):
  Test_list.append(random.randrange(10,99))
New_list = Test_list.copy()
New_list.reverse()
print("Original List: ", Test_list)  # Output: [1,2,3,4,5]
print("Reversed List: ", New_list)  # Output: [5,4,3,2,1]

