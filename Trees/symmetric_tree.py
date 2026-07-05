# Problem: Symmetric Tree
# Platform: LeetCode
# Difficulty: Easy

# Approach:
# Use Depth-First Search (DFS) with Recursion.
#
# Two trees are mirrors if:
# 1. Their root values are equal.
# 2. Left subtree of one equals the right subtree of the other.
# 3. Right subtree of one equals the left subtree of the other.
#
# Start by comparing:
# root.left and root.right.

# Time Complexity: O(n)
# Space Complexity: O(h)
# h = Height of the tree (recursion stack)

# Common Mistake:
# Comparing:
# left with left
# and
# right with right.
#
# For symmetry, always compare:
# left ↔ right
# right ↔ left

# Revision Note:
#
# Mirror Check:
#
# node1.left  ↔ node2.right
# node1.right ↔ node2.left

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def is_mirror(n1, n2):

            if not n1 and not n2:
                return True

            if not n1 or not n2:
                return False

            return (
                n1.val == n2.val
                and is_mirror(n1.left, n2.right)
                and is_mirror(n1.right, n2.left)
            )

        return is_mirror(root.left, root.right)