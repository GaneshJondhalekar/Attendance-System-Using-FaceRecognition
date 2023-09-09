import psycopg2

dbname='ztpeoaeg'
dbuser='ztpeoaeg'
dbserver='rajje.db.elephantsql.com'
dbport='5432'
dbpass='6CJMqjVNVzdHoOwADIE0MgaBVutwQTLl'

conn=psycopg2.connect(database=dbname,user=dbuser,password=dbpass,host=dbserver,port=dbport)

cursor = conn.cursor()

create_table_query = '''CREATE TABLE registratio
          (ID INT PRIMARY KEY NOT NULL,
           DEPT VARCHAR(6) NOT NULL,
           NAME VARCHAR(30) NOT NULL,
           EMAIL VARCHAR(20) NOT NULL,
           PHONE DOUBLE NOT NULL,
          ); '''

cursor.execute(create_table_query)
