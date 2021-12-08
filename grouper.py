from collections import defaultdict
from issue_list import IssueList
import pprint

new_list = IssueList()
new_list.add_new(title = "new issue", user = "Anna", status = 0)
new_list.add_new(title = "issue", user = "AnnaD", status = 0)
new_list.add_new(title = "new", user = "AnnaS", status = 1)
new_list.add_new(title = "lala", user = "AnnaG", status = 1)
new_list.add_new(title = "new lala", user = "AnnaK", status = 1)
new_list.add_new(title = "lala new", user = "Anna", status = 2)
new_list.add_new(title = "haha", user = "AnnaS", status = 3)
new_list.add_new(title = "what", user = "AnnaD", status = 3)

def group_issues(_property):
    issues_grouped = defaultdict(list)
    for issue in new_list.issues:
        issues_grouped[getattr(issue, _property)].append(issue)
    return issues_grouped

# def group_issues(fn):
#     issues_grouped = defaultdict(list)
#     for issue in new_list.issues:
#         issues_grouped[fn(issue)].append(issue)
#     return issues_grouped

def display_grouped(groups):
    for key in groups:
        print(f'Group: {key}')
        for issue in groups[key]:
            print(issue)
        print()

# display_grouped(group_issues('status'))
# fn = lambda issue: issue.user.endswith('S')
# fn = lambda issue: issue.status
# fn = lambda issue: issue.status in [1, 2]

# display_grouped(group_issues(fn))

# print(group_issues(fn)[True])

def make_jira_table(groups):
    make_border = lambda rows: '=' * len(max(rows, key = lambda e: len(e)))
    rows = []
    fmt_row = lambda columns: "\n".join(columns)
    for column in groups:
        rows.append(fmt_row(map(lambda obj: obj.title, groups[column])))
    print(make_border(rows))
    print(rows)
    print(make_border(rows))

make_jira_table(group_issues('status'))

# 1)
# dokonczyc rysowanie tabelki
# ma wyjsc cos takiego, numerki w naglowku to klucze/grupy
# |================================|
# |0        |1       |2       |3   |
# |================================|
# |new issue|new     |lala new|haha|
# |issue    |lala    |        |what|
# |         |new lala|        |    |
# |=================================

# potem zmienimy printowanie do konsoli na wyswietlenie tabelki HTMLowej

# 2)
# edycja issuesow
# napisz funkcje analogiczna do delete i filter
# ktora przyjmuje nazwe property i nowa wartosc (i nadpisuje nia stara)
# jesli property nie istnieje to pomin (nic nie rob)

# 3)
# masz zaprojektowac SQLa, ktory przechowa dane w tabeli
# zastanow sie co bedzie kluczem obcym i jakie relacje beda
# ile bedzie tabel, i ktore dane ida do jakiej tabeli

# zamodeluj zeby uwzglednic nastepujace elementy:
# = issue
# = user
# = board
# = project
#* = comment (do issue)

# 4)
# uzyc modulu sqlite3
# conn = sqlite3.connect('issues.db')
# cur = conn.cursor()
# DB_DEFINITION = '''
# CREATE TABLE IF NOT EXISTS ... (...)
# ...
#'''
# cur.execute(DB_DEFINITION)
# insert_stmts = [...]
# for insert_stmt in insert_stmts:
#     cur.execute(insert_stmt)

# pamietaj zeby zbindowac parametry podczas dodawania rekordow do bazy
# https://docs.python.org/3/library/sqlite3.html
# search for "use the DB-API’s parameter substitution" section with examples

# na poczatek uzyj listy tupli do wypelnienia kazdej tabeli danymi
# jesli chcesz to umiesc dane najpierw w pliku csv / json
# i wczytaj go
# podczas wczytywania poszczegolnych wierszy z pliku wykonaj odpowiednie
# zapytania

# 5)
# przechodzimy na operacje bazodanowe
# musimy stworzyc klase ktora ukryje nam wszystkie zapytania do podstawowych
# operacji tzw. CRUD (create read update delete)
# czyli w jezyku sqlowym: INSERT, SELECT, UPDATE, DELETE
# class DatabaseAbstractionLayer:
#     @staticmethod
#     def add_new_issue(*args, **kwargs):
#         # tu wykonaj odpowiednie zapytanie
#
# i tak dalej, dla kazdej z operacji