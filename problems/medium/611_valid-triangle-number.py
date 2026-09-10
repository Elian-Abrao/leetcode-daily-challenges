from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        Count the number of valid triangle triplets.
        Approach: sort the array, then for each largest side (nums[k]),
        use two pointers to count pairs (nums[i], nums[j]) with i < j < k
        such that nums[i] + nums[j] > nums[k].
        Time: O(n^2), Space: O(1) (excluding sort).
        """
        n = len(nums)
        if n < 3:
            return 0

        nums.sort()                     # ascending order
        count = 0

        # Fix the largest side index k (starting from 2)
        for k in range(2, n):
            i = 0                       # smallest side index
            j = k - 1                   # middle side index

            # Two-pointer scan for valid pairs (i, j) with nums[i] + nums[j] > nums[k]
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    # All pairs (i, i+1, ..., j-1) with current j are valid
                    count += (j - i)
                    j -= 1               # try smaller middle side
                else:
                    i += 1               # need larger smallest side

        return count