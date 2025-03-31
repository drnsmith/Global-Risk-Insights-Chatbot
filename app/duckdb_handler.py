import duckdb

# Connect to DuckDB in-memory (change ':memory:' to a file path for persistence)
con = duckdb.connect(database=':memory:')

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
    Retrieve the last 'limit' conversation entries from the DuckDB table.
    Returns the records in chronological order.
    """
    result = con.execute(
        f"SELECT * FROM conversations ORDER BY id DESC LIMIT {limit}"
    ).fetchall()
    # Reverse to return messages in the order they were added
    return result[::-1]

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
