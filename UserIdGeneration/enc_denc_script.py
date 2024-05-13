from cryptography.fernet import Fernet

def encrypt_file(filename, key):
    with open(filename, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    with open(filename + '.enc', 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(filename, key):
    with open(filename, 'rb') as f:
        encrypted_data = f.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    print(decrypted_data)
    # with open(filename[:-4], 'wb') as f:  # Remove the .enc extension
    #     f.write(decrypted_data)

# Example usage:
with open('user_key.key' , 'r') as file :
    key  =  file.read()

print(key)
# encrypt_file('normalFile.txt', key)
decrypt_file('normalFile.txt.enc', key)