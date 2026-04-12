class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        """
        Determine the minimum number of pigs needed to identify the poisonous bucket.

        Each pig can have (rounds + 1) distinct outcomes:
        - dies in round 1, dies in round 2, ..., dies in last round, or survives all rounds.
        With 'rounds' being minutesToTest // minutesToDie.

        We need the smallest number of pigs p such that (rounds + 1) ** p >= buckets.
        """
        # Trivial case: only one bucket, no pig is needed.
        if buckets <= 1:
            return 0

        # Number of complete testing rounds we can perform.
        rounds = minutesToTest // minutesToDie
        # Each pig has (rounds + 1) states.
        states_per_pig = rounds + 1

        pigs = 0
        capacity = 1  # Maximum number of buckets distinguishable with 'pigs' pigs.

        # Increase pigs until we can distinguish all buckets.
        while capacity < buckets:
            pigs += 1
            capacity *= states_per_pig

        return pigs