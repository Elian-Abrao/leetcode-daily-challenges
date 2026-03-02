class Solution:
    def cloneGraph(self, node: 'Optional[Node]') -> 'Optional[Node]':
        # If input graph is empty, return None
        if node is None:
            return None

        # Map original node -> its clone to preserve structure and identity
        clones = {node: Node(node.val, [])}

        from collections import deque
        queue = deque([node])

        # BFS to traverse and clone all connected nodes
        while queue:
            current = queue.popleft()
            current_clone = clones[current]

            for neighbor in current.neighbors:
                if neighbor not in clones:
                    # Create clone for unseen neighbor and push to queue for further exploration
                    clones[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                # Connect the current node's clone with the neighbor's clone
                current_clone.neighbors.append(clones[neighbor])

        # Return the clone corresponding to the original input node
        return clones[node]