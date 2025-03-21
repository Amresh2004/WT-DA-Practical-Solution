import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('vader_lexicon')

# Read the dataset
df = pd.read_csv(r'C:\Users\amres\Downloads\covid_2021_1.csv')

# Data Cleaning: Remove null values and duplicates
df.dropna(subset=['comment_text'], inplace=True)
df.drop_duplicates(subset='comment_text', inplace=True)

# Tokenize comments into words
df['tokens'] = df['comment_text'].apply(nltk.word_tokenize)

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Perform sentiment analysis
df['sentiment_score'] = df['comment_text'].apply(lambda x: sia.polarity_scores(x)['compound'])

# Categorize comments as positive, negative, or neutral
df['sentiment'] = df['sentiment_score'].apply(lambda x: 'positive' if x > 0 else ('negative' if x < 0 else 'neutral'))

# Calculate percentages of each sentiment
total_comments = len(df)
positive_comments = len(df[df['sentiment'] == 'positive'])
negative_comments = len(df[df['sentiment'] == 'negative'])
neutral_comments = len(df[df['sentiment'] == 'neutral'])

positive_percentage = (positive_comments / total_comments) * 100
negative_percentage = (negative_comments / total_comments) * 100
neutral_percentage = (neutral_comments / total_comments) * 100

# Print results
print(f'Total Comments: {total_comments}')
print(f'Positive Comments: {positive_comments} ({positive_percentage:.2f}%)')
print(f'Negative Comments: {negative_comments} ({negative_percentage:.2f}%)')
print(f'Neutral Comments: {neutral_comments} ({neutral_percentage:.2f}%)')
