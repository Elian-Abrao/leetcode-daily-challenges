import collections
from typing import Optional

# Definition for a binary tree node.
# This class needs to be defined here for the test script to construct trees.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Helper function to build a binary tree from a list representation
# (similar to LeetCode's input format: level-order traversal with nulls)
def build_tree_from_list(arr: list) -> Optional[TreeNode]:
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    queue = collections.deque([root])
    i = 1
    while queue and i < len(arr):
        current_node = queue.popleft()

        # Process left child
        if i < len(arr) and arr[i] is not None:
            current_node.left = TreeNode(arr[i])
            queue.append(current_node.left)
        i += 1

        # Process right child
        if i < len(arr) and arr[i] is not None:
            current_node.right = TreeNode(arr[i])
            queue.append(current_node.right)
        i += 1
    return root

# Import the Solution class from the user's solution module
from solution import Solution

def run_tests():
    sol = Solution()

    print("Running tests for Symmetric Tree (Problem 101)...")

    # Test Case 1: Official Example 1 - Symmetric Tree
    # Input: root = [1,2,2,3,4,4,3]
    # Expected Output: true
    input1_list = [1,2,2,3,4,4,3]
    root1 = build_tree_from_list(input1_list)
    expected1 = True
    result1 = sol.isSymmetric(root1)
    assert result1 == expected1, \
        f"Test Case 1 Failed: Input: {input1_list}, Expected: {expected1}, Got: {result1}"
    print(f"Test Case 1 Passed: Input: {input1_list}, Output: {result1}")

    # Test Case 2: Official Example 2 - Asymmetric Tree
    # Input: root = [1,2,2,null,3,null,3]
    # Expected Output: false
    input2_list = [1,2,2,None,3,None,3]
    root2 = build_tree_from_list(input2_list)
    expected2 = False
    result2 = sol.isSymmetric(root2)
    assert result2 == expected2, \
        f"Test Case 2 Failed: Input: {input2_list}, Expected: {expected2}, Got: {result2}"
    print(f"Test Case 2 Passed: Input: {input2_list}, Output: {result2}")

    # Test Case 3: Edge Case - Empty Tree
    # Input: root = [] (represented as None by build_tree_from_list)
    # Expected Output: true (an empty tree is vacuously symmetric)
    input3_list = []
    root3 = build_tree_from_list(input3_list)
    expected3 = True
    result3 = sol.isSymmetric(root3)
    assert result3 == expected3, \
        f"Test Case 3 Failed: Input: {input3_list}, Expected: {expected3}, Got: {result3}"
    print(f"Test Case 3 Passed: Input: {input3_list}, Output: {result3}")

    # Test Case 4: Edge Case - Single Node Tree
    # Input: root = [1]
    # Expected Output: true
    input4_list = [1]
    root4 = build_tree_from_list(input4_list)
    expected4 = True
    result4 = sol.isSymmetric(root4)
    assert result4 == expected4, \
        f"Test Case 4 Failed: Input: {input4_list}, Expected: {expected4}, Got: {result4}"
    print(f"Test Case 4 Passed: Input: {input4_list}, Output: {result4}")

    # Test Case 5: Edge Case - Tree with only left child
    # Input: root = [1,2]
    # Expected Output: false
    input5_list = [1,2]
    root5 = build_tree_from_list(input5_list)
    expected5 = False
    result5 = sol.isSymmetric(root5)
    assert result5 == expected5, \
        f"Test Case 5 Failed: Input: {input5_list}, Expected: {expected5}, Got: {result5}"
    print(f"Test Case 5 Passed: Input: {input5_list}, Output: {result5}")

    # Test Case 6: Edge Case - Tree with only right child
    # Input: root = [1,null,2]
    # Expected Output: false
    input6_list = [1,None,2]
    root6 = build_tree_from_list(input6_list)
    expected6 = False
    result6 = sol.isSymmetric(root6)
    assert result6 == expected6, \
        f"Test Case 6 Failed: Input: {input6_list}, Expected: {expected6}, Got: {result6}"
    print(f"Test Case 6 Passed: Input: {input6_list}, Output: {result6}")

    # Test Case 7: Asymmetric structure with same values on same level
    # Input: root = [1,2,2,3,null,3,null]
    # Expected Output: false (left.left is 3, right.left is 3, but right.right is null, left.right is null. This forms:
    #      1
    #     / \
    #    2   2
    #   /   /
    #  3   3
    # This is NOT symmetric because 2's children are (3, None) and 2's children are (3, None).
    # For symmetry it must be left.left mirror right.right AND left.right mirror right.left.
    # So (3, None) vs (None, 3) for the children of 2 and 2.
    input7_list = [1,2,2,3,None,3,None] # The children of 1.left are (3, None). The children of 1.right are (3, None).
    # Symmetry needs (1.left.left, 1.left.right) to mirror (1.right.right, 1.right.left)
    # (3, None) must mirror (None, 3) which is false.
    root7 = build_tree_from_list(input7_list)
    expected7 = False
    result7 = sol.isSymmetric(root7)
    assert result7 == expected7, \
        f"Test Case 7 Failed: Input: {input7_list}, Expected: {expected7}, Got: {result7}"
    print(f"Test Case 7 Passed: Input: {input7_list}, Output: {result7}")

    # Test Case 8: Symmetric tree with nulls, but correctly mirrored
    # Input: root = [1,2,2,null,3,3,null]
    # Expected Output: true
    #      1
    #     / \
    #    2   2
    #     \ /
    #      3
    input8_list = [1,2,2,None,3,3,None]
    root8 = build_tree_from_list(input8_list)
    expected8 = True
    result8 = sol.isSymmetric(root8)
    assert result8 == expected8, \
        f"Test Case 8 Failed: Input: {input8_list}, Expected: {expected8}, Got: {result8}"
    print(f"Test Case 8 Passed: Input: {input8_list}, Output: {result8}")

    # Test Case 9: Deep symmetric tree
    # Input: root = [1,2,2,3,4,4,3,5,6,7,8,8,7,6,5]
    # Expected Output: true
    input9_list = [1,2,2,3,4,4,3,5,6,7,8,8,7,6,5]
    root9 = build_tree_from_list(input9_list)
    expected9 = True
    result9 = sol.isSymmetric(root9)
    assert result9 == expected9, \
        f"Test Case 9 Failed: Input: {input9_list}, Expected: {expected9}, Got: {result9}"
    print(f"Test Case 9 Passed: Input: {input9_list}, Output: {result9}")

    # Test Case 10: Deep asymmetric tree (value mismatch)
    # Input: root = [1,2,2,3,4,4,9] (right-most leaf is 9 instead of 3)
    # Expected Output: false
    input10_list = [1,2,2,3,4,4,9]
    root10 = build_tree_from_list(input10_list)
    expected10 = False
    result10 = sol.isSymmetric(root10)
    assert result10 == expected10, \
        f"Test Case 10 Failed: Input: {input10_list}, Expected: {expected10}, Got: {result10}"
    print(f"Test Case 10 Passed: Input: {input10_list}, Output: {result10}")

    # Test Case 11: Tree with root and two children with different values
    # Input: root = [1,2,3]
    # Expected Output: false
    input11_list = [1,2,3]
    root11 = build_tree_from_list(input11_list)
    expected11 = False
    result11 = sol.isSymmetric(root11)
    assert result11 == expected11, \
        f"Test Case 11 Failed: Input: {input11_list}, Expected: {expected11}, Got: {result11}"
    print(f"Test Case 11 Passed: Input: {input11_list}, Output: {result11}")

    # Test Case 12: Tree with values 0
    # Input: root = [0,0,0,0,0,0,0]
    # Expected Output: true
    input12_list = [0,0,0,0,0,0,0]
    root12 = build_tree_from_list(input12_list)
    expected12 = True
    result12 = sol.isSymmetric(root12)
    assert result12 == expected12, \
        f"Test Case 12 Failed: Input: {input12_list}, Expected: {expected12}, Got: {result12}"
    print(f"Test Case 12 Passed: Input: {input12_list}, Output: {result12}")

    print("\nAll tests passed!")

if __name__ == "__main__":
    run_tests()