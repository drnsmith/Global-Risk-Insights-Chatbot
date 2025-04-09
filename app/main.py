import os
import openai
from dotenv import load_dotenv
from duckdb_handler import log_message, get_chat_history, clear_chat_history

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("Missing OpenAI API key. Please set OPENAI_API_KEY in your .env file.")

# System prompt to guide the assistant's behaviour
SYSTEM_PROMPT = (
    "You are a helpful assistant designed to support users with global risk and international business insights. "
    "Provide clear, concise, and friendly responses based on user queries about risk and market trends."
)

def build_prompt(user_input: str) -> list:
    """
    Constructs a prompt for OpenAI API including system message and chat history.
    """
    chat_history = get_chat_history()[-5:]  # Use last 5 interactions
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    for sender, message in [(row[1], row[2]) for row in chat_history]:
        role = "user" if sender == "user" else "assistant"
        messages.append({"role": role, "content": message})
    
    messages.append({"role": "user", "content": user_input})
    return messages

def get_bot_reply(prompt: list) -> str:
    """
    Calls OpenAI's API to generate a response from the prompt.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=prompt,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return "Sorry, I encountered an error while processing your request. Please try again."

def chat():
    """
    Starts a CLI chat session with the bot.
    """
    print("GlobalRiskBot: Hello! How can I assist you with global risk insights today?\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("GlobalRiskBot: Goodbye!")
            break

        log_message("user", user_input)
        prompt = build_prompt(user_input)
        reply = get_bot_reply(prompt)
        log_message("bot", reply)
        print(f"GlobalRiskBot: {reply}\n")

if __name__ == "__main__":
    # Optional: uncomment if you want to start fresh each time
    # clear_chat_history()
    chat()
