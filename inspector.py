class Inspector():


    def __init__(self):
        self.user_hashs = []
        self.uuid = []
        self.errors = []
        self.results = {}


    def check_user(self, id_hash):
        return id_hash in self.user_hashs


    def check_uuid(self, uuid):
        return uuid in self.uuid


    def add_user(self, id_hash, uuid):
        if self.check_user(id_hash):
            return False
        else:
            self.user_hashs.append(id_hash)
            self.add_uuid(uuid)
            return True


    def add_uuid(self, uuid):
        if self.check_uuid(uuid):
            return False
        else:
            self.uuid.append(uuid)
            return True


    def remove_user(self, id_hash, uuid):
        self.remove_uuid(uuid)
        if self.check_user(id_hash):
            self.user_hashs.remove(id_hash)
            return True
        else:   
            return False


    def remove_uuid(self,uuid):
        if self.check_uuid(uuid):
            self.uuid.remove(uuid)
            return True
        else:   
            return False


    def check_error(self, uuid):
        return uuid in self.errors


    def add_error(self, uuid):
        if self.check_error(uuid):
            return False
        else:
            self.errors.append(uuid)
            return True


    def remove_error(self, uuid):
        if self.check_eror(uuid):
            self.errors.remove(uuid)
            return True
        else:   
            return False


    def setResult(self, data, uuid):
        self.results[uuid] = data


    def getResult(self, uuid):
        if uuid in self.results.keys():
            return self.results[uuid]
        else:
            return {}