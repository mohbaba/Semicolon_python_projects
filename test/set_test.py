import unittest
from main_file.set_assignment import *



class MyTestCase(unittest.TestCase):

    def test_duplicates(self):
        user_input = [1, 2, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 0, 0, 8, 9]
        expected = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

        self.assertEqual(expected, find_set(user_input))

    def test_sum_collections(self):
        set_collection = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
        expected = 45

        self.assertEqual(expected, sum_collection(set_collection))

    def test_remove_item(self):
        set_collection = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
        item = 10
        expected = None

        self.assertEqual(expected, remove_item(set_collection, item))

    def test_find_intersection(self):
        set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        set2 = {2, 4, 6, 7, 8, -2, -4, -5}
        expected = {2, 4, 6, 7, 8}

        self.assertEqual(expected, find_intersection(set1, set2))

    def test_sequential_list(self):
        expected = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        self.assertEqual(expected, generate_list())

    def test_duplicate_list_elements(self):
        list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        expected = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15]

        self.assertEqual(expected, duplicate_element(list1))

    def test_eliminate_duplicate_list(self):
        list1 = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15]
        expected = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        self.assertEqual(expected,eliminate_duplicates(list1))
