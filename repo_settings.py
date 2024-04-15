import pathlib

from tufup.repo import DEFAULT_KEY_MAP, DEFAULT_KEYS_DIR_NAME, DEFAULT_REPO_DIR_NAME


# Path to directory containing current module
MODULE_DIR = pathlib.Path(__file__).resolve().parent
print(MODULE_DIR,"----------------")

# For development
DEV_DIR = MODULE_DIR / 'temp_my_app'
print("DEVDIR  ",DEV_DIR)
PYINSTALLER_DIST_DIR_NAME = 'dist'

DIST_DIR = DEV_DIR / PYINSTALLER_DIST_DIR_NAME
print("DIST_DIR   ",DIST_DIR)

# Local repo path and keys path (would normally be offline)
KEYS_DIR = DEV_DIR / DEFAULT_KEYS_DIR_NAME
REPO_DIR = DEV_DIR / DEFAULT_REPO_DIR_NAME
print("KEYS_DIR  ",KEYS_DIR)
print("REPO_DIR  ",REPO_DIR)
print()

# Key settings
KEY_NAME = 'my_key'
PRIVATE_KEY_PATH = KEYS_DIR / KEY_NAME
KEY_MAP = {role_name: [KEY_NAME] for role_name in DEFAULT_KEY_MAP.keys()}
print("KEY_MAP   ",KEY_MAP)
ENCRYPTED_KEYS = []
THRESHOLDS = dict(root=1, targets=1, snapshot=1, timestamp=1)
EXPIRATION_DAYS = dict(root=365, targets=7, snapshot=7, timestamp=1)