def togglingOld(original_key:str, isPrivate:bool):
    if isPrivate:
        masking_key=''
        masking_key+=original_key[:37]
        for s in original_key[37:-37]:
            make = s.lower()
            if ord(s) == ord(make) :
                masking_key+= s.upper()
            elif ord(s) != ord(make):
                masking_key+=s.lower()
            else:
                masking_key+=s
        masking_key+=original_key[-37:]
        return masking_key        
    else:
        masking_key=''
        masking_key+=original_key[:26]
        for s in original_key[26:-26]:
            make = s.lower()
            if ord(s) == ord(make) :
                masking_key+= s.upper()
            elif ord(s) != ord(make):
                masking_key+=s.lower()
            else:
                masking_key+=s
        masking_key+=original_key[-26:]
        return masking_key
    



import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


from dotenv import load_dotenv
load_dotenv(override=True)
PRIVATE_KEY:str = os.environ.get('PRV_KEY')
PUBLIC_KEY :str = os.environ.get('PUB_KEY')
# print("----------prv------>",PRIVATE_KEY)



def toggling(string:str):  
    start_marker = "KEY-----"
    end_marker = "-----END"
    start_index = string.find(start_marker) + len(start_marker)
    end_index = string.find(end_marker)
    
    text_to_toggle = string[start_index:end_index]
    
    # Toggle the case of each letter in the extracted text
    toggled_text = ''.join([char.upper() if char.islower() else char.lower() for char in text_to_toggle])
    
    # Replace the original text with the toggled text in the string
    result = string[:start_index] + toggled_text + string[end_index:]
    
    return result


def load_public_key(public_key_bytes):
    public_key = serialization.load_pem_public_key(
        public_key_bytes,    #public key must be in binary or bytes
        backend=default_backend()
    )
    return public_key


def load_private_key(private_key_bytes):
    ps='PyLeap'
    private_key= serialization.load_pem_private_key(
        private_key_bytes,
        password=ps.encode(),
        backend=default_backend()
    )
    return private_key

def encrypt_data(data, public_key):
    encrypted_data = public_key.encrypt(
        data.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_data

def decrypt_data(encrypted_data, private_key):
    decrypted_data = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_data.decode()

if __name__=="__main__":
    
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    private_key_file = os.path.join(curr_dir, 'private.key')
    pub_key_file = os.path.join(curr_dir, 'pub.key')    


    mydata = '''
            Hello Darkness my old friend
            I want to see you again'''
    print('mydata----------->',mydata)
    print()

    my_pub_key_org = toggling(PUBLIC_KEY)
    print(my_pub_key_org)
    my_pub_key = load_public_key(my_pub_key_org.encode())
    print("GETPUBKEY",my_pub_key)
    my_enc_data = encrypt_data(mydata , my_pub_key)
    print('my encrypted data------------->',my_enc_data)

    print()

    my_private_key_org = toggling(PRIVATE_KEY)
    print(my_private_key_org)
    my_private_key = load_private_key(my_private_key_org.encode())
    my_decrypted_data = decrypt_data(my_enc_data,my_private_key)
    print('my decrypted data------------->',my_decrypted_data)
