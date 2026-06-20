from pydantic import BaseModel


class SentimentResult(BaseModel):
    text: str
    polarity: float
    sentiment: str