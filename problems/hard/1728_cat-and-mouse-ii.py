from typing import List

class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        
        # Find initial positions of cat, mouse, and food
        cat_pos = mouse_pos = food_pos = None
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'C':
                    cat_pos = (r, c)
                elif grid[r][c] == 'M':
                    mouse_pos = (r, c)
                elif grid[r][c] == 'F':
                    food_pos = (r, c)
        
        # Maximum turns - if we exceed this, it's a draw (cat wins)
        MAX_TURNS = rows * cols * 2
        
        # Memoization: (mouse_pos, cat_pos, turn % (MAX_TURNS), is_mouse_turn) -> can_mouse_win
        memo = {}
        
        def get_moves(pos, max_jump):
            """Generate all possible moves from a position with given jump limit"""
            r, c = pos
            moves = [(r, c)]  # Stay in place is allowed
            
            # Four directions: up, down, left, right
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                # Try all jump distances from 1 to max_jump
                for jump in range(1, max_jump + 1):
                    nr, nc = r + dr * jump, c + dc * jump
                    
                    # Check bounds
                    if not (0 <= nr < rows and 0 <= nc < cols):
                        break
                    
                    # Check wall - cannot jump over or land on wall
                    if grid[nr][nc] == '#':
                        break
                    
                    moves.append((nr, nc))
            
            return moves
        
        def can_mouse_win_from(mouse_pos, cat_pos, turn, is_mouse_turn):
            """
            DFS with memoization to determine if mouse can win from current state.
            Returns True if mouse can win, False otherwise.
            """
            # Base case: too many turns, cat wins (draw counts as cat win)
            if turn >= MAX_TURNS:
                return False
            
            # Terminal conditions - check cat conditions first
            # Cat catches mouse or cat reaches food
            if cat_pos == mouse_pos or cat_pos == food_pos:
                return False
            
            # Mouse reaches food
            if mouse_pos == food_pos:
                return True
            
            # Check memoization - use turn modulo to detect cycles
            state = (mouse_pos, cat_pos, turn % (MAX_TURNS // 2), is_mouse_turn)
            if state in memo:
                return memo[state]
            
            if is_mouse_turn:
                # Mouse's turn: mouse wins if ANY move leads to a winning state
                mouse_moves = get_moves(mouse_pos, mouseJump)
                for new_mouse_pos in mouse_moves:
                    if can_mouse_win_from(new_mouse_pos, cat_pos, turn + 1, False):
                        memo[state] = True
                        return True
                
                # No winning move found for mouse
                memo[state] = False
                return False
            else:
                # Cat's turn: mouse wins only if ALL cat moves lead to mouse winning
                cat_moves = get_moves(cat_pos, catJump)
                for new_cat_pos in cat_moves:
                    if not can_mouse_win_from(mouse_pos, new_cat_pos, turn + 1, True):
                        # Found a cat move that prevents mouse from winning
                        memo[state] = False
                        return False
                
                # All cat moves lead to mouse winning
                memo[state] = True
                return True
        
        # Start game: mouse moves first at turn 0
        return can_mouse_win_from(mouse_pos, cat_pos, 0, True)