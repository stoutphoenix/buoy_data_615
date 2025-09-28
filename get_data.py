import requests

base_url = 'https://www.ndbc.noaa.gov/view_text_file.php?filename=44013h{}.txt.gz&dir=data/historical/stdmet/'

for year in range(2000, 2025):
    url = base_url.format(year)
    print(f"Downloading {url}")
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"data/{year}.txt", "wb") as f:
            f.write(response.content)
        print(f"Saved {year}.txt")
    else:
        print(f"Failed to download for year {year}: {response.status_code}")