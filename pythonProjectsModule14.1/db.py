import sqlite3
import random

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}", f"example{i}@gmail.com", i * 10, 1000))

cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2")
cursor.execute("DELETE FROM Users WHERE id % 3 = 1")
cursor.execute("DELETE FROM Users WHERE id == 6")

connection.commit()
connection.close()
