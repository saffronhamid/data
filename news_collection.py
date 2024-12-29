import requests
import csv

def fetch_news(category, page_size=100):
    """
    Fetch news articles from the free API for a given category.

    :param category: Category of news (e.g., 'business', 'technology').
    :param page_size: Number of articles to fetch (default is 10).
    :return: List of articles with title, description, url, and published date.
    """
    url = f"https://saurav.tech/NewsAPI/top-headlines/category/{category}/in.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        return [
            {
                'title': article['title'],
                'description': article.get('description', ''),
                'url': article['url'],
                'publishedAt': article['publishedAt']
            }
            for article in articles[:page_size]
        ]
    else:
        print(f"Error fetching news for {category}: {response.status_code}")
        return []

def save_to_csv(filename, articles):
    """
    Save articles to a CSV file.

    :param filename: Name of the CSV file.
    :param articles: List of articles.
    """
    keys = ['title', 'description', 'url', 'publishedAt']
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(articles)
    print(f"Saved articles to {filename}.")

def main():
    stock_categories = {
        "AAPL": "technology",
        "GOOGL": "technology",
        "MSFT": "technology",
        "GLD": "business"
    }

    for stock, category in stock_categories.items():
        print(f"Fetching news for {stock} in category {category}...")
        articles = fetch_news(category)
        if articles:
            save_to_csv(f"{stock}_news.csv", articles)
        else:
            print(f"No articles found for {stock}.")

if __name__ == "__main__":
    main()
