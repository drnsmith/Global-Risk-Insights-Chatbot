# Global Risk Insights Chatbot with Embedded Analytics
![Project Banner](./assets/image.png)

A lightweight, AI-powered chatbot designed to support international business and risk analysis. This bot connects to a DuckDB database to answer natural language queries about global risk data and international business metrics. Built using **LangChain and OpenAI's GPT** models, it offers a flexible interface to explore structured datasets and derive actionable insights.

## Overview

In today’s global environment, understanding risk is critical. This project leverages my expertise in international business and risk management to build a chatbot that helps users:
- Query structured risk data (e.g., institutional, regulatory, operational metrics).
- Gain instant insights on global market trends and risk exposures.
- Support strategic decision-making with natural language queries and AI-enhanced responses.

### Features

- **Natural Language Queries:** Convert everyday language into SQL queries against a DuckDB-backed dataset.
- **Instant Insights:** Receive real-time responses powered by OpenAI GPT models.
- **Modular Codebase:** Clean separation between logic, data access, and interface layers.
- **Flexible Deployment:** Option to use a lightweight Streamlit interface for an interactive frontend.
- **International Focus:** Tailored to highlight international business risk and institutional data.

### Tech Stack

- **Python**
- **LangChain** – for prompt chaining and conversational flows.
- **DuckDB** – as the local, lightweight SQL engine for structured data.
- **OpenAI GPT** – for generating dynamic responses.
- **Streamlit (Optional)** – for building an interactive UI.


### Quickstart

1. **Clone the Repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/global-risk-insights-chatbot.git
   cd global-risk-insights-chatbot


2. **Install Dependencies**
```bas
pip install -r requirements.txt
```

3. **Configure Environment Variables**
Create a .env file in the root directory:
```bash
OPENAI_API_KEY=your-api-key
```
Make sure to add .env to your .gitignore to keep your keys secure.

4. **Run the Chatbot**
```bash
python app/main.py
```

### Project Structure
```bash
global-risk-insights-chatbot/
├── app/
│   ├── main.py
│   ├── chatbot_main.py
│   ├── chatbot_logic.py
│   ├── duckdb_handler.py
│   ├── dashboard.py
│   ├── dashboard_world_bank.py
├── data/
│   ├── world_bank.duckdb
│   ├── chat_history.duckdb
├── scripts/
│   ├── transparency_scraper.py
│   ├── world_bank_cleaning.py (if needed)
├── assets/
│   └── (any visuals or docs)
├── .env
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
```
### Future Enhancements
	•	Advanced AI Capabilities:
	•	Implement contextual memory and multi-turn conversation support.
	•	Integrate dynamic summarisation for long or complex responses.
	•	Interactive Frontend:
	•	Build a user-friendly Streamlit dashboard for visualising data insights alongside chatbot interactions.
	•	Expanded Data Sources:
	•	Connect to additional datasets on international business risk.
	•	Incorporate live APIs for up-to-date global risk metrics.
	•	Enhanced Query Mapping:
	•	Improve natural language to SQL query conversion using advanced prompt engineering or fine-tuned models.

#### Contributing

Contributions are welcome! Please fork the repository and open a pull request with your enhancements. For major changes, please open an issue first to discuss what you would like to change.

#### License
MIT
