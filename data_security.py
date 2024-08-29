import hashlib
import os

class DataSecurity:
    def __init__(self, data):
        self.data = data

    def encrypt_data(self):
        salt = os.urandom(16)
        key = hashlib.pbkdf2_hmac('sha256', self.data.encode(), salt, 100000)
        return salt, key

    def decrypt_data(self, salt, key):
        # This is a placeholder for actual decryption logic
        return "Decrypted data"

if __name__ == "__main__":
    data = "Customer's body data"
    security = DataSecurity(data)

    salt, encrypted_key = security.encrypt_data()
    print("Encrypted Data Key:", encrypted_key)

    decrypted_data = security.decrypt_data(salt, encrypted_key)
    print("Decrypted Data:", decrypted_data)
