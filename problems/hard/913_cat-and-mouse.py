class Solution:
    def catMouseGame(self, graph: list[list[int]]) -> int:
        # ------------------------------------------------------------
        # Problem: Cat-and-Mouse on an undirected graph.
        # Players: Mouse (M, start=1, moves first), Cat (C, start=2, moves second).
        # Hole at node 0. Cat cannot go to node 0.
        # Winner: 1 = Mouse, 2 = Cat, 0 = Draw (infinite optimal play).
        # Graph size ≤ 50. Use minimax with state (mouse, cat, turn).
        # Turn: 0 = mouse to move, 1 = cat to move.
        # We compute outcome via DFS with memoization and cycle detection.
        # ------------------------------------------------------------
        
        n = len(graph)
        # memo[(m, c, turn)] = outcome (0=unknown, 1=mouse win, 2=cat win)
        memo = {}
        
        # For detecting cycles during recursion (to mark draws).
        # visited set for current path helps identify when we revisit the same state.
        visited = set()
        
        # ------------------------------------------------------------
        # Precompute for each node whether the mouse can reach hole in one move.
        # Not strictly needed, but clarifies the base-case logic.
        # ------------------------------------------------------------
        
        def dfs(m: int, c: int, turn: int) -> int:
            # Base cases
            if m == 0:
                # Mouse reached hole -> Mouse wins
                return 1
            if m == c:
                # Cat caught Mouse -> Cat wins
                return 2
            # No repetition check here; handled in recursion loop.
            
            state = (m, c, turn)
            if state in memo:
                return memo[state]
            
            # Cycle detection: if we see this state again in current recursion stack
            if state in visited:
                # Cycle implies both can avoid losing -> draw
                return 0
            
            visited.add(state)
            
            if turn == 0:  # Mouse's turn
                # Mouse tries to force a win; if any move leads to win, take it.
                # If all moves lead to cat win, then cat wins; else draw if some lead to draw.
                any_draw = False
                for nm in graph[m]:
                    # Mouse can stay? graph has no self-loops per constraints.
                    res = dfs(nm, c, 1)
                    if res == 1:
                        visited.discard(state)
                        memo[state] = 1
                        return 1  # Mouse wins
                    if res == 0:
                        any_draw = True
                # No winning move
                outcome = 0 if any_draw else 2
                visited.discard(state)
                memo[state] = outcome
                return outcome
            
            else:  # Cat's turn
                # Cat cannot go to node 0.
                any_draw = False
                for nc in graph[c]:
                    if nc == 0:
                        continue  # Cat not allowed in hole
                    res = dfs(m, nc, 0)
                    if res == 2:
                        visited.discard(state)
                        memo[state] = 2
                        return 2  # Cat wins
                    if res == 0:
                        any_draw = True
                outcome = 0 if any_draw else 1
                visited.discard(state)
                memo[state] = outcome
                return outcome
        
        return dfs(1, 2, 0)