# Problem: Same Tree
# Platform: LeetCode
# Difficulty: Easy

# Approach:
# Use Depth-First Search (DFS) with Recursion.
#
# Compare both trees simultaneously.
#
# Base Cases:
# 1. If both nodes are None, they are identical.
# 2. If one node is None and the other isn't,
#    the trees are different.
# 3. If both nodes exist but their values differ,
#    the trees are different.
#
# Otherwise:
# Recursively compare:
# - Left subtrees
# - Right subtrees
#
# Both comparisons must be True.

# Time Complexity: O(n)
# Space Complexity: O(h)
# h = Height of the tree (recursion stack)

# Common Mistake:
# Comparing only the node values.
# The structure of both trees must also be identical.

# Revision Note:
#
# Same Tree =
# Same Value
# AND
# Same Left Subtree
# AND
# Same Right Subtree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(
        self,
        p: Optional[TreeNode],
        q: Optional[TreeNode]
    ) -> bool:

        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return (
                self.isSameTree(p.left, q.left)
                and
                self.isSameTree(p.right, q.right)
            )

        return False