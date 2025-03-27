def generate_response(user_message: str) -> str:
    """
    Generates a basic rule-based chatbot response.
    Replace with LLM or other intelligent systems as needed.
    """
    user_message = user_message.lower().strip()

    if "hello" in user_message or "hi" in user_message:
        return "Hello! How can I assist you today?"
    elif "help" in user_message:
        return "Sure, I'm here to help. Could you please provide more details?"
    elif "bye" in user_message:
        return "Goodbye! Have a great day."
    else:
        return "That's interesting. Can you tell me more?"
