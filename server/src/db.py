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

    # Create a revoked_tokens table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS revoked_tokens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            token TEXT UNIQUE
        )
    ''')

    conn.commit()
    conn.close()

def revoke_refresh_token(refresh_token):
    conn = sqlite3.connect('../database.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO revoked_tokens (token) VALUES (?)
    ''', (refresh_token,))

    conn.commit()
    conn.close()

def is_refresh_token_revoked(refresh_token):
    conn = sqlite3.connect('../database.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT EXISTS (SELECT 1 FROM revoked_tokens WHERE token=?)
    ''', (refresh_token,))

    result = cursor.fetchone()
    conn.close()

    return result[0] == 1

def register_user(username, email, password):
    conn = sqlite3.connect('../database.db')
    cursor = conn.cursor()

    try:
        # Hash the password
        hashed_password = bcrypt.hash(password)

        # Insert the user data into the database
        cursor.execute('''
            INSERT INTO users (username, email, password)
            VALUES (?, ?, ?)
        ''', (username, email, hashed_password))

        conn.commit()
        conn.close()
    except sqlite3.IntegrityError as e:
        conn.close()
        error_message = str(e)

        if "UNIQUE constraint failed: users.username" in error_message:
            return "Username already in use."
        elif "UNIQUE constraint failed: users.email" in error_message:
            return "Email already in use."
    
    return "User registered successfully."

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

def is_email_registered(email):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id FROM users WHERE email=?', (email,))
    user_id = cursor.fetchone()

    conn.close()

    return user_id is not None

def get_user_id_by_email(email):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id FROM users WHERE email=?', (email,))
    user_id = cursor.fetchone()

    conn.close()

    return user_id[0] if user_id else None

def update_user_password(user_id, new_password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    hashed_password = bcrypt.hash(new_password)

    cursor.execute('UPDATE users SET password=? WHERE id=?', (hashed_password, user_id))

    conn.commit()
    conn.close()