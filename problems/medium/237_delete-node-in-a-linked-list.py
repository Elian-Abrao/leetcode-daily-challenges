class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Since we don't have access to the previous node, we can't actually
        # remove this node from the list by updating the previous node's next pointer.
        # 
        # Key insight: We can "delete" this node by copying the next node's value
        # into the current node, then removing the next node from the list.
        # This effectively makes the current node "become" the next node.
        
        # Copy the value from the next node into the current node
        node.val = node.next.val
        
        # Skip over the next node by pointing to the node after it
        # This effectively removes the next node from the list
        node.next = node.next.next
        
        # Time Complexity: O(1) - constant time operation
        # Space Complexity: O(1) - no extra space used