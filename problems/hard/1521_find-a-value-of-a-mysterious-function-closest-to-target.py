from typing import List

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        """
        Use the fact that the set of possible bitwise AND results for subarrays ending at
        index i is small. For each position, we compute all distinct AND results for
        subarrays ending at i by intersecting with the current element.
        We track the closest difference to the target across all such results.
        """
        # res holds the minimum absolute difference found so far
        res = float('inf')
        # prev stores all distinct AND results for subarrays ending at previous index
        prev = set()

        for x in arr:
            # Start new subarrays ending at current index with just x
            curr = {x}
            # Extend previous subarrays by including arr[i], i.e., take bitwise AND
            for val in prev:
                curr.add(val & x)

            # Update the answer with all results that can end at current index
            for val in curr:
                diff = abs(val - target)
                if diff < res:
                    res = diff
                    if res == 0:
                        return 0  # can't get better than a perfect match

            # Move to next position
            prev = curr

        return int(res)