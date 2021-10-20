from status import Status
from issue import Issue

def main():
    issue_list = []

    # issue_1 = Issue(user="Anna", title="New bug", description="This is a new bug")
    # issue_2 = Issue(user="Monika", title="Another bug", description="This is another new bug")
    #
    # issue_list.append(issue_1)
    # issue_list.append(issue_2)

    def create_issue(**kwargs):
        issue_list.append(Issue(**kwargs))

    # def create_issue(**kwargs):
    #     return Issue(**kwargs)
    #
    # def add_to_list():
    #     issue_list.append(create_issue)

    create_issue(user="John", title="New issue 1", description="This is the first issue")
    create_issue(user="Anna", title="New issue 2", description="This is the second issue")
    create_issue(user="Monika", title="New issue 3", description="This is the third issue")

    # print(issue_list)

    # print(add_to_list())

    def delete_from_list(number):
        for issue in issue_list:
            if issue._id == number:
                issue_list.remove(issue)

    delete_from_list(1)

    print(issue_list)

    def write_to_csv(issue):
        with open("C:/Users/Fernweh/PycharmProjects/BugTrackerNew/issues.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(issue.to_csv())

    write_to_csv(Issue(user="Lala", title="New issue 4", description="This is the fourth issue"))


if __name__ == '__main__':
    main()


