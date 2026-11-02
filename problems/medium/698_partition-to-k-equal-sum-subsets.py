class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total = sum(nums)
        # All subsets must have the same sum, so total must be divisible by k
        if total % k != 0:
            return False
        target = total // k

        # If any element exceeds the target, it's impossible to place it
        if max(nums) > target:
            return False

        n = len(nums)
        # Trivial case: one subset – the whole array
        if k == 1:
            return True

        # Sorting descending helps pruning: we place large numbers first,
        # which causes early failure if a configuration is impossible.
        nums.sort(reverse=True)

        used = [False] * n

        # ------------------------------------------------------------
        # Backtracking routine:
        #   start    – minimal index to consider (keeps subset order)
        #   cur_sum  – current sum of the subset being built
        #   k_left   – number of subsets still to complete (including current)
        # ------------------------------------------------------------
        def backtrack(start: int, cur_sum: int, k_left: int) -> bool:
            # All required subsets have been formed successfully
            if k_left == 0:
                return True

            # Current subset is finished -> start building the next one
            if cur_sum == target:
                return backtrack(0, 0, k_left - 1)

            # Try to add a number to the current subset
            for i in range(start, n):
                if used[i]:
                    continue
                if cur_sum + nums[i] > target:
                    # Since nums is sorted descending, later numbers are
                    # smaller and may still fit; do not break.
                    continue

                # --- Duplicate value pruning ---
                # If this value equals the previous one and the previous
                # occurrence is still free, we already considered it at
                # this level, so skip to avoid symmetric states.
                if i > start and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                used[i] = True
                # Recurse with increased current sum and updated start
                if backtrack(i + 1, cur_sum + nums[i], k_left):
                    return True
                used[i] = False

                # --- Critical pruning for the first element of a subset ---
                # When cur_sum == 0, we are placing the first element of a
                # new subset.  Because we always start with the largest
                # unused number, if it fails, no alternative placement can
                # succeed (by reordering subsets).  This breaks symmetry
                # and drastically reduces the search tree.
                if cur_sum == 0:
                    break

            return False

        return backtrack(0, 0, k)