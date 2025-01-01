import sqlite3
import random
from texts import *

def initiate_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL)
        ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
            id INEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL)
        ''')
    conn.commit()
    conn.close()

def add_user(username, email, age):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Users (username, email, age, balance) 
        VALUES (?, ?, ?, ?);
        ''', (username, email, age, 1000))  # Баланс по умолчанию равен 1000
    conn.commit()
    cursor.close()
    conn.close()

def is_included(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM Users WHERE username = ?', (username,))
    result = cursor.fetchone()
    conn.close()
    return result == 1

def get_all_products():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    conn.commit()
    conn.close()
    return products

def insert_products(title, description, price):
    conn3 = sqlite3.connect('database.db')
    cursor3 = conn3.cursor()
    insert = 'INSERT INTO Products (title, description, price) VALUES (?, ?, ?);'
    cursor3.execute(insert, (title, description, price))
    conn3.commit()
    conn3.close()

def data():
    sample_products = [
        ("Витамин D3 500 МЕ", vitamin_D3, 873),
        ("Креатин", creatine, 1800),
        ("Протеин", protein, 3000),
        ("БЦА", bcaa, 1000)
    ]
    for product in sample_products:
        insert_products(* product)



if __name__ == "__main__":
    data()
    products = get_all_products()
    print(products)
