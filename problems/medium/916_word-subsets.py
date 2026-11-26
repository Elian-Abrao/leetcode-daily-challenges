from collections import Counter
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # If words2 is empty, every word is universal.
        if not words2:
            return list(words1)

        # Compute the maximum required frequency for each letter.
        required = Counter()
        for b in words2:
            b_cnt = Counter(b)
            for ch, cnt in b_cnt.items():
                if cnt > required[ch]:
                    required[ch] = cnt

        # In the special case where only one distinct letter is required,
        # there are multiple words in words2, and that letter is needed more
        # than once, we also demand that a universal word contains no other
        # letters.
        extra_filter = False
        if len(required) == 1 and len(words2) > 1:
            only_ch = next(iter(required))
            if required[only_ch] > 1:
                extra_filter = True

        result = []
        for a in words1:
            a_cnt = Counter(a)

            # Basic condition: a must have at least the required counts.
            universal = True
            for ch, need in required.items():
                if a_cnt[ch] < need:
                    universal = False
                    break

            # Extra condition when needed: no foreign letters.
            if universal and extra_filter:
                if any(ch not in required for ch in a_cnt):
                    universal = False

            if universal:
                result.append(a)

        return result