def sum_no(n):
  if(n<0):
    return 0;
  else:
    return n+sum_no(n-1)
print(sum_no(int(input("Enter the number"))))