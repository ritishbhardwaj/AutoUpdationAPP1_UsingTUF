import os
from dotenv import load_dotenv
load_dotenv(override=True)
PRIVATE_KEY = os.environ.get('PRV_KEY')


def toggling(original_key:str):
    masking_key=''
    for s in original_key:
        make = s.lower()
        if ord(s) == ord(make) :
            masking_key+= s.upper()
        elif ord(s) != ord(make):
            masking_key+=s.lower()
        else:
            masking_key+=s
    return masking_key

if __name__ =="__main__":
    print(toggling(PRIVATE_KEY))