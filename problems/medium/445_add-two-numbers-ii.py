from __future__ import annotations
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Strategy: Use stacks to reverse the order without modifying input lists
        # This allows us to add digits from least significant to most significant
        # while maintaining the original list structure
        
        # Build stacks from both linked lists
        stack1 = []
        stack2 = []
        
        # Traverse l1 and push all values onto stack1
        curr = l1
        while curr:
            stack1.append(curr.val)
            curr = curr.next
        
        # Traverse l2 and push all values onto stack2
        curr = l2
        while curr:
            stack2.append(curr.val)
            curr = curr.next
        
        # Process addition from least significant digit (top of stacks)
        carry = 0
        head = None  # Will build result list in reverse order
        
        # Continue while there are digits in either stack or a carry exists
        while stack1 or stack2 or carry:
            # Get current digit from each number (0 if stack is empty)
            digit1 = stack1.pop() if stack1 else 0
            digit2 = stack2.pop() if stack2 else 0
            
            # Calculate sum of current digits plus carry
            total = digit1 + digit2 + carry
            carry = total // 10
            digit = total % 10
            
            # Create new node and prepend to result list
            # This builds the list in correct order (most significant first)
            new_node = ListNode(digit)
            new_node.next = head
            head = new_node
        
        return head