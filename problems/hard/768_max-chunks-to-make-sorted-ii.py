class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        n = len(arr)
        # suffix_min[i] = minimum element in arr[i:] (inclusive)
        suffix_min = [0] * n
        suffix_min[-1] = arr[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(arr[i], suffix_min[i + 1])

        chunks = 0
        cur_max = -1               # running maximum of arr[0..i]
        # Try to cut after each index i (0 <= i < n-1)
        for i in range(n - 1):
            cur_max = max(cur_max, arr[i])
            # A cut is valid iff every element on the left is <= every element on the right
            if cur_max <= suffix_min[i + 1]:
                chunks += 1

        # Each valid cut increases the number of chunks by 1; the whole array is the base chunk
        return chunks + 1