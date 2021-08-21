class GlobalValues():
    def __init__(self):
        self.userDataList = []


class UserData():
    def __init__(self, listname, url, username, password):
        self.listname = listname
        self.url = url
        self.username = username
        self.password = password

    def get_listname(self):
        return self.listname
    def get_url(self):
        return self.url
    def get_username(self):
        return self.username
    def get_password(self):
        return self.password


