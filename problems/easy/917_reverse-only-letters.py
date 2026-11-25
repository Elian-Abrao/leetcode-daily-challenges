class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # Convert to list for mutable operations
        chars = list(s)
        left, right = 0, len(chars) - 1

        while left < right:
            # Move left pointer if it's not a letter
            if not chars[left].isalpha():
                left += 1
                continue
            # Move right pointer if it's not a letter
            if not chars[right].isalpha():
                right -= 1
                continue

            # Both are letters -> swap them
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

        # Reconstruct string from the modified list
        return "".join(chars)