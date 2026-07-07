# Problem: Lowest Common Ancestor of a Binary Search Tree
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# Use the properties of a Binary Search Tree (BST).
#
# For each node:
# 1. If both p and q are greater than the current node,
#    move to the right subtree.
# 2. If both p and q are smaller than the current node,
#    move to the left subtree.
# 3. Otherwise, the current node is where the paths split,
#    making it the Lowest Common Ancestor (LCA).

# Time Complexity: O(h)
# Space Complexity: O(1)
# h = Height of the BST

# Common Mistake:
# Thinking p is always the left node and q is always the right node.
# They are simply the two target nodes whose LCA we need to find.

# Revision Note:
#
# Both Left  -> Move Left
# Both Right -> Move Right
# Split Here -> Current Node is LCA

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(
        self,
        root: 'TreeNode',
        p: 'TreeNode',
        q: 'TreeNode'
    ) -> 'TreeNode':

        while root:

            if p.val > root.val and q.val > root.val:
                root = root.right

            elif p.val < root.val and q.val < root.val:
                root = root.left

            else:
                return root