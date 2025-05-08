import requests
from bs4 import BeautifulSoup
import pandas as pd

# Line names and their relative URL paths (adjust if needed)
line_paths = {
    "Main Line": "main-line",
    "Coastal Line": "coastal-line",
    "Northern Line": "northern-line",
    "Eastern Line": "eastern-line",
    "Puttalam Line": "puttalam-line"
}

base_url = "https://colombofort.com/train.schedule.htm"
all_data = []

for line_name, path in line_paths.items():
    url = base_url
    print(f"Scraping {line_name} from {url}")

    # Fetch and parse the page
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the correct table
    main_table = soup.find("table", {"id": "table4"})
    if not main_table:
        print(f"Could not find schedule table for {line_name}")
        continue

    # Extract headers
    headers = [th.get_text(strip=True) for th in main_table.find_all("td")[0].find_all("th")]
    
    # Extract rows
    for row in main_table.find_all("tr")[1:]:
        cols = row.find_all("td")
        if len(cols) == 5:
            row_data = {
                "Line": line_name,
                "Train Name": cols[0].text.strip(),
                "From": cols[1].text.strip(),
                "Departure": cols[2].text.strip(),
                "To": cols[3].text.strip(),
                "Arrival": cols[4].text.strip()
            }
            all_data.append(row_data)

# Convert to DataFrame
df = pd.DataFrame(all_data)

# Save to CSV
df.to_csv("sri_lanka_train_schedule.csv", index=False)
print("All train schedules saved to sri_lanka_train_schedule.csv")
