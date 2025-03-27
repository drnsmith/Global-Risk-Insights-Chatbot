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

SYSTEM_PROMPT = (
    "You are a helpful assistant designed to support customers of a retail store. "
    "Provide clear, friendly responses based on user queries."
)

def generate_response(user_input: str) -> str:
    # Prepare the prompt with context
    chat_history = get_chat_history()
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    for row in chat_history[-5:]:  # Use last 5 interactions for brevity
        sender, message = row[1], row[2]
        role = "user" if sender == "user" else "assistant"
        messages.append({"role": role, "content": message})
    
    messages.append({"role": "user", "content": user_input})
    
    # Call OpenAI API
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

def chat():
    print("RetailBot: Hello! How can I assist you today?\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("RetailBot: Goodbye!")
            break
        
        log_message("user", user_input)
        response = generate_response(user_input)
        log_message("bot", response)
        print(f"RetailBot: {response}\n")

if __name__ == "__main__":
    chat()
