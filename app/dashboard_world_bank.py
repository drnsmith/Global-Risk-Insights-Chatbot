import wbdata
import pandas as pd
import streamlit as st
import plotly.express as px

# Example: specifying a range of years as strings
START_YEAR = 2010
END_YEAR = 2020

# Indicators to fetch
indicators = {
    "GB.XPD.RSDV.GD.ZS": "R&D Expenditure (% of GDP)",
    "SE.XPD.TOTL.GD.ZS": "Education Expenditure (% of GDP)",
    "NE.GDI.TOTL.ZS": "Gross Fixed Capital Formation (% of GDP)",
    # If the roads indicator is unavailable, it may return empty data
    "IS.ROD.PAVE.K2": "Length of Paved Roads (km)"
}

@st.cache_data
def load_world_bank_data():
    try:
        # Provide a date range as strings, e.g. ("2010", "2020")
        df = wbdata.get_dataframe(indicators, date=(str(START_YEAR), str(END_YEAR)))
        # Reset index to have 'country' and 'date' columns
        df.reset_index(inplace=True)
        # Convert the 'date' column to numeric (assuming it returns a year as a string)
        df["date"] = pd.to_numeric(df["date"])
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        df = pd.DataFrame()
    return df

def main():
    st.title("World Bank Global Investment & Infrastructure Dashboard")
    df = load_world_bank_data()

    st.subheader("Data Preview")
    st.write(df.head())

    if df.empty:
        st.warning("No data returned from wbdata for these indicators or date range.")
        return

    # For each indicator, check if it exists and plot
    for code, name in indicators.items():
        if name in df.columns:
            st.subheader(name)
            # Filter out rows without data for this indicator
            sub_df = df.dropna(subset=[name])
            if not sub_df.empty:
                fig = px.line(sub_df, x="date", y=name, color="country", title=f"{name} Over Time")
                st.plotly_chart(fig)
            else:
                st.warning(f"No data found for {name} in the selected range.")
        else:
            st.warning(f"Data for {name} is not available.")

if __name__ == "__main__":
    main()
