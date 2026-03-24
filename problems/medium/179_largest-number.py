from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert once to strings because all comparisons are concatenation-based.
        parts = [str(num) for num in nums]

        def compare(left: str, right: str) -> int:
            # Order by which concatenation yields the larger overall number.
            # If left+right is larger, left must come before right.
            if left + right > right + left:
                return -1
            if left + right < right + left:
                return 1
            return 0

        # Custom sort is necessary because numeric or lexicographic order is insufficient.
        parts.sort(key=cmp_to_key(compare))

        # If the largest piece is "0", then every piece is "0".
        # Returning repeated zeros like "000" would be incorrect.
        if parts[0] == "0":
            return "0"

        # Joining the sorted pieces directly gives the maximal arrangement.
        return "".join(parts)