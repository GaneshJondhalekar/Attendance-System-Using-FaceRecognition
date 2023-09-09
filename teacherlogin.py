import psycopg2
dbname = 'ganesh'
dbuser = 'postgres'
dbserver = 'localhost'
dbport = '5432'
dbpass = '1234'

conn=psycopg2.connect(user=dbuser,password=dbpass,host=dbserver,database=dbname)
cursor=conn.cursor()
e=[1,2,3]
t='''create table attendence(id INT PRIMARY KEY,ATTENDENCE Boolean);'''
#cursor.execute(t)
#q='''ALTER TABLE StudentEncoding ALTER COLUMN encoding TYPE float USING encoding::double precision;'''
#ursor.execute(q)
e="""TRUNCATE TABLE attendence;"""
cursor.execute(e)
#cursor.execute(query,(1,e))
print("done")
conn.commit()
cursor.close()
conn.close()
