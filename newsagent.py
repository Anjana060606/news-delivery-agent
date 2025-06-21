import requests

API_KEY = "YOU_API_KEY_HERE"   # Paste your key here
url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}"

response = requests.get(url)
data = response.json()

if data["status"] == "ok":
    articles = data["articles"]
    for i, article in enumerate(articles[:10], start=1):
        print(f"{i}. {article['title']}")
        print("Description:", article['description'])
        print("-" * 60)
else:
    print("Error fetching news.")

    
    
with open("top_news.txt", "w", encoding="utf-8") as file:
    for i, article in enumerate(articles[:10], start=1):
        file.write(f"{i}. {article['title']}\n")
        file.write(f"Description: {article['description']}\n\n")