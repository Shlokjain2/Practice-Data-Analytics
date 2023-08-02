import sqlite3 as sq
con=sq.connect("DataAnalytics.db")
cur=con.cursor()
z='select * from hospital where hid in(select hid from doctor group by hid having count(hid)>=50)'
cur.execute(z)
print(cur.fetchall())
con.close()
