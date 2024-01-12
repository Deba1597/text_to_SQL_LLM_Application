import sqlite3


# connect to sqlite3
connection = sqlite3.connect('student.db')
#create a cursur object to insert record , create table

cursor = connection.cursor()

# Create table
table_info="""
CREATE TABLE student(
    name VARCHAR(25),
    class VARCHAR(25),
    section VARCHAR(25)
)
"""
cursor.execute(table_info)

# Insert record
cursor.execute("""INSERT INTO student VALUES('deba','Data Science','a');""")
cursor.execute("""INSERT INTO student VALUES('riku','mlops','b');""")
cursor.execute("""INSERT INTO student VALUES('krish','Data Science','a');""")
cursor.execute("""INSERT INTO student VALUES('sunnny','devops','b');""")
cursor.execute("""INSERT INTO student VALUES('sudhansu','Data Science','a');""")

#dislpay all record
print('The records are :')
data = cursor.execute("""SELECT * FROM student;""")
for row in data:
    print(row)

connection.commit()
connection.close()