import os

from config.settings import PERSISTENT_STORAGE_PATH


def path_raw_storage() -> str:
    raw_folder = f"{PERSISTENT_STORAGE_PATH}/raw"
    if not os.path.exists(raw_folder):
        os.makedirs(raw_folder)
    return raw_folder


def path_databases() -> str:
    db_folder = f"{PERSISTENT_STORAGE_PATH}/databases"
    if not os.path.exists(db_folder):
        os.makedirs(db_folder)
    return db_folder
