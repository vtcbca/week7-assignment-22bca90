import sqlite3
conn=sqlite3.connect('student.db')
c=conn.cursor()
c.execute('''create table student_mast
           (id int,name varchar,address varchar)''')
c.execute('''insert into student_mast values
            (1,'om','surat'),(2,'sai','bardoli'),(3,'ram','dastan')''')
c.execute('''select*from student_mast''')
result=c.fetchall()
print(result)
conn.commit()
conn.close()

