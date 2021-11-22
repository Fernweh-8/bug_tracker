import unittest
import sys
from unittest.mock import patch

# https://stackoverflow.com/questions/30669474/beyond-top-level-package-error-in-relative-import
# to be able to import our modules from the parent folder
sys.path.append("..")

from issue_list import IssueList
from issue import Issue
from status import Status


class TestIssueList(unittest.TestCase):
    def setUp(self):
        self.issue_list = IssueList([
            Issue(user='Anna', title='App does not work'),
            Issue(user='John', title='App crashes'),
            Issue(user='Anna', title='User account does not exist', status=Status.ON_HOLD),
            Issue(user='Anna', title='App still does not work', status=Status.REOPENED),
            Issue(user='John', title='Strange behavior', flagged=True),
        ])

    def tearDown(self):
        del self.issue_list

    def test_delete_by_id(self):
        self.issue_list.delete_by_id("One")
        self.assertRaises(TypeError)
        self.issue_list.delete_by_id(0)
        self.assertRaises(ValueError)
        ids = [3, 4, 1]
        size = len(self.issue_list.issues)
        for idx, _id in enumerate(ids):
            self.issue_list.delete_by_id(_id)
            new_size = size - idx - 1
            self.assertEqual(len(self.issue_list.issues), new_size)


    @patch('builtins.print')
    def test_show(self, mock_print):
        self.issue_list.show()
        mock_print.call_args_list = self.issue_list.issues


    def test_filter_by(self):
        self.issue_list.filter_by("owner", "App not loading")
        self.assertRaises(AttributeError)
        self.assertEqual(len(self.issue_list.filter_by('user', 'Anna')), 3)
        self.assertEqual(len(self.issue_list.filter_by('user', 'John')), 2)
        self.assertEqual(len(self.issue_list.filter_by('user', 'Bob')), 0)


if __name__ == '__main__':
    unittest.main()

    # to run tests from command line use this (from within this folder):
    # $ python3 -m unittest -v
