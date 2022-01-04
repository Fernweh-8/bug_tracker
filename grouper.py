from collections import defaultdict
from issue_list import IssueList

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


def display_grouped(groups):
    for key in groups:
        print(f'Group: {key}')
        for issue in groups[key]:
            print(issue)
        print()




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

