from issue import Issue
from issue_list import IssueList
from helpers import write_to_csv

def main():
    my_issues = IssueList()
    for i in range(2):
        user_name = input("Enter username: ")
        bug_title = input("Enter bug title: ")
        bug_description = input("Enter bug description: ")
        my_issues.add_new(user = user_name, title = bug_title, description = bug_description)

    # to_delete = int(input("Enter the id number of the issue you want to delete - only integers allowed."))
    # my_issues.delete_by_id(to_delete)
    #
    # my_issues.show()
    print(my_issues.filter_by("user", "Anna"))

    #
    # write_to_csv()


if __name__ == '__main__':
    main()


