# Problem: Diameter of Binary Tree
# Platform: LeetCode
# Difficulty: Easy

# Approach:
# Use Depth-First Search (DFS) with Recursion.
#
# For every node:
# 1. Find the height of the left subtree.
# 2. Find the height of the right subtree.
# 3. The diameter passing through this node is:
#    left height + right height.
# 4. Keep track of the maximum diameter found.
#
# Return the height of the current node
# to its parent.

# Time Complexity: O(n)
# Space Complexity: O(h)
# h = Height of the tree (recursion stack)

# Common Mistake:
# Confusing height with diameter.
#
# Height:
# Number of nodes from the current node
# to the deepest leaf.
#
# Diameter:
# Number of edges in the longest path
# between any two nodes.

# Revision Note:
#
# Height = 1 + max(left, right)
#
# Diameter = left + right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(
        self,
        root: Optional[TreeNode]
    ) -> int:

        diameter = 0

        def dfs(node):

            nonlocal diameter

            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            diameter = max(
                diameter,
                left_height + right_height
            )

            return 1 + max(left_height, right_height)

        dfs(root)

        return diameter