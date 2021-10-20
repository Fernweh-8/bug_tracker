from status import Status
from issue import Issue
from issue_list import IssueList

def main():

    def write_to_csv(issue):
        with open("C:/Users/Fernweh/PycharmProjects/BugTrackerNew/issues.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(issue.to_csv())

    write_to_csv(Issue(user="Lala", title="New issue 4", description="This is the fourth issue"))


if __name__ == '__main__':
    main()


