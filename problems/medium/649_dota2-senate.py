from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Queues storing indices of Radiant and Dire senators.
        # Indices preserve the original order and help decide who acts first.
        radiant = deque()
        dire = deque()
        n = len(senate)

        # Record the initial positions of each party.
        for i, ch in enumerate(senate):
            if ch == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        # Simulate the banning process.
        # Each senator bans the first opposing senator and then re-enters
        # with an index increased by n to stay behind newer senators in future rounds.
        while radiant and dire:
            r_idx = radiant.popleft()
            d_idx = dire.popleft()

            if r_idx < d_idx:
                # Radiant acts first, bans this Dire, and goes to the next round.
                radiant.append(r_idx + n)
            else:
                # Dire acts first, bans this Radiant, and goes to the next round.
                dire.append(d_idx + n)

        # The party with remaining senators wins.
        return "Radiant" if radiant else "Dire"