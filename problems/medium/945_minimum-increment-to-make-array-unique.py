from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        """
        Returns the minimum number of increments to make all array values unique.
        Approach: sort the array, then greedily adjust each element to be at least
        one greater than the previous (unique) value.
        """
        # Sort so duplicates and ordered values are adjacent
        nums.sort()
        
        moves = 0
        # 'need' is the smallest value we need to assign to the current element
        # to ensure uniqueness (the next available smallest unused integer)
        need = 0
        
        for val in nums:
            if val < need:
                # This value is already taken; we must raise it to 'need'
                # The cost is (need - val)
                moves += need - val
                # After increment, it becomes 'need', so next must be at least need+1
                need += 1
            else:
                # val >= need, so it is not conflicting; we leave it as is
                # The next required smallest unique value is val+1
                need = val + 1
        
        return moves