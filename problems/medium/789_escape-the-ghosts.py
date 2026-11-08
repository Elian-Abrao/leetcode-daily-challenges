class Solution:
    def escapeGhosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
        target_x, target_y = target

        # The player's fastest arrival time is the Manhattan distance from (0, 0).
        player_time = abs(target_x) + abs(target_y)

        for ghost_x, ghost_y in ghosts:
            # A ghost only needs to reach the target no later than the player.
            # Arriving at the same time still prevents escape, so use <=.
            ghost_time = abs(ghost_x - target_x) + abs(ghost_y - target_y)
            if ghost_time <= player_time:
                return False

        return True