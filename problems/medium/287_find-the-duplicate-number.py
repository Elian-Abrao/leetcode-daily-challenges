from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's Cycle Detection (Tortoise and Hare) approach
        # Treat array as a linked list where nums[i] points to index nums[i]
        # Since there's a duplicate, there must be a cycle in this "linked list"
        
        # Phase 1: Detect cycle using slow and fast pointers
        # slow moves one step at a time, fast moves two steps
        slow = nums[0]
        fast = nums[0]
        
        # Find intersection point in the cycle
        # This loop will always terminate because a cycle exists (pigeonhole principle)
        while True:
            slow = nums[slow]           # Move one step
            fast = nums[nums[fast]]     # Move two steps
            if slow == fast:
                break
        
        # Phase 2: Find the entrance to the cycle (the duplicate number)
        # Mathematical proof: distance from start to cycle entrance equals
        # distance from intersection point to cycle entrance (modulo cycle length)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        # At this point, both pointers meet at the duplicate number
        return slow