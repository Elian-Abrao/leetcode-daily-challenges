from __future__ import annotations
import sys
from collections import Counter

class Solution:
    @staticmethod
    def word_frequency_from_text(text: str) -> list:
        if not text:
            return []
        words = text.split()
        if not words:
            return []
        cnt = Counter(words)
        # Sort by frequency descending
        items = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))
        return [f"{w} {c}" for w, c in items]

def main():
    data = sys.stdin.read()
    if not data:
        # Try reading words.txt if present
        try:
            with open('words.txt', 'r', encoding='utf-8') as f:
                data = f.read()
        except Exception:
            data = ''
    lines = Solution.word_frequency_from_text(data)
    out = "\n".join(lines)
    if out:
        sys.stdout.write(out)

if __name__ == "__main__":
    main()