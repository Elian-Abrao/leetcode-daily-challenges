class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # Key insight: In a binary tree, each non-null node creates 2 "slots" for children
        # and consumes 1 slot (where it's placed). Each null node consumes 1 slot.
        # We start with 1 available slot (for the root).
        # 
        # Valid serialization: slots should become exactly 0 after processing all nodes,
        # and should never go negative during processing.
        
        nodes = preorder.split(',')
        
        # Start with 1 slot available for the root
        slots = 1
        
        for node in nodes:
            # Each node (null or non-null) consumes one slot
            slots -= 1
            
            # If slots go negative, we've consumed more than available
            # This means the serialization is invalid
            if slots < 0:
                return False
            
            # Non-null nodes add 2 new slots (for left and right children)
            if node != '#':
                slots += 2
        
        # Valid tree must have exactly 0 remaining slots at the end
        # If slots > 0, tree is incomplete (missing nodes)
        # If slots < 0, we consumed too many (handled in loop)
        return slots == 0