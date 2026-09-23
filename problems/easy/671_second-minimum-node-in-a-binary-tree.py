class Solution:
    def findSecondMinimumValue(self, root) -> int:
        if not root:
            return -1
        
        first_min = root.val
        self.second_min = float('inf')
        
        def dfs(node):
            if not node:
                return
            if node.val > self.second_min:
                return
            if first_min < node.val < self.second_min:
                self.second_min = node.val
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.second_min if self.second_min != float('inf') else -1