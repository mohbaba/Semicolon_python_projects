from DiaryApp.exceptions.EntryNotFoundException import EntryNotFoundException
from DiaryApp.exceptions.IncorrectPasswordException import IncorrectPasswordException
from DiaryApp.exceptions.LockedDiaryException import LockedDiaryException
from DiaryApp.Entry import *


class Diary:
    is_locked = True
    entries = []

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def unlock_diary(self, password):
        self.validate_password(password)
        self.is_locked = False

    def isLocked(self):
        return self.is_locked

    def validate_password(self, password):
        return self.password == password

    def validate_username(self, username):
        return self.username == username


    def lock_diary(self):
        self.is_locked = True

    def generate_id(self):
        return len(self.entries)

    def create_entry(self, title, body):
        self.check_lock()
        entry = Entry(self.generate_id(), title, body)
        self.entries.append(entry)

    def get_number_of_entries(self):
        return len(self.entries)

    def check_lock(self):
        if self.is_locked:
            raise LockedDiaryException("Diary is locked")

    def find_entry_by_id(self, id):
        self.check_lock()
        for entry in self.entries:
            if entry.get_id() == id:
                return entry
        return None

    def update_entry(self, id, title, body):
        self.check_lock()
        entry = self.find_entry_by_id(id)
        self.validate_entry(entry)
        entry.setTitle(title)
        entry.setBody(body)


    def validate_entry(self, entry):
        if entry is None:
            raise EntryNotFoundException("Entry does not exist")

    def delete_entry(self, entry_id):
        self.check_lock()
        entry = self.find_entry_by_id(entry_id)
        self.validate_entry(entry)
        self.entries.remove(entry)
        
    
