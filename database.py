# This file handle's database opreations.

# import SQLite Module
import sqlite3

# DB Class
class Database :

    # DB initialize
    def db_initialize(self):
        db_connection = sqlite3.connect("urls.db")
        cursor = db_connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS urls(
        short_code TEXT PRIMARY KEY,
        original_url TEXT NOT NULL)""")

        db_connection.commit()
        db_connection.close()

    # Add URL
    def add_url(self,short_code,original_url):
        db_connection = sqlite3.connect("urls.db")
        cursor = db_connection.cursor()
        cursor.execute("""INSERT INTO urls (short_code,original_url) VALUES (?,?)""",
                            (short_code,original_url))
        db_connection.commit()
        db_connection.close()