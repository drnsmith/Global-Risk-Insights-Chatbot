import os
import duckdb

# Define the path for persistent DuckDB storage
DB_PATH = "data/conversations.db"

# Ensure the data directory exists
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

# Connect to the DuckDB database file
con = duckdb.connect(database=DB_PATH)

# Create the conversations table if it doesn't exist
con.execute("""
    CREATE TABLE IF NOT EXISTS conversations (
        id INTEGER,
        role TEXT,
        message TEXT
    );
""")

def get_chat_history(limit=5):
    """
    Retrieves the last 'limit' messages from the conversation history in chronological order.
    """
    try:
        rows = con.execute(
            "SELECT id, role, message FROM conversations ORDER BY id DESC LIMIT ?",
            (limit,)
        ).fetchall()
        return rows[::-1]  # Return in chronological order
    except Exception as e:
        print(f"[DB ERROR] Failed to retrieve chat history: {e}")
        return []

def log_message(role: str, message: str):
    """
    Logs a new message to the database with the next incremental ID.
    """
    try:
        last_id = con.execute("SELECT COALESCE(MAX(id), 0) FROM conversations").fetchone()[0]
        next_id = last_id + 1
        con.execute(
            "INSERT INTO conversations (id, role, message) VALUES (?, ?, ?)",
            (next_id, role.lower(), message)
        )
    except Exception as e:
        print(f"[DB ERROR] Failed to log message: {e}")

def clear_chat_history():
    """
    Clears all records from the conversations table.
    """
    try:
        con.execute("DELETE FROM conversations;")
    except Exception as e:
        print(f"[DB ERROR] Failed to clear chat history: {e}")
