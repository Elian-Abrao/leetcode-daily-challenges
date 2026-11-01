class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        # bucket for each lowercase letter (0..25)
        # each entry is a list of (word_index, position_in_word)
        bucket = [[] for _ in range(26)]

        # initial placement: put each word into the bucket of its first character
        for idx, w in enumerate(words):
            if not w:  # skip empty words (not per constraints, but test includes them)
                continue
            first_char_idx = ord(w[0]) - 97
            bucket[first_char_idx].append((idx, 0))

        count = 0
        # scan the source string character by character
        for ch in s:
            ci = ord(ch) - 97
            # collect all words waiting for this character and clear the bucket
            waiting = bucket[ci]
            bucket[ci] = []  # will redistribute them to new buckets or finish

            for word_idx, pos in waiting:
                w = words[word_idx]
                # if we just matched the last character, the word is a subsequence
                if pos + 1 == len(w):
                    count += 1
                else:
                    # move to the next needed character
                    next_char = w[pos + 1]
                    bucket[ord(next_char) - 97].append((word_idx, pos + 1))

        return count