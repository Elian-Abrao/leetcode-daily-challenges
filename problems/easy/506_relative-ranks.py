from __future__ import annotations
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        """
        Returns the ranks for each athlete based on their scores.
        The highest score gets "Gold Medal", second "Silver Medal",
        third "Bronze Medal", and all others get their placement number
        (as a string).
        """
        n = len(score)
        # Pair each score with its original index for later placement.
        # Sorting descending by score gives us the order of finish.
        indexed_scores = [(score[i], i) for i in range(n)]
        indexed_scores.sort(key=lambda x: x[0], reverse=True)

        # Prepare result array; placeholder strings will be overwritten.
        result = [""] * n

        # Assign ranks based on sorted order.
        for rank, (_, original_idx) in enumerate(indexed_scores, start=1):
            if rank == 1:
                result[original_idx] = "Gold Medal"
            elif rank == 2:
                result[original_idx] = "Silver Medal"
            elif rank == 3:
                result[original_idx] = "Bronze Medal"
            else:
                # For ranks 4 and beyond, use the string representation.
                result[original_idx] = str(rank)

        return result