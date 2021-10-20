from issue import Issue
from issue_list import IssueList
from csv_writer import write_to_csv

def main():

    IssueList.add_new()
    IssueList.delete_by_id()
    IssueList.show()


    write_to_csv()


if __name__ == '__main__':
    main()


