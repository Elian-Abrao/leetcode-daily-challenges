class Solution:
    def countSegments(self, s: str) -> int:
        # Count starts of segments instead of splitting, which avoids extra memory.
        segments = 0

        for index, char in enumerate(s):
            # A new segment starts when we see a non-space character
            # whose previous character is either absent or a space.
            if char != ' ' and (index == 0 or s[index - 1] == ' '):
                segments += 1

        return segments