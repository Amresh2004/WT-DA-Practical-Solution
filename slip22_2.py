import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure stopwords are downloaded
nltk.download('stopwords')
nltk.download('punkt')

# Sample paragraph
paragraph = """Hello all, Welcome to Python Programming Academy. Python 
Programming Academy is a nice platform to learn new programming skills. 
It is difficult to get enrolled in this Academy."""

# Define stopwords and tokenize the paragraph
stop_words = set(stopwords.words('english'))
words = word_tokenize(paragraph)

# Remove stopwords
filtered_words = [word for word in words if word.lower() not in stop_words]

# Output the result
print("Original Paragraph:\n", paragraph)
print("\nFiltered Words (No Stopwords):\n", ' '.join(filtered_words))
