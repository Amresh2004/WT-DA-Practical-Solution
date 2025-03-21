import re
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Define the paragraph
text = """Hello all, Welcome to Python Programming Academy. Python 
Programming Academy is a nice platform to learn new programming skills. 
It is difficult to get enrolled in this Academy."""

# Preprocess the text: remove special characters and digits
clean_text = re.sub(r'[^a-zA-Z\s]', '', text)

print("Cleaned Text:\n", clean_text)

# Summarize the text
parser = PlaintextParser.from_string(clean_text, Tokenizer("english"))
summarizer = LsaSummarizer()
summary = summarizer(parser.document, 2)  # Extract 2 sentences

# Print the summary
print("\nExtractive Summary:")
for sentence in summary:
    print(sentence)
