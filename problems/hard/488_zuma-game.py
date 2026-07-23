from collections import Counter

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def remove_consecutive(s):
            while True:
                new_s = ""
                i = 0
                removed = False
                
                while i < len(s):
                    j = i
                    while j < len(s) and s[j] == s[i]:
                        j += 1
                    
                    if j - i < 3:
                        new_s += s[i:j]
                    else:
                        removed = True
                    
                    i = j
                
                if not removed:
                    return new_s
                
                s = new_s
        
        from collections import deque
        
        hand_count = Counter(hand)
        queue = deque([(board, hand_count, 0)])
        visited = set()
        visited.add((board, tuple(sorted(hand_count.items()))))
        
        while queue:
            curr_board, curr_hand, steps = queue.popleft()
            
            if not curr_board:
                return steps
            
            for color in curr_hand:
                if curr_hand[color] == 0:
                    continue
                
                for i in range(len(curr_board) + 1):
                    # Smart pruning: only insert at meaningful positions
                    # 1. Insert next to the same color
                    # 2. Insert between two same colors (different from our color)
                    
                    should_try = False
                    
                    # Check left neighbor
                    if i > 0 and curr_board[i-1] == color:
                        should_try = True
                    # Check right neighbor
                    elif i < len(curr_board) and curr_board[i] == color:
                        should_try = True
                    # Insert between two consecutive same colors (can trigger chain reaction)
                    elif i > 0 and i < len(curr_board) and curr_board[i-1] == curr_board[i]:
                        should_try = True
                    # At the start or end (boundary cases)
                    elif i == 0 or i == len(curr_board):
                        # Only try at boundaries if the adjacent ball is the same color
                        if i == 0 and len(curr_board) > 0 and curr_board[0] == color:
                            should_try = True
                        elif i == len(curr_board) and len(curr_board) > 0 and curr_board[-1] == color:
                            should_try = True
                    
                    if not should_try:
                        continue
                    
                    new_board = curr_board[:i] + color + curr_board[i:]
                    new_board = remove_consecutive(new_board)
                    
                    new_hand = curr_hand.copy()
                    new_hand[color] -= 1
                    
                    state_key = (new_board, tuple(sorted(new_hand.items())))
                    
                    if state_key not in visited:
                        visited.add(state_key)
                        queue.append((new_board, new_hand, steps + 1))
        
        return -1