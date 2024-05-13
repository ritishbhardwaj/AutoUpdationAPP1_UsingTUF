from cryptography.hazmat.primitives import serialization

from cryptography.hazmat.backends import default_backend
def load_public_key(public_key_bytes):
    public_key = serialization.load_pem_public_key(
        public_key_bytes,
        backend=default_backend()
    )
    return public_key


def load_private_key(private_key_bytes):
    private_key= serialization.load_pem_private_key(
        private_key_bytes,
        password=None,
        backend=default_backend()
    )
    return private_key

def print_public_key(public_key):
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    print("Public Key:")
    print(public_key_pem.decode())

def print_private_key(private_key):
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        # format=serialization.PrivateFormat.OpenSSH,
        encryption_algorithm=serialization.NoEncryption()
    )
    print("Private Key:")
    print(private_key_pem.decode())

human_readable_publicKey = b'''
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxyi0xxam1flrsf4poGWJ
mTWPXL/c2nzqdmIKrF7YmBD7skH1ncBb4qBdWmDvxLZ+Wxx/wCpQsmFEH39uydpx
6zxDeiVoIGSvjKOnUvonNlsKVi8waFfoXGT10wmsedJZPFXiGI7cjO61DL8RjwBB
qGqCHmI0tH6CHuh5D2839VGF+AZrSWfud2jYiWb7CMFhEiS/ItqfyTRK8eXnrWzX
7q5yIYhP2D5lEjokhoPKoo0Ba2TWqgjKiBgKoZ7NRctFveC/qd4Oa+FbVdVQuP5E
FedWPIbUoa62bB1Z2cF3EoSqHHT5IF1YgQKjYUV9DbvapLQ+uYAiqhx6opy6ISM6
5QIDAQAB
-----END PUBLIC KEY-----
'''

human_readable_privateKey = b'''
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDHKLTHFqbV+Wux
/imgZYmZNY9cv9zafOp2YgqsXtiYEPuyQfWdwFvioF1aYO/Etn5bHH/AKlCyYUQf
f27J2nHrPEN6JWggZK+Mo6dS+ic2WwpWLzBoV+hcZPXTCax50lk8VeIYjtyM7rUM
vxGPAEGoaoIeYjS0foIe6HkPbzf1UYX4BmtJZ+53aNiJZvsIwWESJL8i2p/JNErx
5eetbNfurnIhiE/YPmUSOiSGg8qijQFrZNaqCMqIGAqhns1Fy0W94L+p3g5r4VtV
1VC4/kQV51Y8htShrrZsHVnZwXcShKocdPkgXViBAqNhRX0Nu9qktD65gCKqHHqi
nLohIzrlAgMBAAECggEAEJc8BA/HgzC9f3zoU9PRlCFJmZTkHZFlaMo/EF/wVC6q
AQ4Mm4EgRm9Mh5BmuPDo8scbf1MnGM0Qgz026frYHZwOFPlTxMsOcr1ZXYi4Rods
A4T31+Fm2neQoO1/4EAdLfELnjcceWMTUwYBvPNtBM4mm8hbkqOtTEzadOYzd6yW
q0IuveA/pttjWirC3t5J2T/p+BP2ZFMhwjKrNu7b7g89ZtjBvVkSt6GIIGaZgX8z
nYvzlDQyXky30M8MVEBZjChGo0N2u2lNIVWno3KirQ3F8iFFMIzSRli7fbr6IE3K
X7fVbGGqBFozo+mhP2Ob9w/iNhQ2ozbJOZd1YLRpAQKBgQD0TOW+PWMomGBfaExx
h5y+mPQfSOpj3cm6vBEqVM9KwVJPz2Ftncc4rLcXLNCpyDFEeWdC4sngWsL0R3At
jaMXL+Rm3UiaxuDX2oJ7qbvKbn4OHpFlUyZx9zaMMYB7Qy88xR42H6b2NcCQTciz
EDKiRNBQTnyrjrKMhnROo+HZZQKBgQDQsmEUlDaX0c7bqukEzC8sxp4goxpX5l/Y
ShFZmtJbXA4cFJOwivBWBqPpFWSLOFdTN+zI0/CylpkY0BJjo2ZATWzq7qspkCJR
425bv5pXuDlWAFBLR5eJ3tnSfR2ofs2BhvhdMWGEN/nK8+rVhkyw7DHN1Klyxel/
ziWDm16DgQKBgQDpS9oGD2d3J/S4h8igjknwde6DRcWYMv/nVJvr2evPTsiFMNyw
qoDKrZ13AzQNPwFVi75B0IPKvcH5N5N33Q+HIBQ061Lfg9bKK4B6CcAs89FrOGPO
6FYJdXRg8xDoJWOh2/ga5aUy8GgBJlboMSq5bY+lcR57Up1Nt0SwqK4QRQKBgBQe
fjlrqG+ubFDFAz3RKWMZqrjewHVk4iyJx25p/ImOMFYIrcxBOLYyYa7gvxak0dZV
99/MftHYrt2zgXJVmE/upudnJt0U5hoa4NK7f/eg7PYbhaIcPsGt2DXwleFeiBVK
m7rwPcRvWQd1yFfZYJ9Vxd9f9w33gnEtwHQVkGEBAoGAIKwX9J05ciXqYs+qsUoT
bgSFIrJpkVVMF5THHNq0bMbDOB7L0/L9rpCRrlED9AT/9tQzCFQMgZWdvMjQkraj
VJKI7sjOK4HpC4V0hhp4+r9+SbJVbX06+t2I0Bvah53VDSUxJsaPLHsARI4EL0xM
BuEnqqSdiclbvgTU5U6ffIA=
-----END PRIVATE KEY-----
'''

pb_key= load_public_key(human_readable_publicKey)
pr_key= load_private_key(human_readable_privateKey)
print(pb_key)
print(pr_key)
print_public_key(pb_key)
print_private_key(pr_key)


