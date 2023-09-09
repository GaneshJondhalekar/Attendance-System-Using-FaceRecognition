import psycopg2

dbname='ztpeoaeg'
dbuser='ztpeoaeg'
dbserver='rajje.db.elephantsql.com'
dbport='5432'
dbpass='6CJMqjVNVzdHoOwADIE0MgaBVutwQTLl'

conn=psycopg2.connect(database=dbname,user=dbuser,password=dbpass,host=dbserver,port=dbport)

cursor = conn.cursor()

    
value1=1
value2='CSE' 
value3='mailk'
value4='mike@gmail.com'
value5='kar'




sql = """INSERT INTO registration(ID,DEPT,NAME,EMAIL,PHONE)
             VALUES(%s,%s,%s,%s,%s)"""

cursor.execute(sql, (value1,value2,value3,value4,value5))
conn.commit()
conn.close()
print("Table created successfully in PostgreSQL ")


