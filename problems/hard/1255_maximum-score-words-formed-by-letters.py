class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        # Count available letters
        avail = [0] * 26
        for ch in letters:
            avail[ord(ch) - 97] += 1

        n = len(words)
        # Preprocess each word: letter frequency vector and total score
        word_cnt = []   # list of [26] ints
        word_score = [] # int
        for w in words:
            cnt = [0] * 26
            cur_score = 0
            for ch in w:
                idx = ord(ch) - 97
                cnt[idx] += 1
                cur_score += score[idx]
            word_cnt.append(cnt)
            word_score.append(cur_score)

        best = 0
        # Enumerate all subsets of words (bitmask)
        for mask in range(1 << n):
            need = [0] * 26
            ok = True
            total = 0
            # Add words that are set in mask, early abort if a letter runs out
            for i in range(n):
                if mask & (1 << i):
                    # Add letter counts of word i
                    for c in range(26):
                        need[c] += word_cnt[i][c]
                        if need[c] > avail[c]:
                            ok = False
                            break
                    if not ok:
                        break
                    total += word_score[i]
            if ok and total > best:
                best = total

        return best