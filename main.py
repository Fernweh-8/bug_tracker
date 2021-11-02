from issue import Issue
from issue_list import IssueList
from helpers import write_to_csv

def main():
    my_issues = IssueList()
    for i in range(2):
        user_name = input("Enter username: ")
        bug_title = input("Enter bug title: ")
        bug_description = input("Enter bug description: ")
        my_issues.add_new(user = user_name, title = bug_title, description = bug_description, flagged = True)


    # print(my_issues.filter_by("user", "Anna"))

    # print(my_issues.choose_attr())
    print(my_issues.filter_by())



if __name__ == '__main__':
    main()


