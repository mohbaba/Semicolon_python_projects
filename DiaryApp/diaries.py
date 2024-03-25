from DiaryApp.Diary import Diary
from DiaryApp.exceptions.DiaryNotFoundException import *
from DiaryApp.exceptions.IncorrectPasswordException import *


class Diaries:

    def __init__(self):
        self.diaries = []

    def add(self, username, password):
        diary = Diary(username, password)
        self.diaries.append(diary)

    def get_number_of_diaries(self):
        return len(self.diaries)

    def find_by_username(self, username):
        found_diary = None
        for diary in self.diaries:
            if diary.username == username:
                found_diary = diary
        self.check_diary(found_diary)
        return found_diary

    def delete(self, username, password):
        diary = self.find_by_username(username)
        self.check_diary(diary)

        if diary.validate_password(password):
            if diary.validate_username(username):
                self.diaries.remove(diary)
            else:
                raise DiaryNotFoundException("Username does not exist")
        else:
            raise IncorrectPasswordException("Incorrect Password")

    def check_diary(self, diary):
        if diary is None:
            raise DiaryNotFoundException("Diary Not Found")


