import distutils
from typing import List
from dataclasses import dataclass, field
from issue import Issue
from distutils import util
from status import Status


@dataclass
class IssueList:
    issues: List[Issue] = field(default_factory = list)

    def add_new(self, **kwargs):
        self.issues.append(Issue(**kwargs))

    def delete_by_id(self, _id):
        for index, issue in enumerate(self.issues):
            if issue._id == _id:
                del self.issues[index]

    def show(self):
        for issue in self.issues:
            print(issue)


    def filter_by(self):
        matched = []
        value = self.choose_value()
        for issue in self.issues:
            param = getattr(issue, self.choose_attr())
            if param == value:
                matched.append(issue)
        return matched

    def choose_attr(self):
        print("List of available attributes:")
        attrs = [att for att in Issue.__dataclass_fields__.keys() if not att.startswith('_')]
        for index, attr in enumerate(attrs, start = 1):
            print(f"{index}: {attr}")
        while True:
            try:
                choice = int(input("Enter the correct number to choose the attribute you want to filter by: "))
                if 1 <= choice < len(attrs) + 1:
                    return attrs[choice - 1]
                else:
                    raise ValueError
            except(TypeError, ValueError):
                print("You entered the wrong number. Try again.")
                continue


    def choose_value(self):
        attr = self.choose_attr()
        while True:
            attr_value = input(f'Enter the value of the {attr} attribute: ')
            if attr == "status":
                attr_value = Status.parse_status(attr_value)
            if attr == "flagged":
                try:
                    attr_value = bool(distutils.util.strtobool(attr_value))
                except ValueError:
                    print("No such value. Try again. Enter yes for a flagged issue or no for an unflagged one: ")
            return attr_value








