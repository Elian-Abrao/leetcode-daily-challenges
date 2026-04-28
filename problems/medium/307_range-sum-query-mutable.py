from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        # Use a Segment Tree for efficient range queries and point updates
        # Segment tree supports O(log n) update and O(log n) range sum
        self.n = len(nums)
        self.nums = nums
        # Tree array: internal nodes store sums, leaves store original values
        # Size is 4*n to ensure enough space for complete binary tree representation
        self.tree = [0] * (4 * self.n)
        # Build the segment tree from the input array
        self._build(0, 0, self.n - 1)
    
    def _build(self, node: int, start: int, end: int) -> None:
        # Recursively build segment tree
        # node: current tree node index
        # [start, end]: range this node represents
        if start == end:
            # Leaf node: store the actual array value
            self.tree[node] = self.nums[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            # Build left and right subtrees
            self._build(left_child, start, mid)
            self._build(right_child, mid + 1, end)
            # Internal node stores sum of its children
            self.tree[node] = self.tree[left_child] + self.tree[right_child]
    
    def update(self, index: int, val: int) -> None:
        # Update value at given index
        # Propagate change up the tree to maintain correctness
        self._update(0, 0, self.n - 1, index, val)
    
    def _update(self, node: int, start: int, end: int, index: int, val: int) -> None:
        # Recursively update the tree
        if start == end:
            # Reached the leaf node corresponding to index
            self.nums[index] = val
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            # Determine which subtree contains the index
            if index <= mid:
                self._update(left_child, start, mid, index, val)
            else:
                self._update(right_child, mid + 1, end, index, val)
            # Recompute current node's value from updated children
            self.tree[node] = self.tree[left_child] + self.tree[right_child]
    
    def sumRange(self, left: int, right: int) -> int:
        # Query sum in range [left, right]
        return self._query(0, 0, self.n - 1, left, right)
    
    def _query(self, node: int, start: int, end: int, left: int, right: int) -> int:
        # Recursively query the segment tree
        # [start, end]: range represented by current node
        # [left, right]: query range
        
        if right < start or left > end:
            # No overlap between query range and node range
            return 0
        
        if left <= start and end <= right:
            # Current node range is completely within query range
            # Return the precomputed sum for this node
            return self.tree[node]
        
        # Partial overlap: query both children and combine results
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        left_sum = self._query(left_child, start, mid, left, right)
        right_sum = self._query(right_child, mid + 1, end, left, right)
        return left_sum + right_sum