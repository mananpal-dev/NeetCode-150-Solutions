# Problem: Maximum Depth of Binary Tree
# Platform: LeetCode
# Difficulty: Easy

# Approach:
# Use Depth-First Search (DFS) with Recursion.
#
# For each node:
# 1. Find the maximum depth of the left subtree.
# 2. Find the maximum depth of the right subtree.
# 3. Return 1 + the larger depth.
#
# The extra 1 counts the current node.

# Time Complexity: O(n)
# Space Complexity: O(h)
# h = Height of the tree (recursion stack)

# Common Mistake:
# Returning 1 when the node is None.
# An empty tree has depth 0.

# Revision Note:
# Depth(node)
# =
# 1 + max(left depth, right depth)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        return 1 + max(
            self.maxDepth(root.left),
            self.maxDepth(root.right)
        )