import os
import sqlite3
from issue_list import IssueList

db_filename = 'issues.db'

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print('Creating schema')
        cur = conn.cursor()
        new_list = IssueList()
        new_list.add_new(title="new issue", user="Anna", status=0)
        new_list.add_new(title="issue", user="AnnaD", status=0)
        new_list.add_new(title="new", user="AnnaS", status=1)
        new_list.add_new(title="lala", user="AnnaG", status=1)
        new_list.add_new(title="new lala", user="AnnaK", status=1)
        new_list.add_new(title="lala new", user="Anna", status=2)
        new_list.add_new(title="haha", user="AnnaS", status=3)
        new_list.add_new(title="what", user="AnnaD", status=3)

        cur.execute('''CREATE TABLE issue
                       (id INTEGER PRIMARY KEY NOT NULL, 
                       title TEXT, 
                       description TEXT, 
                       status TEXT, 
                       flagged INTEGER, 
                       user TEXT, 
                       created TEXT)''')
        cur.executemany("INSERT INTO issue VALUES (?, ?, ?, ?, ?, ?, ? )", new_list.issues)
        conn.commit()
        cur.execute("SELECT * FROM issue")
        print(cur.fetchall())
    else:
        print("Database already exists.")
conn.close()
