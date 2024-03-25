
import unittest
from DiaryApp.diaries import Diaries
from DiaryApp.exceptions.DiaryNotFoundException import *
from DiaryApp.exceptions.IncorrectPasswordException import *


class DiariesTest(unittest.TestCase):

    def setUp(self):
        self.diaries = Diaries()

    def test_add_diary(self):
        self.diaries.add("username", "password")
        self.assertEqual(1, self.diaries.get_number_of_diaries())

    def test_find_diary_by_username(self):
        self.diaries.add("username", "password")
        self.diaries.add("username1", "password1")
        self.assertIsNotNone(self.diaries.find_by_username("username1"))

    def test_find_diary_by_username_that_does_not_exist(self):
        with self.assertRaises(DiaryNotFoundException):
            self.diaries.find_by_username("username20")

    def test_delete_diary(self):
        self.diaries.add("Mohababa", "bossman")
        self.diaries.add("Promises", "BlackFlash")
        self.diaries.delete("Mohababa", "bossman")
        self.assertEqual(1, self.diaries.get_number_of_diaries())
        with self.assertRaises(DiaryNotFoundException):
            self.diaries.find_by_username("Mohababa")

    def test_delete_diary_with_incorrect_password_throws_exception(self):
        self.diaries.add("Mohababa", "bossman")
        self.diaries.add("Stark", "BlackFlash")
        with self.assertRaises(IncorrectPasswordException):
            self.diaries.delete("Mohababa", "wrong password")

    def test_delete_diary_with_incorrect_username_throws_exception(self):
        self.diaries.add("Mohababa", "bossman")
        self.diaries.add("Stark", "BlackFlash")
        with self.assertRaises(IncorrectPasswordException):
            self.diaries.delete("Mohababa", "wrong password")
        with self.assertRaises(DiaryNotFoundException):
            self.diaries.delete("Mohbaba", "bossman")


if __name__ == '__main__':
    unittest.main()
