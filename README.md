# Global Risk Insights Chatbot with Embedded Analytics
![Project Banner](./assets/image.png)

A lightweight, AI-powered chatbot designed to support international business and risk analysis. This bot connects to a DuckDB database to answer natural language queries about global risk data and international business metrics. Built using **LangChain and OpenAI's GPT** models, it offers a flexible interface to explore structured datasets and derive actionable insights.

## Overview

In today’s global environment, understanding risk is critical. This project leverages my expertise in international business and risk management to build a chatbot that helps users:
- Query structured risk data (e.g., institutional, regulatory, operational metrics).
- Gain instant insights on global market trends and risk exposures.
- Support strategic decision-making with natural language queries and AI-enhanced responses.

### 🚀 Features

- 🤖 **AI Chatbot**: Ask risk-related questions in plain English — get GPT-generated responses, backed by historical data.
- 📊 **Risk Insights Dashboard**: Interactive visualisation of global risk scores, trends, and regions.
- 🌐 **World Bank Indicators**: Explore country-level economic indicators from 1991–2020 using curated World Bank data.
- 📁 **Modular Codebase**: Fully extensible with LangChain, DuckDB, and Streamlit.
- 📦 **Single-File Local Database**: All chat logs and data queries are stored via DuckDB.

---
## 🧱 Tech Stack

- **Python 3.11+**
- [Streamlit](https://streamlit.io/)
- [DuckDB](https://duckdb.org/)
- [OpenAI GPT-4](https://platform.openai.com/)
- `pandas`, `plotly`, `dotenv`
---

### 📦 Installation

```bash
# 1. Clone the repo
git clone https://github.com/your-username/global-risk-insights-chatbot.git
cd global-risk-insights-chatbot

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your OpenAI API key
echo "OPENAI_API_KEY=your-key-here" > .env
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
### Run the App
```
streamlit run app/app.py
```
### 🧭 Navigation

Once the app launches, use the sidebar to switch between:
	•	🤖 Chatbot: Ask about global risks, institutions, policies.
	•	📊 Risk Dashboard: Time series of global risk scores by region.
	•	🌐 World Bank: Select indicators, countries, and date ranges to visualise investment, trade, GDP, and more.

#### Contributing

Contributions are welcome! Please fork the repository and open a pull request with your enhancements. For major changes, please open an issue first to discuss what you would like to change.

#### License
MIT
