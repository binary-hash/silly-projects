from strongcrypter import encrypt,decrypt

class data:
    def __init__(self,data):
        self.data = data

    def encrypt_data(self):
        return encrypt(self.data)

class decode:
    def __init__(self, encoded,dummy):
        self.encoded = encoded
        self.dummy = dummy
    
    def decode_data(self):
        return decrypt(self.dummy,self.encoded)