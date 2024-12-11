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

# cursor.execute("INSERT INTO Users (username, email, age) VALUES (?, ?, ?)", ("newuser", "ex@gmail.com", "28"))
for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}", f"example{i}@gmail.com", i * 10, 1000))

cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2")

#cursor.execute("DELETE FROM Users Where username = ?", ("newuser",))
# cursor.execute("SELECT * FROM Users")
# SELECT FROM WHERE GROUP BY HAVING ORDER BY

cursor.execute("DELETE FROM Users WHERE id % 3 = 1")

# cursor.execute("SELECT age FROM Users GROUP BY AGE")
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user3}')
connection.commit()
connection.close()