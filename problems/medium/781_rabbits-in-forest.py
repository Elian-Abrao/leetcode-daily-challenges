from collections import Counter

class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        """
        Returns the minimum number of rabbits in the forest given their answers.
        
        The insight: rabbits of the same color must give the same answer.
        For a given answer x, each group of same-colored rabbits has exactly x+1 members.
        If we have `freq` rabbits that answered x, they must be partitioned into groups
        of size (x+1). The minimum number of groups is ceil(freq / (x+1)).
        Total rabbits contributed by these groups = ceil(freq / (x+1)) * (x+1).
        """
        # Count how many rabbits gave each answer.
        freq_map = Counter(answers)
        
        total = 0
        for answer, freq in freq_map.items():
            group_size = answer + 1          # each color group must have this many rabbits
            # Number of full groups needed to accommodate all rabbits with this answer
            groups = (freq + group_size - 1) // group_size   # equivalent to ceil division
            total += groups * group_size
        
        return total