from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        
        def get_next(index):
            # Calculate next index in circular array
            return (index + nums[index]) % n
        
        def is_same_direction(i, j):
            # Check if two indices have same movement direction
            return (nums[i] > 0) == (nums[j] > 0)
        
        # Try starting from each index to find a valid cycle
        for start in range(n):
            # Skip if already marked as visited (not part of a cycle)
            if nums[start] == 0:
                continue
            
            # Use slow and fast pointers to detect cycle (Floyd's algorithm)
            slow = fast = start
            is_forward = nums[start] > 0
            
            # Move pointers until we find a cycle or reach an invalid state
            while True:
                # Move slow pointer one step
                slow = get_next(slow)
                
                # Check if slow pointer direction changed or self-loops
                if not is_same_direction(start, slow) or slow == get_next(slow):
                    break
                
                # Move fast pointer two steps
                fast = get_next(fast)
                if not is_same_direction(start, fast) or fast == get_next(fast):
                    break
                    
                fast = get_next(fast)
                if not is_same_direction(start, fast) or fast == get_next(fast):
                    break
                
                # Cycle detected when slow meets fast
                if slow == fast:
                    return True
            
            # Mark all nodes in this path as visited by setting to 0
            # This ensures we don't revisit nodes that don't lead to valid cycles
            curr = start
            direction = nums[start] > 0
            
            while is_same_direction(curr, start):
                next_idx = get_next(curr)
                nums[curr] = 0  # Mark as visited
                curr = next_idx
                
                # Stop if we've circled back or reached already marked node
                if curr == start or nums[curr] == 0:
                    break
        
        return False