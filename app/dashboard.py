import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Global Risk Insights Dashboard")

@st.cache_data
def load_data():
    try:
        # Attempt to load your global risk data from CSV.
        data = pd.read_csv("data/global_risk_data.csv", parse_dates=["date"])
    except Exception as e:
        # If the CSV is not available, create sample data.
        st.warning("Global risk data not found. Using sample data.")
        dates = pd.date_range(start="2020-01-01", periods=100, freq='W')
        risk_scores = pd.Series(range(100)) % 10 + 50  # Sample risk scores
        data = pd.DataFrame({"date": dates, "risk_score": risk_scores})
    return data

data = load_data()

# Display a key metric: the average global risk score.
avg_risk = data["risk_score"].mean()
st.metric("Average Global Risk Score", round(avg_risk, 2))

# Display a line chart showing risk trends over time.
fig = px.line(data, x="date", y="risk_score", title="Risk Trend Over Time")
st.plotly_chart(fig)

# (Optional) Additional filters or insights can go here.
