class Solution:
    def magicalString(self, n: int) -> int:
        # The magical string is built from a sequence of 1s and 2s.
        # The lengths of consecutive groups in this string form the string itself.
        # A known constructive approach builds the sequence iteratively.

        if n <= 0:
            return 0

        # Seed with the known initial part of the magical string: "1 2 2"
        s = [1, 2, 2]

        # If we only need the first n elements, we can short-circuit early.
        if n <= 3:
            return s[:n].count(1)

        # i points to the current count in s that dictates how many times to repeat the current value
        i = 2          # s[2] is the last count we used in the seed
        cur = 1        # The next block to append will start with 1, then alternate (1,2,1,2,...)

        # Build the sequence until we reach length n
        while len(s) < n:
            times = s[i]  # how many times to append the current value
            for _ in range(times):
                s.append(cur)
                if len(s) >= n:
                    break
            # Move to the next block and switch the value between 1 and 2
            cur = 3 - cur  # toggles between 1 and 2
            i += 1

        # Count how many 1's appear in the first n elements
        return s[:n].count(1)