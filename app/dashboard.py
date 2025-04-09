import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(
    page_title="Global Risk Insights",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🌍 Global Risk Insights Dashboard")

@st.cache_data(show_spinner=True)
def load_data():
    try:
        path = "data/global_risk_data.csv"
        if not os.path.exists(path):
            raise FileNotFoundError

        data = pd.read_csv(path, parse_dates=["date"])
    except Exception:
        st.warning("⚠️ Global risk data not found. Using sample data.")
        dates = pd.date_range(start="2020-01-01", periods=100, freq='W')
        risk_scores = pd.Series(range(100)) % 10 + 50
        data = pd.DataFrame({"date": dates, "risk_score": risk_scores, "region": "Global"})
    return data

# Load and display data
data = load_data()

# Optional region filter (future-proofing for when you have more granular data)
if "region" in data.columns:
    regions = data["region"].unique()
    selected_region = st.sidebar.selectbox("Select Region", sorted(regions))
    data = data[data["region"] == selected_region]

# Metrics
col1, col2 = st.columns(2)
with col1:
    avg_risk = round(data["risk_score"].mean(), 2)
    st.metric("📊 Avg Global Risk Score", avg_risk)

with col2:
    latest_score = data.sort_values("date").iloc[-1]["risk_score"]
    st.metric("🕒 Latest Risk Score", latest_score)

# Trend Chart
st.markdown("### 📈 Risk Score Trend Over Time")
fig = px.line(
    data,
    x="date",
    y="risk_score",
    title="Risk Score Trend",
    labels={"risk_score": "Risk Score", "date": "Date"},
    template="plotly_white"
)
st.plotly_chart(fig, use_container_width=True)

# Optional: add export/download or raw data viewer
with st.expander("📄 View Raw Data"):
    st.dataframe(data, use_container_width=True)
