class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Convert to list of characters for in-place mutation.
        chars = list(s)
        n = len(s)

        # Process each block of 2k characters.
        for start in range(0, n, 2 * k):
            # Determine the index range to reverse: [start, start+k) or the remainder.
            left = start
            right = min(start + k - 1, n - 1)  # inclusive end index

            # Reverse the substring in-place using two-pointer swap.
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        # Join back into a string.
        return "".join(chars)