from __future__ import annotations
from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # If total cards not divisible by group size, impossible to form groups
        if len(hand) % groupSize != 0:
            return False
        
        # Trivial case: groupSize == 1 means every single card is its own group
        if groupSize == 1:
            return True

        # Count frequency of each card value
        freq = Counter(hand)
        
        # Sort unique card values to process in ascending order
        # This ensures we form groups starting from the smallest available card
        sorted_values = sorted(freq.keys())
        
        for value in sorted_values:
            # If this card value is already exhausted, skip it
            if freq[value] == 0:
                continue
            
            # We need to use all remaining copies of this value
            count = freq[value]
            
            # Try to form groups starting from this value
            # For each copy needed, we require 'groupSize' consecutive cards
            for i in range(groupSize):
                needed_card = value + i
                # If we don't have enough of the needed card, impossible
                if freq[needed_card] < count:
                    return False
                # Consume the cards we're using for this group
                freq[needed_card] -= count
        
        return True