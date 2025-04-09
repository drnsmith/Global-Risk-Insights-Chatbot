import os
from fastapi import FastAPI
from pydantic import BaseModel
from chatbot_logic import generate_response
from duckdb_handler import log_message, get_chat_history
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

class UserInput(BaseModel):
    message: str

@app.post("/chat")
def chat(user_input: UserInput):
    user_msg = user_input.message

    # Log user input
    log_message("user", user_msg)

    # Generate bot response
    bot_msg = generate_response(user_msg)

    # Log bot response
    log_message("bot", bot_msg)

    return {"response": bot_msg}

@app.get("/history")
def get_conversation():
    history = get_chat_history()
    formatted = [{"role": row[1], "message": row[2]} for row in history]
    return {"conversations": formatted}
