# Imports
from source.config import AppConfig
from source.dbm import Database, DatabaseManager


class CredNetMaster:
    def __init__(self):
        self.config = AppConfig()
        self.db_manager = DatabaseManager()
        self.db_manager.add_db("crednet", self.config.cred_db_path)


if __name__ == "__main__":
    pass
