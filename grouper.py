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



issues_grouped = defaultdict(list)

for issue in new_list.issues:
    issues_grouped[issue.status].append(issue)

pprint.pprint(issues_grouped)

