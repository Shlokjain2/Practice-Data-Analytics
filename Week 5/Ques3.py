import sqlite3 as sq
con=sq.connect("DataAnalytics.db")
cur=con.cursor()
a=input("enter salary")
b=input("enter specialty")
l=["Doctor id","Doctor Name","Hospital Id","Joining Date","Speciality","Salary","Experience"]
z='select * from doctor where spe like "'+b+'" and salary>'+a
data=cur.execute(z)
for column in data:
  for i in range(7):
   print(l[i],":",column[i])
con.close()
