import unittest
from DiaryApp.diaries import Diaries


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.diaries = Diaries()

    def add_diary_test(self):
        self.diaries.add("username","password")
        self.assertEqual(1,self.diaries.get_number_of_diaries())



if __name__ == '__main__':
    unittest.main()
