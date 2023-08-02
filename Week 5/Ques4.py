import sqlite3 as sq
con=sq.connect("DataAnalytics.db")
cur=con.cursor()
a=input("enter doctor id")
b=input("enter experience")
z='update doctor set exp='+b+' where did='+a
cur.execute(z)
con.close()
