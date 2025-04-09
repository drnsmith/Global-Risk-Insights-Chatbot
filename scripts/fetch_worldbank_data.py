import requests
import pandas as pd
from datetime import datetime

# Define the World Bank indicators and descriptions
indicators = {
    "NY.GDP.MKTP.CD": "GDP (current US$)",
    "NY.GDP.PCAP.CD": "GDP per capita (current US$)",
    "GC.DOD.TOTL.GD.ZS": "Central government debt (% of GDP)",
    "NE.EXP.GNFS.ZS": "Exports (% of GDP)",
    "NE.IMP.GNFS.ZS": "Imports (% of GDP)",
    "BX.KLT.DINV.CD.WD": "FDI net inflows (US$)",
    "IC.BUS.EASE.XQ": "Ease of doing business index",
    "GE.EST": "Government effectiveness",
    "GE.PER": "Political stability",
    "RL.EST": "Rule of law",
    "CC.EST": "Control of corruption"
}

# List of countries (BRICS + key others)
countries = ["NZ", "US", "CN", "IN", "ZA", "BR", "RU", "EG", "ET", "IR", "SA", "AE"]

# Years
start_year = 1991
end_year = datetime.now().year


# Fetch data
all_data = []
for indicator, description in indicators.items():
    for country in countries:
        url = f"http://api.worldbank.org/v2/country/{country}/indicator/{indicator}?format=json&per_page=1000&date={start_year}:{end_year}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if len(data) == 2 and isinstance(data[1], list):
                for entry in data[1]:
                    if entry["value"] is not None:
                        all_data.append({
                            "country": entry["country"]["value"],
                            "date": entry["date"],
                            "indicator": indicator,
                            "description": description,
                            "value": entry["value"]
                        })

# Create dataframe
df = pd.DataFrame(all_data)

# Save to CSV
df.to_csv("global_risk_insights_data.csv", index=False)
print("✅ Data saved to global_risk_insights_data.csv")
