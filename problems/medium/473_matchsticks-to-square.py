from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        side = total // 4
        
        matchsticks.sort(reverse=True)
        
        if not matchsticks or matchsticks[0] > side:
            return False
        
        n = len(matchsticks)
        sides = [0] * 4
        
        def dfs(idx: int) -> bool:
            if idx == n:
                return sides[0] == side and sides[1] == side and sides[2] == side and sides[3] == side
            
            stick = matchsticks[idx]
            for i in range(4):
                if sides[i] + stick > side:
                    continue
                if i > 0 and sides[i] == sides[i - 1]:
                    continue
                
                sides[i] += stick
                if dfs(idx + 1):
                    return True
                sides[i] -= stick
            
            return False
        
        return dfs(0)