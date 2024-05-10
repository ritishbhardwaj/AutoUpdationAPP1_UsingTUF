from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


import os 
curr_dir = os.path.dirname(os.path.abspath(__file__))


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

def toggling(string):
    
    # Find the indices of the start and end markers
    
    start_marker = "KEY-----"
    end_marker = "-----END"
    

    start_index = string.find(start_marker) + len(start_marker)
    end_index = string.find(end_marker)
    
    # Extract the text between the start and end markers
    text_to_toggle = string[start_index:end_index]
    
    # Toggle the case of each letter in the extracted text
    toggled_text = ''.join([char.upper() if char.islower() else char.lower() for char in text_to_toggle])
    
    # Replace the original text with the toggled text in the string
    result = string[:start_index] + toggled_text + string[end_index:]
    
    return result

def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key


#Getting Human readable format of private keys
def print_private_key(private_key):
    private_key_pem:bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    print("Private Key:")
    print(private_key_pem.decode())
    return private_key_pem

def print_private_key_with_password(private_key, password = b"PyLeap"):
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(password)
    )
    print("Encrypted Private Key:")
    print(private_key_pem.decode())
    return private_key_pem

#Getting Human readable format of public keys
def print_public_key(public_key):
    public_key_pem:bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    print("Public Key:")
    print(public_key_pem.decode())
    return public_key_pem
    

if __name__ =="__main__":
    private_key, public_key = generate_key_pair()    # here we are getting the private and public keys in the
                                                     # form of objects
    print(public_key)
    pub_key_file = os.path.join(curr_dir, 'pub.key')    
    with open(pub_key_file , 'wb') as file:
        pub_key:bytes =print_public_key(public_key)
        pub_key_s = toggling(pub_key.decode())
        file.write(pub_key_s.encode())

    # print(private_key)
    # private_key_file = os.path.join(curr_dir, 'private.key')
    # with open(private_key_file,'wb') as file:
    #     pr_key:bytes= print_private_key(private_key)
    #     pr_key_s :str = toggling(pr_key.decode())
    #     file.write(pr_key_s.encode())

    private_key_file = os.path.join(curr_dir, 'private_pass.key')
    with open(private_key_file,'wb') as file:
        pr_key:bytes= print_private_key_with_password(private_key, b"PyLeap")
        # print('------------>',pr_key)
        pr_key_s :str = toggling(pr_key.decode())
        file.write(pr_key_s.encode())