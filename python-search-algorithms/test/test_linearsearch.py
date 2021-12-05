import unittest
from app import linear_search

class TestLinearSearch(unittest.TestCase):

    def test_doSearch_for_found(self):
        cars = ["Ford", "Volvo", "BMW"]
        self.assertEqual(1,linear_search.doSearch(cars,"Volvo"))

    def test_doSearch_for_not_found(self):
        cars = ["Ford", "Volvo", "BMW"]
        self.assertEqual(-1,linear_search.doSearch(cars,"Tesls"))

if __name__ == '__main__':
    unittest.main()