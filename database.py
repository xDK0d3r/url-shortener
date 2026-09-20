# This file handle's database opreations.

# import SQLite Module
import sqlite3

# DB Class
class Database :
    def __init__(self):
        self.db_connection = sqlite3.connect("urls.db")
        self.cursor = self.db_connection.cursor()

    # DB initialize
    def db_initialize(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS urls(
        short_code TEXT PRIMARY KEY,
        original_url TEXT NOT NULL)""")

        self.db_connection.commit()

