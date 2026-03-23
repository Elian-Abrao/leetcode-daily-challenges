class Solution:
    def numDecodings(self, s: str) -> int:
        # A leading zero cannot be decoded by itself, so the whole string is invalid.
        if not s or s[0] == "0":
            return 0

        # dp_prev2 = ways to decode prefix ending two positions back
        # dp_prev1 = ways to decode prefix ending one position back
        # Start with the first character already validated as non-zero.
        dp_prev2 = 1
        dp_prev1 = 1

        for i in range(1, len(s)):
            ways = 0

            # A non-zero digit can always stand alone as one letter.
            if s[i] != "0":
                ways += dp_prev1

            # Two-digit decoding is allowed only for values 10..26.
            # This also correctly handles zeros: only 10 and 20 are valid.
            two_digit = (ord(s[i - 1]) - ord("0")) * 10 + (ord(s[i]) - ord("0"))
            if 10 <= two_digit <= 26:
                ways += dp_prev2

            # If neither single-digit nor two-digit decoding works, decoding stops here.
            if ways == 0:
                return 0

            dp_prev2, dp_prev1 = dp_prev1, ways

        return dp_prev1