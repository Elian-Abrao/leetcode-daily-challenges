from collections import defaultdict
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # If the target is absent, no valid sequence can end there.
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        word_length = len(beginWord)
        parents = defaultdict(list)  # child -> all predecessors on shortest paths

        # Standard BFS by layers guarantees the first time we reach a word
        # is through a shortest transformation distance.
        current_level = {beginWord}
        found_end = False

        # Remove the start if it appears in the dictionary to avoid revisiting it.
        word_set.discard(beginWord)

        while current_level and not found_end:
            next_level = set()

            # Delay removals until the whole layer is processed so that
            # multiple shortest parents in the same layer are all preserved.
            for word in current_level:
                word_chars = list(word)

                for i in range(word_length):
                    original_char = word_chars[i]

                    # Try every one-letter mutation.
                    for code in range(26):
                        new_char = chr(ord('a') + code)
                        if new_char == original_char:
                            continue

                        word_chars[i] = new_char
                        candidate = ''.join(word_chars)

                        # Only unseen dictionary words can belong to the next BFS layer.
                        if candidate in word_set:
                            if candidate not in next_level:
                                next_level.add(candidate)
                            parents[candidate].append(word)

                            # We still finish the whole layer to collect every
                            # shortest parent chain that reaches endWord.
                            if candidate == endWord:
                                found_end = True

                    word_chars[i] = original_char

            # Removing the entire next layer prevents longer paths from reusing
            # words already reached at the shortest possible distance.
            word_set -= next_level
            current_level = next_level

        if not found_end:
            return []

        result = []
        path = [endWord]

        def build_paths(word: str) -> None:
            # Once we reach the start, the current reversed path is complete.
            if word == beginWord:
                result.append(path[::-1])
                return

            # Every stored parent lies on a shortest path by BFS construction.
            for prev_word in parents[word]:
                path.append(prev_word)
                build_paths(prev_word)
                path.pop()

        build_paths(endWord)
        return result