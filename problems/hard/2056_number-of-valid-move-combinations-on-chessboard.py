from typing import List

class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        # Define movement directions for each piece type
        directions = {
            'rook': [(0, 1), (0, -1), (1, 0), (-1, 0)],
            'bishop': [(1, 1), (1, -1), (-1, 1), (-1, -1)],
            'queen': [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        }
        
        n = len(pieces)
        
        # Generate all possible moves for each piece
        # A move is (start_r, start_c, dir_r, dir_c, steps)
        # where steps=0 means staying in place
        all_moves = []
        for i in range(n):
            r, c = positions[i]
            piece_moves = []
            
            # Option to stay in place (0 steps)
            piece_moves.append((r, c, 0, 0, 0))
            
            # Try each direction
            for dr, dc in directions[pieces[i]]:
                # Try different number of steps in this direction
                nr, nc = r + dr, c + dc
                steps = 1
                while 1 <= nr <= 8 and 1 <= nc <= 8:
                    piece_moves.append((r, c, dr, dc, steps))
                    nr += dr
                    nc += dc
                    steps += 1
            
            all_moves.append(piece_moves)
        
        # Check if a combination of moves is valid
        def is_valid(move_combo):
            # move_combo[i] = (start_r, start_c, dr, dc, steps) for piece i
            # Simulate the moves and check for collisions at each time step
            
            # Find max time needed (maximum steps among all pieces)
            max_time = max(move[4] for move in move_combo)
            
            # Check collision at each time point
            for t in range(max_time + 1):
                positions_at_t = set()
                
                for i in range(n):
                    start_r, start_c, dr, dc, steps = move_combo[i]
                    
                    # Current position at time t
                    if t <= steps:
                        # Still moving
                        curr_r = start_r + dr * t
                        curr_c = start_c + dc * t
                    else:
                        # Already reached destination, stay there
                        curr_r = start_r + dr * steps
                        curr_c = start_c + dc * steps
                    
                    pos = (curr_r, curr_c)
                    if pos in positions_at_t:
                        # Collision detected
                        return False
                    positions_at_t.add(pos)
            
            return True
        
        # Backtrack through all combinations
        def backtrack(piece_idx, current_combo):
            if piece_idx == n:
                # All pieces have chosen a move, check validity
                if is_valid(current_combo):
                    return 1
                return 0
            
            count = 0
            # Try each possible move for current piece
            for move in all_moves[piece_idx]:
                current_combo.append(move)
                count += backtrack(piece_idx + 1, current_combo)
                current_combo.pop()
            
            return count
        
        return backtrack(0, [])