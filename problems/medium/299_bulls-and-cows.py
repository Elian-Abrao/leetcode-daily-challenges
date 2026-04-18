class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        """
        Compute Bulls and Cows hint.
        Bulls: digits that are correct in both value and position.
        Cows: digits present in both numbers but in different positions.
        The algorithm uses a single pass to count bulls and accumulate
        unmatched digits, then computes cows from the remaining counts.
        """
        bulls = 0
        # Counts for digits 0-9 for non-bull positions
        count_secret = [0] * 10
        count_guess = [0] * 10

        n = len(secret)
        for i in range(n):
            s = secret[i]
            g = guess[i]
            if s == g:
                bulls += 1
            else:
                count_secret[ord(s) - ord('0')] += 1
                count_guess[ord(g) - ord('0')] += 1

        cows = 0
        for d in range(10):
            cows += min(count_secret[d], count_guess[d])

        return f"{bulls}A{cows}B"