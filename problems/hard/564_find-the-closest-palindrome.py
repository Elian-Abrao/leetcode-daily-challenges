class Solution:
    def nearestPalindromic(self, n: str) -> str:
        L = len(n)
        # Length of the first half (including middle for odd length)
        half_len = (L + 1) // 2
        half = n[:half_len]

        # Build a palindrome of length L from a candidate first half.
        def make_pal(s: str) -> str:
            if L % 2 == 0:
                # Even length: mirror completely
                return s + s[::-1]
            else:
                # Odd length: mirror everything except the middle digit
                return s + s[:-1][::-1]

        candidates = set()

        # 1) Mirror the original first half
        candidates.add(make_pal(half))

        # 2) Increment and decrement the first half, keeping the same digit length
        half_val = int(half)
        for delta in (-1, 1):
            new_half = str(half_val + delta)
            if len(new_half) == len(half):          # same digit length
                candidates.add(make_pal(new_half))

        # 3) Edge cases: all 9's (one digit fewer) and 1...1 (one digit more)
        candidates.add(str(10 ** (L - 1) - 1))      # e.g., 9, 99, 999, ...
        candidates.add(str(10 ** L + 1))            # e.g., 11, 101, 1001, ...

        # Remove the original number if it is a palindrome (added by case 1)
        candidates.discard(n)

        # Find the closest palindrome among the candidates
        n_int = int(n)
        best_str = None
        best_int = None
        best_diff = None

        for cand_str in candidates:
            cand_int = int(cand_str)
            diff = abs(cand_int - n_int)
            # Choose smaller difference; on tie, choose smaller numeric value
            if (best_diff is None or diff < best_diff or
                (diff == best_diff and cand_int < best_int)):
                best_str = cand_str
                best_int = cand_int
                best_diff = diff

        return best_str