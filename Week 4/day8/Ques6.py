import sqlite3 as sq
con=sq.connect("DataAnalytics.db")
cur=con.cursor()
s=input("enter emp id")
data=cur.execute('SELECT count() FROM emp where empid like '+s)
l=[]
for column in data:
 l.append((column[0]))
if(l[0]==1):
  cur.execute('update emp set salary=salary+(0.05*salary)')
else:
  print("id not found")
con.commit();
con.close();
