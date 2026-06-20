import pandas as pd


class TwitterClient:
    def __init__(self, file_path="data/raw/tweets.csv"):
        self.file_path = file_path

    def search_tweets(self, query=None, max_results=10):
        df = pd.read_csv(self.file_path)

        tweets = df["text"].tolist()

        if query:
            tweets = [
                tweet
                for tweet in tweets
                if query.lower() in tweet.lower()
            ]

        return tweets[:max_results]