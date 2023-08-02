import sqlite3 as sq
con=sq.connect("DataAnalytics.db")
cur=con.cursor()
cur.execute('create table hospital(hid int primary key \
check(typeof(hid)="integer"),\
hname varchar2 NOT NULL check(typeof(hname)="text"),\
bcnt int not null check(typeof(bcnt)="integer"))')
print("h table created")
cur.execute('create table doctor(did int primary key \
check(typeof(did)="integer"),\
dname varchar2 NOT NULL check(typeof(dname)="text"),\
hid int references hospital(hid),\
jdt varchar2 not null check(typeof(jdt)="text"),\
spe varchar2 NOT NULL check(typeof(spe)="text"),\
Salary int not null check(typeof(salary)="integer"),\
exp int not null check(typeof(exp)="integer"))')
print("d table created")
list=[[1,"Mayo Clinic",200],[2,"Cleveland Clinic",400],[3,"John Hopkins",1000],[4,"UCLA Medical Center",1500]]
cur.executemany('insert into hospital values(?,?,?)',list)
list=[[101,"David",1,"2005-02-10","Paediatric",40000,0],[102,"Michael",1,"2018-07-23","Oncologist",20000,0],[103,"Susan",2,"2016-05-19","Gynaecologist",25000,0],[104,"Robert",2,"2017-12-28","Paediatric",28000,0],[105,"Linda",3,"2004-06-04","Gynaecologist",42000,0],[106,"William",3,"2012-09-11","Dermatologist",30000,0],[107,"Richard",4,"2014-08-21","Gynaecologist",32000,0],[108,"Karen",4,"2011-10-17","Radiologist",30000,0]]
cur.executemany('insert into doctor values(?,?,?,?,?,?,?)',list)
con.commit()
print("Hospital")
cur.execute('select * from hospital')
print(cur.fetchall())
print("Doctor")
cur.execute('select * from doctor')
print(cur.fetchall())
con.close()