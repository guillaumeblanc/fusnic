import os
import sys
import logging
import unittest
import functools

from fusnic.tests.utils import *
import fusnic


class TestSession(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.invalid = 'Invalid93#!'
        cls.user, cls.password = credentials()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_invalid_user(self):
        with self.assertRaises(fusnic.LoginFailed) as context:
            with fusnic.Session(user=self.invalid, password=self.invalid):
                pass

    @frequency_limit
    def test_invalid_password(self):
        with self.assertRaises(fusnic.LoginFailed) as context:
            with fusnic.Session(user=self.user, password=self.invalid):
                pass

    @frequency_limit
    def test_valid_login(self):
        with fusnic.Session(user=self.user, password=self.password):
            pass


if __name__ == '__main__':
    unittest.main()
