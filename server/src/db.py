import sqlite3
from passlib.hash import bcrypt

def initialize_database():
    conn = sqlite3.connect('../database.db')
    cursor = conn.cursor()

    # Create a users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def register_user(username, email, password):
    conn = sqlite3.connect('../database.db')
    cursor = conn.cursor()

    # Hash the password
    hashed_password = bcrypt.hash(password)

    # Insert the user data into the database
    cursor.execute('''
        INSERT INTO users (username, email, password)
        VALUES (?, ?, ?)
    ''', (username, email, hashed_password))

    conn.commit()
    conn.close()

def verify_user(username, password):
    conn = sqlite3.connect('../database.db')
    cursor = conn.cursor()

    # Retrieve the user data from the database
    cursor.execute('''
        SELECT id, username, password FROM users WHERE username=?
    ''', (username,))
    user_data = cursor.fetchone()

    if user_data:
        user_id, _, hashed_password = user_data
        if bcrypt.verify(password, hashed_password):
            conn.close()
            return user_id

    conn.close()
    return None
