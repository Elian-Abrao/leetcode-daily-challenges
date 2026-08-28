from typing import List
import bisect

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        """
        Return the minimum number of insertions needed to make target a subsequence of arr.
        
        The problem reduces to finding the longest subsequence of arr that is already
        a subsequence of target. Since target consists of distinct integers, we can map
        each element to its index in target, then the longest common subsequence becomes
        the longest increasing subsequence (LIS) of these indices.
        
        Answer = len(target) - LIS_length
        """
        # Map each target value to its index (0-based)
        pos = {val: idx for idx, val in enumerate(target)}
        
        # Collect indices of arr elements that appear in target, preserving order in arr
        indices = []
        for val in arr:
            if val in pos:
                indices.append(pos[val])
        
        # Compute LIS on the collected indices using patience sorting (O(n log n))
        tails = []  # tails[l] = smallest possible last element of an increasing subsequence of length l+1
        for idx in indices:
            # Find the position to place idx (strictly increasing, so bisect_left)
            p = bisect.bisect_left(tails, idx)
            if p == len(tails):
                tails.append(idx)
            else:
                tails[p] = idx
        
        # Length of LIS is the longest subsequence of arr that is also a subsequence of target
        lis_len = len(tails)
        # Minimum operations = elements of target not covered by LIS
        return len(target) - lis_len