import sqlite3 as sq
con=sq.connect("DataAnalytics.db")
cur=con.cursor()
data=cur.execute('''SELECT salary FROM emp where empname in ('john','black')  ''')
l=[]
for column in data:
 l.append((column[0]))
if(l[0]+2000 < 50000):
  cur.execute('update emp set salary=(salary+2000) where empname="john" ')
if(l[1]+5000 < 50000):
  cur.execute('update emp set salary=(salary+5000) where empname="black" ')
con.commit();
con.close();
