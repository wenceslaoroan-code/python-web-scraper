import json
import csv
import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = "http://quotes.toscrape.com/"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve page. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    quotes_data = []

    for quote_box in soup.find_all("div", class_="quote"):
        text = quote_box.find("span", class_="text").get_text()
        author = quote_box.find("small", class_="author").get_text()
        tags = [tag.get_text() for tag in quote_box.find_all("a", class_="tag")]
        
        quotes_data.append({
            "quote": text,
            "author": author,
            "tags": tags
        })

    # Save to JSON file
    with open("quotes.json", "w", encoding="utf-8") as f:
        json.dump(quotes_data, f, indent=4)

    # Save to CSV file
    with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["quote", "author", "tags"])
        writer.writeheader()
        for row in quotes_data:
            row_copy = row.copy()
            row_copy["tags"] = ", ".join(row_copy["tags"])
            writer.writerow(row_copy)

    print(f"Successfully scraped {len(quotes_data)} quotes into quotes.json and quotes.csv!")

if __name__ == "__main__":
    scrape_quotes()
