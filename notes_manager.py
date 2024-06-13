import sqlite3

# Create database and table if not exists
db2 = sqlite3.connect('notestest2.db')
cursor = db2.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS notes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    user_login TEXT,
    note_text TEXT,
    pos_X INTEGER,
    pos_y INTEGER,
    state TEXT DEFAULT 'active'
)
''')
db2.commit()
db2.close()


# Create connection function
def create_connection():
    conn = sqlite3.connect('notestest2.db')
    return conn


# Function to add a note to the database
def add_note_to_db(user_login, note_text, pos_x, pos_y, state='active'):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO notes (user_login, note_text, pos_x, pos_y, state) VALUES (?, ?, ?, ?, ?)",
                (user_login, note_text, pos_x, pos_y, state))
    conn.commit()
    conn.close()


# Function to delete a note from the database
def delete_note_from_db(user_login, note_text):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("UPDATE notes SET state='deleted' WHERE user_login = ? AND note_text = ?", (user_login, note_text))
    conn.commit()
    conn.close()


def get_notes_from_db(user_login, state='active'):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT note_text, pos_x, pos_y, ID FROM notes WHERE user_login = ? AND state = ?", (user_login, state))
    notes = cur.fetchall()
    conn.close()
    return notes



def get_archived_notes(user_login):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT note_text FROM notes WHERE user_login = ? AND state = 'archived'", (user_login,))
    notes = cur.fetchall()
    conn.close()
    return [note[0] for note in notes]


def update_note_state(user_login, note_text, state):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("UPDATE notes SET state=? WHERE user_login=? AND note_text=?", (state, user_login, note_text))
    conn.commit()
    conn.close()