from app.services.twitter_client import TwitterClient

client = TwitterClient()

tweets = client.search_tweets(
    query="Artificial Intelligence",
    max_results=5
)

print("\nRecent Tweets:\n")

for idx, tweet in enumerate(tweets, start=1):
    print(f"{idx}. {tweet}\n")