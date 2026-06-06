from typing import List
import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        max_heap = []
        min_heap = []
        balance = 0
        to_remove = defaultdict(int)
        result = []
        
        def cleanup():
            while max_heap and to_remove[-max_heap[0]] > 0:
                to_remove[-max_heap[0]] -= 1
                heapq.heappop(max_heap)
            
            while min_heap and to_remove[min_heap[0]] > 0:
                to_remove[min_heap[0]] -= 1
                heapq.heappop(min_heap)
        
        def rebalance():
            nonlocal balance
            if balance > 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
                balance -= 2
            elif balance < 0:
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
                balance += 2
            cleanup()
        
        def add_num(num):
            nonlocal balance
            if not max_heap or num <= -max_heap[0]:
                heapq.heappush(max_heap, -num)
                balance += 1
            else:
                heapq.heappush(min_heap, num)
                balance -= 1
            rebalance()
        
        def remove_num(num):
            nonlocal balance
            to_remove[num] += 1
            
            if num <= -max_heap[0]:
                balance -= 1
            else:
                balance += 1
            
            cleanup()
            rebalance()
        
        def get_median():
            cleanup()
            if k % 2 == 1:
                return float(-max_heap[0])
            else:
                return (-max_heap[0] + min_heap[0]) / 2.0
        
        for i in range(k):
            add_num(nums[i])
        
        result.append(get_median())
        
        for i in range(k, len(nums)):
            outgoing = nums[i - k]
            remove_num(outgoing)
            incoming = nums[i]
            add_num(incoming)
            result.append(get_median())
        
        return result