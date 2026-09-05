from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        for root in dictionary:
            node = trie
            for ch in root:
                node = node.setdefault(ch, {})
            node['#'] = True

        def find_root(word: str) -> str:
            node = trie
            for i, ch in enumerate(word):
                if ch not in node:
                    return word
                node = node[ch]
                if '#' in node:
                    return word[:i + 1]
            return word

        return ' '.join(find_root(word) for word in sentence.split())