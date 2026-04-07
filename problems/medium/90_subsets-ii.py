from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sorting groups equal values together, which lets us skip duplicate branches cleanly.
        nums.sort()

        result: List[List[int]] = []
        current_subset: List[int] = []
        n = len(nums)

        def backtrack(start_index: int) -> None:
            # Every recursion state represents one valid subset.
            # Copy is required because current_subset is mutated in-place afterward.
            result.append(current_subset[:])

            # Try adding each remaining number as the next element.
            for index in range(start_index, n):
                # If this value equals the previous one at the same depth,
                # choosing it would recreate subsets already generated earlier.
                if index > start_index and nums[index] == nums[index - 1]:
                    continue

                current_subset.append(nums[index])
                # Move forward so each element is used at most once per subset position.
                backtrack(index + 1)
                # Restore state for the next candidate choice.
                current_subset.pop()

        backtrack(0)
        return result