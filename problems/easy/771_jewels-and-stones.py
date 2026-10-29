class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Convert jewels string to a set for O(1) membership checks
        jewel_set = set(jewels)
        # Count stones that are also jewels
        return sum(1 for stone in stones if stone in jewel_set)