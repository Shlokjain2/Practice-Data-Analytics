import sqlite3 as sq
con=sq.connect("DataAnalytics.db")
cur=con.cursor()
cur.execute('select avg(salary) from emp group by deptid')
print(cur.fetchall())
cur.execute('select count(empid) from emp group by deptid')
print(cur.fetchall())
cur.execute('drop table dept')
cur.execute('create table dept(Deptid int primary key \
check(typeof(Deptid)="integer"),\
noe int not null check(typeof(noe)="integer"),\
asal real not null check(typeof(asal)="real" and asal>12000))')
print("table created")
data=cur.execute('''SELECT deptid,count(deptid),avg(salary) FROM emp group by deptid''')
l=[]
for column in data:
 if(column[2]>12000):
    l.append((column[0],column[1],(int)(column[2])))
cur.executemany('insert into dept values(?,?,?)',l)
con.commit()
cur.execute('select * from dept')
print(cur.fetchall())

con.close();




