
import duckdb
import os
from datetime import datetime

# Set up or connect to local DuckDB file
DB_FILE = "chat_history.duckdb"
con = duckdb.connect(DB_FILE)

# Create a table for storing chats
def setup_db():
    con.execute("""
        CREATE TABLE IF NOT EXISTS chat_log (
            timestamp TIMESTAMP,
            sender TEXT,
            message TEXT
        )
    """)

# Add a message to the log
def log_message(sender: str, message: str):
    timestamp = datetime.now()
    con.execute("INSERT INTO chat_log VALUES (?, ?, ?)", (timestamp, sender, message))

# Retrieve entire chat history
def get_chat_history():
    result = con.execute("SELECT * FROM chat_log ORDER BY timestamp").fetchall()
    return result

# Call setup_db once at import
setup_db()
