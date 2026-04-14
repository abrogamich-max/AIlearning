import sqlite3

def init_db():

    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()


    cursor.execute(''' CREATE TABLE IF NOT EXISTS history (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_name TEXT,
                        user_message TEXT,
                        ai_response TEXT
                   )
                ''')
    
    conn.commit()
    conn.close()


def save_message(name, user_msg, ai_msg):
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO history (user_name, user_message, ai_response) VALUES (?, ?, ?)',
        (name, user_msg, ai_msg)
    )
    conn.commit()
    conn.close()



def get_history(name):
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()

    cursor.execute(
        'SELECT user_message, ai_response FROM history WHERE user_name = ? ORDER BY id DESC LIMIT 5',
        (name,)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows