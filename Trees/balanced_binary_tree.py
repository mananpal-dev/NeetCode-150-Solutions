# Problem: Balanced Binary Tree
# Platform: LeetCode
# Difficulty: Easy

# Approach:
# Use Depth-First Search (DFS) with Recursion.
#
# For every node:
# 1. Check if the left subtree is balanced.
# 2. Check if the right subtree is balanced.
# 3. Find the height of both subtrees.
# 4. The current node is balanced if:
#    - Left subtree is balanced.
#    - Right subtree is balanced.
#    - Height difference is at most 1.
#
# Return both:
# - Whether the subtree is balanced.
# - Its height.

# Time Complexity: O(n)
# Space Complexity: O(h)
# h = Height of the tree (recursion stack)

# Common Mistake:
# Calculating the height separately for every node,
# which results in O(n²).
#
# Instead, compute the balance status and height
# together in a single DFS traversal.

# Revision Note:
#
# Return:
# [isBalanced, height]
#
# Balance Condition:
# abs(left_height - right_height) <= 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):

            if not node:
                return [True, 0]

            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)

            balanced = (
                left_balanced and
                right_balanced and
                abs(left_height - right_height) <= 1
            )

            height = 1 + max(left_height, right_height)

            return [balanced, height]

        return dfs(root)[0]