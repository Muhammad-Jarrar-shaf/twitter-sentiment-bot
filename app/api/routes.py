from app.models.sentiment_result import SentimentResult
from fastapi import APIRouter
import pandas as pd

router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "Twitter Sentiment Analyzer API"
    }


@router.get(
    "/sentiments",
    response_model=list[SentimentResult]
)
def get_sentiments():
    df = pd.read_csv(
        "data/processed/sentiment_results.csv"
    )

    return df.to_dict(orient="records")

@router.get("/summary")
def get_summary():
    df = pd.read_csv(
        "data/processed/sentiment_results.csv"
    )

    return {
        "total_tweets": len(df),
        "positive": len(
            df[df["sentiment"] == "Positive"]
        ),
        "negative": len(
            df[df["sentiment"] == "Negative"]
        ),
        "neutral": len(
            df[df["sentiment"] == "Neutral"]
        )
    }