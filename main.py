import requests
from get_email import send_email
def fetch_techcrunch_articles(api_key):
    """Function to fetch Techcrunch Data from API with all information. """
    articles_info = ""  # Keep as a string throughout the function
    url = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # This will raise an exception for HTTP errors
        articles = response.json().get('articles', [])
        for article in articles[:15]:
            title = article.get("title", "No Title")
            description = article.get("description", "No Description")
            author = article.get("author", "Author Unknown")
            published_at = article.get("publishedAt", "Publish Date Unknown")
            url = article.get("url", "#")

            # Keep accumulating information as a string
            articles_info += f"Subject: Today's Tech-crunch Digest\n\nTitle: {title}\nDescription: {description}\nAuthor: {author}\nPublished At: {published_at}\nURL: {url}\n\n"
    except requests.exceptions.HTTPError as err:
        articles_info += f"HTTP error occurred: {err}\n"
    except Exception as err:
        articles_info += f"An error occurred: {err}\n"

    return articles_info

# Use the function and send the email
api_key = "9eb6fff0da414635bc1c41efe5786ba5"
articles_info = fetch_techcrunch_articles(api_key)
if articles_info:
    articles_info_encoded = articles_info.encode("utf-8")  # Do the encoding here if needed
    # Assuming send_email function expects bytes
    send_email(articles_info_encoded)
else:
    print("No articles information to send.")
