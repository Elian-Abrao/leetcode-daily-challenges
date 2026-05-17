from typing import List
import heapq

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        current_sums = mat[0][:k]
        
        for row_idx in range(1, len(mat)):
            current_row = mat[row_idx]
            next_sums = []
            
            heap = []
            heapq.heappush(heap, (current_sums[0] + current_row[0], 0, 0))
            
            visited = set()
            visited.add((0, 0))
            
            while heap and len(next_sums) < k:
                total, sum_idx, row_col_idx = heapq.heappop(heap)
                next_sums.append(total)
                
                if row_col_idx + 1 < len(current_row):
                    next_state = (sum_idx, row_col_idx + 1)
                    if next_state not in visited:
                        visited.add(next_state)
                        new_sum = current_sums[sum_idx] + current_row[row_col_idx + 1]
                        heapq.heappush(heap, (new_sum, sum_idx, row_col_idx + 1))
                
                if sum_idx + 1 < len(current_sums):
                    next_state = (sum_idx + 1, row_col_idx)
                    if next_state not in visited:
                        visited.add(next_state)
                        new_sum = current_sums[sum_idx + 1] + current_row[row_col_idx]
                        heapq.heappush(heap, (new_sum, sum_idx + 1, row_col_idx))
            
            current_sums = next_sums
        
        return current_sums[k - 1]