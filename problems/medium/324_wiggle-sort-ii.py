from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Reorder nums in-place so that nums[0] < nums[1] > nums[2] < nums[3] ...
        Uses:
          - Counting sort based median selection (values in [0, 5000])
          - Virtual indexing to place larger elements at odd indices and smaller at even indices
          - A 3-way partition around the median (Dutch National Flag style)
        Complexity:
          - Time: O(n + range) where range = 5001
          - Space: O(range) for counts (treated as O(1) relative to input size)
        """
        n = len(nums)
        if n <= 1:
            return

        # 1) Find the median using counting sort since nums[i] in [0, 5000]
        MAX_VAL = 5000
        counts = [0] * (MAX_VAL + 1)
        for v in nums:
            counts[v] += 1

        target = n // 2  # index of median in the sorted order
        cum = 0
        median = 0
        for val, c in enumerate(counts):
            cum += c
            if cum > target:
                median = val
                break

        # 2) Virtual index mapping:
        #    Ensures we populate the array in a wiggle-friendly order.
        #    map_index(i) = (1 + 2*i) % (n | 1)
        #    (n | 1) gives an odd number: cycles through indices starting with 1,3,5,..., then 0,2,4,...
        def map_index(i: int) -> int:
            return (1 + 2 * i) % (n | 1)

        # 3) Three-way partition around median using mapped indices
        left, i, right = 0, 0, n - 1
        while i <= right:
            mapped_i = map_index(i)
            cur = nums[mapped_i]

            if cur > median:
                nums[mapped_i], nums[map_index(left)] = nums[map_index(left)], nums[mapped_i]
                left += 1
                i += 1
            elif cur < median:
                nums[mapped_i], nums[map_index(right)] = nums[map_index(right)], nums[mapped_i]
                right -= 1
            else:
                i += 1