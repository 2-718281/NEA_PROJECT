import json
class db:
    def __init__(self, name, data):
        self.db_name = name
        with open(name, 'w+') as outfile:
            json.dump(data, outfile)

    def replace_db(self, new):
        with open(self.db_name, 'w+') as outfile:
            json.dump(new, outfile)

