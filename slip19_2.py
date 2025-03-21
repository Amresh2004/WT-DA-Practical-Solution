import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Sample movie reviews dataset
data = {
    'review': [
        "I loved this movie, it was fantastic!",
        "Absolutely terrible, I hated every second.",
        "It was okay, some parts were good, some were bad.",
        "One of the best movies I've ever seen!",
        "I wouldn't recommend this to anyone.",
        "Brilliant performances by the actors, loved it.",
        "A complete waste of time.",
        "The plot was interesting, but the ending ruined it."
    ],
    'sentiment': ['positive', 'negative', 'neutral', 'positive', 'negative', 'positive', 'negative', 'neutral']
}

# Convert to DataFrame
reviews_df = pd.DataFrame(data)

# Convert text into numerical data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(reviews_df['review'])
y = reviews_df['sentiment']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Build a Naive Bayes model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predict and check accuracy
predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))

# Generate Word Cloud
all_reviews = " ".join(reviews_df['review'])
wordcloud = WordCloud(width=800, height=400, background_color='black').generate(all_reviews)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Movie Reviews Word Cloud')
plt.show()
