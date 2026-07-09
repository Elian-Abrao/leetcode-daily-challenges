from typing import List
from collections import deque
import bisect

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        # Sort tasks in ascending order (easiest first)
        # Sort workers in descending order (strongest first)
        tasks.sort()
        workers.sort(reverse=True)
        
        n, m = len(tasks), len(workers)
        
        # Binary search on the number of tasks we can complete
        # If we can complete k tasks, we should try the k easiest tasks
        # with the k strongest workers
        left, right = 0, min(n, m)
        
        def can_complete(k: int) -> bool:
            # Try to complete the k easiest tasks using the k strongest workers
            if k == 0:
                return True
            
            # Get k easiest tasks and k strongest workers
            task_subset = tasks[:k]
            worker_subset = workers[:k]
            
            # Use a greedy approach with a deque to efficiently assign tasks
            # Process workers from weakest to strongest among the selected k workers
            # This allows us to use pills optimally
            worker_subset_sorted = sorted(worker_subset)
            
            pills_used = 0
            available_tasks = deque(task_subset)
            
            # For each worker (from weakest to strongest in the subset)
            for worker_strength in worker_subset_sorted:
                if not available_tasks:
                    break
                
                # Check if current worker can do the easiest remaining task without pill
                if worker_strength >= available_tasks[0]:
                    # Assign easiest task without using a pill
                    available_tasks.popleft()
                elif pills_used < pills and worker_strength + strength >= available_tasks[0]:
                    # Worker needs a pill, check if they can do any task with pill
                    # Find the hardest task this worker can do with a pill
                    # Greedy: use pill to complete the hardest possible task
                    # to save easier tasks for weaker workers
                    
                    # Binary search for the rightmost task worker can do with pill
                    target = worker_strength + strength
                    idx = bisect.bisect_right(available_tasks, target) - 1
                    
                    if idx >= 0:
                        # Remove this task (worker with pill completes it)
                        del available_tasks[idx]
                        pills_used += 1
                    else:
                        # Worker can't complete any task even with pill
                        return False
                else:
                    # Worker can't complete any task (no pills left or pill doesn't help)
                    return False
            
            # Check if all tasks were assigned
            return len(available_tasks) == 0
        
        # Binary search for maximum k
        result = 0
        while left <= right:
            mid = (left + right) // 2
            if can_complete(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result