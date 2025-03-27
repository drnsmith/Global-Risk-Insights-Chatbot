import duckdb
from fastapi import FastAPI, Request
from pydantic import BaseModel
from chatbot_logic import generate_response

app = FastAPI()

# Sample DuckDB in-memory database
con = duckdb.connect(database=':memory:')
con.execute("CREATE TABLE conversations (id INTEGER, user_input TEXT, bot_response TEXT);")

class UserInput(BaseModel):
    message: str

@app.post("/chat")
def chat(user_input: UserInput):
    user_msg = user_input.message
    bot_msg = generate_response(user_msg)

    # Save to database
    con.execute("INSERT INTO conversations VALUES (?, ?, ?);", (1, user_msg, bot_msg))

    return {"response": bot_msg}

@app.get("/history")
def get_conversation():
    result = con.execute("SELECT * FROM conversations;").fetchall()
    return {"conversations": result}
