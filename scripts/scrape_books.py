import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Base URL
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

books_data = []

# Loop through pages (1 to 50)
for page in range(1, 51):
    url = base_url.format(page)
    print(f"Scraping page {page}...")

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve page {page}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.strip()
        availability = book.find("p", class_="instock availability").text.strip()
        rating = book.p["class"][1]  # e.g., "Three", "Four"

        books_data.append({
            "Title": title,
            "Price": price,
            "Availability": availability,
            "Rating": rating
        })

    time.sleep(1)  # gentle delay to avoid hammering server

# Convert to DataFrame
df = pd.DataFrame(books_data)

# Export to Excel
df.to_excel("books_data.xlsx", index=False)

print("✅ Scraping complete! Data saved to 'books_price_tracker.xlsx'")
