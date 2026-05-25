class Solution:
    def canWinNim(self, n: int) -> bool:
        # Key insight: This is a game theory problem with optimal play
        # 
        # Let's think about winning/losing positions:
        # - If n = 1, 2, 3: we can take all stones and win immediately
        # - If n = 4: no matter what we take (1, 2, or 3), opponent is left with
        #   3, 2, or 1 stones respectively, and they can take all remaining stones to win
        # - If n = 5, 6, 7: we can take enough stones to leave opponent with exactly 4,
        #   putting them in a losing position
        # - If n = 8: any move (1, 2, or 3) leaves opponent with 7, 6, or 5 stones,
        #   all of which are winning positions for them
        #
        # Pattern emerges: positions that are multiples of 4 are losing positions
        # because any move we make leaves opponent in a winning position.
        # All other positions are winning because we can always reduce to a multiple of 4
        # for the opponent.
        #
        # Proof by induction:
        # Base: n=4 is losing (verified above)
        # Step: If n % 4 == 0, then n is losing because taking 1,2,3 leaves
        #       n-1, n-2, n-3 (all not divisible by 4), which are winning for opponent.
        #       If n % 4 != 0, we can take (n % 4) stones to leave opponent with
        #       a multiple of 4, which is a losing position for them.
        #
        # Time: O(1)
        # Space: O(1)
        
        return n % 4 != 0