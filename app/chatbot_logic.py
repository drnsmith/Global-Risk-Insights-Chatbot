import os
import openai
from dotenv import load_dotenv
from duckdb_handler import get_chat_history

# Load environment variables
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("Missing OpenAI API key. Please set OPENAI_API_KEY in your .env file.")

# System prompt to guide the assistant's behaviour
SYSTEM_PROMPT = (
    "You are a helpful assistant designed to support users with global risk and international business insights. "
    "Provide clear, concise, and friendly responses based on user queries about risk and market trends."
)

def generate_response(user_input: str) -> str:
    """
    Generates a response using OpenAI's GPT-4 model based on user input and recent chat history.
    """

    # Get the last 5 interactions from chat history
    chat_history = get_chat_history()[-5:]
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    for sender, message in [(row[1], row[2]) for row in chat_history]:
        role = "user" if sender == "user" else "assistant"
        messages.append({"role": role, "content": message})

    messages.append({"role": "user", "content": user_input})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return "Sorry, I'm having trouble generating a response right now. Please try again."
