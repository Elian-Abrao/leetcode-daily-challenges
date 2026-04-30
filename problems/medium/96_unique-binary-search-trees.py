class Solution:
    def numTrees(self, n: int) -> int:
        # This problem is about counting Catalan numbers
        # The number of unique BSTs with n nodes is the nth Catalan number
        
        # Dynamic programming approach:
        # dp[i] = number of unique BSTs that can be formed with i nodes
        # For i nodes, we can choose any node j (1 to i) as root:
        #   - Left subtree has j-1 nodes
        #   - Right subtree has i-j nodes
        #   - Total combinations = dp[j-1] * dp[i-j]
        # Sum over all possible roots j
        
        # dp[i] represents number of unique BSTs with i nodes
        dp = [0] * (n + 1)
        
        # Base cases:
        # 0 nodes: empty tree (1 way - the empty tree itself)
        # 1 node: only one tree possible
        dp[0] = 1
        dp[1] = 1
        
        # For each number of nodes from 2 to n
        for num_nodes in range(2, n + 1):
            # Try each node as the root
            for root_pos in range(1, num_nodes + 1):
                # Nodes in left subtree: root_pos - 1
                # Nodes in right subtree: num_nodes - root_pos
                left_count = root_pos - 1
                right_count = num_nodes - root_pos
                
                # Multiply combinations of left and right subtrees
                dp[num_nodes] += dp[left_count] * dp[right_count]
        
        return dp[n]