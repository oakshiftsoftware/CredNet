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
    
    def insert_record(self, table_name: str, record: dict):
        if self.conn is None:
            raise Exception("Database connection is not established.")
        
        columns_str = ", ".join(record.keys())
        placeholders_str = ", ".join(["?" for _ in record])
        insert_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders_str})"
        self.cursor.execute(insert_query, tuple(record.values()))
        self.conn.commit()
    
    def fetch_records(self, table_name: str, conditions: dict = None):
        if self.conn is None:
            raise Exception("Database connection is not established.")
        
        query = f"SELECT * FROM {table_name}"
        if conditions:
            # Example: conditions = {"column1": "value1", "column2": "value2"}
            conditions_str = " AND ".join([f"{col} = ?" for col in conditions.keys()])
            query += f" WHERE {conditions_str}"
            self.cursor.execute(query, tuple(conditions.values()))
        else:
            self.cursor.execute(query)
        
        return self.cursor.fetchall()


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
