from wbdata.api import get_source, get_series, get_country
import wbdata
import pandas as pd
from datetime import datetime
import time

# Indicators dictionary
indicators = {
    "NY.GDP.MKTP.CD": "GDP (current US$)",
    "NY.GDP.PCAP.CD": "GDP per capita (current US$)",
    "GC.DOD.TOTL.GD.ZS": "External debt stocks (% of GNI)",
    "NE.EXP.GNFS.ZS": "Exports of goods and services (% of GDP)",
    "NE.IMP.GNFS.ZS": "Imports of goods and services (% of GDP)",
    "BX.KLT.DINV.CD.WD": "Foreign direct investment, net inflows (BoP, current US$)",
    "IC.BUS.EASE.XQ": "Ease of doing business index",
    "GE.EST": "Government effectiveness (estimate)",
    "RL.EST": "Rule of law (estimate)",
    "CC.EST": "Control of corruption (estimate)"
}

# BRICS countries (expanded)
countries = {
    "BR": "Brazil",
    "RU": "Russian Federation",
    "IN": "India",
    "CN": "China",
    "ZA": "South Africa",
    "EG": "Egypt, Arab Rep.",
    "ET": "Ethiopia",
    "IR": "Iran, Islamic Rep.",
    "AE": "United Arab Emirates",
    "SA": "Saudi Arabia"
}

# Prepare container
all_data = []

# Loop through each country and each indicator
for iso, country_name in countries.items():
    for indicator_code, indicator_name in indicators.items():
        try:
            df = wbdata.get_dataframe(
                {indicator_code: indicator_name},
                country=iso,
                convert_date=True
            )
            df = df.reset_index()
            df = df.dropna(subset=[indicator_name])
            df["country"] = country_name
            df["indicator"] = indicator_code
            df["description"] = indicator_name
            df.rename(columns={indicator_name: "value", "date": "date"}, inplace=True)
            all_data.append(df)
            time.sleep(1)  # Respect rate limits
        except Exception as e:
            print(f"Error fetching {indicator_code} for {country_name}: {e}")

# Combine and save
final_df = pd.concat(all_data)
final_df = final_df[["country", "date", "indicator", "description", "value"]]
final_df.to_csv("data/global_risk_insights_data_all_years.csv", index=False)
print("✅ Data saved with earliest available years per indicator-country pair.")
