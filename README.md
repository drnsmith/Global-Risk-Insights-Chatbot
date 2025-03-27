# AI Retail Chatbot with Embedded Analytics
![Project Banner](./assets/image.png)

A lightweight, AI-powered chatbot that connects to **DuckDB** and answers questions about retail data. Built using **LangChain and OpenAI's GPT** models, this chatbot allows you to run natural language queries on structured retail datasets.

## Features

- Query DuckDB using natural language
- Instant insights from structured retail data
- Lightweight and fast — ideal for rapid demos or internal tools
- Modular codebase with clear separation of logic, data, and interface

## Tech Stack

- **Python**
- **LangChain**
- **DuckDB**
- **OpenAI GPT**
- **Streamlit** (optional interface)

## Quickstart

1. Clone the repo  
   `git clone https://github.com/YOUR-USERNAME/retail-insights-chatbot.git`

2. Install dependencies  
   `pip install -r requirements.txt`

3. Set your OpenAI key in a `.env` file:  
   `OPENAI_API_KEY=your-api-key`

4. Run the chatbot:  
   `python app/main.py`

## Future Ideas

- Add knowledge graph integration  
- Connect to live retail APIs  
- Use Streamlit UI for a friendly frontend  
- Plug in summarisation and visualisation modules

---

Let me know once you’ve pasted that in and saved it.  
Then we’ll finish with **Step 9: `.env` setup and .gitignore safety check.**

## Dataset
Using a public retail dataset from Kaggle. [Link to source](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store)

## License
MIT
