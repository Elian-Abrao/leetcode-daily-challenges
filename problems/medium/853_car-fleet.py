class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Pair each car's starting position with its speed.
        cars = list(zip(position, speed))
        # Sort by position descending so nearest to target is processed first.
        cars.sort(key=lambda x: x[0], reverse=True)

        fleets = 0
        # The leader of the current fleet is the car with the longest travel time;
        # we store its position and speed.
        leader_pos = leader_speed = 0  # placeholder, set on first car

        for pos, spd in cars:
            if fleets == 0:
                # The closest car always constitutes a new fleet.
                fleets = 1
                leader_pos, leader_speed = pos, spd
            else:
                # Compare individual times using cross multiplication to avoid float imprecision:
                #   (target - pos) / spd  >  (target - leader_pos) / leader_speed ?
                # Equivalent to: (target - pos) * leader_speed > (target - leader_pos) * spd
                if (target - pos) * leader_speed > (target - leader_pos) * spd:
                    # Slower than the current fleet's slowest car -> cannot catch up.
                    # Start a new fleet with this car as its leader.
                    fleets += 1
                    leader_pos, leader_speed = pos, spd
                # Else it catches up and merges; the leader (and maximum time) stays unchanged.

        return fleets