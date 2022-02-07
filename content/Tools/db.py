import json
class db:
    def __init__(self, name, data):
        self.db_name = name+'.json'
        with open(name, 'w+') as outfile:
            json.dump(data, outfile)

    def update_db(self, update, updated):
        self.data[update] = updated
        open(self.db_name, mode='w+', newline=self.data)

    def replace_db(self, new):
        self.data = new
        open(self.db_name ,mode='w+', newline= self.data)


