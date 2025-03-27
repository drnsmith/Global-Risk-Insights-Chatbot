import duckdb
import openai
import os
from dotenv import load_dotenv
from IPython.display import display
import ipywidgets as widgets

# Load environment variables (optional)
load_dotenv()

# OpenAI API key (store this in Colab’s secret or manually)
openai.api_key = os.getenv("OPENAI_API_KEY", "sk-...")

# Connect to a DuckDB file (can be mounted from Google Drive or loaded from URL)
DB_PATH = "/content/conversations.db"  # adjust if you mount GDrive
con = duckdb.connect(database=DB_PATH)

# Ensure table exists
con.execute("""
    CREATE TABLE IF NOT EXISTS conversations (
        id INTEGER AUTOINCREMENT,
        sender TEXT,
        message TEXT
    );
""")

# Chat UI widgets
input_box = widgets.Text(
    placeholder='Ask your question...',
    description='You:',
    layout=widgets.Layout(width='95%')
)
output_box = widgets.Output()

display(input_box, output_box)

SYSTEM_PROMPT = (
    "You are a helpful assistant designed to support customers of a retail store. "
    "Provide clear, friendly responses based on user queries."
)

def get_chat_history():
    return con.execute(
        "SELECT * FROM conversations ORDER BY id ASC;"
    ).fetchall()

def log_message(sender, message):
    con.execute(
        "INSERT INTO conversations (sender, message) VALUES (?, ?);",
        (sender, message)
    )

def generate_response(user_input):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    # Load last 5 messages for context
    for row in get_chat_history()[-5:]:
        sender, msg = row[1], row[2]
        role = "user" if sender == "user" else "assistant"
        messages.append({"role": role, "content": msg})

    messages.append({"role": "user", "content": user_input})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            temperature=0.7
        )
        reply = response.choices[0].message.content.strip()
    except Exception as e:
        reply = f"Error: {str(e)}"
    
    return reply

# Event handler
def on_submit(change):
    user_input = input_box.value
    input_box.value = ''
    if not user_input.strip():
        return

    log_message("user", user_input)
    response = generate_response(user_input)
    log_message("bot", response)

    with output_box:
        print(f"You: {user_input}")
        print(f"RetailBot: {response}\n")

input_box.on_submit(on_submit)
