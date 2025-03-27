import duckdb

# Persistent local database file (can change path if needed)
DB_PATH = "data/conversations.db"

# Establish a connection to the DuckDB database file
con = duckdb.connect(database=DB_PATH)

# Ensure the table exists
con.execute("""
    CREATE TABLE IF NOT EXISTS conversations (
        id INTEGER AUTOINCREMENT,
        sender TEXT,
        message TEXT
    );
""")

def log_message(sender: str, message: str):
    """Logs a message (user or bot) to the DuckDB database."""
    con.execute(
        "INSERT INTO conversations (sender, message) VALUES (?, ?);",
        (sender, message)
    )

def get_chat_history():
    """Retrieves all conversation history from the database."""
    return con.execute(
        "SELECT * FROM conversations ORDER BY id ASC;"
    ).fetchall()
