import sqlite3 as sq
con=sq.connect("DataAnalytics.db")
cur=con.cursor()
a=input("enter hospital id")
b=input("enter doctor id")
print("Hospital Record:")
l=["Hospital Id","Hospital Name","Bed Count"]
data=cur.execute('select * from hospital where hid='+a)
for column in data:
  for i in range(3):
   print(l[i],":",column[i])
print("Doctor Record")   
l=["Doctor id","Doctor Name","Hospital Id","Joining Date","Speciality","Salary","Experience"]
data=cur.execute('select * from doctor where did='+b)
for column in data:
  for i in range(7):
   print(l[i],":",column[i])
con.close()
