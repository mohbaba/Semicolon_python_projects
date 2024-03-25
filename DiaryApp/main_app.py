from DiaryApp.diaries import Diaries


class MainApp:
    def __init__(self):
        self.diaries = Diaries()
        self.current_diary = None

    def register(self):
        username = self.set_username()
        password = self.password()
        self.diaries.add(username, password)

    def main_menu(self):
        print("""
                Welcome to Mo's Diary App
                1 -> Create New Diary
                2 -> Delete Diary
                3 -> Create New Entry
                4 -> Delete Entry
                5 -> Update An Entry
                6 -> Find Diary
                7 -> Unlock Diary
                8 -> Lock Diary
                9 -> Exit


                """)


    def set_username(self):
        return input("Please enter username: ")

    def password(self):
        return input("Please enter password")

    def null_contingency(self):
        print("Diary hasn't been created, create diary first")
        self.create_diary()

    def create_diary(self):
        username = self.set_username()
        password = self.password()
        self.diaries.add(username, password)

    def delete_diary(self):
        try:
            username = self.set_username()
            password = self.password()
            self.diaries.delete(username, password)
            print("*****Diary Deleted Successfully*****")
        except Exception as message:
            print(message)

    def create_diary_entry(self):
        try:
            username = self.set_username()
            password = self.password()
            diary = self.diaries.find_by_username(username)
            diary.unlock_diary(password)
            title = input("Enter Title of Entry: ")
            body = input("Enter Body of Entry: ")
            diary.create_entry(title, body)
            print("*****Entry Successfully Added*****")
        except Exception as message:
            print(message)

    def delete_entry_from_diary(self):
        try:
            username = self.set_username()
            password = self.password()
            diary = self.diaries.find_by_username(username)
            diary.unlock_diary(password)
            entry_id = input("Enter the id of the entry you'd like to delete: ")
            diary.delete_entry(int(entry_id))
            print("Entry successfully deleted ")
        except Exception as message:
            print(message)

    def update_diary_entry(self):
        try:
            username = self.set_username()
            password = self.password()
            diary = self.diaries.find_by_username(username)
            diary.unlock_diary(password)
            entry_id = input("Enter the id of the entry you'd like to update: ")
            title = input("Enter new title: ")
            body = input("Enter body of the entry: ")
            diary.update_entry(int(entry_id), title, body)
            print("Entry successfully updated ")
        except Exception as message:
            print(message)

    def find_diary(self):
        try:
            username = self.set_username()
            password = self.password()
            diary = self.diaries.find_by_username(username)
            self.current_diary = diary
            print("Found the Diary! you may proceed to use now ")
        except Exception as message:
            print(message)

    def unlockDiary(self):
        try:
            username = self.set_username()
            password = self.password()
            diary = self.diaries.find_by_username(username)
            diary.unlock_diary(password)
            print("Diary is unlocked you may now proceed to use!")
        except Exception as message:
            print(message)

    def lockDiary(self):
        try:
            username = self.set_username()
            password = self.password()
            diary = self.diaries.find_by_username(username)
            diary.lock_diary()
            print("Diary is locked!")
        except Exception as message:
            print(message)


main_app = MainApp()
main_app.main_menu()