class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert number to list of digit characters for easy manipulation.
        digits = list(str(num))
        n = len(digits)

        # Track the maximum digit seen from the right and its index.
        max_digit = -1
        max_idx = -1

        # Indices of the two digits to swap; -1 means no swap found yet.
        left_idx = -1
        right_idx = -1

        # Scan from right to left to find the best swap.
        # We want the leftmost digit that is smaller than a larger digit to its right.
        # The larger digit should be the rightmost occurrence of the maximum digit
        # to ensure the largest possible result after swap.
        for i in range(n - 1, -1, -1):
            d = int(digits[i])
            if d > max_digit:
                # New maximum digit seen from the right.
                max_digit = d
                max_idx = i
            elif d < max_digit:
                # Current digit is smaller than the max to its right.
                # Record this as the best candidate so far (most significant left).
                left_idx = i
                right_idx = max_idx

        # If a swap was found, perform it.
        if left_idx != -1:
            digits[left_idx], digits[right_idx] = digits[right_idx], digits[left_idx]

        # Convert back to integer.
        return int(''.join(digits))