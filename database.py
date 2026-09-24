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

    # Get URL
    def get_url(self,short_code):
        db_connection = sqlite3.connect("urls.db")
        cursor = db_connection.cursor()
        cursor.execute("""SELECT original_url FROM urls WHERE short_code = ?""",(short_code,))
        response = cursor.fetchone()
        db_connection.close()
        if response is None:
            return None

        return response[0]
    