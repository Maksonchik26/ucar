from common.enums import SentimentEnum


sentiment_dict = {
    "хорош": SentimentEnum.POSITIVE,
    "люблю": SentimentEnum.POSITIVE,
    "плох": SentimentEnum.NEGATIVE,
    "ненавиж": SentimentEnum.NEGATIVE,
}


def detect_sentiment(text: str) -> SentimentEnum:
    text = text.lower()

    for word, sentiment in sentiment_dict.items():
        if word in text:
            return sentiment

    return SentimentEnum.NEUTRAL
