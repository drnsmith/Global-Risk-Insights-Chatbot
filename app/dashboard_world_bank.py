import pandas as pd
import streamlit as st
import plotly.express as px

# ---------------------------
# CONFIG
# ---------------------------
st.set_page_config(
    page_title="World Bank Investment Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🌐 World Bank Economic Indicators Dashboard")

# ---------------------------
# LOAD DATA
# ---------------------------
@st.cache_data(show_spinner=True)
def load_data():
    df = pd.read_csv("data/world_bank_data_pivoted.csv")
    df["date"] = pd.to_numeric(df["date"], errors="coerce")
    return df

df = load_data()

# ---------------------------
# SIDEBAR FILTERS
# ---------------------------
with st.sidebar:
    st.header("📊 Filter Options")

    # Country filter
    countries = sorted(df["country"].dropna().unique())
    selected_countries = st.multiselect("Select Countries", countries, default=countries[:1])

    # Indicator filter
    numeric_cols = df.select_dtypes(include=["float", "int"]).columns.tolist()
    exclude = ["date"]  # we always keep 'date'
    indicators = [col for col in numeric_cols if col not in exclude]
    selected_indicator = st.selectbox("Select Indicator", indicators)

    # Year range slider
    min_year = int(df["date"].min())
    max_year = int(df["date"].max())
    selected_years = st.slider("Select Year Range", min_year, max_year, (min_year, max_year))

# ---------------------------
# FILTERED DATA
# ---------------------------
filtered_df = df[
    (df["country"].isin(selected_countries)) &
    (df["date"].between(*selected_years))
]

# Drop rows with missing values for selected indicator
plot_df = filtered_df.dropna(subset=[selected_indicator])

# ---------------------------
# PLOT
# ---------------------------
if plot_df.empty:
    st.warning("No data available for this selection.")
else:
    fig = px.line(
        plot_df,
        x="date",
        y=selected_indicator,
        color="country",
        markers=True,
        title=f"{selected_indicator} from {selected_years[0]} to {selected_years[1]}",
        labels={"date": "Year", selected_indicator: selected_indicator},
        template="plotly_white"
    )
    st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# RAW DATA & EXPORT
# ---------------------------
with st.expander("📄 View Filtered Data"):
    st.dataframe(plot_df, use_container_width=True)
    csv = plot_df.to_csv(index=False).encode("utf-8")
    st.download_button("Download CSV", csv, "filtered_world_bank_data.csv", "text/csv")
