from DiaryApp.Diary import Diary
class Diaries:
    def __init__(self):
        self.diaries  = []

    def add(self, username, password):
        diary = Diary(username, password)
        self.diaries.append(diary)

    def get_number_of_diaries(self):
        pass
