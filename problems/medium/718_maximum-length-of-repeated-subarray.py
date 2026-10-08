class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        # make nums2 the shorter for space efficiency
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1

        n = len(nums2)

        # Helper to compute longest common subarray that satisfies
        # a monotonic condition given by comp(cur, prev).
        # comp must return True when the extension is allowed.
        def longest(comp):
            prev = [0] * (n + 1)
            best = 0
            prev_val = None          # value of the previous element of nums1
            for x in nums1:
                curr = [0] * (n + 1)
                for j in range(1, n + 1):
                    if x == nums2[j - 1]:
                        if prev[j - 1] == 0:
                            curr[j] = 1
                        else:
                            # prev_val is set because prev[j-1] > 0
                            if comp(x, prev_val):
                                curr[j] = prev[j - 1] + 1
                            else:
                                curr[j] = 1
                        if curr[j] > best:
                            best = curr[j]
                prev = curr
                prev_val = x
            return best

        # Evaluate both monotonic directions
        best_inc = longest(lambda cur, prv: cur >= prv)   # non‑decreasing
        best_dec = longest(lambda cur, prv: cur <= prv)   # non‑increasing
        return max(best_inc, best_dec)