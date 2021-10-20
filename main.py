from issue import Issue
from issue_list import IssueList
from csv_writer import write_to_csv

def main():
    user_name = input("Enter username: ")
    bug_title = input("Enter bug title: ")
    bug_description = input("Enter bug description: ")
    my_issues = IssueList([Issue])
    my_issues.add_new(user = user_name, title = bug_title, description = bug_description)
    #
    # IssueList.delete_by_id()
    my_issues.show()

    #
    # write_to_csv()


if __name__ == '__main__':
    main()


