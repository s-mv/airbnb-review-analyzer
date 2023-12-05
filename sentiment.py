import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


def analyze(text: str) -> float:
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(text)
    return scores["compound"]
