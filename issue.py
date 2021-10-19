import csv
from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Dict, Set, Optional
from enum import Enum, auto
from itertools import count
from pprint import pprint
from datetime import datetime as dt

ID_GENERATOR = count(start=1)


class Status(Enum):
    NEW = auto()
    IN_PROGRESS = auto()
    REOPENED = auto()
    ON_HOLD = auto()
    CLOSED = auto()


@dataclass()
class Issue:
    user: str
    title: str
    description: str = field(default='')
    status: Status = field(default=Status.NEW, repr=False)
    _id: int = field(default_factory=lambda: next(ID_GENERATOR))
    date_created: dt = field(default=dt.now(), repr=True)

    # def __repr__(self):
    #     return f'(user: {self.user}, title: {self.title}, description: {self.description})'

    #
    # @property
    # def date_created(self):
    #     return self.date_created.strftime("%m/%d/%Y, %H:%M:%S")
    #
    def to_csv(self):
        return f"{self._id},{self.title},{self.description},{self.status},{self.user},{self.date_created}."


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
s
def write_to_csv(issue):
    with open("C:/Users/Fernweh/PycharmProjects/BugTrackerNew/issues.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(issue.to_csv())
        
write_to_csv(Issue(user="Lala", title="New issue 4", description="This is the fourth issue"))





