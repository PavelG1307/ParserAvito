class Inspector():


    def __init__(self):
        self.user_hashs = []
        self.owner_id = []
        self.errors = []
        self.results = {}


    def check_user_in_parsing(self, id_hash):
        return id_hash in self.user_hashs


    def add_user_in_parsing(self, id_hash):
        if self.check_user_in_parsing(id_hash):
            return False
        else:
            self.user_hashs.append(id_hash)
            if self.check_user_in_error(id_hash):
                self.remove_user_in_error(id_hash)
            return True


    def remove_user_in_parsing(self, id_hash):
        if self.check_user_in_parsing(id_hash):
            self.user_hashs.remove(id_hash)
            return True
        else:   
            return False

    
    def check_user_in_error(self, id_hash):
        return id_hash in self.errors


    def add_user_in_error(self, id_hash):
        if self.check_user_in_parsing(id_hash):
            return False
        else:
            self.errors.append(id_hash)
            return True


    def remove_user_in_error(self, id_hash):
        if self.check_user_in_eror(id_hash):
            self.errors.append(id_hash)
            return True
        else:   
            return False


    def setResult(self, data, id_hash):
        self.results[id_hash] = data
    
    def getResult(self, id_hash):
        if id_hash in self.results.keys():
            return self.results[id_hash]
        else:
            return {}