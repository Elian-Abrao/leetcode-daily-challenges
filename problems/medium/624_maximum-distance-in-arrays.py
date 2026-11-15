class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        overall_min = min(arr[0] for arr in arrays)
        overall_max = max(arr[-1] for arr in arrays)
        return overall_max - overall_min