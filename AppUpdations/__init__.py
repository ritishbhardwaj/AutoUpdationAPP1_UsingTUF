__version__ = '13.0.0'

import tuf
import tufup
from typing import Dict, List, Tuple
from tufup.utils.platform_specific import  ON_WINDOWS
import tufup.client
import pathlib,sys
import os

import json
import time

APP_NAME = 'demoApp1'
print(ON_WINDOWS)
MODULE_DIR = pathlib.Path(__file__).resolve().parent.parent
print("MODULE_DIR   ->",MODULE_DIR, type(MODULE_DIR))

FROZEN = getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')

DEV_DIR = MODULE_DIR / f'temp_{APP_NAME}'
print("DEV_DIR    :->", DEV_DIR,type(DEV_DIR))

METADATA_BASE_URL = 'http://127.0.0.1:8000/metadata/'
TARGET_BASE_URL = 'http://127.0.0.1:8000/targets/'

def progress_hook(bytes_downloaded: int, bytes_expected: int):
    progress_percent = bytes_downloaded / bytes_expected * 100
    print(f'\r{progress_percent:.1f}%', end='')
    time.sleep(0.2)  # quick and dirty: simulate slow or large download
    if progress_percent >= 100:
        print('')


def updateHandler(install_dir:str,meta_dir:str,target_dir:str):
    client = tufup.client.Client(APP_NAME, install_dir, #it is app install directory on client machine 
                                 __version__, meta_dir, #this is meta directory   on client machine 
                                 METADATA_BASE_URL,
                                 target_dir , TARGET_BASE_URL)

    # client.refresh()
    any_update = client.check_for_updates()
    print("AnyUpdate---------->    ",any_update)
    # getInfo = client.get_targetinfo(DEV_DIR / 'repository/metadata')
    # print(getInfo)
    if any_update:
        print("woooooohoooooooo")

        if any_update.custom:
            print('changes in this update:')
            for item in any_update.custom.get('changes', []):
                print(f'\t- {item}')

        client.download_and_apply_update()
        print("Downloading......")


def main():
    # Create meta_data directory if it doesn't exist
    meta_data_dir = DEV_DIR / 'repository/metadata'
    # meta_data_dir.mkdir(exist_ok=True, parents=True)
    for make in [DEV_DIR / 'demoApp1',DEV_DIR/'repository/targets',DEV_DIR / 'repository/metadata']:
        make.mkdir(exist_ok=True,parents=True)
    # Path to root.json file

    ROOT_JSON_FILE = meta_data_dir / 'root.json'

    # Create root.json file if it doesn't exist
    if ROOT_JSON_FILE.exists():
        print("hahahahahahha")
        
    FROZEN = getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')
    if not FROZEN:
        install_dir = str(DEV_DIR / 'demoApp1')
        meta_dir =str(DEV_DIR / 'repository/metadata')
        targets_dir = str(DEV_DIR/'repository/targets')
        updateHandler(install_dir,meta_dir,targets_dir)
    # Check if root.json file was created successfully
    else:
        # install_dir = str(DEV_DIR / 'demoApp1')
        install_dir = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        # install_dir = os.path.join(desktop_dir, 'demoApp1')
        meta_dir =str(MODULE_DIR/'metadata')
        targets_dir = str(DEV_DIR/'repository/targets')
        updateHandler(install_dir,meta_dir,targets_dir)


if __name__ == "__main__":
    print("--------=-=-====================")
    print(DEV_DIR)
    main()




