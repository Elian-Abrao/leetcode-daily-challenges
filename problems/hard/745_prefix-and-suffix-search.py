from typing import List, Dict

class WordFilter:
    def __init__(self, words: List[str]) -> None:
        self.lookup: Dict[str, int] = {}
        for idx, word in enumerate(words):
            n = len(word)
            # Generate all non-empty prefixes
            for p_len in range(1, n + 1):
                prefix = word[:p_len]
                # Generate all substrings (anywhere in the word)
                for i in range(n):
                    for j in range(i + 1, n + 1):
                        sub = word[i:j]
                        key = prefix + "#" + sub
                        self.lookup[key] = idx

    def f(self, pref: str, suff: str) -> int:
        key = pref + "#" + suff
        return self.lookup.get(key, -1)