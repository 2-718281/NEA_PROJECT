class db:
    def __init__(self, name, data):
        self.data = data
        self.db_name = name
        open(name, mode='w+')

    def update_db(self, update, updated):
        self.data[update] = updated
        open(self.db_name, mode='w+', newline=self.data)

    def replace_db(self, new):
        self.data = new
        open(self.db_name ,mode='w+', newline= self.data)


