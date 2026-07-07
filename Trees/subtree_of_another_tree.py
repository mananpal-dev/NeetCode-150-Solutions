# Problem: Subtree of Another Tree
# Platform: LeetCode
# Difficulty: Easy

# Approach:
# Use DFS with Recursion.
#
# For every node in the main tree:
# 1. Check if the subtree rooted at this node
#    is identical to subRoot.
# 2. If yes, return True.
# 3. Otherwise, recursively check the left
#    and right subtrees.
#
# Use a helper function (isSameTree) to compare
# two trees node by node.

# Time Complexity: O(m × n)
# m = Number of nodes in root
# n = Number of nodes in subRoot

# Space Complexity: O(h)
# h = Height of the tree (recursion stack)

# Common Mistake:
# Comparing only the root values.
# Even if the values match, the entire
# subtree structure and values must match.

# Revision Note:
#
# DFS on root
# ↓
# For every node
# ↓
# Check Same Tree
# ↓
# If not same
# Search Left OR Search Right

# Definition for a binary tree node.
# class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

class Solution:
    def isSubtree(
        self,
        root: Optional[TreeNode],
        subRoot: Optional[TreeNode]
    ) -> bool:

        def isSameTree(p, q):

            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False

            return (
                isSameTree(p.left, q.left)
                and
                isSameTree(p.right, q.right)
            )

        def helper(node, sub):

            if not node:
                return False

            if isSameTree(node, sub):
                return True

            return (
                helper(node.left, sub)
                or
                helper(node.right, sub)
            )

        return helper(root, subRoot)