import sqlite3

# Initialize the database
conn = sqlite3.connect('user_data.db')
c = conn.cursor()

# Create tables for users and history
c.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                action TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )''')

conn.commit()
conn.close()

def register_user(username, password):
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists. Please choose a different username.")
    finally:
        conn.close()

def login_user(username, password):
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    conn.close()
    if user:
        print("Login successful!")
        return user[0]  # Return user ID
    else:
        print("Invalid username or password.")
        return None

def save_history(user_id, action):
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO history (user_id, action) VALUES (?, ?)", (user_id, action))
    conn.commit()
    conn.close()

def view_history(user_id):
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute("SELECT action, timestamp FROM history WHERE user_id = ? ORDER BY timestamp DESC", (user_id,))
    history = c.fetchall()
    conn.close()
    return history