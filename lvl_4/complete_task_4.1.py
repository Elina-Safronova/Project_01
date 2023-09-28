import sqlite3
import pandas as pd

con1 = sqlite3.connect("Students.db")
query = "SELECT * FROM Students"
df = pd.read_sql(query, con1)
print(df)

con2 = sqlite3.connect("teachers.db")
df.to_sql("Students", con2, index=False)
df.to_excel('students.xlsx', index=False)


def test(student_id):
    con = sqlite3.connect("teachers.db")
    cur = con.cursor()
    query = "SELECT * FROM School JOIN Students ON School.School_Id = Students.School_Id WHERE Students.Student_Id = ?"
    cur.execute(query, (student_id,))
    result = cur.fetchall()
    con.close()
    print(result)


test(201)
