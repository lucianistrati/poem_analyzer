import string

def analyze_poem(poem):
    # Remove punctuation
    poem = poem.translate(str.maketrans('', '', string.punctuation))

    # Split the poem into lines
    lines = poem.split('\n')

    # Count the number of lines
    num_lines = len(lines)

    # Count the number of words
    words = poem.split()
    num_words = len(words)

    # Count the number of unique words
    unique_words = set(words)
    num_unique_words = len(unique_words)

    # Calculate the average word length
    total_word_length = sum(len(word) for word in words)
    avg_word_length = total_word_length / num_words

    # Calculate the average words per line
    avg_words_per_line = num_words / num_lines

    # Calculate the rhyme scheme (for simple AABB rhyme scheme)
    last_words = [line.split()[-1].lower() for line in lines]
    rhyme_scheme = "AABB" if last_words[0] == last_words[1] and last_words[2] == last_words[3] else "Unknown"

    # Print the statistics
    print("Poem Analysis:")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Number of unique words: {num_unique_words}")
    print(f"Average word length: {avg_word_length:.2f}")
    print(f"Average words per line: {avg_words_per_line:.2f}")
    print(f"Rhyme scheme: {rhyme_scheme}")

# Example poem
poem = """
    I wandered lonely as a cloud
    That floats on high o'er vales and hills,
    When all at once I saw a crowd,
    A host, of golden daffodils;
"""

# Analyze the poem
analyze_poem(poem)
