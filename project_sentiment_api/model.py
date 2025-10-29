from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="cointegrated/rubert-tiny-sentiment-balanced",
    return_all_scores=False
)


def predict_sentiment(text: str):
    result = classifier(text)[0]
    return result['label'].lower()


