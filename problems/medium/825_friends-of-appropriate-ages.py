class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        # Frequency array for ages 1..120 inclusive.
        freq = [0] * 121
        for age in ages:
            freq[age] += 1

        total = 0
        # Consider every possible age as the sender's age.
        for a in range(1, 121):
            cnt_a = freq[a]
            if cnt_a == 0:
                continue

            # Condition 1: age[y] > 0.5 * age[x] + 7
            # Using integer arithmetic: minimum age y must be at least age[x] // 2 + 8.
            low = a // 2 + 8
            if low > a:          # No receiver can satisfy both conditions.
                continue

            # Scan all possible receiver ages b in [low, a].
            for b in range(low, a + 1):
                cnt_b = freq[b]
                if cnt_b == 0:
                    continue
                if b == a:
                    # Same age: exclude self-pair (x != y).
                    total += cnt_a * (cnt_a - 1)
                else:
                    # Every sender of age a can send to every receiver of age b.
                    total += cnt_a * cnt_b

        return total