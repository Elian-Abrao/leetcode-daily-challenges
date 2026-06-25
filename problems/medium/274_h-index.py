from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Sort citations in descending order to process highest citations first
        # This allows us to check h-index candidates efficiently
        citations.sort(reverse=True)
        
        h = 0
        # Iterate through sorted citations
        # At index i, we have (i+1) papers with at least citations[i] citations
        for i, c in enumerate(citations):
            # The h-index is the maximum h where at least h papers have >= h citations
            # Since citations are sorted descending, citations[i] is the (i+1)-th highest
            # We need at least (i+1) papers with >= (i+1) citations
            # This is satisfied when citations[i] >= (i+1)
            if c >= i + 1:
                h = i + 1
            else:
                # Once citations[i] < (i+1), no higher h-index is possible
                # because we need at least (i+1) papers but the (i+1)-th paper
                # has fewer than (i+1) citations
                break
        
        return h