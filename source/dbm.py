# Imports
import sqlite3


class Database:
    db_path = None
    conn = None
    cursor = None

    def __init__(self, db_path: str):
        self.db_path = db_path
    
    def connect(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
    
    def disconnect(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None
    
    def create_table(self, table_name: str, columns: dict):
        if self.conn is None:
            raise Exception("Database connection is not established.")
        
        columns_str = ", ".join([f"{col} {dtype}" for col, dtype in columns.items()])
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})"
        self.cursor.execute(create_table_query)
        self.conn.commit()


class DatabaseManager:
    db_list = dict()

    def __init__(self):
        pass

    def add_db(self, name: str, db_path: str):
        if name not in self.db_list:
            db = Database(db_path)
            self.db_list[name] = db


if __name__ == "__main__":
    pass
