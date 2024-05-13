from cryptography.fernet import Fernet
import os
key = Fernet.generate_key()

loc = os.path.dirname(os.path.abspath(__file__))
key_loc  =  os.path.join(loc, 'user_key.key')


with open(key_loc, 'wb') as filekey:
   filekey.write(key)


