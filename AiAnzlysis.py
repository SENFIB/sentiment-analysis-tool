from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sentiment_analyze = SentimentIntensityAnalyzer()

user_Input = input("Enter Your sentence:\n")

user_sentiment = sentiment_analyze.polarity_scores(user_Input)

sentiment_compound = user_sentiment['compound']

if sentiment_compound >= 0.5:
    sentiment_label = "Positive 😊"
elif sentiment_compound <= -0.5:
    sentiment_label = "Negative 😔"
else:
    sentiment_label = "Neutral 😐"

print(f"\n--- Sentiment Analysis Results ---")
print(f"Your Text: {user_Input}")
print(f"Positive: {user_sentiment['pos'] * 100:.1f}%")
print(f"Neutral: {user_sentiment['neu'] * 100:.1f}%")
print(f"Negative: {user_sentiment['neg'] * 100:.1f}%")
print(f"Overall Sentiment: {sentiment_label}")
