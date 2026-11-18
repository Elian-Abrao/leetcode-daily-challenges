class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        # Strategy: simulate the process in reverse.
        # 1) Sort the deck ascending — these are the reveal order.
        # 2) Work backwards: we know the last card revealed must be
        #    at the top of the deck after all moves are undone.
        # The reverse process: take the bottom card and move it to the top,
        # then place the next smallest card on top.

        # Sort deck to get reveal order (smallest first)
        deck.sort()
        n = len(deck)
        
        # Use a deque to simulate the reverse process efficiently.
        from collections import deque
        result = deque()
        
        # Process from largest to smallest (reverse reveal order)
        for card in reversed(deck):
            if result:
                # Reverse step: move the current bottom card to the top
                # (this undoes "put next top card at bottom")
                result.appendleft(result.pop())
            # Place the current card on top
            result.appendleft(card)
        
        return list(result)