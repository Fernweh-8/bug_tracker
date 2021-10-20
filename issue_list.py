from typing import List
from dataclasses import dataclass
from issue import Issue

@dataclass
class IssueList:
    issues: List[Issue]

    def add_new(self, **kwargs):
        self.issues.append(Issue(**kwargs))

    def delete_by_id(self, _id):
        for index, issue in enumerate(self.issues):
            if issue._id == _id:
                del self.issues[index]

    def show(self):
        for issue in self.issues:
            print(issue)