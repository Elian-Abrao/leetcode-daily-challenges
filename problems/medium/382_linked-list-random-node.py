from __future__ import annotations
from typing import Optional
import random

class Solution:

    def __init__(self, head: Optional[ListNode]):
        # Store the head of the linked list for traversal during getRandom()
        # This approach uses O(1) space but O(n) time per getRandom() call
        # Alternative: convert to array in O(n) space for O(1) getRandom()
        # Given follow-up asks for space efficiency, we use reservoir sampling
        self.head = head

    def getRandom(self) -> int:
        # Use reservoir sampling algorithm to select uniformly random element
        # in a single pass without knowing the length beforehand
        # This satisfies the follow-up: efficient for unknown/large lists
        
        # Initialize result with the first node's value
        result = self.head.val
        current = self.head.next
        index = 2  # Current position in the list (1-indexed, starting from 2nd node)
        
        # Traverse the rest of the list
        while current:
            # With probability 1/index, replace result with current node's value
            # This ensures each element has equal probability 1/n of being selected
            # Proof: P(element i is chosen) = (1/i) * (i/(i+1)) * ... * ((n-1)/n) = 1/n
            if random.randint(1, index) == 1:
                result = current.val
            
            current = current.next
            index += 1
        
        return result