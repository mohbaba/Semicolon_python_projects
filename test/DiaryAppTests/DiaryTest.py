import unittest

from DiaryApp.Diary import Diary
from DiaryApp.exceptions.EntryNotFoundException import EntryNotFoundException
from DiaryApp.exceptions.IncorrectPasswordException import IncorrectPasswordException
from DiaryApp.exceptions.LockedDiaryException import LockedDiaryException


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.diary = Diary("username", "password")

    def tearDown(self):
        self.diary.entries.clear()

    def testDiaryCanBeUnlockedWithPassword(self):
        self.diary.unlock_diary("password")
        self.assertFalse(self.diary.isLocked())

    def testDiaryCanBeLocked(self):
        self.diary.lock_diary()
        self.assertTrue(self.diary.isLocked())

    def testThatDiaryWillThrowExceptionWhenPasswordIsIncorrect(self):
        with self.assertRaises(IncorrectPasswordException):
            self.diary.unlock_diary("wrong password")

    def testDiaryCanCreateEntry(self):
        self.diary.unlock_diary("password")
        self.diary.create_entry("How far", "I Dey oooo")
        self.assertEqual(1, self.diary.get_number_of_entries())

    def testDeleteEntryThatDoesNotExist_RaiseException(self):
        self.diary.unlock_diary("password")
        self.diary.create_entry("Mohbaba", "number")
        with self.assertRaises(EntryNotFoundException):
            self.diary.delete_entry(2)

    def testCreateThreeEntries_deleteSecondEntryTestThatTheThirdAndFirstIdAreStillTheSame(self):
        self.diary.unlock_diary("password")
        self.diary.create_entry("Name of the day", "I had fun today!")
        self.diary.create_entry("Game of the day", "I had a fun day!")
        self.diary.create_entry("Aim of the day", "I had one today!")
        self.diary.delete_entry(1)
        self.assertEqual(0, self.diary.find_entry_by_id(0).get_id())
        self.assertEqual(2, self.diary.find_entry_by_id(2).get_id())

    def testCreateEntryOnDiaryWhenLocked_ThrowExceptionTest(self):
        with self.assertRaises(LockedDiaryException):
            self.diary.create_entry("hello", "sup")

    def testDeleteEntryOnDiaryWhenLocked_ThrowExceptionTest(self):
        with self.assertRaises(LockedDiaryException):
            self.diary.create_entry("hello", "sup")

    def testFindEntryOnDiaryWhenLocked_ThrowExceptionTest(self):
        with self.assertRaises(LockedDiaryException):
            self.diary.create_entry("hello", "sup")

    def testFindAnEntry_WhenTheEntryExists(self):
        self.diary.unlock_diary("password")
        self.diary.create_entry("Gym bro", "cave")
        self.assertIsNotNone(self.diary.find_entry_by_id(0))

    def testFindAnEntryThatDoesNotExist_returnNoneTest(self):
        self.diary.unlock_diary("password")
        self.assertIsNone(self.diary.find_entry_by_id(20))

    def testUpdateEntryInDiaryWhenLocked_ThrowExceptionTest(self):
        with self.assertRaises(LockedDiaryException):
            self.diary.update_entry(0, "title", "body")

    def testUpdateEntryInDiary_EntryChanges(self):
        self.diary.unlock_diary("password")
        self.diary.create_entry("Bossman", "Moh")
        entry = self.diary.find_entry_by_id(0)

        self.assertEqual("Bossman", entry.getTitle())
        self.assertEqual("Moh", entry.getBody())
        self.diary.update_entry(0, "big man", "nw_body")

        self.assertEqual("big man", entry.getTitle())
        self.assertEqual("nw_body", entry.getBody())


if __name__ == '__main__':
    unittest.main()
