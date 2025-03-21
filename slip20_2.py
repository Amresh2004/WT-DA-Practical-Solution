import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure stopwords are downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Original paragraph
text = """Hello all, Welcome to Python Programming Academy. Python 
Programming Academy is a nice platform to learn new programming skills. 
It is difficult to get enrolled in this Academy."""

# Define stopwords and tokenize the paragraph
stop_words = set(stopwords.words('english'))
words = word_tokenize(text)

# Remove stopwords
filtered_text = [word for word in words if word.lower() not in stop_words]

# Print the result
print("Original Text:\n", text)
print("\nText after removing stopwords:\n", " ".join(filtered_text))
