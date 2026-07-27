#!/usr/bin/env python3

import sys
from collections import Counter

def main():
    # Read all lines from stdin or file
    words = []
    for line in sys.stdin:
        # Split line by whitespace and collect all words
        words.extend(line.split())
    
    # Count frequency of each word
    word_count = Counter(words)
    
    # Sort by frequency (descending) and then by word (lexicographically) for stability
    # Since problem guarantees unique frequencies, secondary sort doesn't matter
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    # Output each word and its frequency
    for word, count in sorted_words:
        print(f"{word} {count}")

if __name__ == "__main__":
    main()