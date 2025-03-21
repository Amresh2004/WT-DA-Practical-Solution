import re

# Original text
text = """So, keep working. Keep striving. Never give up. Fall down seven times, get up eight. 
Ease is a greater threat to progress than hardship. Ease is a greater threat to progress than hardship. 
So, keep moving, keep growing, keep learning. See you at work."""

# Preprocess the text: remove special characters, digits, and extra spaces
clean_text = re.sub(r'[^a-zA-Z\s]', '', text)  # Keep only letters and spaces
clean_text = re.sub(r'\s+', ' ', clean_text).strip()  # Remove extra spaces

print("Original Text:\n", text)
print("\nCleaned Text:\n", clean_text)
