from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Track the top three distinct values seen so far.
        # Using None avoids any collision with the full integer range.
        first = second = third = None

        for value in nums:
            # Distinct maxima matter, so duplicates must be ignored.
            if value == first or value == second or value == third:
                continue

            if first is None or value > first:
                # Shift down because a new largest value changes all ranks.
                third = second
                second = first
                first = value
            elif second is None or value > second:
                # Value fits strictly between first and second.
                third = second
                second = value
            elif third is None or value > third:
                # Value is the best candidate for third distinct maximum.
                third = value

        # If fewer than three distinct values exist, return the overall maximum.
        return first if third is None else third