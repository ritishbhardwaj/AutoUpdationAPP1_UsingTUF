import logging
import os
import pathlib
import sys

from tufup.utils.platform_specific import ON_WINDOWS

# logger = logging.getLogger(__name__)

# App info
APP_NAME = 'demoApp1'  # BEWARE: app name cannot contain whitespace
APP_VERSION = '1.0.0'

MODULE_DIR = pathlib.Path(__file__).resolve().parent
print("MODULE_DIR   ->",MODULE_DIR, type(MODULE_DIR))

FROZEN = getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')

DEV_DIR = MODULE_DIR / f'temp_{APP_NAME}'
print("DEV_DIR    :->", DEV_DIR,type(DEV_DIR))

# App directories
if ON_WINDOWS:
    # Windows per-user paths
    PER_USER_DATA_DIR = pathlib.Path(os.getenv('LOCALAPPDATA'))
    PER_USER_PROGRAMS_DIR = PER_USER_DATA_DIR / 'Programs'
    print(PER_USER_DATA_DIR,")))))))))))")
    print(PER_USER_PROGRAMS_DIR,"(((((((((())))))))))")

PROGRAMS_DIR = PER_USER_PROGRAMS_DIR if FROZEN else DEV_DIR
DATA_DIR = PER_USER_DATA_DIR if FROZEN else DEV_DIR

INSTALL_DIR = PROGRAMS_DIR / APP_NAME
UPDATE_CACHE_DIR = DATA_DIR / APP_NAME / 'update_cache'
METADATA_DIR = UPDATE_CACHE_DIR / 'metadata'
TARGET_DIR = UPDATE_CACHE_DIR / 'targets'
print("METADATA_DIR--> ",METADATA_DIR)
print("TARGET_DIR -->  ",TARGET_DIR)

METADATA_BASE_URL = 'http://127.0.0.1:8000/metadata/'
TARGET_BASE_URL = 'http://127.0.0.1:8000/check_update'


# Location of trusted root metadata file
# TRUSTED_ROOT_SRC = MODULE_DIR.parent / 'root.json'
# if not FROZEN:
#     # for development, get the root metadata directly from local repo
#     sys.path.insert(0, str(MODULE_DIR.parent.parent))
#     from repo_settings import REPO_DIR

#     TRUSTED_ROOT_SRC = REPO_DIR / 'metadata' / 'root.json'
# TRUSTED_ROOT_DST = METADATA_DIR / 'root.json'




