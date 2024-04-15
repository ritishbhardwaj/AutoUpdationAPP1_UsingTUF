'''NOT USING IT RIGHT NOW WILL FIGURE IT OUT IN FUTURE'''

import logging
import sys

from tufup.repo import Repository
from repo_settings import DIST_DIR,KEYS_DIR
import pathlib

import AppUpdations


MODULE_DIR = pathlib.Path(__file__).resolve().parent
DIST_DIR=MODULE_DIR/'dist'
# KEYS_DIR = MODULE_DIR.parent/'temp_demoApp1/keystore'

# print(DIST_DIR)


logger = logging.getLogger(__name__)


if __name__ == '__main__':
    # create archive from latest pyinstaller bundle (assuming we have already
    # created a pyinstaller bundle, and there is only one)
    try:
        bundle_dirs = [path.parent for path in DIST_DIR.iterdir() if path.parent.is_dir()]
        # for p in DIST_DIR.iterdir() :
        #     print(p)
        #     if p.parent.is_dir():
        #         print("True")
        #         print(p)
        print(bundle_dirs)
    except FileNotFoundError:
        sys.exit(f'Directory not found: {DIST_DIR}\nDid you run pyinstaller?')
    if len(bundle_dirs) != 1:
        sys.exit(f'Expected one bundle, found {len(bundle_dirs)}.')
    bundle_dir = bundle_dirs[0]
    print(f'Adding bundle: {bundle_dir}')

    # Create repository instance from config file (assuming the repository
    # has already been initialized)
    repo = Repository.from_config()
    print("Repo is configured")
    # Add new app bundle to repository (automatically reads myapp.__version__)
    repo.add_bundle(
        new_bundle_dir=bundle_dir,
        new_version=AppUpdations.__version__,
        # [optional] custom metadata can be any dict (default is None)
        custom_metadata={'changes': ['new feature 12:21 o clock  added on 15/4/2024', 'bug version naming fixed']},
    )
    print("OK JI")
    repo.publish_changes(private_key_dirs=[KEYS_DIR])

    print('Done.') 