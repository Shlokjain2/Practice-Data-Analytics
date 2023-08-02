import sqlite3 as sq
con=sq.connect("DataAnalytics.db")
cur=con.cursor()
cur.execute('update emp set salary=salary+(0.05*salary)')
cur.execute('select empid,salary from emp x where 5>(select count(distinct salary) from emp y where y.salary>x.salary) order by salary desc')
print(cur.fetchall())
con.commit()
con.close();