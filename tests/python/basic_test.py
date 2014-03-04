import os
import unittest
from server import buildApp


class BasicTest(unittest.TestCase):

    def setUp(self):
        """ setup test app and get a handle to the database """
        self.app = buildApp('test').test_client()

    def tearDown(self):
        """Clean up the database"""
        # self.db.problems.remove()
        pass

    def testGet(self):
        """ A GET request to / (root) should return a 200 OK """
        res = self.app.get('/')
        self.assertEquals(res.status, '200 OK')


if __name__ == '__main__':
    unittest.main()
