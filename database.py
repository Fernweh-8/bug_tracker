import os
import sqlite3
from issue_list import IssueList

db_filename = 'issues.db'

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print('Creating schema')
        cur = conn.cursor()
        issues = IssueList().issues
        cur.execute('''CREATE TABLE issue
                       (id INT PRIMARY KEY NOT NULL, 
                       title TEXT, 
                       description TEXT, 
                       status TEXT, 
                       flagged INT, 
                       user TEXT, 
                       created TEXT)''')
        cur.executemany("INSERT INTO issue VALUES (?, ?, ?, ?, ?, ?, ? )", issues)
        conn.commit()
        cur.execute("SELECT * FROM issue")
        print(cur.fetchall())
    else:
        print("Database already exists.")
conn.close()
