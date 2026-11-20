from __future__ import annotations
import bisect

class TopVotedCandidate:
    """
    Precomputes the winner at each recorded time step,
    then answers queries using binary search.
    """

    def __init__(self, persons: list[int], times: list[int]):
        # Precompute leader for each time step
        self.times = times
        self.leaders = [0] * len(times)

        vote_count = {}          # person -> current vote count
        current_leader = -1      # person id of the leader
        max_votes = 0            # votes for the current leader

        for i, person in enumerate(persons):
            # Count this vote
            cnt = vote_count.get(person, 0) + 1
            vote_count[person] = cnt

            # Update leader if this person ties or exceeds the current max
            # Tie goes to the most recent voter (i.e., this person)
            if cnt >= max_votes:
                max_votes = cnt
                current_leader = person

            self.leaders[i] = current_leader

    def q(self, t: int) -> int:
        # Find the rightmost time index with time <= t
        idx = bisect.bisect_right(self.times, t) - 1
        return self.leaders[idx]