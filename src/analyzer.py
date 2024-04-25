import string
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import Counter

def remove_punctuation(poem):
    """Remove punctuation from the poem."""
    return poem.translate(str.maketrans('', '', string.punctuation))

def count_syllables(word):
    """Count the number of syllables in a word."""
    return nltk.corpus.cmudict.dict().get(word.lower(), [0])[0]

def count_total_syllables(poem):
    """Count the total number of syllables in the poem."""
    words = poem.split()
    total_syllables = sum(count_syllables(word) for word in words)
    return total_syllables

def analyze_sentiment(poem):
    """Analyze the sentiment of the poem."""
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(poem)
    return sentiment_scores

def find_most_common_words(poem, num_words=5):
    """Find the most common words in the poem."""
    words = remove_punctuation(poem).lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(num_words)

# Example poem
poem = """
    I wandered lonely as a cloud
    That floats on high o'er vales and hills,
    When all at once I saw a crowd,
    A host, of golden daffodils;
"""

# Remove punctuation
clean_poem = remove_punctuation(poem)

# Count total syllables
total_syllables = count_total_syllables(clean_poem)

# Analyze sentiment
sentiment_scores = analyze_sentiment(poem)

# Find most common words
common_words = find_most_common_words(poem)

print("Total syllables in the poem:", total_syll
