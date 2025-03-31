import os
from dotenv import load_dotenv
from duckdb_handler import log_message, get_chat_history
import openai

# Load environment variables
load_dotenv()

# Ensure API key is available
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("Missing OpenAI API key. Please set OPENAI_API_KEY in your .env file.")

# Updated system prompt for Global Risk Insights Chatbot
SYSTEM_PROMPT = (
    "You are a helpful assistant designed to support users with global risk and international business insights. "
    "Provide clear, concise, and friendly responses based on user queries about risk and market trends."
)

def generate_response(user_input: str) -> str:
    # Prepare the prompt with context
    chat_history = get_chat_history()
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    # Use the last 5 interactions for context
    for row in chat_history[-5:]:
        sender, message = row[1], row[2]
        role = "user" if sender == "user" else "assistant"
        messages.append({"role": role, "content": message})
    
    messages.append({"role": "user", "content": user_input})
    
    # Call OpenAI API to generate a response
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            temperature=0.7
        )
        reply = response.choices[0].message.content.strip()
    except Exception as e:
        reply = f"Oops! Something went wrong: {str(e)}"
    
    return reply
from duckdb_handler import clear_chat_history
clear_chat_history()
def chat():
    print("GlobalRiskBot: Hello! How can I assist you with global risk insights today?\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("GlobalRiskBot: Goodbye!")
            break
        
        log_message("user", user_input)
        response = generate_response(user_input)
        log_message("bot", response)
        print(f"GlobalRiskBot: {response}\n")

if __name__ == "__main__":
    chat()
