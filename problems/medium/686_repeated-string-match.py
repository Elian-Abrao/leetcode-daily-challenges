class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n, m = len(a), len(b)

        # Minimum repeats needed just to have total length >= len(b).
        reps = (m + n - 1) // n  # ceil(m / n)
        repeated = a * reps

        if b in repeated:
            return reps

        # A substring may start near the end of one copy and cross boundaries.
        # One more copy is sufficient for this case.
        repeated += a
        reps += 1

        if b in repeated:
            return reps

        return -1