from app.services.sentiment_analyzer import SentimentAnalyzer


def test_positive_sentiment():
    result = SentimentAnalyzer.analyze(
        "I love this product"
    )

    assert result["sentiment"] == "Positive"


def test_negative_sentiment():
    result = SentimentAnalyzer.analyze(
        "This is terrible"
    )

    assert result["sentiment"] == "Negative"