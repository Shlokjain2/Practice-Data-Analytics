
import sqlite3 as sq
con=sq.connect("DataAnalytics.db")
cur=con.cursor()
cur.execute('create table EMP(Empid int primary key \
check(typeof(Empid)="integer"),\
Empname varchar2 NOT NULL check(typeof(Empname)="text"),\
Salary int not null check(typeof(salary)="integer" and salary>5000),\
Commission real check(typeof(Commission)="real"),\
Deptid int not null check(typeof(Deptid)="integer"))')
print("table created")
n=int(input("Number of employees"))
for i in range(n):
  eid=int(input("Enter emp id"))
  en=input("Enter name")
  sal=int(input("Enter salary"))
  com=float(input("Enter commission"))
  did=input("Enter dept id")
  cur.execute("""INSERT INTO emp(empid, empname, salary,commission, deptid)VALUES (?,?,?,?,?)""",(eid, en, sal,com, did))
  con.commit()
cur.execute('select * from Emp')
print(cur.fetchall())
con.close()
#[(1, 'asha', 10000, 200.5, 1), (2, 'ray', 7000, 0.0, 2), (3, 'shan', 5500, 0.0, 3), (4, 'prem', 8080, 120.0, 2), (5, 'harry', 9900, 0.0, 4), (6, 'ron', 7500, 80.9, 3), (7, 'josh', 11000, 250.66, 1), (8, 'mike', 6789, 66.94, 2)]