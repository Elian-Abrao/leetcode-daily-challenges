from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # "write_index" always points to the next position where we keep a valid value.
        # Everything before it is guaranteed to be different from val.
        write_index = 0

        for num in nums:
            # Keep only values that should remain in the array.
            if num != val:
                nums[write_index] = num
                write_index += 1

        # The first write_index elements now contain all kept values.
        return write_index