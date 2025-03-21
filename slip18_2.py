import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Sample paragraph
text = """
So, keep working. Keep striving. Never give up. Fall down seven times, get up eight. 
Ease is a greater threat to progress than hardship. Ease is a greater threat to progress than hardship. 
So, keep moving, keep growing, keep learning. See you at work.
"""

# Preprocessing: remove punctuation, lowercase, and tokenize
tokens = word_tokenize(text.lower())

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]

# Sentence tokenization
sentences = sent_tokenize(text)

# Calculate word frequency
word_freq = Counter(filtered_tokens)

# Display word frequencies
print("Word Frequencies:", word_freq)

# Plot word frequency distribution
plt.figure(figsize=(10, 5))
plt.bar(word_freq.keys(), word_freq.values(), color='skyblue')
plt.title('Word Frequency Distribution')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()

# Generate a Word Cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(filtered_tokens))

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
