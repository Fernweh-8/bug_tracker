import unittest
from unittest.mock import patch

from issue_list import IssueList
from issue import Issue
from status import Status

class TestIssueList(unittest.TestCase):

    def setUp(self):
       self.issue_lst = IssueList(
            [(user = 'Anna', title = 'App does not work'),
            (user = 'John', title =  'App crashes'),
            (user = 'Anna', title = 'User account does not exist', status = Status.ON_HOLD),
            (user = 'Anna', title = 'App still does not work', status = Status.REOPENED),
            (user = 'John', title = 'Strange behavior', flagged = True)])

    def tearDown(self):
        pass

    def test_delete_by_id(self):
        pass

    def show(self):
        pass

    def filter_by(self):
        pass


if __name__ == '__main__':
    unittest.main()