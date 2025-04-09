import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import time
import pandas as pd

def scrape_transparency_data():
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options, headless=True)  # remove headless=True if you want to see the browser

    data = []

    for year in range(1995, 2024):
        url = f"https://www.transparency.org/en/cpi/{year}"
        print(f"Scraping {url}...")
        try:
            driver.get(url)
            time.sleep(5)  # wait for JS content to load
            soup = BeautifulSoup(driver.page_source, "html.parser")

            # Find the data table or cards (this will depend on the structure)
            rows = soup.find_all("tr")
            for row in rows:
                cols = row.find_all("td")
                if len(cols) >= 3:
                    country = cols[0].text.strip()
                    score = cols[1].text.strip()
                    rank = cols[2].text.strip()
                    data.append({"year": year, "country": country, "score": score, "rank": rank})

        except Exception as e:
            print(f"Failed to access {url}: {e}")

    driver.quit()

    df = pd.DataFrame(data)
    df.to_csv("transparency_cpi_1995_2023.csv", index=False)
    print("Saved to transparency_cpi_1995_2023.csv")

scrape_transparency_data()
