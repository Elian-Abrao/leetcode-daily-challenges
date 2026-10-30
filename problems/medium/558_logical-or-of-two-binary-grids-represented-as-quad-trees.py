class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        # Both leaves -> result is a leaf with the logical OR of the values.
        if quadTree1.isLeaf and quadTree2.isLeaf:
            return Node(quadTree1.val or quadTree2.val, True, None, None, None, None)

        # QuadTree1 is a leaf.
        if quadTree1.isLeaf:
            if quadTree1.val:
                # Leaf with value 1 => OR covers the whole region with 1.
                return Node(True, True, None, None, None, None)
            else:
                # Leaf with value 0 => OR does nothing, result is the other tree.
                return quadTree2

        # QuadTree2 is a leaf.
        if quadTree2.isLeaf:
            if quadTree2.val:
                return Node(True, True, None, None, None, None)
            else:
                return quadTree1

        # Both are internal nodes: recursively merge each quadrant.
        topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

        # If all four children are leaves with the same value, merge into one leaf.
        if (topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf
                and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
            return Node(topLeft.val, True, None, None, None, None)

        # Otherwise return an internal node with the merged children.
        # The val can be arbitrarily chosen (True/False) because isLeaf is False.
        return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)