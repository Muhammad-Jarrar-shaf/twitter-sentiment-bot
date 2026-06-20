from pathlib import Path

import pandas as pd

from app.services.twitter_client import TwitterClient
from app.services.sentiment_analyzer import SentimentAnalyzer


class SentimentPipeline:
    def __init__(self):
        self.client = TwitterClient()
        self.analyzer = SentimentAnalyzer()

    def run(self, query=None, max_results=10):
        tweets = self.client.search_tweets(
            query=query,
            max_results=max_results
        )

        results = []

        for tweet in tweets:
            results.append(
                self.analyzer.analyze(tweet)
            )

        return results

    def save_results(
        self,
        results,
        output_path="data/processed/sentiment_results.csv"
    ):
        Path("data/processed").mkdir(
            parents=True,
            exist_ok=True
        )

        df = pd.DataFrame(results)
        df.to_csv(output_path, index=False)

        return output_path