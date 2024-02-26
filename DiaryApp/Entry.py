import datetime
class Entry:
    def __init__(self,id,title,body):
        self.id = id
        self.title = title
        self.body = body
        self.dateCreated = datetime.datetime.now()


    def get_id(self):
        return self.id

    def setTitle(self,title):
        self.title = title

    def setBody(self,body):
        self.body = body

    def getTitle(self):
        return self.title

    def getBody(self):
        return self.body
