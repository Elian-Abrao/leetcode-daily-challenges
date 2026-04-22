from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Boyer-Moore Voting Algorithm:
        - Maintain a potential candidate and a count.
        - When count drops to 0, pick the current element as new candidate.
        - If the current element equals the candidate, increment count; else decrement.
        - With the guarantee that a majority element exists (> n/2), the candidate at the end is the result.
        Complexity: O(n) time, O(1) extra space.
        """
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num  # take a new candidate when we have no current one
            if num == candidate:
                count += 1        # matching candidate strengthens confidence
            else:
                count -= 1        # mismatching element weakens confidence

        return candidate