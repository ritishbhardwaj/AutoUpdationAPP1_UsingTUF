from tufup.repo import Repository
import AppUpdations
print(AppUpdations.__version__)

APP_NAME= 'demoApp1'

from repo_settings import (
    ENCRYPTED_KEYS,
    EXPIRATION_DAYS,
    KEY_MAP,
    KEYS_DIR,
    REPO_DIR,
    THRESHOLDS,
)

if __name__ == '__main__':

    # Create repository instance
    repo = Repository(
        app_name=APP_NAME,
        app_version_attr="AppUpdations.__version__",
        repo_dir=REPO_DIR,
        keys_dir=KEYS_DIR,
        key_map=KEY_MAP,
        expiration_days=EXPIRATION_DAYS,
        encrypted_keys=ENCRYPTED_KEYS,
        thresholds=THRESHOLDS,
    )

    # Save configuration (JSON file)
    repo.save_config()

    # Initialize repository (creates keys and root metadata, if necessary)
    repo.initialize()

    # print(repo.app_version)