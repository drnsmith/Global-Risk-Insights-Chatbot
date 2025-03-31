import duckdb

# Define the path for persistence
DB_PATH = "data/conversations.db"

# Connect to DuckDB using the persistent file
con = duckdb.connect(database=DB_PATH)

# Create the conversations table without AUTOINCREMENT
con.execute("""
    CREATE TABLE IF NOT EXISTS conversations (
        id INTEGER,
        role TEXT,
        message TEXT
    );
""")

def get_chat_history(limit=5):
    """
    Retrieve the last 'limit' conversation entries from the DuckDB table.
    Returns records in chronological order.
    """
    result = con.execute(
        f"SELECT * FROM conversations ORDER BY id DESC LIMIT {limit}"
    ).fetchall()
    return result[::-1]  # Reverse to get chronological order

def log_message(role: str, message: str):
    """
    Log a message to the conversations table.
    'role' should be either 'user' or 'assistant'.
    """
    last_id = con.execute("SELECT MAX(id) FROM conversations").fetchone()[0]
    next_id = 1 if last_id is None else last_id + 1
    con.execute(
        "INSERT INTO conversations (id, role, message) VALUES (?, ?, ?)",
        (next_id, role.lower(), message)
    )

def clear_chat_history():
    con.execute("DELETE FROM conversations;")
