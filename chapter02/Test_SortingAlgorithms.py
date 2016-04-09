import unittest
from SortingAlgorithms import *

class TestSortingAlgorithms(unittest.TestCase):

    def get_test_cases(self):
        return (([5, 2, 4, 6, 1, 3], [1, 2, 3, 4, 5, 6]),
                  ([190, 2, 4, 6, 1, 3], [1, 2, 3, 4, 6, 190]),
                  ([-190, 2, 4, 6, 1, 3], [-190, 1, 2, 3, 4, 6]),
                  ([0, 0, 4, 6, 1, 3], [0, 0, 1, 3, 4, 6]),
                  ([0, 0], [0, 0]),
                  ([1, 0], [0, 1]),
                  ([3, 22, 2, 13, 4, 1, 4, 8], [1, 2, 3, 4, 4, 8, 13, 22]))

    def test_insertion_sort(self):
        for test_case in self.get_test_cases():
            self.assertEqual(insertion_sort(test_case[0]), test_case[1])


    def test_merge_sort(self):
        for test_case in self.get_test_cases():
            self.assertEqual(merge_sort(test_case[0], 0, len(test_case[0])), test_case[1])
