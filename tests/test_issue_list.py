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
        ids = [3, 4, 1]
        size = len(self.issue_list.issues)
        for idx, _id in enumerate(ids):
            self.issue_list.delete_by_id(_id)
            new_size = size - idx - 1
            self.assertEqual(len(self.issue_list.issues), new_size)

        # ids = [3, 4, 1]
        # for _id in  ids:
        #     self.issue_list.delete_by_id(_id)
        #     self.assertNotIn(self.issue_list.issues[])

    @patch('builtins.print')
    def test_show(self, mock_print):
        self.issue_list.show()
        mock_print.call_args_list = self.issue_list.issues

    #         # TODO: update this string with proper output
    # #         expected_output = '''
    # # Issue(...)
    # Issue(...)
    #         '''
    # we must strip whitespace characters from beginning / end
    # probably we need to cut only from beginning using lstrip instead
    # expected_output = expected_output.strip()

    # we need to call our show method from issue_list (saved in setUp method)

    # example:
    # print('hello')
    # mock_print.assert_called_with('hello')
    # print('world')
    # mock_print.assert_called_with('world')
    # print('aaa')
    # mock_print.assert_called_with('aaa')

    # if you want to check what's inside mock_print use this:
    # sys.stdout.write(str(mock_print.call_args_list) + '\n')
    # we must pass every parameter that is passed to our normal print function
    # separately to the assert_called_with method
    # example: https://realpython.com/lessons/mocking-print-unit-tests/

    def test_filter_by(self):
        self.issue_list.filter_by("Bob", "App not loading")
        self.assertRaises(AttributeError)






if __name__ == '__main__':
    unittest.main()

    # to run tests from command line use this (from within this folder):
    # $ python3 -m unittest -v
