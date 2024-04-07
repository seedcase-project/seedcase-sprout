def path_raw_storage() -> str:
    raw_folder = f"{PERSISTENT_STORAGE_PATH}/raw"
    if not os.path.exists(raw_folder):
        os.makedirs(raw_folder)
    return raw_folder
