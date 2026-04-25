from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Boyer-Moore Majority Vote algorithm extended for n/3 threshold
        # Key insight: There can be at most 2 elements appearing > n/3 times
        # because 3 * (n/3) = n, so only 2 elements can exceed this threshold
        
        # Phase 1: Find potential candidates
        # We maintain two candidates with their counts
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        
        for num in nums:
            # Check if num matches existing candidates first
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            # If a slot is empty (count is 0), claim it
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            # If num doesn't match either candidate and both slots are occupied,
            # decrement both counts (voting out)
            else:
                count1 -= 1
                count2 -= 1
        
        # Phase 2: Verify candidates
        # The above algorithm only guarantees potential candidates,
        # we need to count their actual occurrences
        result = []
        threshold = len(nums) // 3
        
        # Count actual occurrences of candidate1
        if candidate1 is not None:
            actual_count = sum(1 for num in nums if num == candidate1)
            if actual_count > threshold:
                result.append(candidate1)
        
        # Count actual occurrences of candidate2
        # Make sure candidate2 is different from candidate1
        if candidate2 is not None and candidate2 != candidate1:
            actual_count = sum(1 for num in nums if num == candidate2)
            if actual_count > threshold:
                result.append(candidate2)
        
        return result