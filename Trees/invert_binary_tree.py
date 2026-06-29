# Problem: Invert Binary Tree
# Platform: LeetCode
# Difficulty: Easy

# Approach:
# Use Depth-First Search (DFS) with Recursion.
#
# For every node:
# 1. Swap its left and right child.
# 2. Recursively invert the left subtree.
# 3. Recursively invert the right subtree.
#
# Continue until all nodes have been visited.

# Time Complexity: O(n)
# Space Complexity: O(h)
# h = Height of the tree (recursion stack)

# Common Mistake:
# Forgetting the base case.
# Always return when the current node is None.

# Revision Note:
# Visit Node
# ↓
# Swap Left & Right
# ↓
# Recurse Left
# ↓
# Recurse Right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root