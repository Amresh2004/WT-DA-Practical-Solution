import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Create a custom transactions dataset
data = {
    'TransactionID': [1, 2, 3, 4, 5],
    'Description': [
        "Bought a new phone. Super happy with it!",
        "Service was slow and disappointing.",
        "Received a discount on groceries. Awesome!",
        "Lost money due to a billing error. Terrible experience!",
        "Smooth transaction. Satisfied with the service."
    ]
}

df = pd.DataFrame(data)

# Display initial dataset
print("Original Dataset:\n", df)

# Data Cleaning - no missing values here, but let’s drop duplicates just in case
df.drop_duplicates(subset='Description', inplace=True)

# Tokenize descriptions into words
nltk.download('punkt')
df['Tokens'] = df['Description'].apply(word_tokenize)

# Perform sentiment analysis
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()
df['Sentiment'] = df['Description'].apply(lambda x: sia.polarity_scores(x)['compound'])

# Classify comments as positive, negative, or neutral
df['Sentiment_Type'] = df['Sentiment'].apply(lambda score: 'Positive' if score > 0 else ('Negative' if score < 0 else 'Neutral'))

# Calculate sentiment percentages
total_comments = len(df)
positive_comments = len(df[df['Sentiment_Type'] == 'Positive'])
negative_comments = len(df[df['Sentiment_Type'] == 'Negative'])
neutral_comments = len(df[df['Sentiment_Type'] == 'Neutral'])

positive_percentage = (positive_comments / total_comments) * 100
negative_percentage = (negative_comments / total_comments) * 100
neutral_percentage = (neutral_comments / total_comments) * 100

# Display results
print("\nProcessed Dataset:\n", df)
print("\nSentiment Analysis Results:")
print(f"Positive Comments: {positive_comments} ({positive_percentage:.2f}%)")
print(f"Negative Comments: {negative_comments} ({negative_percentage:.2f}%)")
print(f"Neutral Comments: {neutral_comments} ({neutral_percentage:.2f}%)")
